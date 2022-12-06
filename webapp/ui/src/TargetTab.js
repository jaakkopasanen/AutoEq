import React from 'react';
import {Autocomplete, Checkbox, FormControlLabel, FormGroup, Grid, TextField} from "@mui/material";
import InputSlider from "./InputSlider";

class TargetTab extends React.Component {
  constructor(props) {
    super(props);
    this.state = {showAdvanced: false};
  }

  render() {
    return (
      <Grid container direction='row' spacing={2} sx={{p: 1}}>
        <Grid item xs={12} md={6} container direction='column' rowSpacing={1}>
          {!!this.props.compensations && (
            <Grid item>
              <Autocomplete
                xs={6}
                renderInput={(params) =>
                  <TextField {...params} label="Select compensation"/>
                }
                options={this.props.compensations}
                onChange={(e, val) => {
                  this.props.onEqParamChanged({ compensation: val?.name })
                }}
                sx={{width: '100%'}}
              />
            </Grid>
          )}
          {!!this.props.measurements && (
            <Grid item>
              <Autocomplete
                xs={6}
                renderInput={(params) =>
                  <TextField {...params} label="Select sound signature"/>
                }
                options={this.props.measurements}
                onChange={(e, val) => {
                  this.props.onEqParamChanged({ sound_signature: val?.name })
                }}
                sx={{width: '100%'}}
              />
            </Grid>
          )}
        </Grid>
        <Grid item xs={12} sm={6} container direction='column' rowSpacing={1}>
          <Grid item>
            <InputSlider
              label='Bass boost (dB)' value={this.props.eqParams.bass_boost_gain} min={-10} max={20} step={0.5}
              onChange={(v) => {
                this.props.onEqParamChanged({bass_boost_gain: v})
              }}/>
          </Grid>
          <Grid item>
            <InputSlider
              label='Treble boost (dB)' value={this.props.eqParams.treble_boost_gain} min={-20} max={20} step={0.5}
              onChange={(v) => {
                this.props.onEqParamChanged({ treble_boost_gain: v })
              }}/>
          </Grid>
          <Grid item>
            <InputSlider
              label='Tilt (db/oct)' value={this.props.eqParams.tilt} min={-2} max={2} step={0.1}
              onChange={(v) => {
                this.props.onEqParamChanged({ tilt: v })
              }}/>
          </Grid>
          <Grid>
            <InputSlider
              label='Max gain (dB)' value={this.props.eqParams.max_gain} min={0} max={30} step={0.5}
              onChange={(v) => {
                this.props.onEqParamChanged({ max_gain: v })
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
              label='Bass boost center frequency (Hz)' value={this.props.eqParams.bass_boost_fc}
              min={20.0} max={500.0} step={5.0}
              onChange={(v) => {
                this.props.onEqParamChanged({ bass_boost_fc: v })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Bass boost quality (Q)' value={this.props.eqParams.bass_boost_q}
              min={0.3} max={1.0} step={0.1}
              onChange={(v) => {
                this.props.onEqParamChanged({ bass_boost_q: v })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble boost center frequency (Hz)' value={this.props.eqParams.treble_boost_fc}
              min={1000.0} max={20000.0} step={5.0}
              onChange={(v) => {
                this.props.onEqParamChanged({ treble_boost_fc: v })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble boost quality (Q)' value={this.props.eqParams.treble_boost_q}
              min={0.3} max={1.0} step={0.1}
              onChange={(v) => {
                this.props.onEqParamChanged({ treble_boost_q: v })
              }}/>
          </Grid>
          
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Smoothing window size (octaves)' value={this.props.eqParams.window_size}
              min={0} max={1} step={0.01}
              onChange={(v) => {
                this.props.onEqParamChanged({ window_size: v })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble region smoothing window size (octaves)' value={this.props.eqParams.treble_window_size}
              min={0} max={3} step={0.01}
              onChange={(v) => {
                this.props.onEqParamChanged({ treble_window_size: v })
              }}/>
          </Grid>
          <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble transition region (Hz)' value={[
                this.props.eqParams.treble_f_lower,
                this.props.eqParams.treble_f_upper,
              ]}
              min={1000} max={20000} step={100}
              onChange={(v) => {
                this.props.onEqParamChanged({ treble_f_lower: v[0], treble_f_upper: v[1] })
              }}/>
          </Grid>
        </Grid>
      </Grid>
    )
  }
}

export default TargetTab;
