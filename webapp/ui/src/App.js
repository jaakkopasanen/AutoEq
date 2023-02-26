import React from 'react';
import FrequencyResponseGraph from './FrequencyResponseGraph';
import {
  Alert, Box,
  Container,
  Grid, IconButton,
  Paper, Snackbar, styled, Typography,
} from '@mui/material';
import FileOpenOutlinedIcon from '@mui/icons-material/FileOpenOutlined';
import ClearIcon from '@mui/icons-material/Clear';
import TopBar from './TopBar';
import TargetTab from './TargetTab';
import EqTab from './EqTab';
import cloneDeep from 'lodash/cloneDeep';
import find from 'lodash/find';
import findIndex from 'lodash/findIndex';
import merge from 'lodash/merge';
import {decode} from 'base64-arraybuffer';
import {
  windows as isWindows,
  android as isAndroid,
  linux as isLinux,
  macos as isMacos,
  ios as isIos
} from 'platform-detect'
import {decodeFloat16} from './utils';
import Player from './Player';
import Waves from './Waves';

const SmPaper = styled(Paper)(({ theme }) => ({
  [theme.breakpoints.down('sm')]: {
    borderRadius: 0,
    boxShadow: 'none',
    borderBottom: '1px dashed #aaa',
    paddingLeft: theme.spacing(1),
    paddingRight: theme.spacing(1),
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  background: 'rgba(255, 255, 255, 0.97)',
  backdropFilter: 'blur(3px)',
}));

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
      showInfo: true,

      soundProfiles: [],
      selectedSoundProfile: null,

      compensations: [],
      // Sound signatures preferred for each measurement rig: {source: {form: {rig: label}}
      preferredCompensations: [],
      selectedCompensation: null, // Name (label) of the currently selected compensation.

      soundSignature: null,  // Sound signature { frequency, raw }
      soundSignatureSmoothingWindowSize: 0.0,  // Smoothing window size for sound signature

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

    if (window.localStorage.getItem('soundProfiles')) {
      this.state.soundProfiles = JSON.parse(window.localStorage.getItem('soundProfiles'));
    }

    this.equalizeTimer = null;
    this.fetchMeasurements = this.fetchMeasurements.bind(this);
    this.equalize = this.equalize.bind(this);
    this.onMeasurementSelected = this.onMeasurementSelected.bind(this);
    this.onMeasurementCreated = this.onMeasurementCreated.bind(this);
    this.onSmoothedChanged = this.onSmoothedChanged.bind(this);
    this.onEqParamChanged = this.onEqParamChanged.bind(this);
    this.fetchCompensations = this.fetchCompensations.bind(this);
    this.captureSoundProfile = this.captureSoundProfile.bind(this);
    this.onSoundProfileSelected = this.onSoundProfileSelected.bind(this);
    this.onSoundProfileCreated = this.onSoundProfileCreated.bind(this);
    this.onSoundProfileSaved = this.onSoundProfileSaved.bind(this);
    this.onSoundProfileDeleted = this.onSoundProfileDeleted.bind(this);
    this.onCompensationSelected = this.onCompensationSelected.bind(this);
    this.onCompensationCreated = this.onCompensationCreated.bind(this);
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
    this.onError = this.onError.bind(this);
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
    for (const compensation of compensations) {
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
          preferredCompensations[rigPath[0]][rigPath[1]][rigPath[2]] = compensation.label;
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

    if (this.state.trebleFLower > this.state.trebleFUpper) {
      return;
    }

    const selectedEqualizer = find(this.state.equalizers, (eq) => eq.label === this.state.selectedEqualizer);

    let soundSignature = null;
    if (this.state.soundSignature !== null && this.state.soundSignature.length > 0) {
      soundSignature = { frequency: [], raw: []};
      for (let i = 0; i < this.state.soundSignature.length; ++i) {
        soundSignature.frequency.push(this.state.soundSignature[i].frequency);
        soundSignature.raw.push(this.state.soundSignature[i].raw);
      }
    }

    const selectedCompensation = find(this.state.compensations, (compensation) => compensation.label === this.state.selectedCompensation);
    const compensation = selectedCompensation.frequency?.length > 0
      ? {
          frequency: selectedCompensation.frequency,
          raw: selectedCompensation.raw
        }
      : this.state.selectedCompensation;  // Named compensation, sending just a string

    const base64fp16 = true;
    const body = {
      compensation: compensation,
      sound_signature: soundSignature,
      sound_signature_smoothing_window_size: this.state.soundSignatureSmoothingWindowSize,
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
        if (selectedEqualizer.config.optimizer.maxF !== null && selectedEqualizer.config.optimizer.minF > selectedEqualizer.config.optimizer.maxF) {
          return;
        }
        for (const filter of selectedEqualizer.config.filters) {
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
            min_f: selectedEqualizer.config.optimizer.minF,
            max_f: selectedEqualizer.config.optimizer.maxF,
            max_time: selectedEqualizer.config.optimizer.maxTime,
            min_change_rate: selectedEqualizer.config.optimizer.minChangeRate,
            min_std: selectedEqualizer.config.optimizer.minStd,
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

    if (!selectedEqualizer) {
      keyMap.equalization = null;
      keyMap.equalized_raw = null;
      keyMap.equalized_smoothed = null;
    } else if (selectedEqualizer?.type === 'parametric' && !!fr?.parametric_eq) {
      // Use parametric eq curve as the equalization in the frequency response graph
      keyMap.parametric_eq = 'equalization';
      keyMap.equalization = null;
    } else if (selectedEqualizer?.type === 'fixedBand' && !!fr?.fixed_band_eq) {
      // Use fixed band eq curve as the equalization in the frequency response graph
      keyMap.fixed_band_eq = 'equalization';
      keyMap.equalization = null;
    } else if (selectedEqualizer?.type === 'convolution' && !!fr?.convolution_eq) {
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
    const newState = { graphData };

    for (const eqNode of this.eqNodes) {
      eqNode.disconnect();
    }

    if (!!data.graphic_eq) {
      newState.graphicEq = data.graphic_eq;
    }
    if (!selectedEqualizer) {
      this.eqNodes = [];
      this.preampNode.gain.value = 1.0;
    } else if (!!data.parametric_eq) {
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
        const preamp = 10 ** (-Math.max(...fr.convolution_eq) / 20);
        // Add node for reverting preamp node when eq is activated because FIR filters are already normalized
        const unnormalizer = this.audioContext.createGain();
        unnormalizer.gain.value = 1 / preamp;
        this.eqNodes = [this.initConvolutionNode(audioBuffer), unnormalizer];
        this.preampNode.gain.value = preamp;
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

  onMeasurementSelected(measurement) {
    if (measurement === null) {
      this.setState({
        selectedMeasurement: null,
        graphData: null
      });
      return;
    }

    // TODO: not preferred for any?
    const compensationLabel = this.state.preferredCompensations[measurement.source][measurement.form][measurement.rig];
    const compensation = find(this.state.compensations, (c) => c.label === compensationLabel);
    this.setState({
      showInfo: false,
      selectedMeasurement: { ...measurement },
      selectedCompensation: compensationLabel,
      bassBoostFc: compensation.bassBoost.fc,
      bassBoostQ: compensation.bassBoost.q,
      bassBoostGain: compensation.bassBoost.gain,
    }, () => {
      this.equalize(true);
    });
  }

  onMeasurementCreated(name, dataPoints) {
    const measurements = cloneDeep(this.state.measurements);
    const frequency = [];
    const raw = [];
    for (const dataPoint of dataPoints) {
      frequency.push(dataPoint.frequency);
      raw.push(dataPoint.raw);
    }
    const measurement = {
      label: name,
      form: 'unknown',
      rig: 'unknown',
      source: 'unknown',
      frequency, raw
    };
    measurements.splice(0, 0, measurement);
    this.setState({ measurements }, () => {
      this.onMeasurementSelected(measurement);
    });
  }

  onSmoothedChanged(val) {
    this.setState({smoothed: val}, () => {
      this.equalize(true);
    });
  }

  onSoundProfileSelected(name) {
    const newState = cloneDeep(find(this.state.soundProfiles, (p) => p.name === name));
    delete newState.name;
    newState.selectedSoundProfile = name;
    this.setState(newState, () => {
      this.equalize(true);
    });
  }

  captureSoundProfile() {
    const keys = [
      'selectedCompensation', 'preferredCompensations',
      'soundSignature', 'soundSignatureSmoothingWindowSize',
      'bassBoostGain', 'bassBoostFc', 'bassBoostQ',
      'trebleBoostGain', 'trebleBoostFc', 'trebleBoostQ',
      'tilt', 'maxGain',
      'windowSize', 'trebleWindowSize', 'trebleFLower', 'trebleFUpper', 'trebleGainK',
    ];
    const profile = {};
    for (const key of keys) {
      profile[key] = this.state[key];
    }
    return cloneDeep(profile);
  }

  onSoundProfileCreated() {
    const newSoundProfile = this.captureSoundProfile();
    const soundProfiles = cloneDeep(this.state.soundProfiles);
    newSoundProfile.name = soundProfiles.length;
    soundProfiles.push(newSoundProfile);
    window.localStorage.setItem('soundProfiles', JSON.stringify(soundProfiles));
    this.setState({ soundProfiles }, () => {
      this.onSoundProfileSelected(newSoundProfile.name);
    });
  }

  onSoundProfileSaved(name) {
    const profile = this.captureSoundProfile();
    profile.name = name;
    const soundProfiles = cloneDeep(this.state.soundProfiles);
    const ix = findIndex(soundProfiles, (p) => p.name === name);
    soundProfiles[ix] = profile;
    window.localStorage.setItem('soundProfiles', JSON.stringify(soundProfiles));
    this.setState({ soundProfiles });
  }

  onSoundProfileDeleted(name) {
    const soundProfiles = cloneDeep(this.state.soundProfiles);
    const ix = findIndex(soundProfiles, (p) => p.name === name);
    soundProfiles.splice(ix, 1);
    window.localStorage.setItem('soundProfiles', JSON.stringify(soundProfiles));
    this.setState({ soundProfiles });
  }

  onCompensationSelected(compensation) {
    const preferredCompensations = cloneDeep(this.state.preferredCompensations);
    preferredCompensations[this.state.selectedMeasurement.source][this.state.selectedMeasurement.form][this.state.selectedMeasurement.rig] = compensation.label;
    this.setState(
      {
        selectedCompensation: compensation.label,
        preferredCompensations,
        bassBoostFc: compensation.bassBoost.fc,
        bassBoostQ: compensation.bassBoost.q,
        bassBoostGain: compensation.bassBoost.gain,
      },
      () => { this.equalize(true); }
    );
  }

  onCompensationCreated(name, dataPoints) {
    const compensations = cloneDeep(this.state.compensations);
    const frequency = [];
    const raw = [];
    for (const dataPoint of dataPoints) {
      frequency.push(dataPoint.frequency);
      raw.push(dataPoint.raw);
    }
    compensations.push({
      label: name,
      frequency, raw,
      compatible: [],
      recommended: [],
      bassBoost: {
        fc: 105,
        q: 0.7,
        gain: 0.0
      }
    });
    this.setState({ compensations }, () => {
      this.onCompensationSelected(name);
    })
  }

  onEqParamChanged(newParams) {
    const preferredCompensations = cloneDeep(this.state.preferredCompensations);
    const compensations = cloneDeep(this.state.compensations);
    const compensationLabel = preferredCompensations[this.state.selectedMeasurement.source][this.state.selectedMeasurement.form][this.state.selectedMeasurement.rig];
    const ix = findIndex(compensations, (c) => c.label === compensationLabel);
    for (const [key, val] of Object.entries(newParams)) {
      if (key === 'bassBoostFc') {
        compensations[ix].bassBoost.fc = val;
      } else  if (key === 'bassBoostQ') {
        compensations[ix].bassBoost.q = val;
      } else if (key === 'bassBoostGain') {
        compensations[ix].bassBoost.gain = val;
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
    equalizer.config.filters.push({ type: 'PEAKING', fc: null, q: null, gain: null, minFc: null, maxFc: null, minQ: null, maxQ: null, minGain: null, maxGain: null});
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

  onError(err) {
    this.setState({ isSnackbarOpen: true, snackbarMessage: err.toString()});
  }

  render() {
    const customPeq = find(
      this.state.equalizers,
      (equalizer) => equalizer.label === 'Custom Parametric Eq');
    const customPeqConfig = !!customPeq ? customPeq.config : null;
    const platform = isWindows ? 'Windows' : isMacos ? 'Mac OS' : isLinux ? 'Linux' : isAndroid ? 'Android' : isIos ? 'OSX' : null;  // TODO
    const recommendedApp = {
      'Windows': 'EqualizerAPO GraphicEq',
      'Mac OS': 'Sound Source',
      'Linux': 'EasyEffects',
      'Android': 'Wavelet',
      'iOS': null,
    }[platform];
    return (
      <Box sx={{pt: 10, pb: {xs: 12, md: 6}}}>
        <Waves nWaves={10} />

        {(!!this.state.graphData && !this.state.showInfo) && (
          <Container fixed
            sx={{
              pl: {xs: 0, sm: 2, md: 3},
              pr: {xs: 0, sm: 1, md: 3},
            }}
          >
            <Grid container direction='column' rowSpacing={{xs: 0, sm: 1, md: 2}}>
              <Grid item>
                <SmPaper
                  sx={{
                    pt: 1,
                    pl: {xs: 1, sm: 0, md: 0},
                    pr: {xs: 0, sm: 1, md: 0},
                    pb: {xs: 1, sm: 0.5, md: 0}
                  }}
                >
                  <FrequencyResponseGraph
                    data={this.state.graphData}
                    smoothed={this.state.smoothed}
                    onSmoothedChanged={this.onSmoothedChanged}
                  />
                </SmPaper>
              </Grid>
              <Grid item container direction='row' columnSpacing={{xs: 0, sm: 1, md: 2}} rowSpacing={1} alignItems='stretch'>
                <Grid item xs={12} md={6}>
                  <SmPaper sx={{p: {sm: 1, md: 2}}}>
                    <TargetTab
                      selectedMeasurement={this.state.selectedMeasurement}

                      soundProfiles={this.state.soundProfiles}
                      selectedSoundProfile={this.state.selectedSoundProfile}
                      onSoundProfileSelected={this.onSoundProfileSelected}
                      onSoundProfileCreated={this.onSoundProfileCreated}
                      onSoundProfileSaved={this.onSoundProfileSaved}
                      onSoundProfileDeleted={this.onSoundProfileDeleted}
                      captureSoundProfile={this.captureSoundProfile}

                      compensations={this.state.compensations}
                      selectedCompensation={this.state.selectedCompensation}
                      onCompensationSelected={this.onCompensationSelected}
                      onCompensationCreated={this.onCompensationCreated}

                      soundSignature={this.state.soundSignature}
                      soundSignatureSmoothingWindowSize={this.state.soundSignatureSmoothingWindowSize}

                      graphData={this.state.graphData}
                      smoothed={this.state.smoothed}

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
                      onEqParamChanged={this.onEqParamChanged}

                      onError={this.onError}
                    />
                  </SmPaper>
                </Grid>
                <Grid item xs={12} md={6}>
                  <SmPaper sx={{p: {sm: 1, md: 2}}}>
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
                  </SmPaper>
                </Grid>
              </Grid>
            </Grid>
          </Container>
        )}

        <Container
          fixed
          sx={{
            display: (!!this.state.showInfo || !this.state.graphData) ? 'block' : 'none',
            color: theme => theme.palette.grey.A400
          }}
        >
          <IconButton
            onClick={() => this.setState({ showInfo: false })}
            sx={{
              position: 'absolute', right: 0, top: theme => theme.spacing(10),
              display: !!this.state.graphData ? 'block' : 'none',
              color: theme => theme.palette.grey.A400
            }}
          >
            <ClearIcon />
          </IconButton>
          <Grid
            container direction='column' alignItems='center' rowSpacing={8}
            sx={{'& p': {pb: theme => theme.spacing(1)}}}
          >
            <Grid item sx={{textAlign: 'center', mt: '96px'}}>
              <Typography variant='h1'>AutoEq</Typography>
              <Typography variant='body2'>makes your headphones sound better</Typography>
            </Grid>
            <Grid item container direction='row' columnSpacing={4} rowSpacing={4} justifyContent='center'>
              <Grid item xs={12} sm={4} sx={{textAlign: 'left'}}>
                <Typography variant='h4' sx={{textAlign: 'center'}}>Step 1</Typography>
                <Typography variant='body2'>Choose your headphone make and model from the top.</Typography>
                <Typography variant='body2'>
                  You can also import your own data by dragging and dropping a CSV file to the select field or clicking
                  <FileOpenOutlinedIcon sx={{display: 'inline', height: '17px', width: '16px', transform: 'translate(-1px, 3px)'}} />
                  to select a CSV file on your device.
                </Typography>
              </Grid>
              <Grid item xs={12} sm={4}>
                <Typography variant='h4' sx={{textAlign: 'center'}}>Step 2</Typography>
                <Typography variant='body2'>Choose an equalizer app you wish to use.</Typography>
                <Typography variant='body2'>
                  AutoEq doesn't do the live equalization for your device and so you need a separate equalizer app to
                  do this. AutoEq will produce optimal settings for the app.
                </Typography>
                {platform === 'iOS' && (
                  <Typography variant='body2'>
                    Unfortunately there are no system-wide equalizer apps available for iOS since the devices block app
                    from accessing audio stream of other apps. You can choose iTunes built-in equalizer if you use
                    iTunes but for example with Spotify you're largely out of luck. You may want to look into hardware
                    based solutions such as Qudelix-5K or MiniDSP IL-DSP.
                  </Typography>
                )}
                {platform !== 'iOS' && (
                  <Typography variant='body2'>
                    The recommended equalizer app for <b>{platform}</b> is&nbsp;
                    <b>{recommendedApp}</b> but you are free to use other apps too. AutoEq supports any kind of equalizer and the most
                    popular apps are already listed. For others you can use the generic Graphic Equalizer, Parametric
                    Equalizer or Convolution Equalizer options.
                  </Typography>
                )}
              </Grid>
              <Grid item xs={12} sm={4}>
                <Typography variant='h4' sx={{textAlign: 'center'}}>Step 3</Typography>
                <Typography variant='body2'>Hear the difference with the live demo.</Typography>
                <Typography variant='body2'>
                  Play some songs with player on the bottom and toggle EQ on and off to hear the difference.
                </Typography>
                <Typography variant='body2'>
                  AutoEq simulates the chosen equalizer app so the results should be almost identical to what you'll
                  hear with the app.
                </Typography>
              </Grid>
            </Grid>
          </Grid>
        </Container>

        <Box sx={{position: 'fixed', top: 0, left: 0, width: '100%', padding: 0, background: '#fff'}}>
          <Paper sx={{
            padding: '8px 16px',
            borderRadius: 0,
            background: (theme) => theme.palette.background.default}}
          >
            <TopBar
              onShowInfoClicked={() => this.setState({ showInfo: !this.state.showInfo })}
              selectedMeasurement={this.state.selectedMeasurement}
              isMeasurementSelected={!!this.state.selectedMeasurement}
              measurements={this.state.measurements}
              onMeasurementSelected={this.onMeasurementSelected}
              onMeasurementCreated={this.onMeasurementCreated}
              onError={this.onError}
            />
          </Paper>
        </Box>

        <Box
          sx={{
            position: 'fixed', bottom: theme => theme.spacing(1),
            width: {xs: '252px', sm: '574px', md: '594px'},
            left: {xs: 'calc((100% - 252px) / 2)', sm: 'calc((100% - 574px) / 2)', md: 'calc((100% - 594px) / 2)'}
          }}>
          <Player
            audioContext={this.audioContext}
            audioDestination={this.gainNode}
            gain={this.state.gain}
            onGainChange={this.onGainChange}
            onIsEqOnChange={this.onIsEqOnChange}
            isEqEnabled={this.eqNodes.length > 0 && this.state.selectedEqualizer !== null}
          />
        </Box>

        <Box>
          <Snackbar
            open={this.state.isSnackbarOpen}
            onClose={() => { this.setState({ isSnackbarOpen: false }); }}
            sx={{background: theme => theme.palette.background.default}}
            anchorOrigin={{ vertical: 'top', horizontal: 'center'}}
          >
            <Alert
              onClose={() => { this.setState({ isSnackbarOpen: false }); }}
              severity='error' variant='outlined' sx={{ width: '100%'}}
            >
              {this.state.snackbarMessage}
            </Alert>
          </Snackbar>
        </Box>
      </Box>
    );
  }
}

export default App;
