import React from 'react';
import {Autocomplete, Grid, TextField} from '@mui/material';
import EqAppEqualizerApoGraphicEq from './EqAppEqualizerApoGraphicEq';
import EqAppParametricEq from './EqAppParametricEq';
import find from 'lodash/find';
import EqAppConvolutionEq from "./EqAppConvolutionEq";

const EqTab = (props) => {
  let selectedEqualizer = find(props.equalizers, (equalizer) => equalizer.label === props.selectedEqualizer);
  if (typeof selectedEqualizer === 'undefined') {
    selectedEqualizer = null;
  }
  return (
    <Grid container direction='column' rowSpacing={1}>
      <Grid item>
        <Autocomplete
          renderInput={(params) =>
            <TextField {...params} label='Select equalizer app' />
          }
          options={props.equalizers}
          value={selectedEqualizer}
          isOptionEqualToValue={(option, value) => option.label === value.label}
          onChange={(e, val) => { props.onEqualizerSelected(val.label); }}
          disableClearable
          blurOnSelect
        />
      </Grid>
      {selectedEqualizer?.type === 'graphic' && (
        <Grid item sx={{maxWidth: '100%', width: '100%'}}>
          <EqAppEqualizerApoGraphicEq
            selectedMeasurement={props.selectedMeasurement}
            graphicEq={props.graphicEq}
            instructions={selectedEqualizer?.instructions}
          />
        </Grid>
      )}
      {selectedEqualizer?.type === 'parametric' && selectedEqualizer?.label !== 'Custom Parametric Eq' && (
        <Grid item>
          <EqAppParametricEq
            selectedMeasurement={props.selectedMeasurement}
            parametricEq={props.parametricEq}
            fs={props.fs}
            onEqParamChanged={props.onEqParamChanged}
            uiConfig={selectedEqualizer?.uiConfig}
            eqParams={selectedEqualizer?.eqParams}
            instructions={selectedEqualizer?.instructions}
            preamp={props.preamp}
            fileFormatter={selectedEqualizer?.fileFormatter}
          />
        </Grid>
      )}
      {selectedEqualizer?.type === 'parametric' && selectedEqualizer?.label === 'Custom Parametric Eq' && (
        <Grid item>
          <EqAppParametricEq
            selectedMeasurement={props.selectedMeasurement}
            parametricEq={props.parametricEq}
            fs={props.fs}
            onEqParamChanged={props.onEqParamChanged}
            uiConfig={selectedEqualizer?.uiConfig}
            showConfig
            config={props.customPeqConfig}
            onConfigChanged={props.onCustomPeqConfigChanged}
            onConfigFilterChanged={props.onCustomPeqConfigFilterChanged}
            onAddFilterClick={props.onCustomPeqAddFilterClick}
            onFilterDeleteClick={props.onCustomPeqDeleteFilterClick}
            instructions={selectedEqualizer?.instructions}
          />
        </Grid>
      )}
      {selectedEqualizer?.type === 'fixedBand' && (
        <Grid item>
          <EqAppParametricEq
            parametricEq={props.fixedBandEq}
            fs={props.fs}
            onEqParamChanged={props.onEqParamChanged}
            fixedBands
            instructions={selectedEqualizer?.instructions}
          />
        </Grid>
      )}
      {selectedEqualizer?.type === 'convolution' && (
        <Grid item>
          <EqAppConvolutionEq
            audioContext={props.audioContext}
            firAudioBuffer={props.firAudioBuffer}
            fs={props.fs}
            bitDepth={props.bitDepth}
            phase={props.phase}
            fRes={props.fRes}
            preamp={props.preamp}
            selectedMeasurement={props.selectedMeasurement}
            onEqParamChanged={props.onEqParamChanged}
            instructions={selectedEqualizer?.instructions}
          />
        </Grid>
      )}
    </Grid>
  );
};

export default EqTab;
