import React from 'react';
import {Autocomplete, Grid, TextField} from '@mui/material';
import EqAppEqualizerApoGraphicEq from './EqAppEqualizerApoGraphicEq';
import EqAppParametricEq from './EqAppParametricEq';
import find from 'lodash/find';
import EqAppConvolutionEq from "./EqAppConvolutionEq";

class EqTab extends React.Component {
  render() {
    let selectedEqualizer = find(this.props.equalizers, (equalizer) => equalizer.label === this.props.selectedEqualizer);
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
            options={this.props.equalizers}
            value={selectedEqualizer}
            isOptionEqualToValue={(option, value) => option.label === value.label}
            onChange={(e, val) => { this.props.onEqualizerSelected(val.label); }}
            disableClearable
          />
        </Grid>
        {selectedEqualizer?.type === 'graphic' && (
          <Grid item sx={{maxWidth: '100%', width: '100%'}}>
            <EqAppEqualizerApoGraphicEq
              selectedMeasurement={this.props.selectedMeasurement}
              graphicEq={this.props.graphicEq}
            />
          </Grid>
        )}
        {selectedEqualizer?.type === 'parametric' && selectedEqualizer?.label !== 'Custom Parametric Eq' && (
          <Grid item>
            <EqAppParametricEq
              selectedMeasurement={this.props.selectedMeasurement}
              parametricEq={this.props.parametricEq}
              fs={this.props.fs}
              onEqParamChanged={this.props.onEqParamChanged}
              uiConfig={selectedEqualizer?.uiConfig}
              preamp={this.props.preamp}
            />
          </Grid>
        )}
        {selectedEqualizer?.type === 'parametric' && selectedEqualizer?.label === 'Custom Parametric Eq' && (
          <Grid item>
            <EqAppParametricEq
              selectedMeasurement={this.props.selectedMeasurement}
              parametricEq={this.props.parametricEq}
              fs={this.props.fs}
              onEqParamChanged={this.props.onEqParamChanged}
              uiConfig={selectedEqualizer?.uiConfig}
              showConfig
              config={this.props.customPeqConfig}
              onConfigChanged={this.props.onCustomPeqConfigChanged}
              onConfigFilterChanged={this.props.onCustomPeqConfigFilterChanged}
              onAddFilterClick={this.props.onCustomPeqAddFilterClick}
              onFilterDeleteClick={this.props.onCustomPeqDeleteFilterClick}
            />
          </Grid>
        )}
        {selectedEqualizer?.type === 'fixedBand' && (
          <Grid item>
            <EqAppParametricEq
              parametricEq={this.props.fixedBandEq}
              fs={this.props.fs}
              onEqParamChanged={this.props.onEqParamChanged}
              fixedBands
            />
          </Grid>
        )}
        {selectedEqualizer?.type === 'convolution' && (
          <Grid item>
            <EqAppConvolutionEq
              firAudioBuffer={this.props.firAudioBuffer}
              fs={this.props.fs}
              bitDepth={this.props.bitDepth}
              phase={this.props.phase}
              fRes={this.props.fRes}
              preamp={this.props.preamp}
              selectedMeasurement={this.props.selectedMeasurement}
              onEqParamChanged={this.props.onEqParamChanged}
            />
          </Grid>
        )}
      </Grid>
    );
  }
}

export default EqTab;
