import React from 'react';
import {Grid, Table, TableBody, TableCell, TableHead, TableRow} from '@mui/material';

class EqAppParametricEq extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showBandwidth: false
    };
  }

  bandwidth(q) {
    // TODO: LowShelf and HighShelf bandwidths
    return Math.log2((2*q**2+1) / (2*q**2) + Math.sqrt((((2*q**2 + 1) / q**2)**2)/4-1));
  }

  render() {
    return (
      <Grid container direction='column'>
        <Grid item>
          <Table size='small'>
            <TableHead>
              <TableRow>
                <TableCell align='center'>Type</TableCell>
                <TableCell align='center'>Fc (Hz)</TableCell>
                <TableCell align='center'>{this.state.showBandwidth ? 'BW (oct)' : 'Q'}</TableCell>
                <TableCell align='center'>Gain (dB)</TableCell>
              </TableRow>
            </TableHead>
            {!!this.props.parametricFilters && (
              <TableBody>
                {this.props.parametricFilters.map(filt => {
                  return (
                    <TableRow key={filt.fc}>
                      <TableCell align='center'>{filt.type}</TableCell>
                      <TableCell align='center'>{filt.fc.toFixed(0)}</TableCell>
                      <TableCell align='center'>
                        {(this.state.showBandwidth ? this.bandwidth(filt.q) : filt.q).toFixed(2)}
                      </TableCell>
                      <TableCell align='center'>{filt.gain.toFixed(1)}</TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            )}
          </Table>
        </Grid>
      </Grid>
    );
  }
}

export default EqAppParametricEq;
