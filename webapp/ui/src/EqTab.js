import React from 'react';
import {Autocomplete, Grid, TextField} from '@mui/material';
import EqAppEqualizerApoGraphicEq from './EqAppEqualizerApoGraphicEq';
import EqAppParametricEq from './EqAppParametricEq';

class EqTab extends React.Component {
  render() {
    return (
      <Grid container direction='column'>
        <Grid item>
          <Autocomplete
            renderInput={(params) =>
              <TextField {...params} label='Select equalizer app' />
            }
            options={[
              {label: 'Wavelet', type: 'graphic'},
              {label: 'EqualizerAPO GraphicEq', type: 'graphic'},
              {label: 'EqualizerAPO ParametricEq', type: 'parametric'}
            ]}
            value={this.props.selectedEqualizer}
            isOptionEqualToValue={(option, value) => option.label === value.label}
            onChange={(e, val) => { this.props.onEqualizerChanged(val); }}
          />
        </Grid>
        {['Wavelet', 'EqualizerAPO GraphicEq'].includes(this.props.selectedEqualizer?.label) && (
          <Grid item sx={{maxWidth: '100%', width: '100%'}}>
            <EqAppEqualizerApoGraphicEq
              selectedMeasurement={this.props.selectedMeasurement}
              graphicEq={this.props.graphicEq}
            />
          </Grid>
        )}
        {this.props.selectedEqualizer?.label === 'EqualizerAPO ParametricEq' && (
          <Grid item>
            <EqAppParametricEq
              parametricFilters={this.props.parametricFilters}
            />
          </Grid>
        )}
      </Grid>
    );
  }
}

export default EqTab;
