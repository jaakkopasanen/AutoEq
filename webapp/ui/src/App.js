import React from 'react';
import FrequencyResponseGraph from './FrequencyResponseGraph';
import {
  Container,
  Grid,
  Paper,
  Tab,
  Tabs,
} from "@mui/material";
import TopBar from "./TopBar";
import TargetTab from "./TargetTab";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      compensations: [],
      soundSignatures: [
        {label: 'Custom', frequency: [], raw: []},
        {label: 'Add current error as a new sound signature'}
      ],
      selectedSoundSignature: null,
      measurements: null,
      selectedMeasurement: null,
      selectedMeasurementData: null,
      activeTab: 'target',
      eqParams: {
        compensation: null,
        sound_signature: null,
        bass_boost_gain: 0.0,
        bass_boost_fc: 105.0,
        bass_boost_q: 0.7,
        treble_boost_gain: 0.0,
        treble_boost_fc: 10000.0,
        treble_boost_q: 0.7,
        tilt: 0.0,
        max_gain: 6.0,
        window_size: 0.08,
        treble_window_size: 2.0,
        treble_f_lower: 6000.0,
        treble_f_upper: 8000.0,
        treble_gain_k: 1.0,
      }
    };
    this.fetchMeasurements = this.fetchMeasurements.bind(this);
    this.equalize = this.equalize.bind(this);
    this.onMeasurementSelected = this.onMeasurementSelected.bind(this);
    this.onActiveTabChanged = this.onActiveTabChanged.bind(this);
    this.onSoundSignatureChanged = this.onSoundSignatureChanged.bind(this);
    this.onAddNewSoundSignature = this.onAddNewSoundSignature.bind(this);
    this.onEqParamChanged = this.onEqParamChanged.bind(this);
    this.fetchCompensations = this.fetchCompensations.bind(this);
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
    const data = await fetch('/compensations').then(res => res.json()).catch(err => {
      throw err;
    });
    const compensations = [];
    for (const [name, fr] of Object.entries(data)) {
      compensations.push({label: name, ...fr});
    }
    this.setState({compensations: compensations});
  }

  componentDidMount() {
    this.fetchMeasurements();
    this.fetchCompensations();
  }

  async equalize() {
    // console.log('equalize');
    // console.log(this.state.eqParams);
    const data = await fetch('/equalize', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        name: this.state.selectedMeasurement.label,
        source: this.state.selectedMeasurement.source,
        rig: this.state.selectedMeasurement.rig,
        ...this.state.eqParams
      })
    }).then(res => res.json()).catch(err => {
      throw err;
    });
    const measurement = [];
    for (let i = 0; i < data.fr.frequency.length; ++i) {
      const dataPoint = {};
      for (const key of Object.keys(data.fr)) {
        dataPoint[key] = data.fr[key][i];
      }
      measurement.push(dataPoint);
    }
    this.setState({selectedMeasurementData: measurement});
  }

  async onMeasurementSelected(e, val) {
    this.setState({
      selectedMeasurement: {
        label: val.label,
        source: val[0].source,
        rig: val[0].rig,
      }
    }, () => {
      this.equalize();
    });
  }

  onActiveTabChanged(e, value) {
    this.setState({activeTab: value});
  }

  onSoundSignatureChanged(value) {
    if (value === null) {
      this.setState({ selectedSoundSignature: null });
      return;
    } else if (value === 'Add current error as a new sound signature') {
      this.setState({ selectedSoundSignature: value });
      return;
    }
    const newState = {
      eqParams: { ...this.state.eqParams },
    };
    newState.selectedSoundSignature = value;
    for (const soundSignature of this.state.soundSignatures) {
      if (soundSignature.label === value) {
        newState.eqParams.sound_signature = {
          frequency: [ ...soundSignature.frequency ],
          raw: [ ...soundSignature.raw ],
        }
        this.setState(newState);
        break;
      }
    }
  }

  onAddNewSoundSignature(label) {
    const newState = { eqParams: { ...this.state.eqParams } };
    const frequency = this.state.selectedMeasurementData.map((dataPoint) => dataPoint.frequency);
    const error = this.state.selectedMeasurementData.map((dataPoint) => dataPoint.error);
    newState.soundSignatures = [ ...this.state.soundSignatures ];
    const newSig = { label: label, frequency, raw: error };
    newState.soundSignatures.push(newSig);
    newState.eqParams.sound_signature = { frequency, raw: error };
    this.setState(newState, () => {
      this.setState({ selectedSoundSignature: label });
    });
  }

  onEqParamChanged(newParams) {
    const newEqParams = {...this.state.eqParams, ...newParams};
    this.setState({eqParams: newEqParams}, () => {
      this.equalize();
    });
  }

  render() {
    return (
      <Grid container direction='column'>
        <Grid item sx={{width: '100%', padding: 0, background: '#fff'}}>
          <Paper sx={{padding: 1, borderRadius: 0, background: (theme) => theme.palette.background.default}}>
            <TopBar
              isMeasurementSelected={!!this.state.selectedMeasurement}
              measurements={this.state.measurements}
              onMeasurementSelected={this.onMeasurementSelected}
            />
          </Paper>

        </Grid>
        {!!this.state.selectedMeasurementData && (
          <Grid item>
            <Container sx={{marginTop: 1}}>
              <Grid container direction='column' rowGap={2}>
                <Grid item>
                  <Paper
                    sx={{
                      pt: 1,
                      pl: {xs: 0, sm: 2, md: 4},
                      pr: {xs: 0, sm: 2, md: 4},
                      pb: {xs: 0, sm: 2, md: 4},
                    }}
                  >
                    <FrequencyResponseGraph data={this.state.selectedMeasurementData}/>
                  </Paper>
                </Grid>
                <Grid item>
                  <Paper>
                    <Grid container direction='column'>
                      <Grid item>
                        <Tabs value={this.state.activeTab} onChange={this.onActiveTabChanged}>
                          <Tab label='Target' id='tab-target' value='target'/>
                          <Tab label='Parametric Eq' id='tab-parametric-eq' value='parametric-eq'/>
                          <Tab label='Fixed Band Eq' id='tab-graphic-eq' value='fixed-band-eq'/>
                          <Tab label='Convolution Eq' id='tab-convolution-eq' value='convolution-eq'/>
                        </Tabs>
                      </Grid>
                      <Grid item sx={{pt: 1}}>
                        {this.state.activeTab === 'target' && (
                          <TargetTab
                            compensations={this.state.compensations}
                            soundSignatures={this.state.soundSignatures}
                            onSoundSignatureChanged={this.onSoundSignatureChanged}
                            onAddNewSoundSignature={this.onAddNewSoundSignature}
                            selectedSoundSignature={this.state.selectedSoundSignature}
                            eqParams={this.state.eqParams}
                            onEqParamChanged={this.onEqParamChanged}
                          />
                        )}
                      </Grid>
                    </Grid>
                  </Paper>
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
