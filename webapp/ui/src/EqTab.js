import React from 'react';
import {Autocomplete, Grid, TextField} from '@mui/material';
import EqAppEqualizerApoGraphicEq from './EqAppEqualizerApoGraphicEq';
import EqAppParametricEq from './EqAppParametricEq';

class EqTab extends React.Component {
  render() {
    console.log(this.props.fixedBandFilters);
    return (
      <Grid container direction='column'>
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
            <EqAppParametricEq filters={this.props.parametricFilters} />
          </Grid>
        )}
        {this.props.selectedEqualizer?.type === 'fixedBand' && (
          <Grid item>
            <EqAppParametricEq filters={this.props.fixedBandFilters} />
          </Grid>
        )}
      </Grid>
    );
  }
}

export default EqTab;
