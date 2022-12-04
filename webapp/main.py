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


class MeasurementData(BaseModel):
    frequency: str
    raw: str


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


class PhaseEnum(str, Enum):
    minimum = 'minimum'
    linear = 'linear'


class EqualizeRequest(BaseModel):
    measurement: Union[str, MeasurementData]
    compensation: Union[str, MeasurementData]
    bass_boost_gain = DEFAULT_BASS_BOOST_GAIN
    bass_boost_fc = DEFAULT_BASS_BOOST_FC
    bass_boost_q = DEFAULT_BASS_BOOST_Q
    treble_boost_gain = DEFAULT_TREBLE_BOOST_GAIN
    treble_boost_fc = DEFAULT_TREBLE_BOOST_FC
    treble_boost_q = DEFAULT_TREBLE_BOOST_Q
    tilt = DEFAULT_TILT
    fs = DEFAULT_FS
    sound_signature: Optional[Union[str, MeasurementData]] = None
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
    if type(req.measurement) == str:
        fr = FrequencyResponse.read_from_csv(ROOT_DIR.joinpath('measurements', f'{req.measurement}.csv'))
    else:
        fr = FrequencyResponse(name='fr', frequency=req.measurement.frequency, raw=req.measurement.raw)

    if type(req.compensation) == str:
        compensation = FrequencyResponse.read_from_csv(ROOT_DIR.joinpath('compensation', f'{req.compensation}.csv'))
    else:
        compensation = FrequencyResponse(
            name='compensation', frequency=req.compensation.frequency, raw=req.compensation.raw)

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
        sound_signature=req.sound_signature,
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
        parametric_peqs = [peq.to_dict() for peq in parametric_peqs]
        res.update({'parametric_eq': parametric_peqs})

    if req.fixed_band_eq:
        if type(req.fixed_band_eq_config) == str:
            fixed_band_eq_config = PEQ_CONFIGS[req.fixed_band_eq_config]
        else:
            fixed_band_eq_config = req.fixed_band_eq_config.dict()
        fixed_band_peq = fr.optimize_fixed_band_eq(fixed_band_eq_config, req.fs, preamp=req.preamp)
        fixed_band_peq = fixed_band_peq.to_dict()
        res.update({'fixed_band_eq': fixed_band_peq})

    if req.graphic_eq:
        graphic_eq = fr.eqapo_graphic_eq(normalize=True, preamp=req.preamp)
        res.update({'graphic_eq': graphic_eq})

    return res


class BitDepthEnum(int, Enum):
    PCM_16 = 16
    PCM_24 = 24
    PCM_32 = 32


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
