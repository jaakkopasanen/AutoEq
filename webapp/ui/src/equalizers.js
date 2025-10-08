export default [
  {
    label: '10-band Graphic Eq',
    type: 'fixedBand',
    config: '10_BAND_GRAPHIC_EQ',
    uiConfig: { showFsControl: false },
    instructions: 'Adjust the sliders in your equalizer app to match the gain values. Set preamp to given value if that option is available in the app.'
  },
  {
    label: '31-band Graphic Eq',
    type: 'fixedBand',
    config: '31_BAND_GRAPHIC_EQ',
    uiConfig: { showFsControl: false },
    instructions: 'Adjust the sliders in your equalizer app to match the gain values. Set preamp to given value if that option is available in the app.'
  },
  {
    label: 'AUNBandEq', type: 'parametric', config: 'AUNBANDEQ',
    uiConfig: {
      bw: true, showDownload: false, showFsControl: false,
      filterNames: { LOW_SHELF: 'Low Shelf', PEAKING: 'Parametric', HIGH_SHELF: 'High Shelf', PREAMP: 'Global Gain' },
      columnNames: { fc: 'Freq', gain: 'Gain (dB)', q: 'Width' }
    },
    eqParams: { fs: 192000 },
    instructions: 'Configure filter types, frequencies, widths and gains manually. You can ignore the shelf filter widths here since AUNBandEq has fixed width shelf filters that match the produced filters.'
  },
  {
    label: 'Convolution Eq',
    type: 'convolution',
    instructions: 'Download the file and import to the equalizer app'
  },
  {
    label: 'Custom Parametric Eq', type: 'parametric',
    uiConfig: { showDownload: true, showFsControl: true },
    config: {
      optimizer: { minF: null, maxF: 10000, maxTime: 0.5, minChangeRate: null, minStd: null },
      filters: [
        { type: 'LOW_SHELF', fc: null, minFc: 105, maxFc: 105, gain: null, minGain: null, maxGain: null, q: null, minQ: 0.7, maxQ: 0.7},
        { type: 'PEAKING', fc: null, minFc: null, maxFc: null, gain: null, minGain: null, maxGain: null, q: null, minQ: null, maxQ: null},
        { type: 'PEAKING', fc: null, minFc: null, maxFc: null, gain: null, minGain: null, maxGain: null, q: null, minQ: null, maxQ: null},
        { type: 'PEAKING', fc: null, minFc: null, maxFc: null, gain: null, minGain: null, maxGain: null, q: null, minQ: null, maxQ: null},
        { type: 'HIGH_SHELF', fc: null, minFc: 10000, maxFc: 10000, gain: null, minGain: null, maxGain: null, q: null, minQ: 0.7, maxQ: 0.7},
      ]
    },
    instructions:
      <div>
        <p style={{marginTop: 0}}>Custom parametric eq allows you to fully control what kind of set of parametric filters will be produced.</p>
        <p style={{marginBottom: 0}}>Add filters, configure their types and allowed ranges for center frequency (Fc), gain and quality (Q).</p>
        <p>Download a file the app supports EqualizerAPO file format or configure the filters in the app manually.</p>
      </div>
  },
  {
    label: 'Contour EQ (Chrome Extension)',
    type: 'parametric',
    config: '8_PEAKING_WITH_SHELVES',
    uiConfig: { showDownload: true, showFsControl: true },
    fileFormatter: (preamp, filters, name) => {
      const filterTypeMap = {
        "PEAKING": "peaking",
        "LOW_SHELF": "lowshelf",
        "HIGH_SHELF": "highshelf"
      }

      return JSON.stringify({
        [name]: {
          bands: filters.map(filter => ({
            frequency: filter.fc,
            gain: filter.gain,
            Q: filter.q,
            type: filterTypeMap[filter.type]
          })),
          preampGain: preamp,
          presetName: name
        }
      }, null, 2);
    },
    fileName: (name) => {
      return `${name} Contour EQ.json`
    },
    instructions: 'Download the file, open Contour, click "Import" and select the downloaded file. Preset will now appear under the Presets dropdown.'
  },
  {
    label: 'EasyEffects',
    type: 'parametric',
    config: '8_PEAKING_WITH_SHELVES',
    uiConfig: { showFsControl: true, showDownload: true },
    instructions: 'Download the file and click "APO" below "Import Preset" in Equalizer plugin in EasyEffects'
  },
  {
    label: 'eqMac (Advanced Equalizer)',
    type: 'fixedBand',
    config: '10_BAND_GRAPHIC_EQ',
    uiConfig: { showFsControl: false },
    instructions: 'Adjust the sliders in eqMac to match the gain values',
  },
  {
    label: 'eqMac (Expert Equalizer)',
    type: 'parametric',
    config: '8_PEAKING_WITH_SHELVES',
    uiConfig: { showFsControl: true },
    instructions: 'Configure frequency, gain and quality (Q) for each band manually on Expert tab'
  },
  {
    label: 'EqualizerAPO GraphicEq',
    type: 'graphic',
    instructions: 'Download the file to "C:\\Program Files\\EqualizerAPO\\config\\", open "Configuration Editor" app, add a filter "Control > Include" and select the file with 📁.'
  },
  {
    label: 'EqualizerAPO ParametricEq', type: 'parametric', config: '8_PEAKING_WITH_SHELVES',
    uiConfig: {
      bw: false, showDownload: true, showFsControl: true,
      filterNames: { LOW_SHELF: 'Low-shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High-shelf', PREAMP: 'Preamplification' },
      columnNames: { fc: 'Center frequency (Hz)', gain: 'Gain (dB)', q: 'Q factor' }
    },
    instructions: 'Download the file to "C:\\Program Files\\EqualizerAPO\\config\\", open "Configuration Editor" app, add a filter "Control > Include" and select the file with 📁.'
  },
  {
    label: 'iTunes built-in equalizer',
    type: 'fixedBand',
    config: '10_BAND_GRAPHIC_EQ',
    uiConfig: { showFsControl: false },
    instructions: 'Adjust the sliders in the equalizer to match the gain values and set Preamp'
  },
  { label: 'JamesDSP', type: 'convolution' },
  { label: 'RootlessJamesDSP', type: 'convolution' },
  {
    label: 'MiniDSP 2x4HD', type: 'parametric', config: 'MINIDSP_2X4HD',
    uiConfig: {
      bw: false, showDownload: false, showFsControl: true,
      filterNames: { LOW_SHELF: 'LOW_SHELF', PEAKING: 'PEAK', HIGH_SHELF: 'HIGH_SHELF', PREAMP: 'Preamp' },
      columnNames: { fc: 'Frequency', gain: 'Gain', q: 'Q' }
    },
    instructions: 'Configure frequency, gain and quality (Q) for each band manually with Parametric EQ'
  },
  {
    label: 'MiniDSP IL-DSP', type: 'parametric', config: 'MINIDSP_IL_DSP',
    uiConfig: {
      bw: false, showDownload: false, showPreampControl: true, showFsControl: false,
      filterNames: { LOW_SHELF: 'LOW_SHELF', PEAKING: 'PEAK', HIGH_SHELF: 'HIGH_SHELF', PREAMP: 'Preamp' },
      columnNames: { fc: 'Frequency', gain: 'Gain', q: 'Q' },
    },
    instructions: 'Configure frequency, gain and quality (Q) for each band manually with Parametric EQ. IL-DSP doesn\'t have preamp control and therefore to prevent clipping, can adjust preamp slider here until the requested preamp at the bottom of the produced settings gives a slightly positive value.'
  },
  {
    label: 'Moondrop Free DSP', type: 'parametric', config: 'MOONDROP_FREE_DSP',
    uiConfig: {
      bw: false, showDownload: false, showPreampControl: true, showFsControl: false,
      filterNames: { LOW_SHELF: 'Low-shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High-shelf', PREAMP: 'Preamp' },
      columnNames: { fc: 'Freq', gain: 'Gain', q: 'Q' },
    },
    instructions: 'Configure frequency, gain and quality (Q) for each band manually with Parametric EQ, as accurately as the app allows. Free DSP doesn\'t have preamp control and therefore to prevent clipping, can adjust preamp slider here until the requested preamp at the bottom of the produced settings gives a slightly positive value.'
  },
  {
    label: 'Neutron Music Player', type: 'parametric', config: 'NEUTRON_MUSIC_PLAYER',
    uiConfig: {
      bw: false, showDownload: false, showFsControl: false,
      filterNames: { LOW_SHELF: 'Low-shelf', PEAKING: 'Peak EQ', HIGH_SHELF: 'High-shelf', PREAMP: 'Preamp' },
      columnNames: { fc: 'Center frequency (Hz)', gain: 'Gain (dB)', q: 'Q' }
    },
    eqParams: { fs: 48000 },
    instructions: 'Go to ⚙ > Playback > DSP Effect > Equalizer, change the band count in ⚙️ and configure frequency, gain and Q for each band and change the filter types from band\'s ⚙️.'
  },
  {
    label: 'Peace', type: 'parametric', config: '8_PEAKING_WITH_SHELVES',
    uiConfig: {
      bw: false, showDownload: true, showFsControl: true,
      filterNames: { LOW_SHELF: 'Low-shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High-shelf', PREAMP: 'Pre Amplifying' },
      columnNames: { fc: 'Frequency', gain: 'Gain', q: 'Quality (Q)' },
    },
    instructions: 'Download file and import it to Peace by clicking "📁 Import" button'
  },
  {
    label: 'Poweramp Equalizer', type: 'parametric', config: 'POWERAMP_EQUALIZER',
    uiConfig: {
      bw: false, showDownload: false, showFsControl: false,
      filterNames: { LOW_SHELF: 'Low Shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High Shelf', PREAMP: 'Preamp' },
      columnNames: { fc: 'Freq', gain: 'Gain', q: 'Q' }
    },
    instructions: 'Enable Parametric equalizer in the settings. Configure frequency, gain and quality (Q) for each band manually and set preamp.'
  },
  {
    label: 'Qudelix-5K', type: 'parametric', config: 'QUDELIX_5K',
    uiConfig: {
      bw: false, showDownload: false, showFsControl: true,
      filterNames: { LOW_SHELF: 'LSHELF', PEAKING: 'PEAK', HIGH_SHELF: 'HSHELF', PREAMP: 'PRE GAIN(dB)' },
      columnNames: { fc: 'FREQ(Hz)', gain: 'GAIN(db)', q: 'Q' }
    },
    instructions: 'Configure frequency, gain and quality (Q) for each band manually on Equalizer tab'
  },
  {
    label: 'Rockbox', type: 'parametric', config: '8_PEAKING_WITH_SHELVES',
    uiConfig: {
      bw: false, showDownload: true, showFsControl: true,
      filterNames: { LOW_SHELF: 'Low Shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High Shelf', PREAMP: 'Pre-cut' },
    },
    instructions: 'Download the file, move it to the device and load it by clicking "Browse EQ Presets"',
    fileFormatter: (preamp, filters) => {
      const filterTypes = {
        'LOW_SHELF': 'low shelf',
        'PEAKING': 'peak',
        'HIGH_SHELF': 'high shelf'
      };
      const lines = [
        'eq enabled: on',
        `eq precut: ${Math.max(0, Math.round(preamp * -10)).toFixed(0)}`,
      ];
      for (const [i, filt] of filters?.entries()) {
        let line = `eq ${filterTypes[filt.type]} filter`;
        if (filt.type === 'PEAKING') {
          line += ` ${i}`
        }
        line += `: ${Math.round(filt.fc).toFixed(0)}, `;
        line += `${Math.round(filt.q * 10).toFixed(0)}, `;
        line += `${Math.round(filt.gain * 10).toFixed(0)}`;
        lines.push(line);
      }
      return lines.join('\n');
    },
    fileName: (name) => {
      return `${name} Rockbox.cfg`
    }
  },
  {
    label: 'SoundSource', type: 'parametric', config: '8_PEAKING_WITH_SHELVES',
    uiConfig: {
      bw: false, showDownload: true, showFsControl: true,
      filterNames: { LOW_SHELF: 'Low Shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High Shelf', PREAMP: 'Preamp' },
      columnNames: { fc: 'Frequency (Hz)', gain: 'Gain (dB)', q: 'Q' }
    },
    instructions: 'Download file and import to SoundSource from Headphone EQ menu by selecting "Add Other Profile..."',
    fileFormatter: (preamp, filters) => {
      const typeMap = { LOW_SHELF: 'LS', PEAKING: 'PK', HIGH_SHELF: 'HS' };
      let s = `Preamp: ${preamp?.toFixed(2)} dB\n`
      for (const [i, filt] of filters?.entries()) {
        s += `Filter ${i + 1}: ON ${typeMap[filt.type]} Fc ${filt.fc.toFixed(1)} Hz Gain ${filt.gain.toFixed(1)} dB Q ${filt.q.toFixed(2)}\n`
      }
      return s;
    }
  },
  {
    label: 'Spotify built-in equalizer',
    type: 'fixedBand',
    config: 'SPOTIFY',
    uiConfig: { showFsControl: false },
    instructions: 'Use Spotify\'s built-in equalizer only as the last resort! Go to Settings and adjust the Equalizer sliders to match the gain values'
  },
  {
    label: 'USB Audio Player PRO', type: 'parametric', config: 'USB_AUDIO_PLAYER_PRO',
    uiConfig: {
      bw: false, showDownload: false, showFsControl: true,
      filterNames: { LOW_SHELF: 'Low shelf', PEAKING: 'Analog bell', HIGH_SHELF: 'High shelf', PREAMP: 'Preamp' },
      columnNames: { fc: 'Frequency (Hz)', gain: 'Gain (dB)', q: 'Q factor' }
    },
    instructions: 'Configure frequency, gain and quality (Q) for each band manually in Toneboosters'
  },
  {
    label: 'Viper4Android',
    type: 'convolution',
    instructions: 'Download the file to "/ViPER4Android/Kernel" on your phone. Then select the file under "Convolver" in the app.'
  },
  {
    label: 'Voicemeeter', type: 'parametric', config: '4_PEAKING_WITH_SHELVES',
    uiConfig: {
      bw: false, showDownload: true, showFsControl: true,
    },
    instructions: 'Download the file and import it to Voicemeeter by opening the EQ window for a channel and right clicking the top bar and selecting "Load EQ Settings"',
    fileFormatter: (preamp, filters) => {
      const filterTypes = {
        'LOW_SHELF': '5',
        'PEAKING': '0',
        'HIGH_SHELF': '6'
      };
      const lines = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<VBAudioVoicemeeterBUSEQConfig>',
        '<VoiceMeeterBUSEQ>'
      ];
      for (let channel = 1; channel < 9; ++channel) {
        for (const [i, filt] of filters?.entries()) {
          lines.push(`<Bus index="1" channel="${channel}" cell="${i+1}" EQon="1" EQtype="${filterTypes[filt.type]}" dblevel="${filt.gain.toFixed(2)}" freq="${filt.fc.toFixed(2)}" Q="${filt.q.toFixed(2)}" />`);
        }
      }
      lines.push('</VoiceMeeterBUSEQ>');
      lines.push('</VBAudioVoicemeeterBUSEQConfig>');
      return lines.join('\n');
    },
    fileName: (name) => {
      return `${name} Voicemeeter.xml`
    }
  },
  {
    label: 'Wavelet',
    type: 'graphic',
    instructions: 'Download the file on your phone and import to Wavelet by selecting AutoEq, clicking the headphone name and then Import button'
  },
];
