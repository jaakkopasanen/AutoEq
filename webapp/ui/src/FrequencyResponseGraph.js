import React from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Legend, ResponsiveContainer} from 'recharts';
import {Grid, Switch, Typography} from "@mui/material";

class FrequencyResponseGraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            show: {
                raw: true,
                error: true,
                target: true,
                equalization: true,
                equalized: true
            },
            smoothed: true,
            height: 0,
            width: 0,
        };
        this.onSmoothedChanged = this.onSmoothedChanged.bind(this);
        this.onLegendItemClick = this.onLegendItemClick.bind(this);
        this.updateWindowDimensions = this.updateWindowDimensions.bind(this);
    }

    componentDidMount() {
        this.updateWindowDimensions();
        window.addEventListener('resize', this.updateWindowDimensions);
    }

    componentWillUnmount() {
        window.removeEventListener('resize', this.updateWindowDimensions);
    }

    updateWindowDimensions() {
        this.setState({ width: window.innerWidth, height: window.innerHeight });
    }

    onSmoothedChanged(e) {
        this.setState({ smoothed: e.target.checked });
    }

    onLegendItemClick(legendItem) {
        const newState = { ...this.state };
        newState.show[legendItem.value] = !this.state.show[legendItem.value];
        this.setState(newState);
    }

    yRange(data) {
        const vals = [];
        for (const dataPoint of data) {
            for (const [key, val] of Object.entries(dataPoint)) {
                if (key === 'frequency') {
                    continue;
                }
                vals.push(val);
            }
        }
        const dataMin = Math.min(...vals);
        const dataMax = Math.max(...vals);
        const dataRange = dataMax - dataMin;
        return [dataMin, dataMax, dataRange];
    }

    render() {
        if (!this.props.data) {
            return null;
        }
        const [dataMin, dataMax, dataRange] = this.yRange(this.props.data);
        let aspect = 1.5;
        if (this.state.width >= 900) {
            aspect = 2.5;
        } else if (this.state.width >= 600) {
            aspect = 2.0;
        }
        return (
            <Grid container>
                <Grid item container xs={12} justifyContent='end' alignItems='center'>
                    <Typography>Smoothed</Typography>
                    <Switch checked={this.state.smoothed} label='Smoothed' onChange={this.onSmoothedChanged} />
                </Grid>
                <ResponsiveContainer width='100%' aspect={aspect} xs={12}>
                    <LineChart data={this.props.data} margin={{top: 0, left: -30, bottom: 0, right: 0}}>
                        {!!this.props.data[0].target && (
                            <Line
                                dataKey={this.state.show.target ? 'target' : ''}
                                name='Target' type='linear' dot={false}
                                stroke={this.state.show.target ? '#7bc8f6' : '#999'}
                                strokeWidth={7.5} isAnimationActive={false}
                            />
                        )}

                        {(
                            (this.state.smoothed && !!this.props.data[0].smoothed)
                            || (!this.state.smoothed && !!this.props.data[0].raw)
                        ) && (
                            <Line
                                dataKey={this.state.show.raw ? this.state.smoothed ? 'smoothed' : 'raw' : ''}
                                name='Frequency Response' type='linear' dot={false}
                                stroke={this.state.show.raw ? '#000' : '#999'}
                                strokeWidth={1.5} isAnimationActive={false}
                            />
                        )}

                        {(
                            (this.state.smoothed && !!this.props.data[0].error_smoothed)
                            || (!this.state.smoothed && !!this.props.data[0].error)
                        ) && (
                            <Line
                                dataKey={this.state.show.error ? this.state.smoothed ? 'error_smoothed' : 'error' : ''}
                                name='Error' type='linear' dot={false}
                                stroke={this.state.show.error ? '#d62728' : '#999'}
                                strokeWidth={1.5} isAnimationActive={false}
                            />
                        )}
                        {!!this.props.data[0].equalization && (
                            <Line
                                dataKey={this.state.show.equalization ? 'equalization' : ''}
                                name='Equalizer' type='linear' dot={false}
                                stroke={this.state.show.equalization ? '#2ca02c' : '#999'}
                                strokeWidth={1.5} isAnimationActive={false}
                            />
                        )}
                        {(
                            (this.state.smoothed && !!this.props.data[0].equalized_smoothed)
                            || (!this.state.smoothed && !!this.props.data[0].equalized_raw)
                        ) && (
                            <Line
                                dataKey={this.state.show.equalized ? this.state.smoothed ? 'equalized_smoothed' : 'equalized_raw' : ''}
                                name='Equalized' type='linear' dot={false}
                                stroke={this.state.show.equalized ? '#0343df' : '#999'}
                                strokeWidth={1.5} isAnimationActive={false}
                            />
                        )}

                        <CartesianGrid stroke='#cfcfcf' />
                        <XAxis
                            dataKey='frequency'
                            scale='log' domain={[20, 20e3]} type='number'
                            ticks={[20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]}
                            fontFamily={'"Roboto", "Helvetica", "Arial", sans-serif'}
                        />
                        <YAxis
                            scale='linear' domain={[ dataMin - dataRange * 0.1, dataMax + dataRange * 0.1 ]}
                            type='number'
                            tickCount={10}
                            fontFamily={'"Roboto", "Helvetica", "Arial", sans-serif'}
                        />
                        <Legend
                            onClick={this.onLegendItemClick}
                            padding={{top: 0, left: 10, right: 10, bottom: 0}}
                            wrapperStyle={{fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif', left: 0, right: 0, width: 'auto'}}
                        />
                    </LineChart>
                </ResponsiveContainer>
            </Grid>
        );
    }

}

export default FrequencyResponseGraph;
