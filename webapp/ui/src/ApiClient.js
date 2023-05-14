import {decode} from "base64-arraybuffer";
import {decodeFloat16, initConvolutionNode, initParametricEqNodes, transposeArrayToObject} from "./utils";

class ApiClient {
  static async fetchMeasurements() {
    const data = await fetch('/entries').then(res => res.json());
    const measurements = [];
    for (const [headphone, items] of Object.entries(data)) {
      measurements.push({label: headphone, ...items[0]});
    }
    return measurements;
  }

  static async fetchCompensations() {
    const compensations = await fetch('/compensations').then(res => res.json()).catch(err => {
      throw err;
    });
    const preferredCompensations = { 'unknown': { 'unknown': { 'unknown': 'Flat' } } };
    for (const compensation of compensations) {
      if (!compensation.recommended) {
        continue;
      }
      for (const measurementSource of compensation.recommended) {
        if (!preferredCompensations[measurementSource.source]) {
          preferredCompensations[measurementSource.source] = {};
        }
        if (!preferredCompensations[measurementSource.source][measurementSource.form]) {
          preferredCompensations[measurementSource.source][measurementSource.form] = {};
        }
        if (!preferredCompensations[measurementSource.source][measurementSource.form][measurementSource.rig]) {
          preferredCompensations[measurementSource.source][measurementSource.form][measurementSource.rig] = compensation.label;
        }
      }
    }
    return [compensations, preferredCompensations];
  }

