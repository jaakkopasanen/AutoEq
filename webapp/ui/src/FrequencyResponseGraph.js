import React from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, Legend, ResponsiveContainer} from 'recharts';
import {Grid, Switch, Typography} from "@mui/material";

class FrequencyResponseGraph extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            show: {
                'Frequency Response': true,
                'Error': true,
                'Target': true,
                'Equalizer': true,
                'Equalized': true
            },
            smoothed: true,
        };
        this.onSmoothedChanged = this.onSmoothedChanged.bind(this);
        this.onLegendItemClick = this.onLegendItemClick.bind(this);
    }

    onSmoothedChanged(e) {
        this.setState({ smoothed: e.target.checked });
    }

    onLegendItemClick(item) {
        const newState = { ...this.state };
        newState.show[item.value] = !this.state.show[item.value];
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
        return (
            <Grid container>
                <Grid item container xs={12} justifyContent='end' alignItems='center'>
                    <Typography>Smoothed</Typography>
                    <Switch checked={this.state.smoothed} label='Smoothed' onChange={this.onSmoothedChanged} />
                </Grid>
                <ResponsiveContainer aspect={1.5} xs={12}>
                    <LineChart data={this.props.data} margin={{top: 0, left: -30, bottom: 0, right: 0}}>
                        <Line dataKey={this.state.show['Target'] ? 'target' : ''} name='Target' type='linear' dot={false} stroke={this.state.show['Target'] ? '#7bc8f6' : '#999'} strokeWidth={7.5} isAnimationActive={false} />
                        <Line dataKey={this.state.show['Frequency Response'] ? this.state.smoothed ? 'smoothed' : 'raw' : ''} name='Frequency Response' type='linear' dot={false} stroke={this.state.show['Frequency Response'] ? '#000' : '#999'} strokeWidth={1.5} isAnimationActive={false} />
                        <Line dataKey={this.state.show['Error'] ? this.state.smoothed ? 'error_smoothed' : 'error' : ''} name='Error' type='linear' dot={false} stroke={this.state.show['Error'] ? '#d62728' : '#999'} strokeWidth={1.5} isAnimationActive={false} />
                        <Line dataKey={this.state.show['Equalizer'] ? 'equalization' : ''} name='Equalizer' type='linear' dot={false} stroke={this.state.show['Equalizer'] ? '#2ca02c' : '#999'} strokeWidth={1.5} isAnimationActive={false} />
                        <Line dataKey={this.state.show['Equalized'] ? this.state.smoothed ? 'equalized_smoothed' : 'equalized_raw' : ''} name='Equalized' type='linear' dot={false} stroke={this.state.show['Equalized'] ? '#0343df' : '#999'} strokeWidth={1.5} isAnimationActive={false} />

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
                            // layout='vertical' align='right' verticalAlign='middle'
                            // margin={{top: 0, left: 10, right: 0, bottom: 0}}
                            wrapperStyle={{fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif', right: -10}}
                        />
                    </LineChart>
                </ResponsiveContainer>
            </Grid>
        );
    }

}

export default FrequencyResponseGraph;
