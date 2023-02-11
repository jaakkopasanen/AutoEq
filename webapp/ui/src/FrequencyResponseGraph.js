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
    this.onLegendShowChanged = this.onLegendShowChanged.bind(this);
  }

  onLegendShowChanged(name, value) {
    const newShow = {...this.state.show};
    newShow[name] = value;
    this.setState({show: newShow});
  }

  yRange(data) {
    const vals = [];
    for (const dataPoint of data) {
      if (dataPoint.frequency > 16000) break;
      for (const [key, val] of Object.entries(dataPoint)) {
        if (key === 'frequency'
          || (this.props.smoothed && ['raw', 'error', 'equalizedRaw'].includes(key))
          || (!this.props.smoothed && ['smoothed', 'errorSmoothed', 'equalizedSmoothed'].includes(key))
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
    const yMin = Math.floor((dataMin - dataRange * 0.05) / 2) * 2; // min - 5% of range, rounded to 2 dB below
    const yMax = Math.ceil((dataMax + dataRange * 0.05) / 2) * 2; // max + 5% of range, rounded to 2 dB above
    const yTicks = (isNaN(yMin) || isNaN(yMax)) ? null : [ ...Array(Math.max((yMax - yMin) / 2 - 1, 2)).keys() ].map(x => yMin + 2 + x * 2) // Every 2 dB, excluding ends

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
                (this.props.smoothed && !!this.props.data[0].smoothed)
                || (!this.props.smoothed && !!this.props.data[0].raw)
              ) && (
                <Line
                  dataKey={this.state.show.raw ? this.props.smoothed ? 'smoothed' : 'raw' : ''}
                  name='Frequency Response' type='linear' dot={false}
                  stroke={this.state.show.raw ? '#000' : '#999'}
                  strokeWidth={1.5} isAnimationActive={false}
                />
              )}

              {(
                (this.props.smoothed && !!this.props.data[0].errorSmoothed)
                || (!this.props.smoothed && !!this.props.data[0].error)
              ) && (
                <Line
                  dataKey={this.state.show.error ? this.props.smoothed ? 'errorSmoothed' : 'error' : ''}
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
              {(
                (this.props.smoothed && !!this.props.data[0].equalizedSmoothed)
                || (!this.props.smoothed && !!this.props.data[0].equalizedRaw)
              ) && (
                <Line
                  dataKey={this.state.show.equalized ? this.props.smoothed ? 'equalizedSmoothed' : 'equalizedRaw' : ''}
                  name='Equalized' type='linear' dot={false}
                  stroke={this.state.show.equalized ? '#0343df' : '#999'}
                  strokeWidth={1.5} isAnimationActive={false}
                />
              )}

              <CartesianGrid stroke='#cfcfcf'/>
              <XAxis
                dataKey='frequency'
                scale='log' domain={[20, 20e3]} type='number'
                ticks={[
                  20, 30, 40, 50, 60, 70, 80, 90,
                  100, 200, 300, 400, 500, 600, 700, 800, 900,
                  1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,
                  10000, 20000
                ]}
                tickFormatter={(x => [1, 2, 5].includes(x / 10**Math.floor(Math.log10(x))) ? ( x >= 1000 ? (x/1000).toFixed(0) + 'k' : x.toFixed(0) ) : '')}
                interval={0}
                label={{ value: 'Frequency (Hz)', position: 'outsideBottomCenter', dy: 20}}
              />
              <YAxis
                scale='linear'
                domain={[yMin, yMax]} ticks={yTicks} interval={0}
                type='number'
                label={{ value: 'dBr', dx: -10, angle: -90}}
                allowDataOverflow={true}
              />
            </LineChart>
          </ResponsiveContainer>
        </Grid>
        <Grid item xs={12} md={2.5} lg={2} sx={{pl: {xs: 1, sm: 1, md: 4}}} container direction={{xs: 'row', md: 'column'}}>
          <Grid item container alignItems='center'>
            <Grid item md={7}>
              <Typography>Smoothed</Typography>
            </Grid>
            <Grid item md={5}>
              <Switch
                checked={this.props.smoothed} label='Smoothed'
                onChange={(e) => this.props.onSmoothedChanged(e.target.checked)}
              />
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
