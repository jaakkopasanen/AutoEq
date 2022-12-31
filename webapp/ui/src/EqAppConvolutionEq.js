import React from 'react';
import {Autocomplete, Button, Grid, Switch, TextField, Typography} from "@mui/material";
import InputSlider from './InputSlider';
import audioBufferToWav from 'audiobuffer-to-wav';

class EqAppConvolutionEq extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      stereo: false,
    };
    this.onStereoChanged = this.onStereoChanged.bind(this);
    this.onDownloadClick = this.onDownloadClick.bind(this);
  }

  onStereoChanged(e) {
    this.setState({ stereo: e.target.checked });
  }

  onDownloadClick() {
    const wav = audioBufferToWav(this.props.firAudioBuffer, {float32: this.props.bitDepth === 32});
    const blob = new window.Blob([ new DataView(wav) ], { type: 'audio/wav' });
    const anchor = document.createElement('a');
    const url = window.URL.createObjectURL(blob);
    anchor.href = url;
    anchor.download = `${this.props.selectedMeasurement} ${this.props.phase} phase ${this.props.fs} Hz.wav`;
    anchor.click();
    window.URL.revokeObjectURL(url);
    anchor.remove();
  }

  render() {
    return (
      <Grid container direction='column' rowSpacing={1}>
        <Grid item container direction='row' columnSpacing={1}>
          <Grid item xs={4}>
            <Autocomplete
              freeSolo
              renderInput={(params) =>
                <TextField {...params} label='Sample rate (Hz)' type='number' />
              }
              value={this.props.fs.toFixed(0)}
              options={['44100', '48000', '96000', '192000', '384000']}
              onChange={(e, val) => {
                this.props.onEqParamChanged({ fs: parseFloat(val) })
              }}
              size='small'
              disableClearable
            />
          </Grid>
          <Grid item xs={4}>
            <Autocomplete
              renderInput={(params) => <TextField {...params} label='Bit depth' /> }
              value={this.props.bitDepth.toFixed(0)}
              options={['16', '32']}
              onChange={(e, val) => {
                this.props.onEqParamChanged({ bitDepth: parseInt(val) })
              }}
              size='small'
            />
          </Grid>
          <Grid item xs={4}>
            <Autocomplete
              renderInput={(params) => <TextField {...params} label='Phase' /> }
              value={this.props.phase}
              options={['minimum', 'linear']}
              onChange={(e, val) => {
                this.props.onEqParamChanged({ phase: val })
              }}
              size='small'
            />
          </Grid>
        </Grid>
        <Grid item>
          <InputSlider
            label='Frequency resolution (Hz)' value={this.props.fRes}
            min={1.0} max={40.0} step={1.0}
            onChange={(v) => { this.props.onEqParamChanged({ fRes: v }) }}
          />
        </Grid>
        <Grid item>
          <InputSlider
            label='Preamp' value={this.props.preamp}
            min={-20} max={20} step={0.5}
            onChange={(v) => { this.props.onEqParamChanged({ preamp: v }) }}
          />
        </Grid>
        <Grid item container direction='row' columnSpacing={1} justifyContent='center' alignItems='center'>
            <Grid item>
              <Typography>Stereo</Typography>
            </Grid>
            <Grid item>
              <Switch checked={this.state.stereo} onChange={this.onStereoChanged} />
            </Grid>
          <Grid item xs={6}>
            <Button variant='outlined' onClick={this.onDownloadClick}>Download</Button>
          </Grid>
        </Grid>
      </Grid>
    );
  }
}

export default EqAppConvolutionEq;
