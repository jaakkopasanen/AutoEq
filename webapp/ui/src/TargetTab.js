import React from 'react';
import {Autocomplete, Button, Checkbox, FormControlLabel, FormGroup, Grid, TextField} from "@mui/material";
import InputSlider from "./InputSlider";

class TargetTab extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showAdvanced: false,
      newSoundSignatureName: '',
      newSoundSignatureText: 'frequency,raw\n',
    };
    this.onUseCurrentErrorClicked = this.onUseCurrentErrorClicked.bind(this);
    this.onSoundSignatureTextChanged = this.onSoundSignatureTextChanged.bind(this);
    this.onSaveSoundSignatureClick = this.onSaveSoundSignatureClick.bind(this);
  }

  onUseCurrentErrorClicked() {
    let newSoundSignatureText = 'frequency,raw\n';
    for (let i = 0; i < this.props.selectedMeasurementData.length; ++i) {
      newSoundSignatureText += this.props.selectedMeasurementData[i].frequency.toFixed(1)
        + ',' + this.props.selectedMeasurementData[i].raw.toFixed(1) + '\n';
    }
    this.setState({ newSoundSignatureText, newSoundSignatureName: this.props.selectedMeasurement.label });
  }

  onSoundSignatureTextChanged(e) {
    this.setState({
      newSoundSignatureText: e.target.value,
      newSoundSignatureError: false
    });
  }

  onSaveSoundSignatureClick() {
    const frequency = [];
    const raw = [];
    const rows = this.state.newSoundSignatureText.trim().split('\n');
    for (const row of rows) {
      if (row.trim() === '') {
        continue;
      }
      const cells = row.trim().split(',');
      if (cells.length !== 2) {
        this.setState({ newSoundSignatureError: true });
        return;
      }
      if (cells[0] === 'frequency') {
        continue;
      }
      if (isNaN(parseFloat(cells[0].trim())) || isNaN(parseFloat(cells[1].trim()))) {
        this.setState({ newSoundSignatureError: true });
        return;
      }
      frequency.push(parseFloat(cells[0].trim()));
      raw.push(parseFloat(cells[1].trim()));
    }
    this.props.onNewSoundSignatureCreated(this.state.newSoundSignatureName, frequency, raw);
    this.setState({ newSoundSignatureName: '', newSoundSignatureText: 'frequency,raw\n' });
  }

  render() {
    return (
      <Grid container direction='row' columnSpacing={1}>
        <Grid item xs={12} sm={12} container direction='column' rowSpacing={1}>
          {!!this.props.compensations && (
            <Grid item>
              <Autocomplete
                renderInput={(params) =>
                  <TextField {...params} label="Select compensation" />
                }
                options={this.props.compensations}
                value={this.props.selectedCompensation}
                onChange={(e, val) => {
                  this.props.onCompensationChanged(val)
                }}
                sx={{width: '100%'}}
              />
            </Grid>
          )}
          {!!this.props.soundSignatures && (
            <Grid item>
              <Autocomplete
                renderInput={(params) =>
                  <TextField {...params} label="Select sound signature"/>
                }
                options={this.props.soundSignatures.map(sig => sig.label)}
                value={this.props.selectedSoundSignature}
                onChange={(e, val) => {
                  this.props.onSoundSignatureChanged(val);
                }}
                sx={{width: '100%'}}
              />
            </Grid>
          )}
          {this.props.selectedSoundSignature === 'Add new' && (
            <Grid item container direction='column' rowSpacing={1} sx={{pl: 2, pr: 2}}>
              <Grid item container direction='row' alignItems='center' columnSpacing={1}>
                <Grid item sx={{flexGrow: 1}}>
                  <TextField
                    value={this.state.newSoundSignatureName}
                    onChange={(e) => {
                      this.setState({ newSoundSignatureName: e.target.value });
                    }}
                    size='small' sx={{width: '100%'}}
                    label='Name of the new sound signature'
                  />
                </Grid>
                <Grid item>
                  <Button
                    onClick={this.onSaveSoundSignatureClick}
                    variant='outlined' size='large'
                    disabled={this.state.newSoundSignatureName.trim().length === 0}
                  >
                    Save
                  </Button>
                </Grid>
              </Grid>
              <Grid item>
                <TextField
                  multiline rows={10} value={this.state.newSoundSignatureText}
                  sx={{width: '100%'}}
                  inputProps={{ style: { fontFamily: 'monospace' } }}
                  onChange={this.onSoundSignatureTextChanged}
                />
              </Grid>
              <Grid item>
                <Button
                  variant='outlined' onClick={this.onUseCurrentErrorClicked}
                  disabled={this.props.selectedMeasurementData.filter(x => !!x.error).length === 0}
                >
                  Use current error
                </Button>
              </Grid>
            </Grid>
          )}
        </Grid>
        <Grid item xs={12} sm={12} container direction='column' rowSpacing={1}>
          <Grid item>
            <InputSlider
              label='Bass boost (dB)' value={this.props.bassBoostGain} min={-10} max={20} step={0.5}
              onChange={(v) => {
                this.props.onEqParamChanged({bassBoostGain: v})
              }}/>
          </Grid>
          <Grid item>
            <InputSlider
              label='Treble boost (dB)' value={this.props.trebleBoostGain} min={-20} max={20} step={0.5}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleBoostGain: v })
              }}/>
          </Grid>
          <Grid item>
            <InputSlider
              label='Tilt (db/oct)' value={this.props.tilt} min={-2} max={2} step={0.1}
              onChange={(v) => {
                this.props.onEqParamChanged({ tilt: v })
              }}/>
          </Grid>
          <Grid>
            <InputSlider
              label='Max gain (dB)' value={this.props.maxGain} min={0} max={30} step={0.5}
              onChange={(v) => {
                this.props.onEqParamChanged({ maxGain: v })
              }}/>
          </Grid>
          <Grid item>
            <FormGroup>
              <FormControlLabel
                control={
                  <Checkbox
                    size='small' color='secondary'
                    value={this.state.showAdvanced}
                    onChange={(e, val) => {
                      this.setState({showAdvanced: val});
                    }}
                  />}
                label={'Show advanced parameters'}
                sx={{color: 'rgba(0, 0, 0, 0.5)'}}
              />
            </FormGroup>
          </Grid>

          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Bass boost center frequency (Hz)' value={this.props.bassBoostFc}
              min={20.0} max={500.0} step={5.0}
              onChange={(v) => {
                this.props.onEqParamChanged({ bassBoostFc: v })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Bass boost quality (Q)' value={this.props.bassBoostQ}
              min={0.3} max={1.0} step={0.1}
              onChange={(v) => {
                this.props.onEqParamChanged({ bassBoostQ: v })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble boost center frequency (Hz)' value={this.props.trebleBoostFc}
              min={1000.0} max={20000.0} step={5.0}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleBoostFc: v })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble boost quality (Q)' value={this.props.trebleBoostQ}
              min={0.3} max={1.0} step={0.1}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleBoostQ: v })
              }}/>
          </Grid>
          
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Smoothing window size (octaves)' value={this.props.windowSize}
              min={0} max={1} step={0.01}
              onChange={(v) => {
                this.props.onEqParamChanged({ windowSize: v })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble region smoothing window size (octaves)' value={this.props.trebleWindowSize}
              min={0} max={3} step={0.01}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleWindowSize: v })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble transition region (Hz)' value={[
                this.props.trebleFLower,
                this.props.trebleFUpper,
              ]}
              min={1000} max={20000} step={100}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleFLower: v[0], trebleFUpper: v[1] })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble region gain multiplier' value={this.props.trebleGainK}
              min={0.0} max={1.0} step={0.01}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleGainK: v })
              }}/>
          </Grid>
        </Grid>
      </Grid>
    )
  }
}

export default TargetTab;
