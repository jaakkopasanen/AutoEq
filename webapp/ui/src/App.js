import React from 'react';
import FrequencyResponseGraph from './FrequencyResponseGraph';
import {
  Alert,
  Container,
  Grid,
  Paper, Snackbar,
} from '@mui/material';
import TopBar from './TopBar';
import TargetTab from './TargetTab';
import EqTab from './EqTab';
import cloneDeep from 'lodash/cloneDeep';
import find from 'lodash/find';
import findIndex from 'lodash/findIndex';
import merge from 'lodash/merge';
import {decode} from 'base64-arraybuffer';
import {decodeFloat16} from "./utils";
import Player from './Player';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.audioContext = new AudioContext();
    this.gainNode = this.audioContext.createGain();
    this.gainNode.gain.value = 0.5;
    this.preampNode = this.audioContext.createGain();
    this.preampNode.gain.value = 1.0;
    this.preampNode.connect(this.audioContext.destination);
    this.gainNode.connect(this.preampNode);
    this.eqNodes = [];

    this.state = {
      isSnackbarOpen: false,
      snackbarMessage: '',

      compensations: [],
      // Sound signatures preferred for each measurement rig: {source: {form: {rig: label}}
      preferredCompensations: [],
      selectedCompensation: null, // Name (label) of the currently selected compensation.

      soundSignatures: [], // Sound signatures
      selectedSoundSignature: null, // Currently selected sound signature

      measurements: null, // { label, source, form, rig }
      selectedMeasurement: null, // { label, source, form, rig }
      graphData: null, // Data for the frequency response graph

      equalizers: [
        { label: '10-band Graphic Eq', type: 'fixedBand', config: '10_BAND_GRAPHIC_EQ' },
        { label: '31-band Graphic Eq', type: 'fixedBand', config: '31_BAND_GRAPHIC_EQ' },
        {
          label: 'AUNBandEq', type: 'parametric', config: 'AUNBANDEQ',
          uiConfig: {
            bw: true, showDownload: false,
            filterNames: { LOW_SHELF: 'Low Shelf', PEAKING: 'Parametric', HIGH_SHELF: 'High Shelf', PREAMP: 'Global Gain' },
            columnNames: { fc: 'Freq', gain: 'Gain (dB)', q: 'Width' }
          }
        },
        { label: 'Convolution Eq', type: 'convolution' },
        {
          label: 'Custom Parametric Eq', type: 'parametric',
          uiConfig: { showDownload: true },
          config: {
            optimizer: { minF: null, maxF: null, maxTime: 0.5, minChangeRate: null, minStd: null },
            filterDefaults: { type: 'PEAKING', minFc: null, maxFc: null, minQ: null, maxQ: null, minGain: null, maxGain: null },
            filters: []
          },
        },
        { label: 'EasyEffects / PulseEffects', type: 'convolution' },
        { label: 'eqMac (Advanced Equalizer)', type: 'fixedBand', config: '10_BAND_GRAPHIC_EQ' },
        { label: 'eqMac (Expert Equalizer)', type: 'parametric', config: '8_PEAKING_WITH_SHELVES' },
        { label: 'EqualizerAPO GraphicEq', type: 'graphic' },
        {
          label: 'EqualizerAPO ParametricEq / Peace', type: 'parametric', config: '8_PEAKING_WITH_SHELVES',
          uiConfig: {
            bw: false, showDownload: true,
            filterNames: { LOW_SHELF: 'Low-shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High-shelf', PREAMP: 'Preamplification' },
            columnNames: { fc: 'Center frequency (Hz)', gain: 'Gain (dB)', q: 'Q factor' }
          }
        },
        { label: 'iTunes built-in equalizer', type: 'fixedBand', config: '10_BAND_GRAPHIC_EQ' },
        { label: 'JamesDSP', type: 'convolution' },
        { label: 'RootlessJamesDSP', type: 'convolution' },
        {
          label: 'MiniDSP 2x4HD', type: 'parametric', config: 'MINIDSP_2X4HD',
          uiConfig: {
            bw: false, showDownload: false,
            filterNames: { LOW_SHELF: 'LOW_SHELF', PEAKING: 'PEAK', HIGH_SHELF: 'HIGH_SHELF', PREAMP: 'Preamp' },
            columnNames: { fc: 'Frequency', gain: 'Gain', q: 'Q' }
          },
        },
        {
          label: 'MiniDSP IL-DSP', type: 'parametric', config: 'MINIDSP_IL_DSP',
          uiConfig: {
            bw: false, showDownload: false, showPreampControl: true,
            filterNames: { LOW_SHELF: 'LOW_SHELF', PEAKING: 'PEAK', HIGH_SHELF: 'HIGH_SHELF', PREAMP: 'Preamp' },
            columnNames: { fc: 'Frequency', gain: 'Gain', q: 'Q' },
          },
        },
        {
          label: 'Neutron Music Player', type: 'parametric', config: 'NEUTRON_MUSIC_PLAYER',
          uiConfig: {
            bw: false, showDownload: false,
            filterNames: { LOW_SHELF: 'Low-shelf', PEAKING: 'Peak EQ', HIGH_SHELF: 'High-shelf', PREAMP: 'Preamp' },
            columnNames: { fc: 'Center frequency (Hz)', gain: 'Gain (dB)', q: 'Q' }
          },
        },
        {
          label: 'Poweramp Equalizer', type: 'parametric', config: 'POWERAMP_EQUALIZER',
          uiConfig: {
            bw: false, showDownload: false,
            filterNames: { LOW_SHELF: 'Low Shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High Shelf', PREAMP: 'Preamp' },
            columnNames: { fc: 'Freq', gain: 'Gain', q: 'Q' }
          }
        },
        {
          label: 'Qudelix-5K', type: 'parametric', config: 'QUDELIX_5K',
          uiConfig: {
            bw: false, showDownload: false,
            filterNames: { LOW_SHELF: 'LSHELF', PEAKING: 'PEAK', HIGH_SHELF: 'HSHELF', PREAMP: 'PRE GAIN(dB)' },
            columnNames: { fc: 'FREQ(Hz)', gain: 'GAIN(db)', q: 'Q' }
          }
        },
        {
          label: 'SoundSource', type: 'parametric', config: '8_PEAKING_WITH_SHELVES',
          uiConfig: {
            bw: false, showDownload: true,
            filterNames: { LOW_SHELF: 'Low Shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High Shelf', PREAMP: 'Preamp' },
            columnNames: { fc: 'Frequency (Hz)', gain: 'Gain (dB)', q: 'Q' }
          }
        },
        {
          label: 'Spotify built-in equalizer', type: 'fixedBand', config: 'SPOTIFY',
        },
        {
          label: 'USB Audio Player PRO', type: 'parametric', config: 'USB_AUDIO_PLAYER_PRO',
          uiConfig: {
            bw: false, showDownload: false,
            filterNames: { LOW_SHELF: 'Low shelf', PEAKING: 'Analog bell', HIGH_SHELF: 'High shelf', PREAMP: 'Preamp' },
            columnNames: { fc: 'Frequency (Hz)', gain: 'Gain (dB)', q: 'Q factor' }
          }
        },
        { label: 'Viper4Android', type: 'convolution' },
        { label: 'Wavelet', type: 'graphic' },
      ],
      selectedEqualizer: null, // Name (label) of the currently selected equalizer app

      smoothed: true,

      // Request parameters
      bassBoostGain: 0.0,
      bassBoostFc: 105.0,
      bassBoostQ: 0.7,
      trebleBoostGain: 0.0,
      trebleBoostFc: 10000.0,
      trebleBoostQ: 0.7,
      tilt: 0.0,
      maxGain: 12.0,
      windowSize: 0.08,
      trebleWindowSize: 2.0,
      trebleFLower: 6000.0,
      trebleFUpper: 8000.0,
      trebleGainK: 1.0,
      fs: this.audioContext.sampleRate,
      bitDepth: 16,
      phase: 'minimum',
      fRes: 16.0,
      preamp: 0.0,

      graphicEq: null,
      parametricEq: null,
      fixedBandEq: null,
      firAudioBuffer: null,

      gain: this.gainNode.gain.value * 100,
      isEqOn: false,
    };
    this.equalizeTimer = null;
    this.fetchMeasurements = this.fetchMeasurements.bind(this);
    this.equalize = this.equalize.bind(this);
    this.onMeasurementSelected = this.onMeasurementSelected.bind(this);
    this.onMeasurementCreated = this.onMeasurementCreated.bind(this);
    this.onMeasurementUpdated = this.onMeasurementUpdated.bind(this);
    this.onSmoothedChanged = this.onSmoothedChanged.bind(this);
    this.onSoundSignatureSelected = this.onSoundSignatureSelected.bind(this);
    this.onSoundSignatureCreated = this.onSoundSignatureCreated.bind(this);
    this.onSoundSignatureUpdated = this.onSoundSignatureUpdated.bind(this);
    this.onEqParamChanged = this.onEqParamChanged.bind(this);
    this.fetchCompensations = this.fetchCompensations.bind(this);
    this.onCompensationSelected = this.onCompensationSelected.bind(this);
    this.onEqualizerSelected = this.onEqualizerSelected.bind(this);
    this.onCustomPeqConfigChanged = this.onCustomPeqConfigChanged.bind(this);
    this.onCustomPeqConfigFilterChanged = this.onCustomPeqConfigFilterChanged.bind(this);
    this.onCustomPeqAddFilterClick = this.onCustomPeqAddFilterClick.bind(this);
    this.onCustomPeqDeleteFilterClick = this.onCustomPeqDeleteFilterClick.bind(this);
    this.onGainChange = this.onGainChange.bind(this);
    this.onIsEqOnChange = this.onIsEqOnChange.bind(this);
    this.initParametricEqNodes = this.initParametricEqNodes.bind(this);
    this.initConvolutionNode = this.initConvolutionNode.bind(this);
    this.connectEqNodes = this.connectEqNodes.bind(this);
    this.disconnectEqNodes = this.disconnectEqNodes.bind(this);
  }

  async fetchMeasurements() {
    const data = await fetch('/entries').then(res => res.json()).catch((err) => {
      throw err;
    });
    const measurements = [];
    for (const [headphone, items] of Object.entries(data)) {
      measurements.push({label: headphone, ...items[0]});
    }
    this.setState({measurements: measurements});
  }

  async fetchCompensations() {
    const compensations = await fetch('/compensations').then(res => res.json()).catch(err => {
      throw err;
    });
    const preferredCompensations = { 'unknown': { 'unknown': { 'unknown': 'Flat' } } };
    for (const [label, compensation] of Object.entries(compensations)) {
      if (!compensation.recommended) {
        continue;
      }
      for (const rigPath of compensation.recommended) {
        if (!preferredCompensations[rigPath[0]]) {
          preferredCompensations[rigPath[0]] = {};
        }
        if (!preferredCompensations[rigPath[0]][rigPath[1]]) {
          preferredCompensations[rigPath[0]][rigPath[1]] = {};
        }
        if (!preferredCompensations[rigPath[0]][rigPath[1]][rigPath[2]]) {
          preferredCompensations[rigPath[0]][rigPath[1]][rigPath[2]] = label;
        }
      }
    }
    this.setState({ compensations, preferredCompensations });
  }

  componentDidMount() {
    this.fetchMeasurements();
    this.fetchCompensations();
  }

  async equalize(skipTimer) {
    if (!!this.equalizeTimer) clearTimeout(this.equalizeTimer);
    if (!skipTimer) {
      this.equalizeTimer = setTimeout(() => { this.equalize(true); }, 500);
      return;
    }

    const soundSignature = !!this.state.selectedSoundSignature ? { ...this.state.selectedSoundSignature } : null;
    let soundSignatureSmoothingWindowSize;
    if (!!soundSignature) {
      delete soundSignature.label;
      soundSignatureSmoothingWindowSize = soundSignature.smoothingWindowSize;
      delete soundSignature.smoothingWindowSize;
    }

    const selectedEqualizer = find(this.state.equalizers, (eq) => eq.label === this.state.selectedEqualizer);

    const base64fp16 = false;

    const body = {
      compensation: this.state.selectedCompensation,
      sound_signature: soundSignature,
      sound_signature_smoothing_window_size: soundSignatureSmoothingWindowSize,
      bass_boost_gain: this.state.bassBoostGain,
      bass_boost_fc: this.state.bassBoostFc,
      bass_boost_q: this.state.bassBoostQ,
      treble_boost_gain: this.state.trebleBoostGain,
      treble_boost_fc: this.state.trebleBoostFc,
      treble_boost_q: this.state.trebleBoostQ,
      tilt: this.state.tilt,
      fs: this.state.fs,
      bit_depth: this.state.bitDepth,
      phase: this.state.phase,
      f_res: this.state.fRes,
      preamp: this.state.preamp,
      max_gain: this.state.maxGain,
      window_size: this.state.windowSize,
      treble_window_size: this.state.trebleWindowSize,
      treble_f_lower: this.state.trebleFLower,
      treble_f_upper: this.state.trebleFUpper,
      treble_gain_k: this.state.trebleGainK,
      graphic_eq: selectedEqualizer?.type === 'graphic',
      parametric_eq: selectedEqualizer?.type === 'parametric',
      fixed_band_eq: selectedEqualizer?.type === 'fixedBand',
      convolution_eq: !['parametric', 'fixedBand'].includes(selectedEqualizer?.type),
      response: {
        fr_f_step: 1.02,
        fr_fields: this.state.smoothed
          ? ['frequency', 'smoothed', 'error_smoothed', 'target', 'equalization', 'equalized_smoothed']
          : ['frequency', 'raw', 'error', 'target', 'equalization', 'equalized_raw'],
        base64fp16: base64fp16
      }
    };

    if (this.state.selectedMeasurement.frequency?.length > 0) {
      body.measurement = {
        frequency: this.state.selectedMeasurement.frequency,
        raw: this.state.selectedMeasurement.raw,
      };
    } else {
      body.name = this.state.selectedMeasurement.label;
      body.source = this.state.selectedMeasurement.source;
      body.rig = this.state.selectedMeasurement.rig;
    }

    if (selectedEqualizer?.type === 'parametric') {
      if (typeof selectedEqualizer.config === 'string') {
        body.parametric_eq_config = selectedEqualizer.config;
      } else {
        if (!selectedEqualizer.config.filters.length) {
          return;
        }
        body.parametric_eq_config = {
          optimizer: {
            min_f: selectedEqualizer.config.optimizer.minF,
            max_f: selectedEqualizer.config.optimizer.maxF,
            max_time: selectedEqualizer.config.optimizer.maxTime,
            min_change_rate: selectedEqualizer.config.optimizer.minChangeRate,
            min_std: selectedEqualizer.config.optimizer.minStd,
          },
          filter_defaults: {
            type: selectedEqualizer.config.filterDefaults.type,
            min_fc: selectedEqualizer.config.filterDefaults.minFc,
            max_fc: selectedEqualizer.config.filterDefaults.maxFc,
            min_q: selectedEqualizer.config.filterDefaults.minQ,
            max_q: selectedEqualizer.config.filterDefaults.maxQ,
            min_gain: selectedEqualizer.config.filterDefaults.minGain
          },
          filters: selectedEqualizer.config.filters.map(filter => ({
            type: filter.type,
            fc: filter.fc, min_fc: filter.minFc, max_fc: filter.maxFc,
            q: filter.q, min_q: filter.minQ, max_q: filter.maxQ,
            gain: filter.gain, min_gain: filter.minGain, max_gain: filter.maxGain
          }))
        };
      }
    } else if (selectedEqualizer?.type === 'fixedBand') {
      body.fixed_band_eq_config = selectedEqualizer.config;
    }

    const data = await fetch('/equalize', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body)
    }).then(async res => {
      if (res.status >= 200 && res.status < 300) {
        return res.json();
      }
      let errorMessage;
      errorMessage = JSON.stringify((await res.json()), null, 4);
      this.setState({ isSnackbarOpen: true, snackbarMessage: errorMessage});
      throw new Error(errorMessage);
    });

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
    if (selectedEqualizer?.type === 'parametric' && !!fr?.parametric_eq) {
      // Use parametric eq curve as the equalization in the frequency response graph
      keyMap.parametric_eq = 'equalization';
      keyMap.equalization = null;
    } else if (selectedEqualizer?.type === 'fixedBand' && !!fr?.fixed_band_eq) {
      // Use fixed band eq curve as the equalization in the frequency response graph
      keyMap.fixed_band_eq = 'equalization';
      keyMap.equalization = null;
    } else if (selectedEqualizer?.type === 'convolution' && !!fr?.convolution_eq) {
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
    const newState = { graphData };

    for (const eqNode of this.eqNodes) {
      eqNode.disconnect();
    }

    if (!!data.graphic_eq) {
      newState.graphicEq = data.graphic_eq;
    }
    if (!!data.parametric_eq) {
      newState.parametricEq = cloneDeep(data.parametric_eq);
      this.eqNodes = this.initParametricEqNodes(data.parametric_eq);
      this.preampNode.gain.value = 10 ** (data.parametric_eq.preamp / 20);
    } else if (!!data.fixed_band_eq) {
      newState.fixedBandEq = cloneDeep(data.fixed_band_eq);
      this.eqNodes = this.initParametricEqNodes(data.fixed_band_eq);
      this.preampNode.gain.value = 10 ** (data.fixed_band_eq.preamp / 20);
    } else if (!!data.fir) {
      await this.audioContext.decodeAudioData(decode(data.fir), (audioBuffer) => {
        newState.firAudioBuffer = audioBuffer;
        this.eqNodes = [this.initConvolutionNode(audioBuffer)];
        this.preampNode.gain.value = 10 ** (Math.max(...data.fr.convolution_eq) / 20);
      });
    }
    if (this.state.isEqOn) {
      this.connectEqNodes();
    } else {
      this.disconnectEqNodes();
    }
    this.setState(newState);
  }

  initParametricEqNodes(parametricEq) {
    const biquadNodes = [];
    const typeMap = { 'LOW_SHELF': 'lowshelf', 'HIGH_SHELF': 'highshelf', 'PEAKING': 'peaking' }
    for (const filter of parametricEq.filters) {
      const node = this.audioContext.createBiquadFilter();
      node.type = typeMap[filter.type];
      node.frequency.value = filter.fc;
      node.Q.value = filter.q;
      node.gain.value = filter.gain;
      if (biquadNodes.length > 0) {
        // Connect subsequent node to this one
        biquadNodes[biquadNodes.length - 1].connect(node);
      }
      biquadNodes.push(node);
    }
    return biquadNodes;
  }

  initConvolutionNode(audioBuffer) {
    const node = this.audioContext.createConvolver();
    node.normalize = false;
    node.buffer = audioBuffer;
    return node;
  }

  connectEqNodes() {
    const nodes = [this.preampNode, ...this.eqNodes, this.audioContext.destination];
    for (let i = 0; i < nodes.length - 1; ++i) {
      nodes[i].disconnect();
      nodes[i].connect(nodes[i + 1]);
    }
  }

  disconnectEqNodes() {
    for (const node of [this.preampNode, ...this.eqNodes]) {
      node.disconnect();
    }
    this.preampNode.connect(this.audioContext.destination);
  }

  async onMeasurementSelected(measurement) {
    if (measurement === null) {
      this.setState({
        selectedMeasurement: null,
        graphData: null
      });
      return;
    }

    // TODO: not preferred for any?
    const compensationLabel = this.state.preferredCompensations[measurement.source][measurement.form][measurement.rig];
    this.setState({
      selectedMeasurement: { ...measurement },
      selectedCompensation: compensationLabel,
      bassBoostFc: this.state.compensations[compensationLabel].bassBoost.fc,
      bassBoostQ: this.state.compensations[compensationLabel].bassBoost.q,
      bassBoostGain: this.state.compensations[compensationLabel].bassBoost.gain,
    }, () => {
      this.equalize(true);
    });
  }

  onMeasurementCreated(name, frequency, raw) {
    const measurements = cloneDeep(this.state.measurements);
    const measurement = {
      label: name,
      form: 'unknown',
      rig: 'unknown',
      source: 'unknown',
      frequency, raw
    };
    measurements.push(measurement);
    this.setState({ measurements }, () => {
      this.onMeasurementSelected(measurement);
    });
  }

  onMeasurementUpdated(label, name, frequency, raw) {
    const measurements = cloneDeep(this.state.measurements);
    const ix = findIndex(measurements, (measurement) => measurement.label === label);
    const measurement = { ...measurements[ix], label: name };
    if (!!frequency.length > 0) {
      measurement.frequency = frequency;
    }
    if (raw.length > 0) {
      measurement.raw = raw;
    }
    measurements[ix] = measurement;
    this.setState({ measurements }, () => {
      this.onMeasurementSelected(measurement);
    });
  }

  onSmoothedChanged(val) {
    this.setState({smoothed: val}, () => {
      this.equalize(true);
    });
  }

  onCompensationSelected(label) {
    const preferredCompensations = cloneDeep(this.state.preferredCompensations);
    preferredCompensations[this.state.selectedMeasurement.source][this.state.selectedMeasurement.form][this.state.selectedMeasurement.rig] = label;
    this.setState(
      {
        selectedCompensation: label,
        preferredCompensations,
        bassBoostFc: this.state.compensations[label].bassBoost.fc,
        bassBoostQ: this.state.compensations[label].bassBoost.q,
        bassBoostGain: this.state.compensations[label].bassBoost.gain,
      },
      () => { this.equalize(true); }
    );
  }

  onSoundSignatureSelected(soundSignature) {
    this.setState({ selectedSoundSignature: soundSignature }, () => {
      if (soundSignature?.label !== 'Add new') {
        this.equalize(true);
      }
    });
  }

  onSoundSignatureCreated(name, frequency, raw, smoothingWindowSize) {
    const soundSignatures = cloneDeep(this.state.soundSignatures);
    const soundSignature = { label: name, frequency, raw, smoothingWindowSize };
    soundSignatures.push(soundSignature);
    this.setState(
      { selectedSoundSignature: soundSignature, soundSignatures },
      () => { this.equalize(true); }
    );
  }

  onSoundSignatureUpdated(label, name, frequency, raw, smoothingWindowSize) {
    const soundSignatures = cloneDeep(this.state.soundSignatures);
    const soundSignature = { label: name, frequency, raw, smoothingWindowSize };
    const ix = findIndex(soundSignatures, (ss) => ss.label === label);
    soundSignatures[ix] = soundSignature;
    this.setState(
      { selectedSoundSignature: soundSignature, soundSignatures },
      () => { this.equalize(true); });
  }

  onEqParamChanged(newParams) {
    const preferredCompensations = cloneDeep(this.state.preferredCompensations);
    const compensations = cloneDeep(this.state.compensations);
    const compensationLabel = preferredCompensations[this.state.selectedMeasurement.source][this.state.selectedMeasurement.form][this.state.selectedMeasurement.rig];
    for (const [key, val] of Object.entries(newParams)) {
      if (key === 'bassBoostFc') {
        compensations[compensationLabel].bassBoost.fc = val;
      } else  if (key === 'bassBoostQ') {
        compensations[compensationLabel].bassBoost.q = val;
      } else if (key === 'bassBoostGain') {
        compensations[compensationLabel].bassBoost.gain = val;
      }
    }
    this.setState({ ...newParams, preferredCompensations, compensations }, () => {
      this.equalize();
    });
  }

  onEqualizerSelected(val) {
    if (val === null) {
      this.setState({ selectedEqualizer: null });
    } else {
      this.setState({ selectedEqualizer: val }, () => {
        this.equalize(true);
      });
    }
  }

  onCustomPeqConfigChanged(newParams) {
    const equalizers = cloneDeep(this.state.equalizers); // Ensure immutability
    // Find custom parametric eq in the equalizers array
    const ix = findIndex(equalizers, (equalizer) => equalizer.label === 'Custom Parametric Eq');
    const equalizer = equalizers[ix];
    equalizer.config = merge(equalizers[ix].config, newParams);
    // Update custom parametric eq and replace in the array
    equalizers.splice(ix, 1, equalizer);
    this.setState({ equalizers }, () => {
      this.equalize();
    });
  }

  onCustomPeqConfigFilterChanged(newParams, i) {
    const equalizers = cloneDeep(this.state.equalizers); // Ensure immutability
    // Find custom parametric eq in the equalizers array
    const ix = findIndex(equalizers, (equalizer) => equalizer.label === 'Custom Parametric Eq');
    const equalizer = equalizers[ix];
    const filter = merge(equalizer.config.filters[i], newParams);
    equalizer.config.filters.splice(i, 1, filter);
    equalizers.splice(ix, 1, equalizer);
    this.setState({ equalizers }, () => {
      this.equalize();
    });
  }

  onCustomPeqAddFilterClick() {
    const equalizers = cloneDeep(this.state.equalizers); // Ensure immutability
    // Find custom parametric eq in the equalizers array
    const ix = findIndex(equalizers, (equalizer) => equalizer.label === 'Custom Parametric Eq');
    const equalizer = equalizers[ix];
    equalizer.config.filters.push({ fc: null, q: null, gain: null, minFc: null, maxFc: null, minQ: null, maxQ: null, minGain: null, maxGain: null});
    equalizers.splice(ix, 1, equalizer);
    this.setState({ equalizers }, () => {
      this.equalize();
    });
  }

  onCustomPeqDeleteFilterClick(i) {
    const equalizers = cloneDeep(this.state.equalizers); // Ensure immutability
    // Find custom parametric eq in the equalizers array
    const ix = findIndex(equalizers, (equalizer) => equalizer.label === 'Custom Parametric Eq');
    const equalizer = equalizers[ix];
    equalizer.config.filters.splice(i, 1);
    this.setState({ equalizers }, () => {
      this.equalize();
    });
  }

  onGainChange(val) {
    this.gainNode.gain.value = val / 100;
    this.setState({ gain: val });
  }

  onIsEqOnChange(val) {
    this.setState({ isEqOn: val });
    if (!val) {  // Disable Eq
      this.disconnectEqNodes();
    } else {  // Enable Eq
      this.connectEqNodes();
    }
  }

  render() {
    const customPeq = find(
      this.state.equalizers,
      (equalizer) => equalizer.label === 'Custom Parametric Eq');
    const customPeqConfig = !!customPeq ? customPeq.config : null;
    return (
      <Grid container direction='column' rowSpacing={{xs: 1, md: 2}} sx={{pb: 8}}>
        <Grid item sx={{width: '100%', padding: 0, background: '#fff'}}>
          <Paper sx={{padding: 1, borderRadius: 0, background: (theme) => theme.palette.background.default}}>
            <TopBar
              selectedMeasurement={this.state.selectedMeasurement}
              isMeasurementSelected={!!this.state.selectedMeasurement}
              measurements={this.state.measurements}
              onMeasurementSelected={this.onMeasurementSelected}
              onMeasurementCreated={this.onMeasurementCreated}
              onMeasurementUpdated={this.onMeasurementUpdated}
            />
          </Paper>
        </Grid>
        {!!this.state.graphData && (
          <Grid item>
            <Container sx={{pl: {xs: 0, sm: 2}, pr: {xs: 0, sm: 2}}}>
              <Grid container direction='column' rowSpacing={{xs: 1, sm: 2}}>
                <Grid item>
                  <Paper
                    sx={{pt: 1, pl: {xs: 1, sm: 2, md: 0}, pr: {xs: 1, sm: 2, md: 0}, pb: {xs: 1, sm: 2, md: 0}}}
                  >
                    <FrequencyResponseGraph
                      data={this.state.graphData}
                      smoothed={this.state.smoothed}
                      onSmoothedChanged={this.onSmoothedChanged}
                    />
                  </Paper>
                </Grid>
                <Grid item container direction='row' columnSpacing={{xs: 1, sm: 2}} alignItems='stretch'>
                  <Grid item xs={6}>
                    <Paper sx={{p: {xs: 1, sm: 2}}}>
                      <TargetTab
                        compensations={Object.keys(this.state.compensations)}
                        selectedCompensation={this.state.selectedCompensation}
                        soundSignatures={this.state.soundSignatures}
                        selectedSoundSignature={this.state.selectedSoundSignature}
                        selectedMeasurement={this.state.selectedMeasurement}
                        graphData={this.state.graphData}
                        bassBoostGain={this.state.bassBoostGain}
                        bassBoostFc={this.state.bassBoostFc}
                        bassBoostQ={this.state.bassBoostQ}
                        trebleBoostGain={this.state.trebleBoostGain}
                        trebleBoostFc={this.state.trebleBoostFc}
                        trebleBoostQ={this.state.trebleBoostQ}
                        tilt={this.state.tilt}
                        maxGain={this.state.maxGain}
                        windowSize={this.state.windowSize}
                        trebleWindowSize={this.state.trebleWindowSize}
                        trebleFLower={this.state.trebleFLower}
                        trebleFUpper={this.state.trebleFUpper}
                        trebleGainK={this.state.trebleGainK}
                        onSoundSignatureSelected={this.onSoundSignatureSelected}
                        onSoundSignatureCreated={this.onSoundSignatureCreated}
                        onSoundSignatureUpdated={this.onSoundSignatureUpdated}
                        onEqParamChanged={this.onEqParamChanged}
                        onCompensationSelected={this.onCompensationSelected}
                      />
                    </Paper>
                  </Grid>
                  <Grid item xs={6}>
                    <Paper sx={{p: {xs: 1, sm: 2}}}>
                      <EqTab
                        selectedMeasurement={this.state.selectedMeasurement?.label}
                        equalizers={this.state.equalizers}
                        selectedEqualizer={this.state.selectedEqualizer}
                        onEqualizerSelected={this.onEqualizerSelected}
                        graphicEq={this.state.graphicEq}
                        parametricEq={this.state.parametricEq}
                        fixedBandEq={this.state.fixedBandEq}
                        firAudioBuffer={this.state.firAudioBuffer}
                        fs={this.state.fs}
                        bitDepth={this.state.bitDepth}
                        phase={this.state.phase}
                        fRes={this.state.fRes}
                        preamp={this.state.preamp}
                        onEqParamChanged={this.onEqParamChanged}
                        customPeqConfig={customPeqConfig}
                        onCustomPeqConfigChanged={this.onCustomPeqConfigChanged}
                        onCustomPeqConfigFilterChanged={this.onCustomPeqConfigFilterChanged}
                        onCustomPeqAddFilterClick={this.onCustomPeqAddFilterClick}
                        onCustomPeqDeleteFilterClick={this.onCustomPeqDeleteFilterClick}
                      />
                    </Paper>
                  </Grid>
                </Grid>
              </Grid>
            </Container>
          </Grid>
        )}
        <Grid
          item sx={{position: 'fixed', bottom: theme => theme.spacing(1), width: '100%'}}
          container direction='column' justifyContent='center' alignItems='center'
        >
          <Player
            audioContext={this.audioContext}
            audioDestination={this.gainNode}
            gain={this.state.gain}
            onGainChange={this.onGainChange}
            onIsEqOnChange={this.onIsEqOnChange}
            isEqEnabled={this.eqNodes.length > 0}
          />
        </Grid>
        <Grid item>
          <Snackbar
            open={this.state.isSnackbarOpen}
            onClose={() => { this.setState({ isSnackBarOpen: false }); }}
            sx={{background: theme => theme.palette.background.default}}
          >
            <Alert
              onClose={() => { this.setState({ isSnackBarOpen: false }); }}
              severity='error' variant='outlined' sx={{ width: '100%'}}
            >
              {this.state.snackbarMessage}
            </Alert>
          </Snackbar>
        </Grid>
      </Grid>
    );
  }
}

export default App;
