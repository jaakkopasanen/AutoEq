import json
import os
from enum import Enum
from io import BytesIO
from pathlib import Path
import numpy as np
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, validator, root_validator
from typing import Union, Optional
import soundfile as sf

from autoeq.constants import DEFAULT_BASS_BOOST_GAIN, DEFAULT_BASS_BOOST_FC, DEFAULT_BASS_BOOST_Q, \
    DEFAULT_TREBLE_BOOST_GAIN, DEFAULT_TREBLE_BOOST_FC, DEFAULT_TREBLE_BOOST_Q, DEFAULT_TILT, DEFAULT_FS, \
    DEFAULT_MAX_GAIN, DEFAULT_SMOOTHING_WINDOW_SIZE, DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE, DEFAULT_TREBLE_F_LOWER, \
    DEFAULT_TREBLE_F_UPPER, DEFAULT_TREBLE_GAIN_K, DEFAULT_PHASE, DEFAULT_PREAMP, DEFAULT_F_RES, \
    PEQ_CONFIGS, DEFAULT_BIT_DEPTH
from autoeq.frequency_response import FrequencyResponse

ROOT_DIR = Path().resolve()

app = FastAPI()
if os.getenv('NODE_ENV') == 'production':
    app.mount('/', StaticFiles(directory=ROOT_DIR.joinpath('ui/build'), html=True), name='static')

with open('data/entries.json') as fh:
    entries = json.load(fh)

with open('data/measurements.json') as fh:
    measurements = json.load(fh)

with open('data/compensations.json') as fh:
    compensations = json.load(fh)


@app.get('/entries')
def get_entries():
    return entries


@app.get('/compensations')
def get_compensations():
    # return [{key: compensation[key] for key in ['name', 'label', 'compatible', 'recommended']} for compensation in compensations]
    return {compensation['label']: {key: compensation[key] for key in ['compatible', 'recommended']} for compensation in compensations}


class MeasurementData(BaseModel):
    frequency: list[float]
    raw: list[float]


class Optimizer(BaseModel):
    min_f: Optional[float]
    max_f: Optional[float]
    max_time: Optional[float]
    min_change_rate: Optional[float]
    min_std: Optional[float]


class FilterTypeEnum(str, Enum):
    LOW_SHELF = 'LOW_SHELF'
    HIGH_SHELF = 'HIGH_SHELF'
    PEAKING = 'PEAKING'


class Filter(BaseModel):
    type: Optional[str]
    min_fc: Optional[float]
    max_fc: Optional[float]
    min_q: Optional[float]
    max_q: Optional[float]
    min_gain: Optional[float]
    max_gain: Optional[float]


class PEQConfig(BaseModel):
    optimizer: Optimizer
    filter_defaults: Optional[Filter]
    filters: list[Filter]


class EqualizeRequest(BaseModel):
    measurement: Optional[MeasurementData]
    name: Optional[str]
    source: Optional[str]
    rig: Optional[str]
    compensation: Optional[Union[str, MeasurementData]]
    bass_boost_gain = DEFAULT_BASS_BOOST_GAIN
    bass_boost_fc = DEFAULT_BASS_BOOST_FC
    bass_boost_q = DEFAULT_BASS_BOOST_Q
    treble_boost_gain = DEFAULT_TREBLE_BOOST_GAIN
    treble_boost_fc = DEFAULT_TREBLE_BOOST_FC
    treble_boost_q = DEFAULT_TREBLE_BOOST_Q
    tilt = DEFAULT_TILT
    fs = DEFAULT_FS
    sound_signature: Optional[MeasurementData]
    max_gain = DEFAULT_MAX_GAIN
    window_size = DEFAULT_SMOOTHING_WINDOW_SIZE
    treble_window_size = DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE
    treble_f_lower = DEFAULT_TREBLE_F_LOWER
    treble_f_upper = DEFAULT_TREBLE_F_UPPER
    treble_gain_k = DEFAULT_TREBLE_GAIN_K
    parametric_eq = False
    parametric_eq_config: Optional[Union[str, PEQConfig, list[Union[str, PEQConfig]]]] = '8_PEAKING_WITH_SHELVES'
    fixed_band_eq = False
    fixed_band_eq_config: Optional[Union[str, PEQConfig]] = '10_BAND_GRAPHIC_EQ'
    graphic_eq = False
    preamp = DEFAULT_PREAMP

    @root_validator
    def only_one_eq_type(cls, values):
        assert values.get('measurement') or (values.get('name') and values.get('source') and values.get('rig'))
        keys = ['parametric_eq', 'fixed_band_eq', 'equalizer_apo_graphic_eq', 'convolution_eq']
        assert len([key for key in keys if values.get(key)]) < 2, 'Only one equalizer type is allowed'
        return values

    @validator('parametric_eq_config')
    def parametric_eq_config_name(cls, v):
        if type(v) == str:
            assert v in PEQ_CONFIGS, f'Unknown parametric eq config name "{v}"'
        if type(v) == list:
            for config in v:
                if type(config) == str:
                    assert config in PEQ_CONFIGS, f'Unknown parametric eq config name "{config}"'
        return v

    @validator('fixed_band_eq_config')
    def fixed_band_eq_config_name(cls, v):
        if type(v) == str:
            assert v in PEQ_CONFIGS, f'Unknown fixed band eq config name "{v}"'
        return v


