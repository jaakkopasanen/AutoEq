import React, { useState } from 'react';
import {Autocomplete, Grid, IconButton, Switch, TextField, Tooltip, Typography} from "@mui/material";
import InputSlider from './InputSlider';
import audioBufferToWav from 'audiobuffer-to-wav';
import DownloadIcon from '@mui/icons-material/Download';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';

const EqAppConvolutionEq = (props) => {
  const [stereo, setStereo] = useState(false);

  const onStereoChanged = (e) => {
    setStereo(e.target.checked);
  };

  const onDownloadClick = () => {
    let audioBuffer;
    if (stereo) {
      const arr = props.firAudioBuffer.getChannelData(0);
      audioBuffer = props.audioContext.createBuffer(2, props.firAudioBuffer.length, props.firAudioBuffer.sampleRate);
      audioBuffer.copyToChannel(arr, 0);
      audioBuffer.copyToChannel(arr, 1);
    } else {
      audioBuffer = props.firAudioBuffer;
    }
    const wav = audioBufferToWav(audioBuffer, {float32: props.bitDepth === 32});
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
      {props.instructions && (
        <Grid
          item
          sx={{
            padding: '8px 12px',
            background: '#e5f3f7',
            borderStyle: 'solid',
            borderWidth: '1px',
            borderColor: '#9abac3',
            borderRadius: '4px',
            marginTop: '8px',
            marginBottom: '8px'
          }}
        >
          <Typography variant='caption'>
            {props.instructions}
          </Typography>
        </Grid>
      )}
      <Grid item container direction='row' columnSpacing={1}>
        <Grid item xs={4} sx={{position: 'relative'}}>
          <Autocomplete
            freeSolo
            renderInput={(params) =>
              <TextField {...params} label='Sample rate' type='number' />
            }
            value={props.fs.toFixed(0)}
            options={['44100', '48000', '96000', '192000', '384000']}
            onChange={(e, val) => {
              props.onEqParamChanged({ fs: parseFloat(val) })
            }}
            size='small'
            disableClearable
          />
          <Tooltip
            title='Sample rate must match the device sample rate'
            disableFocusListener
            enterTouchDelay={0} leaveTouchDelay={0}
            placement='top'
          >
            <InfoOutlinedIcon sx={{ width: 14, height: 14, position: 'absolute', top: -6, right: 10, background: '#fff' }} />
          </Tooltip>
        </Grid>
        <Grid item xs={4} sx={{position: 'relative'}}>
          <Autocomplete
            renderInput={(params) => <TextField {...params} label='Bit depth' /> }
            value={props.bitDepth.toFixed(0)}
            options={['16', '32']}
            onChange={(e, val) => {
              props.onEqParamChanged({ bitDepth: parseInt(val) })
            }}
            size='small'
          />
          <Tooltip
            title='Use 16 bits unless the app requires 32 bits'
            disableFocusListener
            enterTouchDelay={0} leaveTouchDelay={0}
            placement='top'
          >
            <InfoOutlinedIcon sx={{ width: 14, height: 14, position: 'absolute', top: -6, right: 10, background: '#fff' }} />
          </Tooltip>
        </Grid>
        <Grid item xs={4} sx={{position: 'relative'}}>
          <Autocomplete
            renderInput={(params) => <TextField {...params} label='Phase' />}
            value={props.phase}
            options={['minimum', 'linear']}
            onChange={(e, val) => {
              props.onEqParamChanged({ phase: val })
            }}
            size='small'
          />
          <Tooltip
            title='Use minimum phase always when equalizing headphones'
            disableFocusListener
            enterTouchDelay={0} leaveTouchDelay={0}
            placement='top'
          >
            <InfoOutlinedIcon sx={{ width: 14, height: 14, position: 'absolute', top: -6, right: 10, background: '#fff' }} />
          </Tooltip>
        </Grid>
      </Grid>
      <Grid item>
        <InputSlider
          label='Frequency resolution (Hz)' initialValue={props.fRes}
          min={1.0} max={40.0} step={1.0}
          onChange={(v) => { props.onEqParamChanged({ fRes: v }) }}
          tooltip='Smaller values give more accurate bass but require more CPU power. Default value is enough for most cases.'
        />
      </Grid>
      <Grid item>
        <InputSlider
          label='Preamp' initialValue={props.preamp}
          min={-20} max={20} step={0.5}
          onChange={(v) => { props.onEqParamChanged({ preamp: v }) }}
          tooltip="Apply negative preamp if you hear clipping. AutoEq normalizes convolution filters but cannot guarantee the audio won't ever clip."
        />
      </Grid>
      <Grid item container direction='row' columnSpacing={0} justifyContent='space-between' alignItems='center'>
        <Grid item container direction='row' alignItems='center' sx={{ width: 'auto' }}>
          <Grid item>
            <Typography>Stereo</Typography>
          </Grid>
          <Grid item>
            <Switch checked={stereo} onChange={onStereoChanged} />
          </Grid>
          <Grid item>
            <Tooltip
              title='Use stereo only if the equalizer app requires stereo impulse responses'
              disableFocusListener
              enterTouchDelay={0} leaveTouchDelay={0}
              placement='top'
            >
              <InfoOutlinedIcon sx={{width: 18, height: 18, verticalAlign: 'bottom'}} />
            </Tooltip>
          </Grid>
        </Grid>

        <Grid item>
          <IconButton onClick={onDownloadClick}><DownloadIcon /></IconButton>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default EqAppConvolutionEq;
