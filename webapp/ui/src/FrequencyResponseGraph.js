import React from 'react';
import {LineChart, Line, XAxis, YAxis, CartesianGrid, ResponsiveContainer} from 'recharts';
import {Checkbox, FormControlLabel, Grid, Switch, Typography} from "@mui/material";

class FrequencyResponseGraph extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      show: {
        raw: true,
        error: true,
        target: true,
        equalization: true,
        equalized: true,
      },
      smoothed: true,
    };
    this.onSmoothedChanged = this.onSmoothedChanged.bind(this);
    this.onLegendShowChanged = this.onLegendShowChanged.bind(this);
  }

  onSmoothedChanged(e) {
    this.setState({smoothed: e.target.checked});
  }

  onLegendShowChanged(name, value) {
    const newShow = {...this.state.show};
    newShow[name] = value;
    this.setState({show: newShow});
  }

  yRange(data) {
    const vals = [];
    for (const dataPoint of data) {
      for (const [key, val] of Object.entries(dataPoint)) {
        if (key === 'frequency'
          || (this.state.smoothed && ['raw', 'error', 'equalized_raw'].includes(key))
          || !this.state.smoothed && ['smoothed', 'error_smoothed', 'equalized'].includes(key)
        ) {
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
      <Grid container direction={{xs: 'row', md: 'row'}} alignItems='center'>
        <Grid item xs={12} md={9.5} lg={10}>
          <ResponsiveContainer width='100%' aspect={2.3}>
            <LineChart
              data={this.props.data}
              margin={{top: 0, left: 0, bottom: 20, right: 0}}
              fontFamily={'"Roboto", "Helvetica", "Arial", sans-serif'}
            >
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
                  stroke={this.state.show.equalization ? '#38d338' : '#999'}
                  strokeWidth={1.5} isAnimationActive={false}
                />
              )}
              {!!this.props.data[0].parametric_eq && (
                <Line
                  dataKey={this.state.show.parametricEq ? 'parametric_eq' : ''}
                  name='Equalizer' type='linear' dot={false}
                  stroke={this.state.show.parametricEq ? '#2b802b' : '#999'}
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

              <CartesianGrid stroke='#cfcfcf'/>
              <XAxis
                dataKey='frequency'
                scale='log' domain={[20, 20e3]} type='number'
                ticks={[20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]}
                label={{ value: 'Frequency (Hz)', position: 'outsideBottomCenter', dy: 20}}
              />
              <YAxis
                scale='linear' domain={[dataMin - dataRange * 0.1, dataMax + dataRange * 0.1]}
                type='number'
                tickCount={10}
                label={{ value: 'dBr', dx: -10, angle: -90}}
              />
            </LineChart>
          </ResponsiveContainer>
        </Grid>
        <Grid item xs={12} md={2.5} lg={2} sx={{pl: {md: 4}}} container direction={{xs: 'row', md: 'column'}}>
          <Grid item container alignItems='center'>
            <Grid item md={7}>
              <Typography>Smoothed</Typography>
            </Grid>
            <Grid item md={5}>
              <Switch checked={this.state.smoothed} label='Smoothed' onChange={this.onSmoothedChanged}/>
            </Grid>
          </Grid>
          <Grid item>
            <FormControlLabel
              label='Raw'
              control={<Checkbox size='small' checked={this.state.show.raw}
                                 onChange={(e, val) => this.onLegendShowChanged('raw', val)}/>}
              sx={{color: '#000'}}
            />
          </Grid>
          <Grid item>
            <FormControlLabel
              label='Error'
              control={<Checkbox size='small' checked={this.state.show.error}
                                 onChange={(e, val) => this.onLegendShowChanged('error', val)}/>}
              sx={{color: '#d62728'}}
            />
          </Grid>
          <Grid item>
            <FormControlLabel
              label='Target'
              control={<Checkbox size='small' checked={this.state.show.target}
                                 onChange={(e, val) => this.onLegendShowChanged('target', val)}/>}
              sx={{color: '#7bc8f6'}}
            />
          </Grid>
          <Grid item>
            <FormControlLabel
              label='Equalizer'
              control={<Checkbox size='small' checked={this.state.show.equalization}
                                 onChange={(e, val) => this.onLegendShowChanged('equalization', val)}/>}
              sx={{color: '#38d338'}}
            />
          </Grid>
          <Grid item>
            <FormControlLabel
              label='Equalized'
              control={<Checkbox size='small' checked={this.state.show.equalized}
                                 onChange={(e, val) => this.onLegendShowChanged('equalized', val)}/>}
              sx={{color: '#0343df'}}
            />
          </Grid>
        </Grid>
      </Grid>
    );
  }

}

export default FrequencyResponseGraph;
