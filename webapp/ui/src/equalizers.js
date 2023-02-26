export default [
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
];
