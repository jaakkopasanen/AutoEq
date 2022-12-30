import React from 'react';
import FrequencyResponseGraph from './FrequencyResponseGraph';
import {
  Container,
  Grid,
  Paper,
} from "@mui/material";
import TopBar from "./TopBar";
import TargetTab from "./TargetTab";
import EqTab from "./EqTab";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      compensations: [],
      preferredCompensations: [], // Sound signatures preferred for each measurement rig
      selectedCompensation: null, // Name (label) of the currently selected compensation. TODO: Custom compensation?

      soundSignatures: [{label: 'Add new', frequency: [], raw: []}], // Sound signatures
      selectedSoundSignature: null, // Currently selected sound signature

      measurements: null, // { label, source, form, rig }
      selectedMeasurement: null, // Currently selected measurement
      graphData: null, // Data for the frequency response graph

      equalizers: [
        {label: 'Wavelet', type: 'graphic'},
        {label: 'EqualizerAPO GraphicEq', type: 'graphic'},
        //{label: 'EqualizerAPO ParametricEq', type: 'parametric', config: '8_PEAKING_WITH_SHELVES'},
        {label: 'EqualizerAPO ParametricEq', type: 'parametric', config: '4_PEAKING_WITH_LOW_SHELF'},
        {label: '10-band Graphic Eq', type: 'fixedBand', config: '10_BAND_GRAPHIC_EQ'}
      ],
      selectedEqualizer: null, //Currently selected equalizer app: { label, type }

      // Request parameters
      bassBoostGain: 0.0,
      bassBoostFc: 105.0,
      bassBoostQ: 0.7,
      trebleBoostGain: 0.0,
      trebleBoostFc: 10000.0,
      trebleBoostQ: 0.7,
      tilt: 0.0,
      maxGain: 6.0,
      windowSize: 0.08,
      trebleWindowSize: 2.0,
      trebleFLower: 6000.0,
      trebleFUpper: 8000.0,
      trebleGainK: 1.0,

      graphicEq: null,
      parametricFilters: null,
      fixedBandFilters: null,
    };
    this.fetchMeasurements = this.fetchMeasurements.bind(this);
    this.equalize = this.equalize.bind(this);
    this.onMeasurementSelected = this.onMeasurementSelected.bind(this);
    this.onSoundSignatureChanged = this.onSoundSignatureChanged.bind(this);
    this.onNewSoundSignatureCreated = this.onNewSoundSignatureCreated.bind(this);
    this.onEqParamChanged = this.onEqParamChanged.bind(this);
    this.fetchCompensations = this.fetchCompensations.bind(this);
    this.onCompensationChanged = this.onCompensationChanged.bind(this);
    this.onEqualizerChanged = this.onEqualizerChanged.bind(this);
  }

  async fetchMeasurements() {
    const data = await fetch('/entries').then(res => res.json()).catch((err) => {
      throw err;
    });
    const measurements = [];
    for (const [headphone, details] of Object.entries(data)) {
      measurements.push({label: headphone, ...details});
    }
    this.setState({measurements: measurements});
  }

  async fetchCompensations() {
    const compensations = await fetch('/compensations').then(res => res.json()).catch(err => {
      throw err;
    });
    const preferredCompensations = {};
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

  async equalize() {
    // console.log('equalize');
    // console.log(this.state);
    const soundSignature = !!this.state.selectedSoundSignature ? { ...this.state.selectedSoundSignature } : null;
    if (!!soundSignature) {
      delete soundSignature.label;
    }

    const body = {
      name: this.state.selectedMeasurement.label,
      source: this.state.selectedMeasurement.source,
      rig: this.state.selectedMeasurement.rig,
      compensation: this.state.selectedCompensation,
      sound_signature: soundSignature,
      bass_boost_gain: this.state.bassBoostGain,
      bass_boost_fc: this.state.bassBoostFc,
      bass_boost_q: this.state.bassBoostQ,
      treble_boost_gain: this.state.trebleBoostGain,
      treble_boost_fc: this.state.trebleBoostFc,
      treble_boost_q: this.state.trebleBoostQ,
      tilt: this.state.tilt,
      max_gain: this.state.maxGain,
      window_size: this.state.windowSize,
      treble_window_size: this.state.trebleWindowSize,
      treble_f_lower: this.state.trebleFLower,
      treble_f_upper: this.state.trebleFUpper,
      treble_gain_k: this.state.trebleGainK,
      graphic_eq: this.state.selectedEqualizer?.type === 'graphic',
      parametric_eq: this.state.selectedEqualizer?.type === 'parametric',
      fixed_band_eq: this.state.selectedEqualizer?.type === 'fixedBand',
      convolution_eq: this.state.selectedEqualizer?.type === 'convolution',
    };

    if (this.state.selectedEqualizer?.type === 'parametric') {
      body.parametric_eq_config = this.state.selectedEqualizer.config;
    }

    const data = await fetch('/equalize', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(body)
    }).then(res => res.json()).catch(err => {
      throw err; // TODO error handling
    });

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
    if (this.state.selectedEqualizer?.type === 'parametric' && !!data.fr?.parametric_eq) {
      // Use parametric eq curve as the equalization in the frequency response graph
      keyMap.parametric_eq = 'equalization';
      keyMap.equalization = null;
    } else if (this.state.selectedEqualizer?.type === 'fixedBand' && !!data.fr?.fixed_band_eq) {
      // Use fixed band eq curve as the equalization in the frequency response graph
      keyMap.fixed_band_eq = 'equalization';
      keyMap.equalization = null;
    }
    for (let i = 0; i < data.fr.frequency.length; ++i) {
      const dataPoint = {};
      for (const key of Object.keys(data.fr)) {
        if (keyMap[key] === null) {
          continue;
        }
        dataPoint[keyMap[key]] = data.fr[key][i];
      }
      graphData.push(dataPoint);
    }
    if (!!data.fr?.equalization) {
      for (let i = 0; i < graphData.length; ++i) {
        graphData[i].equalizedRaw = graphData[i].raw + graphData[i].equalization;
        graphData[i].equalizedSmoothed = graphData[i].smoothed + graphData[i].equalization;
      }
    }
    const newState = { graphData };

    if (!!data.graphic_eq) {
      newState.graphicEq = data.graphic_eq;
    } else if (!!data.parametric_eq) {
      newState.parametricFilters = data.parametric_eq.filters.map(filt => { return { ...filt }; });
    } else if (!!data.fixed_band_eq) {
      newState.fixedBandFilters = data.fixed_band_eq.filters.map(filt => { return { ...filt }; });
    }

    this.setState(newState);
  }

  async onMeasurementSelected(e, val) {
    this.setState({
      selectedMeasurement: {
        label: val.label,
        form: val[0].form,
        source: val[0].source,
        rig: val[0].rig,
      },
      // TODO: not preferred for any?
      selectedCompensation: this.state.preferredCompensations[val[0].source][val[0].form][val[0].rig],
    }, () => {
      this.equalize();
    });
  }

  onSoundSignatureChanged(soundSignature) {
    if (soundSignature?.label === 'Add new') {
      this.setState({ selectedSoundSignature: soundSignature });
    } else {
      this.setState({ selectedSoundSignature: soundSignature }, () => {
        this.equalize();
      });
    }
  }

  onNewSoundSignatureCreated(name, frequency, raw) {
    const newSoundSignature = { label: name, frequency, raw };
    this.setState({
      selectedSoundSignature: newSoundSignature,
      soundSignatures: [ ...this.state.soundSignatures, newSoundSignature ]
    }, () => {
      this.equalize();
    });
  }

  onEqParamChanged(newParams) {
    this.setState({ ...this.state, ...newParams }, () => {
      this.equalize();
    });
  }

  onCompensationChanged(label) {
    const preferredCompensations = { ...this.state.preferredCompensations };
    preferredCompensations[this.state.selectedMeasurement.source][this.state.selectedMeasurement.form][this.state.selectedMeasurement.rig] = label;
    this.setState({ selectedCompensation: label, preferredCompensations }, () => { this.equalize(); });
  }

  onEqualizerChanged(val) {
    if (val === null) {
      this.setState({ selectedEqualizer: null });
    } else {
      this.setState({ selectedEqualizer: { ...val } }, () => {
        this.equalize();
      });
    }
  }

  render() {
    return (
      <Grid container direction='column' rowSpacing={{xs: 1, md: 2}} sx={{pb: 1}}>
        <Grid item sx={{width: '100%', padding: 0, background: '#fff'}}>
          <Paper sx={{padding: 1, borderRadius: 0, background: (theme) => theme.palette.background.default}}>
            <TopBar
              isMeasurementSelected={!!this.state.selectedMeasurement}
              measurements={this.state.measurements}
              onMeasurementSelected={this.onMeasurementSelected}
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
                    <FrequencyResponseGraph data={this.state.graphData}/>
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

                        onSoundSignatureChanged={this.onSoundSignatureChanged}
                        onNewSoundSignatureCreated={this.onNewSoundSignatureCreated}
                        onEqParamChanged={this.onEqParamChanged}
                        onCompensationChanged={this.onCompensationChanged}
                      />
                    </Paper>
                  </Grid>
                  <Grid item xs={6}>
                    <Paper sx={{p: {xs: 1, sm: 2}}}>
                      <EqTab
                        selectedMeasurement={this.state.selectedMeasurement.label}
                        equalizers={this.state.equalizers}
                        selectedEqualizer={this.state.selectedEqualizer}
                        onEqualizerChanged={this.onEqualizerChanged}
                        graphicEq={this.state.graphicEq}
                        parametricFilters={this.state.parametricFilters}
                        fixedBandFilters={this.state.fixedBandFilters}
                      />
                    </Paper>
                  </Grid>
                </Grid>
              </Grid>
            </Container>
          </Grid>
        )}
      </Grid>
    );
  }
}

export default App;
