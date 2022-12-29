import React from 'react';
import {Autocomplete, Grid, TextField} from "@mui/material";
import EqAppWavelet from "./EqAppWavelet";

class EqTab extends React.Component {
  render() {
    return (
      <Grid container direction='column'>
        <Grid item>
          <Autocomplete
            renderInput={(params) =>
              <TextField {...params} label='Select equalizer app' />
            }
            options={['Wavelet', 'EqualizerAPO GraphicEq']}
            value={this.props.selectedEqualizer}
            onChange={(e, val) => { this.props.onEqualizerChanged(val); }}
          />
        </Grid>
        {this.props.selectedEqualizer === 'Wavelet' && (
          <Grid item sx={{maxWidth: '100%', width: '100%'}}>
            <EqAppWavelet
              selectedMeasurement={this.props.selectedMeasurement}
              graphicEq={this.props.graphicEq}
            />
          </Grid>
        )}
      </Grid>
    );
  }
}

export default EqTab;
