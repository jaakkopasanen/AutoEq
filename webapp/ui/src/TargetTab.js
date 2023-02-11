import React from 'react';
import {Autocomplete, Button, Checkbox, FormControlLabel, FormGroup, Grid, TextField} from "@mui/material";
import InputSlider from "./InputSlider";
import CSVAutocomplete from "./CSVAutocomplete";

class TargetTab extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showAdvanced: false,
      showSoundSignatureEdit: false,
      newSoundSignatureValue: null,
      soundSignatureSmoothingWindowSize: 0,
    };
    this.onUseCurrentErrorClicked = this.onUseCurrentErrorClicked.bind(this);
    this.onUseCurrentErrorClicked = this.onUseCurrentErrorClicked.bind(this);
  }

  onUseCurrentErrorClicked() {
    this.setState({
      newSoundSignatureValue: this.props.graphData.map(dataPoint => ({
        frequency: dataPoint.frequency,
        raw: dataPoint.error
      }))
    });
  }

  render() {
    return (
      <Grid container direction='row' columnSpacing={1}>
        <Grid item xs={12} sm={12} container direction='column' rowSpacing={1}>
          {!!this.props.compensations && (
            <Grid item>
              <Autocomplete
                renderInput={(params) =>
                  <TextField {...params} label='Select compensation'/>
                }
                options={this.props.compensations}
                value={this.props.selectedCompensation}
                onChange={(e, val) => {
                  this.props.onCompensationSelected(val)
                }}
                sx={{width: '100%'}}
              />
            </Grid>
          )}
          <Grid item container direction='column' rowSpacing={1}>
            <Grid item>
              <CSVAutocomplete
                value={this.props.selectedSoundSignature}
                newData={this.state.newSoundSignatureValue}
                options={this.props.soundSignatures}
                onChange={this.props.onSoundSignatureSelected}
                autocompleteProps={{
                  sx: {background: (theme) => theme.palette.background.default},
                  size: 'large',
                  blurOnSelect: true,
                }}
                autocompleteLabel='Sound signature'
                onOptionCreated={(name, frequency, raw) => {
                  this.setState({ showSoundSignatureEdit: false });
                  this.props.onSoundSignatureCreated(name, frequency, raw, this.state.soundSignatureSmoothingWindowSize);
                }}
                onOptionUpdated={(label, name, frequency, raw) => {
                  this.props.onSoundSignatureUpdated(label, name, frequency, raw, this.state.soundSignatureSmoothingWindowSize);
                }}
                showEdit={this.state.showSoundSignatureEdit}
                onShowEditChanged={() => {
                  this.setState({ showSoundSignatureEdit: !this.state.showSoundSignatureEdit });
                }}
              />
            </Grid>
            {this.state.showSoundSignatureEdit && (
              <Grid item>
                <InputSlider
                  label='Smoothing window size'
                  value={this.state.soundSignatureSmoothingWindowSize}
                  onChange={(val) => { this.setState({ soundSignatureSmoothingWindowSize: val}); }}
                  step={0.01} min={0} max={2}
                />
              </Grid>
            )}
            {this.state.showSoundSignatureEdit && (
              <Grid item>
                <Button
                  variant='outlined' onClick={this.onUseCurrentErrorClicked}
                  disabled={this.props.graphData.filter(x => !!x.error).length === 0}
                >
                  Use current error
                </Button>
              </Grid>
            )}
          </Grid>
        </Grid>
        <Grid item xs={12} sm={12} container direction='column' rowSpacing={1}>
          <Grid item>
            <InputSlider
              label='Bass boost (dB)' value={this.props.bassBoostGain} min={0} max={20} step={0.5}
              onChange={(v) => {
                this.props.onEqParamChanged({bassBoostGain: v})
              }}
            />
          </Grid>
          <Grid item>
            <InputSlider
              label='Treble boost (dB)' value={this.props.trebleBoostGain} min={-20} max={20} step={0.5}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleBoostGain: v })
              }}
            />
          </Grid>
          <Grid item>
            <InputSlider
              label='Tilt (db/oct)' value={this.props.tilt} min={-2} max={2} step={0.1}
              onChange={(v) => {
                this.props.onEqParamChanged({ tilt: v })
              }}
            />
          </Grid>
          <Grid>
            <InputSlider
              label='Max gain (dB)' value={this.props.maxGain} min={0} max={30} step={0.5}
              onChange={(v) => {
                this.props.onEqParamChanged({ maxGain: v })
              }}
            />
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
                label={'Show advanced'}
                sx={{color: 'rgba(0, 0, 0, 0.5)'}}
              />
            </FormGroup>
          </Grid>

          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Bass boost center frequency (Hz)' value={this.props.bassBoostFc}
              min={20.0} max={500.0} step={5.0}
              onChange={(v) => { this.props.onEqParamChanged({ bassBoostFc: v }); }}
            />
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Bass boost quality (Q)' value={this.props.bassBoostQ}
              min={0.3} max={1.0} step={0.1}
              onChange={(v) => {
                this.props.onEqParamChanged({ bassBoostQ: v })
              }}
            />
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble boost center frequency (Hz)' value={this.props.trebleBoostFc}
              min={1000.0} max={20000.0} step={5.0}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleBoostFc: v })
              }}
            />
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble boost quality (Q)' value={this.props.trebleBoostQ}
              min={0.3} max={1.0} step={0.1}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleBoostQ: v })
              }}
            />
          </Grid>
          
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Smoothing window size (octaves)' value={this.props.windowSize}
              min={0} max={1} step={0.01}
              onChange={(v) => {
                this.props.onEqParamChanged({ windowSize: v })
              }}
            />
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble region smoothing window size (octaves)' value={this.props.trebleWindowSize}
              min={0} max={3} step={0.01}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleWindowSize: v })
              }}
            />
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
              }}
            />
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble region gain multiplier' value={this.props.trebleGainK}
              min={0.0} max={1.0} step={0.01}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleGainK: v })
              }}
            />
          </Grid>
        </Grid>
      </Grid>
    )
  }
}

export default TargetTab;
