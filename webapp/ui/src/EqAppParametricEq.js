import React from 'react';
import {
  Autocomplete, Button, Grid, IconButton, Table, TableBody, TableCell, TableHead, TableRow, TextField, ToggleButton,
  ToggleButtonGroup, Typography
} from '@mui/material';
import { Delete as DeleteIcon } from '@mui/icons-material';
import { downloadAsFile } from './utils';
import InputSlider from './InputSlider';

class EqAppParametricEq extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showBandwidth: false,
    };
    this.equalizerApoParametricEqString = this.equalizerApoParametricEqString.bind(this);
    this.onDownloadClick = this.onDownloadClick.bind(this);
  }

  bandwidth(q) {
    return Math.log2((2*q**2+1) / (2*q**2) + Math.sqrt((((2*q**2 + 1) / q**2)**2)/4-1));
  }

  parseTextFieldInput(value) {
    return value !== null && typeof value !== 'undefined' ? value : '';
  }

  parseTextFieldOutput(value) {
    return value !== null && typeof value !== 'undefined' && value !== '' ? parseFloat(value) : null;
  }

  equalizerApoParametricEqString() {
    const typeMap = { LOW_SHELF: 'LS', PEAKING: 'PK', HIGH_SHELF: 'HS' };
    let s = `Preamp: ${this.props.parametricEq?.preamp?.toFixed(2)} dB\n`
    for (const [i, filt] of this.props.parametricEq?.filters?.entries()) {
      s += `Filter ${i + 1}: ON ${typeMap[filt.type]} Fc ${filt.fc.toFixed(1)} Hz Gain ${filt.gain.toFixed(1)} dB Q ${filt.q.toFixed(2)}\n`
    }
    return s;
  }

  onDownloadClick() {
    downloadAsFile(this.equalizerApoParametricEqString(), 'text/plain', `${this.props.selectedMeasurement} ParametricEq.txt`)
  }

  render() {
    const useBandwidth = this.props.uiConfig?.bw || this.state.showBandwidth;
    const filterNames = !!this.props.uiConfig?.filterNames ? this.props.uiConfig.filterNames : {
      LOW_SHELF: 'Low shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High shelf', PREAMP: 'Preamp',
    };
    const columnNames = !!this.props.uiConfig?.columnNames ? this.props.uiConfig.columnNames : {
      fc: 'Fc (Hz)', q: useBandwidth ? 'BW (oct)' : 'Q', gain: 'Gain (dB)',
    }
    return (
      <Grid container direction='column' rowSpacing={1}>
        <Grid item>
          <Autocomplete
            freeSolo
            renderInput={(params) =>
              <TextField {...params} label='Sample rate (Hz)' type='number' required={!this.props.fs} />
            }
            value={this.props.fs.toFixed(0)}
            options={['44100', '48000', '96000', '192000', '384000']}
            onChange={(e, val) => {
              this.props.onEqParamChanged({ fs: parseFloat(val) })
            }}
            size='small'
            disableClearable
          />
        </Grid>
        {'showConfig' in this.props && this.props.showConfig !== false && (
          <Grid item container direction='column' rowSpacing={2}>
            <Grid item container direction='column' rowSpacing={1}>
              <Grid item><Typography variant='h6'>Optimizer</Typography></Grid>
              <Grid item><Typography sx={{fontSize: '0.75rem', color: 'grey.700'}}>Optimization algorithm parameters</Typography></Grid>
              <Grid item container direction='row' columnSpacing={1}>
                <Grid item xs={6}>
                  <TextField
                    value={this.parseTextFieldInput(this.props.config.optimizer?.minF)}
                    onChange={(e) => {
                      this.props.onConfigChanged({ optimizer: { minF: this.parseTextFieldOutput(e.target.value) } })
                    }}
                    label='Min frequency (Hz)' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 1.0}}
                  />
                </Grid>
                <Grid item xs={6}>
                  <TextField
                    value={this.parseTextFieldInput(this.props.config.optimizer?.maxF)}
                    onChange={(e) => {
                      this.props.onConfigChanged({ optimizer: { maxF: this.parseTextFieldOutput(e.target.value) } })
                    }}
                    label='Max frequency (Hz)' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 1.0}}
                  />
                </Grid>
              </Grid>
              <Grid item container direction='row' columnSpacing={1}>
                <Grid item xs={4}>
                  <TextField
                    value={(this.parseTextFieldInput(this.props.config.optimizer?.maxTime * 1000))}
                    onChange={(e) => {
                      this.props.onConfigChanged({optimizer: { maxTime: this.parseTextFieldOutput(e.target.value) / 1000 } })
                    }}
                    label='Max time (ms)' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 10.0}}
                  />
                </Grid>
                <Grid item xs={4}>
                  <TextField
                    value={this.parseTextFieldInput(this.props.config.optimizer?.minChangeRate)}
                    onChange={(e) => {
                      this.props.onConfigChanged({ optimizer: { minChangeRate: this.parseTextFieldOutput(e.target.value) } })
                    }}
                    label='Min change' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 0.01}}
                  />
                </Grid>
                <Grid item xs={4}>
                  <TextField
                    value={this.parseTextFieldInput(this.props.config.optimizer?.minStd)}
                    onChange={(e) => {
                      this.props.onConfigChanged({ optimizer: { minStd: this.parseTextFieldOutput(e.target.value) } })
                    }}
                    label='Min STD' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 0.001}}
                  />
                </Grid>
              </Grid>
            </Grid>
            <Grid item container direction='column' rowSpacing={1}>
              <Grid item><Typography variant='h6'>Filter Defaults</Typography></Grid>
              <Grid item><Typography sx={{fontSize: '0.75rem', color: 'grey.700'}}>Will be used for missing values in filters</Typography></Grid>
              <Grid item>
                <ToggleButtonGroup
                  value={this.props.config.filterDefaults?.type}
                  exclusive
                  onChange={(e, val) => {
                    this.props.onConfigChanged({ filterDefaults: { type: val } });
                  }}
                  size='small'
                  color='primary'
                >
                  <ToggleButton value='LOW_SHELF'>Low-shelf</ToggleButton>
                  <ToggleButton value='PEAKING'>Peaking</ToggleButton>
                  <ToggleButton value='HIGH_SHELF'>High-shelf</ToggleButton>
                </ToggleButtonGroup>
              </Grid>
              <Grid item container direction='row' columnSpacing={1}>
                <Grid item xs={4}>
                  <TextField
                    value={this.parseTextFieldInput(this.props.config.filterDefaults?.minFc)}
                    onChange={(e) => {
                      this.props.onConfigChanged({ filterDefaults: { minFc: this.parseTextFieldOutput(e.target.value) } })
                    }}
                    label='Min Fc' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 1.0}}
                  />
                </Grid>
                <Grid item xs={4}>
                  <TextField
                    value={this.parseTextFieldInput(this.props.config.filterDefaults?.minQ)}
                    onChange={(e) => {
                      this.props.onConfigChanged({ filterDefaults: { minQ: this.parseTextFieldOutput(e.target.value) } })
                    }}
                    label='Min Q' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 0.01}}
                  />
                </Grid>
                <Grid item xs={4}>
                  <TextField
                    value={this.parseTextFieldInput(this.props.config.filterDefaults?.minGain)}
                    onChange={(e) => {
                      this.props.onConfigChanged({ filterDefaults: { minGain: this.parseTextFieldOutput(e.target.value) } })
                    }}
                    label='Min gain' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 0.1}}
                  />
                </Grid>
              </Grid>
              <Grid item container direction='row' columnSpacing={1}>
                <Grid item xs={4}>
                  <TextField
                    value={this.parseTextFieldInput(this.props.config.filterDefaults?.maxFc)}
                    onChange={(e) => {
                      this.props.onConfigChanged({ filterDefaults: { maxFc: this.parseTextFieldOutput(e.target.value) } })
                    }}
                    label='Max Fc' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 1.0}}
                  />
                </Grid>
                <Grid item xs={4}>
                  <TextField
                    value={this.parseTextFieldInput(this.props.config.filterDefaults?.maxQ)}
                    onChange={(e) => {
                      this.props.onConfigChanged({ filterDefaults: { maxQ: this.parseTextFieldOutput(e.target.value) } })
                    }}
                    label='Max Q' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 0.01}}
                  />
                </Grid>
                <Grid item xs={4}>
                  <TextField
                    value={this.parseTextFieldInput(this.props.config.filterDefaults?.maxGain)}
                    onChange={(e) => {
                      this.props.onConfigChanged({ filterDefaults: { maxGain: this.parseTextFieldOutput(e.target.value) } })
                    }}
                    label='Max gain' size='small' sx={{width: '100%'}} type='number'
                    inputProps={{step: 0.1}}
                  />
                </Grid>
              </Grid>
            </Grid>
            <Grid item container direction='column' rowSpacing={1}>
              <Grid item><Typography variant='h6'>Filters</Typography></Grid>
              <Grid item>
                <Typography sx={{fontSize: '0.75rem', color: 'grey.700'}}>
                  Add as many filters as you like. Fixed value for Fc, Q or gain will disable optimization for it.
                </Typography>
              </Grid>
              {this.props.config?.filters?.map((filter, i) => (
                <Grid key={i} item container direction='column' rowSpacing={1}>
                  <Grid item container direction='row' justifyContent='space-between' alignItems='center'>
                    <Grid item>
                      <ToggleButtonGroup
                        value={filter.type}
                        exclusive
                        onChange={(e, val) => {
                          this.props.onConfigFilterChanged({ type: val }, i);
                        }}
                        size='small' color='primary'
                      >
                        <ToggleButton value='LOW_SHELF'>Low-shelf</ToggleButton>
                        <ToggleButton value='PEAKING'>Peaking</ToggleButton>
                        <ToggleButton value='HIGH_SHELF'>High-shelf</ToggleButton>
                      </ToggleButtonGroup>
                    </Grid>
                    <Grid item>
                      <IconButton onClick={() => { this.props.onFilterDeleteClick(i); }} size='large' color='error' aria-label='delete'>
                        <DeleteIcon />
                      </IconButton>
                    </Grid>
                  </Grid>
                  <Grid item container direction='row' columnSpacing={1}>
                    <Grid item xs={4}>
                      <TextField
                        value={this.parseTextFieldInput(filter.minFc)}
                        onChange={(e) => {
                          this.props.onConfigFilterChanged({ minFc: this.parseTextFieldOutput(e.target.value) }, i);
                        }}
                        label='Min Fc' size='small' sx={{width: '100%'}} type='number'
                        inputProps={{step: 1.0}}
                      />
                    </Grid>
                    <Grid item xs={4}>
                      <TextField
                        value={this.parseTextFieldInput(filter.minQ)}
                        onChange={(e) => {
                          this.props.onConfigFilterChanged({ minQ: this.parseTextFieldOutput(e.target.value) }, i);
                        }}
                        label='Min Q' size='small' sx={{width: '100%'}} type='number'
                        inputProps={{step: 0.01}}
                      />
                    </Grid>
                    <Grid item xs={4}>
                      <TextField
                        value={this.parseTextFieldInput(filter.minGain)}
                        onChange={(e) => {
                          this.props.onConfigFilterChanged({ minGain: this.parseTextFieldOutput(e.target.value) }, i);
                        }}
                        label='Min gain' size='small' sx={{width: '100%'}} type='number'
                        inputProps={{step: 0.1}}
                      />
                    </Grid>
                  </Grid>

                  <Grid item container direction='row' columnSpacing={1}>
                    <Grid item xs={4}>
                      <TextField
                        value={this.parseTextFieldInput(filter.maxFc)}
                        onChange={(e) => {
                          this.props.onConfigFilterChanged({ maxFc: this.parseTextFieldOutput(e.target.value) }, i);
                        }}
                        label='Max Fc' size='small' sx={{width: '100%'}} type='number'
                        inputProps={{step: 1.0}}
                      />
                    </Grid>
                    <Grid item xs={4}>
                      <TextField
                        value={this.parseTextFieldInput(filter.maxQ)}
                        onChange={(e) => {
                          this.props.onConfigFilterChanged({ maxQ: this.parseTextFieldOutput(e.target.value) }, i);
                        }}
                        label='Max Q' size='small' sx={{width: '100%'}} type='number'
                        inputProps={{step: 0.01}}
                      />
                    </Grid>
                    <Grid item xs={4}>
                      <TextField
                        value={this.parseTextFieldInput(filter.maxGain)}
                        onChange={(e) => {
                          this.props.onConfigFilterChanged({ maxGain: this.parseTextFieldOutput(e.target.value) }, i);
                        }}
                        label='Max gain' size='small' sx={{width: '100%'}} type='number'
                        inputProps={{step: 0.1}}
                      />
                    </Grid>
                  </Grid>
                </Grid>
              ))}
              <Grid item>
                <Button onClick={this.props.onAddFilterClick} variant='outlined'>
                  Add filter
                </Button>
              </Grid>
            </Grid>
          </Grid>
        )}
        {!!this.props.uiConfig?.showPreampControl && (
          <Grid item>
            <InputSlider
              label='Preamp' value={this.props.preamp}
              min={-20} max={20} step={0.5}
              onChange={(v) => { this.props.onEqParamChanged({ preamp: v }) }}
            />
          </Grid>
        )}
        <Grid item>
          <Table size='small'>
            <TableHead>
              <TableRow>
                <TableCell align='left'>Filter Type</TableCell>
                <TableCell align='center'>{columnNames.fc}</TableCell>
                {!('hideQ' in this.props && this.props.hideQ !== false) && (<TableCell align='center'>{columnNames.q}</TableCell>)}
                <TableCell align='center'>{columnNames.gain}</TableCell>
              </TableRow>
            </TableHead>
            {!!this.props.parametricEq?.filters && (
              <TableBody>
                {this.props.parametricEq.filters.map((filt, i) => {
                  return (
                    <TableRow key={i}>
                      <TableCell align='left'>{filterNames[filt.type]}</TableCell>
                      <TableCell align='center'>{filt.fc.toFixed(0)}</TableCell>
                      {!('hideQ' in this.props && this.props.hideQ !== false) && (
                        <TableCell align='center'>
                          {(useBandwidth ? this.bandwidth(filt.q) : filt.q).toFixed(2)}
                        </TableCell>
                      )}
                      <TableCell align='center'>{filt.gain.toFixed(1)}</TableCell>
                    </TableRow>
                  );
                })}
              </TableBody>
            )}
          </Table>
        </Grid>
        <Grid item>
          <Typography><b>{filterNames.PREAMP}:</b> {this.props.parametricEq?.preamp?.toFixed(1)} dB</Typography>
        </Grid>
        {!!this.props.uiConfig?.showDownload && (
          <Grid item container direction='row' columnSpacing={1} justifyContent='center'>
            <Grid item>
              <Button variant='outlined' onClick={this.onDownloadClick}>Download</Button>
            </Grid>
          </Grid>
        )}

      </Grid>
    );
  }
}

export default EqAppParametricEq;
