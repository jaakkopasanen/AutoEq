import React, { useState } from 'react';
import {
  Button,
  Chip,
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
        <Grid item sx={{display: showAdvanced ? 'block' : 'none'}}>
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

      <Grid
        item
        container
        direction='row'
        justifyContent='space-between'
        columnSpacing={2}
        sx={{display: showAdvanced ? 'flex' : 'none'}}
      >
        <Grid item sx={{position: 'relative', flexGrow: 1, width: '185px'}}>
          <CSVField
            label='Sound signature'
            onChange={(dataPoints) => { props.onEqParamChanged({ soundSignature: dataPoints }); }}
            value={props.soundSignature}
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
            initialValue={props.soundSignatureSmoothingWindowSize}
            onChange={(val) => { props.onEqParamChanged({ soundSignatureSmoothingWindowSize: val}); }}
            formatter={(val) => val.toFixed(2)}
            minValue={0} maxValue={2} step={0.1}
            size={115}
            unit='oct'
            nTicks={9}
            label='Smoothing'
            tooltip='Sound signature smoothing window size. Useful for making the sound signature smooth when only a few points are present.'
          />
        </Grid>
      </Grid>

      <Grid item container direction='row' columnSpacing={2} rowSpacing={2} justifyContent='center' sx={{mt: 0}}>
        <Grid item xs={4}>
          <Knob
            initialValue={props.bassBoostGain}
            minValue={0} maxValue={20} step={0.5}
            label='Bass boost'
            onChange={(v) => { props.onEqParamChanged({bassBoostGain: v}) }}
            formatter={(val) => val !== undefined ? val.toFixed(1) : ''}
            size={120}
            unit='dB'
            nTicks={9}
            style={{margin: 'auto'}}
            tooltip='Bass boost level'
          />
        </Grid>

        <Grid item xs={4} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <Knob
            initialValue={props.bassBoostFc}
            minValue={20.0} maxValue={300.0} step={5}
            label='Bass freq'
            onChange={(v) => { props.onEqParamChanged({bassBoostFc: v}) }}
            formatter={(val) => val.toFixed(0)}
            size={120}
            unit='Hz'
            nTicks={9}
            tooltip='Bass boost shelf center frequency'
          />
        </Grid>

        <Grid item xs={4} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <Knob
            initialValue={props.bassBoostQ}
            minValue={0.3} maxValue={0.8} step={0.05}
            label='Bass quality'
            onChange={(v) => { props.onEqParamChanged({bassBoostQ: v}) }}
            formatter={(val) => val.toFixed(2)}
            size={120}
            nTicks={9}
            tooltip='Bass boost shelf quality (slope steepness)'
          />
        </Grid>

        <Grid item xs={4}>
          <Knob
            initialValue={props.trebleBoostGain}
            minValue={-15} maxValue={15} step={0.5}
            label='Treble boost'
            onChange={(v) => { props.onEqParamChanged({trebleBoostGain: v}) }}
            formatter={v => v.toFixed(1)}
            size={120}
            unit='dB'
            nTicks={9}
            tooltip='Treble boost level'
          />
        </Grid>

        <Grid item xs={4} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <Knob
            initialValue={props.trebleBoostFc}
            minValue={1000} maxValue={20000} step={1000}
            label='Treble freq'
            onChange={(v) => { props.onEqParamChanged({trebleBoostFc: v}) }}
            formatter={(val) => val.toFixed(0)}
            size={120}
            unit='Hz'
            nTicks={9}
            tooltip='Treble boost shelf center frequency'
          />
        </Grid>

        <Grid item xs={4} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <Knob
            initialValue={props.trebleBoostQ}
            minValue={0.3} maxValue={0.8} step={0.1}
            label='Treble quality'
            onChange={(v) => { props.onEqParamChanged({trebleBoostQ: v}) }}
            formatter={(val) => val.toFixed(2)}
            size={120}
            nTicks={9}
            tooltip='Treble boost shelf quality (slope steepness)'
          />
        </Grid>

        <Grid item xs={4}>
          <Knob
            initialValue={props.maxGain}
            minValue={0} maxValue={36} step={1}
            label='Max gain'
            onChange={(v) => { props.onEqParamChanged({maxGain: v}) }}
            formatter={(val) => val.toFixed(1)}
            size={120}
            unit='dB'
            nTicks={9}
            tooltip="Maximum gain for EQ. Decrease max gain if you're not getting enough volume."
          />
        </Grid>

        <Grid item xs={4} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <Knob
            initialValue={props.tilt}
            minValue={0} maxValue={2} step={0.1}
            label='Tilt'
            onChange={(v) => { props.onEqParamChanged({ tilt: v }) }}
            formatter={(val) => val.toFixed(2)}
            size={120}
            unit='dB/oct'
            nTicks={9}
            tooltip='Frequency response tilt. Positive values make sound brighter and negative darker.'
          />
        </Grid>

        <Grid item xs={4} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <Knob
            initialValue={props.maxSlope}
            minValue={6} maxValue={36} step={3}
            label='Max slope'
            onChange={(v) => { props.onEqParamChanged({ maxSlope: v }) }}
            formatter={(val) => val.toFixed(0)}
            size={120}
            unit='dB/oct'
            nTicks={9}
            tooltip='Maximum slope steepness for equalizer frequency response. Try lowering the value if peaks at high frequencies sound unpleasant.'
          />
        </Grid>

        <Grid item xs={4} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <Knob
            initialValue={props.windowSize}
            minValue={0} maxValue={1} step={0.1}
            label='Smoothing'
            onChange={(v) => { props.onEqParamChanged({ windowSize: v }) }}
            formatter={(val) => val.toFixed(2)}
            size={120}
            unit='oct'
            nTicks={9}
            tooltip='Smoothing window size. Higher values make curves smoother.'
          />
        </Grid>

        <Grid item xs={4} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <Knob
            initialValue={props.trebleWindowSize}
            minValue={0} maxValue={3} step={0.1}
            label='Treble smoothing'
            onChange={(v) => { props.onEqParamChanged({ trebleWindowSize: v }) }}
            formatter={(val) => val.toFixed(2)}
            size={120}
            unit='oct'
            nTicks={9}
            tooltip='Smoothing window size above treble transition region'
          />
        </Grid>

        <Grid item xs={4} sx={{display: showAdvanced ? 'block' : 'none'}}>
          <Knob
            initialValue={props.trebleGainK}
            minValue={0} maxValue={1} step={0.05}
            label='Treble gain multiplier'
            onChange={(v) => { props.onEqParamChanged({ trebleGainK: v }) }}
            formatter={(val) => val.toFixed(2)}
            size={120}
            nTicks={9}
            tooltip='Treble region gain multiplier. Useful for reducing EQ in the highest frequencies.'
          />
        </Grid>

      </Grid>

      <Grid item xs={4} sx={{display: showAdvanced ? 'block' : 'none'}}>
        <InputSlider
          label='Treble transition region (Hz)'
          initialValue={[ props.trebleFLower, props.trebleFUpper, ]}
          min={1000} max={20000} step={100}
          onChange={(v) => { props.onEqParamChanged({ trebleFLower: v[0], trebleFUpper: v[1] }) }}
          inputChars={5}
        />
      </Grid>

      <Grid item sx={{ mt: 1, textAlign: 'center'}}>
        <Typography
          variant='caption' color='primary'
          sx={{ cursor: 'pointer' }}
          onClick={() => { setShowAdvanced(!showAdvanced); }}>
          {showAdvanced ? 'Hide advanced' : 'Show advanced'}
        </Typography>
      </Grid>
    </Grid>
  )
};

export default TargetTab;