@app.post('/equalize')
def equalize(req: EqualizeRequest):
    if req.measurement:  # Custom measurement data provided
        fr = FrequencyResponse(name='fr', frequency=req.measurement.frequency, raw=req.measurement.raw)
    else:  # Named measurement
        measurement = measurements[req.name][req.source][req.rig]
        fr = FrequencyResponse(name='fr', frequency=measurement['frequency'], raw=measurement['raw'])

    if req.compensation is None:
        fr.smoothen_fractional_octave(
            window_size=req.window_size,
            treble_window_size=req.treble_window_size,
            treble_f_lower=req.treble_f_lower,
            treble_f_upper=req.treble_f_upper
        )
        return {'fr': fr.to_dict()}
    elif type(req.compensation) == str:
        compensation = None
        for comp in compensations:
            if comp['label'] == req.compensation:
                compensation = comp
        if compensation is None:
            raise ValueError(f'Unknown compensation {req.compensation}')
        compensation = FrequencyResponse(
            name='compensation', frequency=compensation['fr']['frequency'], raw=compensation['fr']['raw'])
    else:
        compensation = FrequencyResponse(
            name='compensation', frequency=req.compensation.frequency, raw=req.compensation.raw)

    if req.sound_signature is not None:
        sound_signature = FrequencyResponse(
            name='sound signature', frequency=req.sound_signature.frequency, raw=req.sound_signature.raw)
    else:
        sound_signature = None

    fr.process(
        compensation=compensation,
        min_mean_error=True,
        bass_boost_gain=req.bass_boost_gain,
        bass_boost_fc=req.bass_boost_fc,
        bass_boost_q=req.bass_boost_q,
        treble_boost_gain=req.treble_boost_gain,
        treble_boost_fc=req.treble_boost_fc,
        treble_boost_q=req.treble_boost_q,
        tilt=req.tilt,
        fs=req.fs,
        sound_signature=sound_signature,
        max_gain=req.max_gain,
        window_size=req.window_size,
        treble_window_size=req.treble_window_size,
        treble_f_lower=req.treble_f_lower,
        treble_f_upper=req.treble_f_upper,
        treble_gain_k=req.treble_gain_k)

    res = {'fr': fr.to_dict()}

    if req.parametric_eq:
        parametric_eq_config = req.parametric_eq_config
        if type(parametric_eq_config) != list:
            parametric_eq_config = [parametric_eq_config]
        parametric_eq_config = [
            PEQ_CONFIGS[config] if type(config) == str else config.dict() for config in parametric_eq_config
        ]
        parametric_peqs = fr.optimize_parametric_eq(parametric_eq_config, req.fs, preamp=req.preamp)
        peq = parametric_peqs[0]
        peq.sort_filters()
        res.update({'parametric_eq': peq.to_dict()})
        peq_fr = FrequencyResponse(name='PEQ', frequency=peq.f, raw=peq.fr)
        peq_fr.interpolate()
        res['fr'].update({'parametric_eq': peq_fr.raw.tolist()})

    if req.fixed_band_eq:
        if type(req.fixed_band_eq_config) == str:
            fixed_band_eq_config = PEQ_CONFIGS[req.fixed_band_eq_config]
        else:
            fixed_band_eq_config = req.fixed_band_eq_config.dict()
        fixed_band_peqs = fr.optimize_fixed_band_eq(fixed_band_eq_config, req.fs, preamp=req.preamp)
        fixed_band_peq = fixed_band_peqs[0]
        fixed_band_peq.sort_filters()
        res.update({'fixed_band_eq': fixed_band_peq.to_dict()})
        fbpeq_fr = FrequencyResponse('FBPEQ', frequency=fixed_band_peq.f, raw=fixed_band_peq.fr)
        fbpeq_fr.interpolate()
        res['fr'].update({'fixed_band_eq': fbpeq_fr.raw.tolist()})

    if req.graphic_eq:
        graphic_eq = fr.eqapo_graphic_eq(normalize=True, preamp=req.preamp)
        res.update({'graphic_eq': graphic_eq})

    return res


class BitDepthEnum(int, Enum):
    PCM_16 = 16
    PCM_24 = 24
    PCM_32 = 32


class PhaseEnum(str, Enum):
    minimum = 'minimum'
    linear = 'linear'


class ConvolutionEqRequest(BaseModel):
    frequency: list[float]
    equalization: list[float]
    fs: int
    phase: PhaseEnum = DEFAULT_PHASE
    f_res: float = DEFAULT_F_RES
    preamp: float = DEFAULT_PREAMP
    bit_depth: int = DEFAULT_BIT_DEPTH
    stereo: bool = False


@app.post('/convolution_eq')
def convolution_eq(req: ConvolutionEqRequest):
    if req.bit_depth == 16:
        bit_depth = "PCM_16"
    elif req.bit_depth == 24:
        bit_depth = "PCM_24"
    elif req.bit_depth == 32:
        bit_depth = "PCM_32"
    else:
        raise ValueError('Invalid bit depth. Accepted values are 16, 24 and 32.')

    fr = FrequencyResponse(name='fir', frequency=req.frequency, equalization=req.equalization)
    if req.phase == PhaseEnum.minimum:
        fir = fr.minimum_phase_impulse_response(
            fs=req.fs, f_res=req.f_res, normalize=True, preamp=req.preamp)
    elif req.phase == PhaseEnum.linear:
        fir = fr.linear_phase_impulse_response(
            fs=req.fs, f_res=req.f_res, normalize=True, preamp=req.preamp)
    else:
        raise TypeError
    fir = np.tile(fir, (2, 1)).T if req.stereo else fir.T
    buf = BytesIO()
    sf.write(buf, fir, req.fs, bit_depth)

    return StreamingResponse(buf, media_type='audio/x-wav')
