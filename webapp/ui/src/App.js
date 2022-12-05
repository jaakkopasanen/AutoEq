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
        this.state = { selectedEntry: null, measurements: null, measurement: null, activeTab: 'target' };
        this.fetchMeasurements = this.fetchMeasurements.bind(this);
        this.equalize = this.equalize.bind(this);
        this.onHeadphonesSelected = this.onHeadphonesSelected.bind(this);
        this.onActiveTabChanged = this.onActiveTabChanged.bind(this);
        this.onCompensationChanged = this.onCompensationChanged.bind(this);
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

    componentDidMount() {
        this.fetchMeasurements();
    }

    async equalize() {
        const data = await fetch('/equalize', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name: this.state.selectedEntry.label,
                source: this.state.selectedEntry.source,
                rig: this.state.selectedEntry.rig,
                compensation: this.state.compensation?.name,
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
        this.setState({ measurement });
    }

    async onHeadphonesSelected(e, val) {
        this.setState({
            selectedEntry: {
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

    onCompensationChanged(e, value) {
        this.setState({ compensation: value }, () => {
            this.equalize();
        });
    }

    render() {
        return (
            <Grid container direction='column'>
                <Grid item sx={{width: '100%', padding: 1}}>
                    <TopBar
                        isMeasurementSelected={!!this.state.measurement}
                        measurements={this.state.measurements}
                        onMeasurementSelected={this.onHeadphonesSelected}
                    />
                </Grid>
                {!!this.state.measurement && (
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
                                        <FrequencyResponseGraph data={this.state.measurement} />
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
                                            <TargetTab onCompensationChanged={this.onCompensationChanged} />
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
