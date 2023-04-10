import React, { useState } from 'react';
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
import AddIcon from '@mui/icons-material/Add';
import SaveOutlinedIcon from '@mui/icons-material/SaveOutlined';
import CSVAutocomplete from './CSVAutocomplete';
import Knob from './Knob';
import VolumeUpIcon from '@mui/icons-material/VolumeUp';

const TargetTab = (props) => {
  const [showAdvanced, setShowAdvanced] = useState(false);

  const onUseCurrentErrorClicked = () => {
    props.onEqParamChanged({
      soundSignature: props.graphData.map(dataPoint => ({
        frequency: dataPoint.frequency,
        raw: props.smoothed ? dataPoint.errorSmoothed : dataPoint.error
      }))
    });
  };

  return (
    <Grid item xs={12} sm={12} container direction='column' rowSpacing={1}>
      <Grid
        item
        container direction='row' justifyContent='space-between' alignItems='center' columnSpacing={1}
        sx={{mb: theme => theme.spacing(1)}}
      >
        {!(props.soundProfiles?.length) > 0 && (
          <Grid item><Typography variant='caption'>Profiles</Typography></Grid>
        )}
        {props.soundProfiles.length > 0 && (
          <Grid item container direction='row' columnSpacing={1} alignItems='center' sx={{width: 'calc(100% - 40px)'}}>
            {props.soundProfiles.map((soundProfile) => (
              <Grid item key={soundProfile.name}>
                <Chip
                  label={soundProfile.name}
                  onClick={() => { props.onSoundProfileSelected(soundProfile.name); }}
                  onDelete={soundProfile.name !== 'Default' ? () => { props.onSoundProfileDeleted(soundProfile.name); } : null}
                  color={props.selectedSoundProfile === soundProfile.name ? 'primary' : 'default'}
                  variant='outlined'
                />
                {props.selectedSoundProfile === soundProfile.name && props.selectedSoundProfile !== 'Default' && (
                  <Tooltip title={`Save current settings to profile ${soundProfile.name}`}>
                    <IconButton
                      onClick={() => props.onSoundProfileSaved(soundProfile.name)}
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
              onClick={() => { props.onSoundProfileCreated(); }}
            >
              <AddIcon variant='outlined' />
            </Button>
          </Tooltip>
        </Grid>
      </Grid>

      {props.compensations?.length > 0 && (
        <Grid item>
          <CSVAutocomplete
            value={props.selectedCompensation}
            options={props.compensations}
            onChange={props.onCompensationSelected}
            onOptionCreated={props.onCompensationCreated}
            onError={props.onError}
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

      <Grid item container direction='row' justifyContent='space-between'>
        <Grid item sx={{position: 'relative'}}>
          <CSVField
            label='Sound signature'
            onChange={(dataPoints) => { props.onEqParamChanged({ soundSignature: dataPoints }); }}
            value={props.soundSignature}
            // helperText={
            //   <span>
            //   <Typography variant='body2' sx={{display: 'inline'}}>Edit the text directly, drop a CSV file or click </Typography>
            //   <FileOpenOutlinedIcon sx={{display: 'inline', height: '17px', width: '16px', transform: 'translate(-1px, 3px)'}} />
            //   <Typography variant='body2' sx={{display: 'inline'}}> to open a file. Click </Typography>
            //   <HeadphonesIcon sx={{display: 'inline', height: '17px', width: '16px', transform: 'translate(-1px, 3px)'}} />
            //   <Typography variant='body2' sx={{display: 'inline'}}> to use the current error curve.</Typography>
            // </span>
            // }
            helperText=''
            minRows={5} maxRows={10}
          />
          <Tooltip title='Use current error' placement='left'>
            <IconButton
              variant='outlined' onClick={onUseCurrentErrorClicked}
              disabled={props.graphData.filter(x => props.smoothed ? !!x.errorSmoothed : !!x.error).length === 0}
              sx={{position: 'absolute', top: '80px', right: 0}}
            >
              <HeadphonesIcon />
            </IconButton>
          </Tooltip>
        </Grid>
        <Grid item>
          <Knob
            value={props.soundSignatureSmoothingWindowSize}
            onChange={(val) => { props.onEqParamChanged({ soundSignatureSmoothingWindowSize: val}); }}
            formattedValue={props.soundSignatureSmoothingWindowSize.toFixed(2)}
            minValue={0}
            maxValue={2}
            size={120}
            unit='oct'
            icon={VolumeUpIcon}
            nTicks={9}
            label='Smoothing'
          />
        </Grid>
      </Grid>

      <Grid item container direction='row' columnSpacing={1}>
        <Grid item xs={12} sm={6} container direction='column' rowSpacing={0}>
          <Grid item>
            <InputSlider
              label='Bass boost (dB)' value={props.bassBoostGain} min={0} max={20} step={0.5}
              onChange={(v) => {
                props.onEqParamChanged({bassBoostGain: v})
              }}
            />
          </Grid>
          <Grid item sx={{display: showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Bass freq (Hz)' value={props.bassBoostFc}
              min={20.0} max={500.0} step={5.0}
              onChange={(v) => { props.onEqParamChanged({ bassBoostFc: v }); }}
            />
          </Grid>
          <Grid item sx={{display: showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Bass quality' value={props.bassBoostQ}
              min={0.3} max={1.0} step={0.05}
              onChange={(v) => {
                props.onEqParamChanged({ bassBoostQ: v })
              }}
            />
          </Grid>
        </Grid>
        <Grid item xs={12} sm={6} container direction='column' rowSpacing={0}>
          <Grid item>
            <InputSlider
              label='Treble boost (dB)' value={props.trebleBoostGain} min={-20} max={20} step={0.5}
              onChange={(v) => {
                props.onEqParamChanged({ trebleBoostGain: v })
              }}
            />
          </Grid>
          <Grid item sx={{display: showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble freq (Hz)' value={props.trebleBoostFc}
              min={1000.0} max={20000.0} step={5.0}
              onChange={(v) => {
                props.onEqParamChanged({ trebleBoostFc: v })
              }}
            />
          </Grid>
          <Grid item sx={{display: showAdvanced ? 'block' : 'none'}}>
            <InputSlider
              label='Treble quality' value={props.trebleBoostQ}
              min={0.3} max={1.0} step={0.05}
              onChange={(v) => {
                props.onEqParamChanged({ trebleBoostQ: v })
              }}
            />
          </Grid>
        </Grid>
      </Grid>

      <Grid item container direction='row' columnSpacing={1}>
        <Grid item xs={12} sm={6}>
          <InputSlider
            label='Tilt (db/oct)' value={props.tilt} min={-2} max={2} step={0.1}
            onChange={(v) => {
              props.onEqParamChanged({ tilt: v })
            }}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <InputSlider
            label='Max gain (dB)' value={props.maxGain} min={0} max={30} step={0.5}
            onChange={(v) => {
              props.onEqParamChanged({ maxGain: v })
            }}
          />
        </Grid>
      </Grid>

      <Grid item container direction='row' columnSpacing={1}>
        <Grid item xs={12} sm={6} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <InputSlider
            label='Smoothing size' value={props.windowSize}
            min={0} max={1} step={0.01}
            onChange={(v) => {
              props.onEqParamChanged({ windowSize: v })
            }}
          />
        </Grid>
        <Grid item xs={12} sm={6} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <InputSlider
            label='Treble smoothing' value={props.trebleWindowSize}
            min={0} max={3} step={0.01}
            onChange={(v) => {
              props.onEqParamChanged({ trebleWindowSize: v })
            }}
          />
        </Grid>
      </Grid>

      <Grid item sx={{display: showAdvanced ? 'block' : 'none'}}>
        <InputSlider
          label='Treble transition region (Hz)' value={[
            props.trebleFLower,
            props.trebleFUpper,
          ]}
          min={1000} max={20000} step={100}
          onChange={(v) => {
            props.onEqParamChanged({ trebleFLower: v[0], trebleFUpper: v[1] })
          }}
        />
      </Grid>

      <Grid item sx={{display: showAdvanced ? 'block' : 'none'}}>
        <InputSlider
          label='Treble region gain multiplier' value={props.trebleGainK}
          min={0.0} max={1.0} step={0.01}
          onChange={(v) => {
            props.onEqParamChanged({ trebleGainK: v })
          }}
        />
      </Grid>

      <Grid item>
        <FormGroup>
          <FormControlLabel
            control={
              <Checkbox
                size='small' color='secondary'
                value={showAdvanced}
                onChange={(e, val) => setShowAdvanced(val)}
              />
            }
            label='Show advanced' sx={{color: 'rgba(0, 0, 0, 0.5)'}}
          />
        </FormGroup>
      </Grid>
    </Grid>
  )
};

export default TargetTab;
