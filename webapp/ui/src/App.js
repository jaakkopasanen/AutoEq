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
            measurements: null,
            selectedMeasurement: null,
            selectedMeasurementData: null,
            activeTab: 'target',
            eqParams: {
                compensation: null,
                soundSignature: null,
                bass_boost_gain: 0.0,
                treble_boost_gain: 0.0,
                tilt: 0.0,
                max_gain: 6.0,
                window_size: 1/12,
            }
        };
        this.fetchMeasurements = this.fetchMeasurements.bind(this);
        this.equalize = this.equalize.bind(this);
        this.onMeasurementSelected = this.onMeasurementSelected.bind(this);
        this.onActiveTabChanged = this.onActiveTabChanged.bind(this);
        this.onEqParamChanged = this.onEqParamChanged.bind(this);
        this.fetchCompensations = this.fetchCompensations.bind(this);
    }

    async fetchMeasurements() {
        const data = await fetch('/entries').then(res => res.json()).catch((err) => {
            throw err;
        });
        const measurements = [];
        for (const [headphone, details] of Object.entries(data)) {
            measurements.push({ label: headphone, ...details });
        }
        this.setState({measurements: measurements});
    }

    async fetchCompensations() {
        const data = await fetch('/compensations').then(res => res.json()).catch(err => {
            throw err;
        });
        const compensations = [];
        for (const [name, fr] of Object.entries(data)) {
            compensations.push({ label: name, ...fr });
        }
        this.setState({ compensations: compensations });
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
            headers: { 'Content-Type': 'application/json' },
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
        this.setState({ selectedMeasurementData: measurement });
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
        this.setState({ activeTab: value });
    }

    onEqParamChanged(key, value) {
        const newEqParams = { ...this.state.eqParams };
        newEqParams[key] = value;
        this.setState({ eqParams: newEqParams }, () => {
            this.equalize();
        });
    }

    render() {
        return (
            <Grid container direction='column'>
                <Grid item sx={{width: '100%', padding: 1}}>
                    <TopBar
                        isMeasurementSelected={!!this.state.selectedMeasurement}
                        measurements={this.state.measurements}
                        onMeasurementSelected={this.onMeasurementSelected}
                    />
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
                                        <FrequencyResponseGraph data={this.state.selectedMeasurementData} />
                                    </Paper>
                                </Grid>
                                <Grid item>
                                    <Paper>
                                        <Tabs value={this.state.activeTab} onChange={this.onActiveTabChanged}>
                                            <Tab label='Target' id='tab-target' value='target' />
                                            <Tab label='Parametric Eq' id='tab-parametric-eq' value='parametric-eq' />
                                            <Tab label='Fixed Band Eq' id='tab-graphic-eq' value='fixed-band-eq' />
                                            <Tab label='Convolution Eq' id='tab-convolution-eq' value='convolution-eq' />
                                        </Tabs>
                                        {this.state.activeTab === 'target' && (
                                            <TargetTab
                                                compensations={ this.state.compensations }
                                                measurements={ this.state.measurements }
                                                eqParams={ this.state.eqParams }
                                                onEqParamChanged={this.onEqParamChanged}
                                            />
                                        )}
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
