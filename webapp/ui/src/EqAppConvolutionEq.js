import React, { useState } from 'react';
import { Autocomplete, Grid, IconButton, Switch, TextField, Typography } from "@mui/material";
import InputSlider from './InputSlider';
import audioBufferToWav from 'audiobuffer-to-wav';
import DownloadIcon from '@mui/icons-material/Download';

const EqAppConvolutionEq = (props) => {
  const [stereo, setStereo] = useState(false);

  const onStereoChanged = (e) => {
    setStereo(e.target.checked);
  };

  const onDownloadClick = () => {
    const wav = audioBufferToWav(props.firAudioBuffer, {float32: props.bitDepth === 32});
    const blob = new window.Blob([ new DataView(wav) ], { type: 'audio/wav' });
    const anchor = document.createElement('a');
    const url = window.URL.createObjectURL(blob);
    anchor.href = url;
    anchor.download = `${props.selectedMeasurement} ${props.phase} phase ${props.fs} Hz.wav`;
    anchor.click();
    window.URL.revokeObjectURL(url);
    anchor.remove();
  };

  return (
    <Grid container direction='column' rowSpacing={1}>
      <Grid item container direction='row' columnSpacing={1}>
        <Grid item xs={4}>
          <Autocomplete
            freeSolo
            renderInput={(params) =>
              <TextField {...params} label='Sample rate (Hz)' type='number' />
            }
            value={props.fs.toFixed(0)}
            options={['44100', '48000', '96000', '192000', '384000']}
            onChange={(e, val) => {
              props.onEqParamChanged({ fs: parseFloat(val) })
            }}
            size='small'
            disableClearable
          />
        </Grid>
        <Grid item xs={4}>
          <Autocomplete
            renderInput={(params) => <TextField {...params} label='Bit depth' /> }
            value={props.bitDepth.toFixed(0)}
            options={['16', '32']}
            onChange={(e, val) => {
              props.onEqParamChanged({ bitDepth: parseInt(val) })
            }}
            size='small'
          />
        </Grid>
        <Grid item xs={4}>
          <Autocomplete
            renderInput={(params) => <TextField {...params} label='Phase' /> }
            value={props.phase}
            options={['minimum', 'linear']}
            onChange={(e, val) => {
              props.onEqParamChanged({ phase: val })
            }}
            size='small'
          />
        </Grid>
      </Grid>
      <Grid item>
        <InputSlider
          label='Frequency resolution (Hz)' initialValue={props.fRes}
          min={1.0} max={40.0} step={1.0}
          onChange={(v) => { props.onEqParamChanged({ fRes: v }) }}
        />
      </Grid>
      <Grid item>
        <InputSlider
          label='Preamp' initialValue={props.preamp}
          min={-20} max={20} step={0.5}
          onChange={(v) => { props.onEqParamChanged({ preamp: v }) }}
        />
      </Grid>
      <Grid item container direction='row' columnSpacing={1} justifyContent='center' alignItems='center'>
          <Grid item>
            <Typography>Stereo</Typography>
          </Grid>
          <Grid item>
            <Switch checked={stereo} onChange={onStereoChanged} />
          </Grid>
        <Grid item xs={6}>
          <IconButton onClick={onDownloadClick}><DownloadIcon /></IconButton>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default EqAppConvolutionEq;
