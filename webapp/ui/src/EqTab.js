import React from 'react';
import {Autocomplete, Grid, TextField} from '@mui/material';
import EqAppEqualizerApoGraphicEq from './EqAppEqualizerApoGraphicEq';
import EqAppParametricEq from './EqAppParametricEq';

class EqTab extends React.Component {
  render() {
    return (
      <Grid container direction='column' rowSpacing={1}>
        <Grid item>
          <Autocomplete
            renderInput={(params) =>
              <TextField {...params} label='Select equalizer app' />
            }
            options={this.props.equalizers}
            value={this.props.selectedEqualizer}
            isOptionEqualToValue={(option, value) => option.label === value.label}
            onChange={(e, val) => { this.props.onEqualizerChanged(val); }}
          />
        </Grid>
        {this.props.selectedEqualizer?.type === 'graphic' && (
          <Grid item sx={{maxWidth: '100%', width: '100%'}}>
            <EqAppEqualizerApoGraphicEq
              selectedMeasurement={this.props.selectedMeasurement}
              graphicEq={this.props.graphicEq}
            />
          </Grid>
        )}
        {this.props.selectedEqualizer?.type === 'parametric' && (
          <Grid item>
            <EqAppParametricEq
              filters={this.props.parametricFilters}
              fs={this.props.fs}
              onEqParamChanged={this.props.onEqParamChanged}
            />
          </Grid>
        )}
        {this.props.selectedEqualizer?.type === 'fixedBand' && (
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
