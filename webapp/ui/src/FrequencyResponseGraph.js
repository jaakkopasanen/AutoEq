import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, ResponsiveContainer } from 'recharts';
import { Checkbox, FormControlLabel, Grid, Switch, Typography } from '@mui/material';

const FrequencyResponseGraph = (props) => {
  const [showRaw, setShowRaw] = useState(true);
  const [showError, setShowError] = useState(true);
  const [showTarget, setShowTarget] = useState(true);
  const [showEqualization, setShowEqualization] = useState(true);
  const [showEqualized, setShowEqualized] = useState(true);

  const yRange = (data) => {
    const vals = [];
    for (const dataPoint of data) {
      if (dataPoint.frequency > 16000) break;
      for (const [key, val] of Object.entries(dataPoint)) {
        if (key === 'frequency'
          || (props.smoothed && ['raw', 'error', 'equalizedRaw'].includes(key))
          || (!props.smoothed && ['smoothed', 'errorSmoothed', 'equalizedSmoothed'].includes(key))
          || isNaN(val)
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
  };

  if (!props.data) {
    return null;
  }
  const [dataMin, dataMax, dataRange] = yRange(props.data);
  const interval = Math.ceil(dataRange / 10);
  // min - 5% of range, rounded to interval below
  const yMin = Math.floor((dataMin - dataRange * 0.05) / interval) * interval;
  // max + 5% of range, rounded to interval above
  const yMax = Math.ceil((dataMax + dataRange * 0.05) / interval) * interval;
  // Every interval, excluding ends
  const yTicks = (isNaN(yMin) || isNaN(yMax)) ? null : [ ...Array(Math.max((yMax - yMin) / interval - 1, interval)).keys() ].map(x => yMin + interval + x * interval);

  return (
    <Grid container direction={{xs: 'row', md: 'row'}} alignItems='center' sx={{marginLeft: {xs: '-12px', sm: 0}}}>
      <Grid item xs={12} md={9.5} lg={10}>
        <ResponsiveContainer width='100%' aspect={2.3}>
          <LineChart
            data={props.data}
            margin={{top: 0, left: 0, bottom: 20, right: 0}}
            fontFamily={'"Roboto", "Helvetica", "Arial", sans-serif'}
          >
            {!!props.data[0].target && (
              <Line
                dataKey={showTarget ? 'target' : ''}
                name='Target' type='linear' dot={false}
                stroke={showTarget ? '#7bc8f6' : '#999'}
                strokeWidth={7.5} isAnimationActive={false}
              />
            )}

            {((props.smoothed && !!props.data[0].smoothed) || (!props.smoothed && !!props.data[0].raw)) && (
              <Line
                dataKey={showRaw ? props.smoothed ? 'smoothed' : 'raw' : ''}
                name='Frequency Response' type='linear' dot={false}
                stroke={showRaw ? '#000' : '#999'}
                strokeWidth={1.5} isAnimationActive={false}
              />
            )}

            {((props.smoothed && !!props.data[0].errorSmoothed) || (!props.smoothed && !!props.data[0].error)) && (
              <Line
                dataKey={showError ? props.smoothed ? 'errorSmoothed' : 'error' : ''}
                name='Error' type='linear' dot={false}
                stroke={showError ? '#d62728' : '#999'}
                strokeWidth={1.5} isAnimationActive={false}
              />
            )}
            {!!props.data[0].equalization && (
              <Line
                dataKey={showEqualization ? 'equalization' : ''}
                name='Equalizer' type='linear' dot={false}
                stroke={showEqualization ? '#38d338' : '#999'}
                strokeWidth={1.5} isAnimationActive={false}
              />
            )}
            {((props.smoothed && !!props.data[0].equalizedSmoothed) || (!props.smoothed && !!props.data[0].equalizedRaw)) && (
              <Line
                dataKey={showEqualized ? props.smoothed ? 'equalizedSmoothed' : 'equalizedRaw' : ''}
                name='Equalized' type='linear' dot={false}
                stroke={showEqualized ? '#0343df' : '#999'}
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
              checked={props.smoothed} label='Smoothed'
              onChange={(e) => props.onSmoothedChanged(e.target.checked)}
            />
          </Grid>
        </Grid>
        <Grid item>
          <FormControlLabel
            label='Raw' sx={{color: '#000'}}
            control={<Checkbox size='small' checked={showRaw} onChange={(e, val) => setShowRaw(val)} />}
          />
        </Grid>
        <Grid item>
          <FormControlLabel
            label='Error' sx={{color: '#d62728'}}
            control={<Checkbox size='small' checked={showError} onChange={(e, val) => setShowError(val)}/>}
          />
        </Grid>
        <Grid item>
          <FormControlLabel
            label='Target' sx={{color: '#7bc8f6'}}
            control={<Checkbox size='small' checked={showTarget} onChange={(e, val) => setShowTarget(val)}/>}
          />
        </Grid>
        <Grid item>
          <FormControlLabel
            label='Equalizer' sx={{color: '#38d338'}}
            control={<Checkbox size='small' checked={showEqualization} onChange={(e, val) => setShowEqualization(val)}/>}
          />
        </Grid>
        <Grid item>
          <FormControlLabel
            label='Equalized' sx={{color: '#0343df'}}
            control={<Checkbox size='small' checked={showEqualized} onChange={(e, val) => setShowEqualized(val)}/>}
          />
        </Grid>
      </Grid>
    </Grid>
  );
}

export default FrequencyResponseGraph;