  async equalize(params, audioContext) {
    if (params.trebleFLower > params.trebleFUpper) {
      throw new Error('trebleFLower is greater than trebleFUpper');
    }

    let soundSignature = transposeArrayToObject(params.soundSignature, ['frequency', 'raw']);

    const base64fp16 = true;
    const body = {
      compensation: params.compensation,
      sound_signature: soundSignature,
      sound_signature_smoothing_window_size: params.soundSignatureSmoothingWindowSize,
      bass_boost_gain: params.bassBoostGain,
      bass_boost_fc: params.bassBoostFc,
      bass_boost_q: params.bassBoostQ,
      treble_boost_gain: params.trebleBoostGain,
      treble_boost_fc: params.trebleBoostFc,
      treble_boost_q: params.trebleBoostQ,
      tilt: params.tilt,
      fs: params.fs,
      bit_depth: params.bitDepth,
      phase: params.phase,
      f_res: params.fRes,
      preamp: params.preamp,
      max_gain: params.maxGain,
      max_slope: params.maxSlope,
      window_size: params.windowSize,
      treble_window_size: params.trebleWindowSize,
      treble_f_lower: params.trebleFLower,
      treble_f_upper: params.trebleFUpper,
      treble_gain_k: params.trebleGainK,
      graphic_eq: params.equalizer?.type === 'graphic',
      parametric_eq: params.equalizer?.type === 'parametric',
      fixed_band_eq: params.equalizer?.type === 'fixedBand',
      convolution_eq: !['parametric', 'fixedBand'].includes(params.equalizer?.type),
      response: {
        fr_f_step: 1.02,
        fr_fields: params.smoothed
          ? ['frequency', 'smoothed', 'error_smoothed', 'target', 'equalization', 'equalized_smoothed']
          : ['frequency', 'raw', 'error', 'target', 'equalization', 'equalized_raw'],
        base64fp16: base64fp16
      }
    };

    if (params.selectedMeasurement.frequency?.length > 0) {
      body.measurement = {
        frequency: params.selectedMeasurement.frequency,
        raw: params.selectedMeasurement.raw,
      };
    } else {
      body.name = params.selectedMeasurement.label;
      body.source = params.selectedMeasurement.source;
      body.rig = params.selectedMeasurement.rig;
    }

    if (params.equalizer?.type === 'parametric') {
      if (typeof params.equalizer.config === 'string') {
        body.parametric_eq_config = params.equalizer.config;
      } else {
        if (!params.equalizer.config.filters.length) {
          return;
        }
        if (params.equalizer.config.optimizer.maxF !== null && params.equalizer.config.optimizer.minF > params.equalizer.config.optimizer.maxF) {
          return;
        }
        for (const filter of params.equalizer.config.filters) {
          if (
            (filter.maxFc !== null && filter.minFc > filter.maxFc) ||
            (filter.maxQ !== null && filter.minQ > filter.maxQ) ||
            (filter.maxGain !== null && filter.minGain > filter.maxGain)
          ) {
            return;
          }
        }
        body.parametric_eq_config = {
          optimizer: {
            min_f: params.equalizer.config.optimizer.minF,
            max_f: params.equalizer.config.optimizer.maxF,
            max_time: params.equalizer.config.optimizer.maxTime,
            min_change_rate: params.equalizer.config.optimizer.minChangeRate,
            min_std: params.equalizer.config.optimizer.minStd,
          },
          filters: params.equalizer.config.filters.map(filter => ({
            type: filter.type,
            fc: filter.fc, min_fc: filter.minFc, max_fc: filter.maxFc,
            q: filter.q, min_q: filter.minQ, max_q: filter.maxQ,
            gain: filter.gain, min_gain: filter.minGain, max_gain: filter.maxGain
          }))
        };
      }
    } else if (params.equalizer?.type === 'fixedBand') {
      body.fixed_band_eq_config = params.equalizer.config;
    }

    const apiRes = await fetch('/equalize', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body)
    });
    if (apiRes.status < 200 || apiRes.status >= 300) {
      const errorMessage = await apiRes.text();
      throw new Error(errorMessage);
    }
    const data = await apiRes.json();

    // Decode base64 encoded half-precision binary arrays
    const fr = {};
    for (const [key, val] of Object.entries(data.fr)) {
      if (base64fp16) {
        const uint16arr = new Uint16Array(decode(val));
        const arr = [];
        for (const x of uint16arr) {
          arr.push(decodeFloat16(x));
        }
        fr[key] = arr;
      } else {
        fr[key] = [ ...val ];
      }
    }

    const graphData = [];
    const keyMap = {
      frequency: 'frequency',
      raw: 'raw',
      error: 'error',
      smoothed: 'smoothed',
      error_smoothed: 'errorSmoothed',
      equalization: 'equalization',
      equalized_raw: 'equalizedRaw',
      equalized_smoothed: 'equalizedSmoothed',
      target: 'target',
      parametric_eq: 'parametricEq',
      fixed_band_eq: 'fixedBandEq',
    };

    if (!params.equalizer) {
      keyMap.equalization = null;
      keyMap.equalized_raw = null;
      keyMap.equalized_smoothed = null;
    } else if (params.equalizer?.type === 'parametric' && !!fr?.parametric_eq) {
      // Use parametric eq curve as the equalization in the frequency response graph
      keyMap.parametric_eq = 'equalization';
      keyMap.equalization = null;
    } else if (params.equalizer?.type === 'fixedBand' && !!fr?.fixed_band_eq) {
      // Use fixed band eq curve as the equalization in the frequency response graph
      keyMap.fixed_band_eq = 'equalization';
      keyMap.equalization = null;
    } else if (params.equalizer?.type === 'convolution' && !!fr?.convolution_eq) {
      // Use convolution eq curve as the equalization in the frequency response graph
      keyMap.convolution_eq = 'equalization';
      keyMap.equalization = null;
    }

    for (let i = 0; i < fr.frequency.length; ++i) {
      const dataPoint = {};
      for (const key of Object.keys(fr)) {
        if (keyMap[key] === null) {
          continue;
        }
        dataPoint[keyMap[key]] = fr[key][i];
      }
      graphData.push(dataPoint);
    }
    if (!!fr?.equalization) {
      for (let i = 0; i < graphData.length; ++i) {
        graphData[i].equalizedRaw = graphData[i].raw + graphData[i].equalization;
        graphData[i].equalizedSmoothed = graphData[i].smoothed + graphData[i].equalization;
      }
    }
    const res = { graphData };

    if (!!data.graphic_eq) {
      res.graphicEq = data.graphic_eq;
    }
    if (!params.equalizer) {
      res.eqNodes = [];
      res.preampGain = 1.0;
    } else if (!!data.parametric_eq) {
      res.parametricEq = data.parametric_eq;
      res.eqNodes = initParametricEqNodes(data.parametric_eq, audioContext);
      res.preampGain = 10 ** (data.parametric_eq.preamp / 20);
    } else if (!!data.fixed_band_eq) {
      res.fixedBandEq = data.fixed_band_eq;
      res.eqNodes = initParametricEqNodes(data.fixed_band_eq, audioContext);
      res.preampGain = 10 ** (data.fixed_band_eq.preamp / 20);
    } else if (!!data.fir) {
      await audioContext.decodeAudioData(decode(data.fir), (audioBuffer) => {
        res.firAudioBuffer = audioBuffer;
        const preamp = 10 ** (-Math.max(...fr.convolution_eq) / 20);
        // Add node for reverting preamp node when eq is activated because FIR filters are already normalized
        const unnormalizer = audioContext.createGain();
        unnormalizer.gain.value = 1 / preamp;
        res.eqNodes = [initConvolutionNode(audioBuffer, audioContext), unnormalizer];
        res.preampGain = preamp;
      });
    }

    return res;
  }
}

export default ApiClient;
