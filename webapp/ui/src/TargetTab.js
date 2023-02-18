import React from 'react';
import {
  Button,
  Checkbox, Chip,
  FormControlLabel,
  FormGroup,
  Grid,
  IconButton, Tooltip,
  Typography
} from '@mui/material';
import InputSlider from './InputSlider';
import CSVField from './CSVField';
import HeadphonesIcon from '@mui/icons-material/Headphones';
import FileOpenOutlinedIcon from '@mui/icons-material/FileOpenOutlined';
import AddIcon from '@mui/icons-material/Add';
import CSVAutocomplete from "./CSVAutocomplete";
import SaveOutlinedIcon from '@mui/icons-material/SaveOutlined';

class TargetTab extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showAdvanced: false,
      addingNewSoundProfile: false
    };
    this.onUseCurrentErrorClicked = this.onUseCurrentErrorClicked.bind(this);
  }

  onUseCurrentErrorClicked() {
    this.props.onEqParamChanged({
      soundSignature: this.props.graphData.map(dataPoint => ({
        frequency: dataPoint.frequency,
        raw: this.props.smoothed ? dataPoint.errorSmoothed : dataPoint.error
      }))
    });
  }

  render() {
    return (
      <Grid item xs={12} sm={12} container direction='column' rowSpacing={1}>
        <Grid
          item
          container direction='row' justifyContent='space-between' alignItems='center' columnSpacing={1}
          sx={{mb: theme => theme.spacing(1)}}
        >
          {this.props.soundProfiles.length === 0 && (
            <Grid item><Typography variant='caption'>Profiles</Typography></Grid>
          )}
          {this.props.soundProfiles.length > 0 && (
            <Grid item container direction='row' columnSpacing={1} alignItems='center' sx={{width: 'calc(100% - 40px)'}}>
              {this.props.soundProfiles.map((soundProfile) => (
                <Grid item key={soundProfile.name}>
                  <Chip
                    label={soundProfile.name}
                    onClick={() => { this.props.onSoundProfileSelected(soundProfile.name); }}
                    onDelete={soundProfile.name !== 'Default' ? () => { this.props.onSoundProfileDeleted(soundProfile.name); } : null}
                    color={this.props.selectedSoundProfile === soundProfile.name ? 'primary' : 'default'}
                    variant='outlined'
                  />
                  {this.props.selectedSoundProfile === soundProfile.name && this.props.selectedSoundProfile !== 'Default' && (
                    <Tooltip title={`Save current settings to profile ${soundProfile.name}`}>
                      <IconButton
                        onClick={() => this.props.onSoundProfileSaved(soundProfile.name)}
                        color='default'
                        sx={{p: '4px'}}
                      >
                        <SaveOutlinedIcon />
                      </IconButton>
                    </Tooltip>
                  )}
                </Grid>
              ))
              }
            </Grid>
          )}

          <Grid item>
            <Tooltip title='Create new profile with current settings' placement='left'>
              <Button
                variant='outlined'
                sx={{
                  minWidth: '32px',
                  width: '32px',
                  height: '32px',
                  borderRadius: '16px',
                  padding: 0
                }}
                onClick={() => { this.props.onSoundProfileCreated(); }}
              >
                <AddIcon variant='outlined' />
              </Button>
            </Tooltip>
          </Grid>
        </Grid>

        {this.props.compensations?.length > 0 && (
          <Grid item>
            <CSVAutocomplete
              value={this.props.selectedCompensation}
              options={this.props.compensations}
              onChange={this.props.onCompensationSelected}
              onOptionCreated={this.props.onCompensationCreated}
              onError={this.props.onError}
              sx={{width: '100%'}}
              label='Target'
              autocompleteProps={{
                disableClearable: true,
                blurOnSelect: true,
                isOptionEqualToValue: (opt, val) => opt.label === val
              }}
            />
          </Grid>
        )}

        <Grid item sx={{position: 'relative'}}>
          <CSVField
            label='Sound signature'
            onChange={(dataPoints) => { this.props.onEqParamChanged({ soundSignature: dataPoints }); }}
            value={this.props.soundSignature}
            helperText={
              <span>
                <Typography variant='body2' sx={{display: 'inline'}}>Edit the text directly, drop a CSV file or click </Typography>
                <FileOpenOutlinedIcon sx={{display: 'inline', height: '17px', width: '16px', transform: 'translate(-1px, 3px)'}} />
                <Typography variant='body2' sx={{display: 'inline'}}> to open a file. Click </Typography>
                <HeadphonesIcon sx={{display: 'inline', height: '17px', width: '16px', transform: 'translate(-1px, 3px)'}} />
                <Typography variant='body2' sx={{display: 'inline'}}> to use the current error curve.</Typography>
              </span>
            }
            minRows={5} maxRows={10}
          />
          <Tooltip title='Use current error' placement='left'>
            <IconButton
              variant='outlined' onClick={this.onUseCurrentErrorClicked}
              disabled={this.props.graphData.filter(x => this.props.smoothed ? !!x.errorSmoothed : !!x.error).length === 0}
              sx={{position: 'absolute', top: '88px', right: 0}}
            >
              <HeadphonesIcon />
            </IconButton>
          </Tooltip>
        </Grid>
        <Grid item>
          <InputSlider
            label='Sound signature smoothing'
            value={this.props.soundSignatureSmoothingWindowSize}
            onChange={(val) => { this.props.onEqParamChanged({ soundSignatureSmoothingWindowSize: val}); }}
            step={0.01} min={0} max={2}
          />
        </Grid>

        <Grid item container direction='row' columnSpacing={1}>
          <Grid item xs={12} sm={6} container direction='column' rowSpacing={0}>
            <Grid item>
              <InputSlider
                label='Bass boost (dB)' value={this.props.bassBoostGain} min={0} max={20} step={0.5}
                onChange={(v) => {
                  this.props.onEqParamChanged({bassBoostGain: v})
                }}
              />
            </Grid>
            <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
              <InputSlider
                label='Bass freq (Hz)' value={this.props.bassBoostFc}
                min={20.0} max={500.0} step={5.0}
                onChange={(v) => { this.props.onEqParamChanged({ bassBoostFc: v }); }}
              />
            </Grid>
            <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
              <InputSlider
                label='Bass quality' value={this.props.bassBoostQ}
                min={0.3} max={1.0} step={0.1}
                onChange={(v) => {
                  this.props.onEqParamChanged({ bassBoostQ: v })
                }}
              />
            </Grid>
          </Grid>
          <Grid item xs={12} sm={6} container direction='column' rowSpacing={0}>
            <Grid item>
              <InputSlider
                label='Treble boost (dB)' value={this.props.trebleBoostGain} min={-20} max={20} step={0.5}
                onChange={(v) => {
                  this.props.onEqParamChanged({ trebleBoostGain: v })
                }}
              />
            </Grid>
            <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
              <InputSlider
                label='Treble freq (Hz)' value={this.props.trebleBoostFc}
                min={1000.0} max={20000.0} step={5.0}
                onChange={(v) => {
                  this.props.onEqParamChanged({ trebleBoostFc: v })
                }}
              />
            </Grid>
            <Grid item sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
              <InputSlider
                label='Treble quality' value={this.props.trebleBoostQ}
                min={0.3} max={1.0} step={0.1}
                onChange={(v) => {
                  this.props.onEqParamChanged({ trebleBoostQ: v })
                }}
              />
            </Grid>
          </Grid>
        </Grid>

        <Grid item container direction='row' columnSpacing={1}>
          <Grid item xs={12} sm={6}>
            <InputSlider
              label='Tilt (db/oct)' value={this.props.tilt} min={-2} max={2} step={0.1}
              onChange={(v) => {
                this.props.onEqParamChanged({ tilt: v })
              }}
            />
          </Grid>
          <Grid item xs={12} sm={6}>
            <InputSlider
              label='Max gain (dB)' value={this.props.maxGain} min={0} max={30} step={0.5}
              onChange={(v) => {
                this.props.onEqParamChanged({ maxGain: v })
              }}
            />
          </Grid>
        </Grid>

        <Grid item container direction='row' columnSpacing={1}>
          <Grid item xs={12} sm={6} sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Smoothing window' value={this.props.windowSize}
              min={0} max={1} step={0.01}
              onChange={(v) => {
                this.props.onEqParamChanged({ windowSize: v })
              }}
            />
          </Grid>
          <Grid item xs={12} sm={6} sx={{display: this.state.showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble smoothing' value={this.props.trebleWindowSize}
              min={0} max={3} step={0.01}
              onChange={(v) => {
                this.props.onEqParamChanged({ trebleWindowSize: v })
              }}
            />
          </Grid>
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
      </Grid>
    )
  }
}

export default TargetTab;
