import React from 'react';
import {Autocomplete, Grid, TextField} from '@mui/material';
import EqAppEqualizerApoGraphicEq from './EqAppEqualizerApoGraphicEq';
import EqAppParametricEq from './EqAppParametricEq';
import find from 'lodash/find';

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
              filters={this.props.parametricFilters}
              fs={this.props.fs}
              onEqParamChanged={this.props.onEqParamChanged}
            />
          </Grid>
        )}
        {selectedEqualizer?.type === 'parametric' && selectedEqualizer?.label === 'Custom Parametric Eq' && (
          <Grid item>
            <EqAppParametricEq
              filters={this.props.parametricFilters}
              fs={this.props.fs}
              onEqParamChanged={this.props.onEqParamChanged}
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
              filters={this.props.fixedBandFilters}
              fs={this.props.fs}
              onEqParamChanged={this.props.onEqParamChanged}
            />
          </Grid>
        )}
      </Grid>
    );
  }
}

export default EqTab;
