import React from 'react';
import {
  Autocomplete,
  Button,
  Grid,
  IconButton,
  styled,
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  TextField,
  ToggleButton,
  ToggleButtonGroup, Tooltip,
  Typography
} from '@mui/material';
import DeleteIcon from '@mui/icons-material/Delete';
import DownloadIcon from '@mui/icons-material/Download';
import { bandwidth, downloadAsFile } from './utils';
import InputSlider from './InputSlider';
import InfoOutlinedIcon from "@mui/icons-material/InfoOutlined";

const CompactTableCell = styled(TableCell)(({ theme }) => ({
  padding: `6px`,
  [theme.breakpoints.up('md')]: {
    padding: `6px ${theme.spacing(2)}`
  }
}));

const EqAppParametricEq = (props) => {
  const parseTextFieldInput = (value) => {
    return value !== null && typeof value !== 'undefined' ? value : '';
  };

  const parseTextFieldOutput = (value) => {
    return value !== null && typeof value !== 'undefined' && value !== '' ? parseFloat(value) : null;
  };

  const equalizerApoParametricEqString = () => {
    const typeMap = { LOW_SHELF: 'LS', PEAKING: 'PK', HIGH_SHELF: 'HS' };
    let s = `Preamp: ${props.parametricEq?.preamp?.toFixed(2)} dB\n`
    for (const [i, filt] of props.parametricEq?.filters?.entries()) {
      s += `Filter ${i + 1}: ON ${typeMap[filt.type]} Fc ${filt.fc.toFixed(1)} Hz Gain ${filt.gain.toFixed(1)} dB Q ${filt.q.toFixed(2)}\n`
    }
    return s;
  };

  const onDownloadClick = () => {
    downloadAsFile(
      equalizerApoParametricEqString(),
      'text/plain',
      `${props.selectedMeasurement} ParametricEq.txt`);
  };

  const filterNames = !!props.uiConfig?.filterNames ? props.uiConfig.filterNames : {
    LOW_SHELF: 'Low shelf', PEAKING: 'Peaking', HIGH_SHELF: 'High shelf', PREAMP: 'Preamp',
  };
  const columnNames = !!props.uiConfig?.columnNames ? props.uiConfig.columnNames : {
    fc: 'Frequency (Hz)', q: props.uiConfig?.bw ? 'BW (oct)' : 'Q', gain: 'Gain (dB)',
  };

  return (
    <Grid container direction='column' rowSpacing={1}>
      {props.instructions && (
        <Grid
          item
          sx={{
            padding: '8px 12px',
            background: '#e5f3f7',
            borderStyle: 'solid',
            borderWidth: '1px',
            borderColor: '#9abac3',
            borderRadius: '4px',
            marginTop: '8px',
            marginBottom: '8px',
          }}
          key='instructions'
        >
          <Typography variant='caption'>
            {props.instructions}
          </Typography>
        </Grid>
      )}
      {props.uiConfig?.showFsControl && (
        <Grid item sx={{ position: 'relative' }}>
          <Autocomplete
            freeSolo
            renderInput={(params) =>
              <TextField {...params} label='Sample rate (Hz)' type='number' required={!props.fs} />}
            value={props.fs.toFixed(0)}
            options={['44100', '48000', '96000', '192000', '384000']}
            onChange={(e, val) => {
              props.onEqParamChanged({ fs: parseFloat(val) })
            }}
            size='small'
            disableClearable
          />
          <Tooltip title='Ideally sample rate should match the device sample rate but will in most cases have only a very minor impact in the highest frequencies.'>
            <InfoOutlinedIcon sx={{ width: 14, height: 14, position: 'absolute', top: 1, right: 10, background: '#fff' }} />
          </Tooltip>
        </Grid>
      )}
      {'showConfig' in props && props.showConfig !== false && (
        <Grid item container direction='column' rowSpacing={2}>
          <Grid item container direction='column' rowSpacing={1}>
            <Grid item><Typography variant='h6'>Optimizer</Typography></Grid>
            <Grid item container direction='row' columnSpacing={1}>
              <Grid item xs={6} sx={{ position: 'relative' }}>
                <TextField
                  value={parseTextFieldInput(props.config.optimizer?.minF)}
                  onChange={(e) => {
                    props.onConfigChanged({ optimizer: { minF: parseTextFieldOutput(e.target.value) } })
                  }}
                  label='Min frequency (Hz)' size='small' sx={{width: '100%'}} type='number'
                  inputProps={{step: 1.0}}
                  error={props.config.optimizer?.maxF !== null && props.config.optimizer?.minF > props.config.optimizer?.maxF}
                />
                <Tooltip title='Lower bound of the optimization region. Can be left empty in most cases. Useful for example for avoiding sub-bass boost when equalizing bookshelf speakers.'>
                  <InfoOutlinedIcon sx={{ width: 14, height: 14, position: 'absolute', top: -6, right: 10, background: '#fff' }} />
                </Tooltip>
              </Grid>
              <Grid item xs={6} sx={{ position: 'relative' }}>
                <TextField
                  value={parseTextFieldInput(props.config.optimizer?.maxF)}
                  onChange={(e) => {
                    props.onConfigChanged({ optimizer: { maxF: parseTextFieldOutput(e.target.value) } })
                  }}
                  label='Max frequency (Hz)' size='small' sx={{width: '100%'}} type='number'
                  inputProps={{step: 1.0}}
                />
                <Tooltip title='Upper bound of the optimization region. Default value should serve most cases.'>
                  <InfoOutlinedIcon sx={{ width: 14, height: 14, position: 'absolute', top: -6, right: 10, background: '#fff' }} />
                </Tooltip>
              </Grid>
            </Grid>
          </Grid>
          <Grid item container direction='column' rowSpacing={1}>
            <Grid item><Typography variant='h6'>Filters</Typography></Grid>
            {props.config?.filters?.map((filter, i) => (
              <Grid key={i} item container direction='column' rowSpacing={1}>
                <Grid item container direction='row' justifyContent='space-between' alignItems='center'>
                  <Grid item>
                    <ToggleButtonGroup
                      value={filter.type}
                      exclusive
                      onChange={(e, val) => {
                        props.onConfigFilterChanged({ type: val }, i);
                      }}
                      size='small' color='primary'
                    >
                      <ToggleButton value='LOW_SHELF'>Low-shelf</ToggleButton>
                      <ToggleButton value='PEAKING'>Peaking</ToggleButton>
                      <ToggleButton value='HIGH_SHELF'>High-shelf</ToggleButton>
                    </ToggleButtonGroup>
                  </Grid>
                  <Grid item>
                    <IconButton onClick={() => { props.onFilterDeleteClick(i); }} size='large' color='error' aria-label='delete'>
                      <DeleteIcon />
                    </IconButton>
                  </Grid>
                </Grid>
                <Grid item container direction='row' columnSpacing={1}>
                  <Grid item xs={4}>
                    <TextField
                      value={parseTextFieldInput(filter.minFc)}
                      onChange={(e) => {
                        props.onConfigFilterChanged({ minFc: parseTextFieldOutput(e.target.value) }, i);
                      }}
                      label='Min Fc' size='small' sx={{width: '100%'}} type='number'
                      inputProps={{step: 1.0}}
                      error={filter.maxFc !== null && filter.minFc > filter.maxFc}
                    />
                  </Grid>
                  <Grid item xs={4}>
                    <TextField
                      value={parseTextFieldInput(filter.minQ)}
                      onChange={(e) => {
                        props.onConfigFilterChanged({ minQ: parseTextFieldOutput(e.target.value) }, i);
                      }}
                      label='Min Q' size='small' sx={{width: '100%'}} type='number'
                      inputProps={{step: 0.01}}
                      error={filter.maxQ !== null && filter.minQ > filter.maxQ}
                    />
                  </Grid>
                  <Grid item xs={4}>
                    <TextField
                      value={parseTextFieldInput(filter.minGain)}
                      onChange={(e) => {
                        props.onConfigFilterChanged({ minGain: parseTextFieldOutput(e.target.value) }, i);
                      }}
                      label='Min gain' size='small' sx={{width: '100%'}} type='number'
                      inputProps={{step: 0.1}}
                      error={filter.maxGain !== null && filter.minGain > filter.maxGain}
                    />
                  </Grid>
                </Grid>

                <Grid item container direction='row' columnSpacing={1}>
                  <Grid item xs={4}>
                    <TextField
                      value={parseTextFieldInput(filter.maxFc)}
                      onChange={(e) => {
                        props.onConfigFilterChanged({ maxFc: parseTextFieldOutput(e.target.value) }, i);
                      }}
                      label='Max Fc' size='small' sx={{width: '100%'}} type='number'
                      inputProps={{step: 1.0}}
                    />
                  </Grid>
                  <Grid item xs={4}>
                    <TextField
                      value={parseTextFieldInput(filter.maxQ)}
                      onChange={(e) => {
                        props.onConfigFilterChanged({ maxQ: parseTextFieldOutput(e.target.value) }, i);
                      }}
                      label='Max Q' size='small' sx={{width: '100%'}} type='number'
                      inputProps={{step: 0.01}}
                    />
                  </Grid>
                  <Grid item xs={4}>
                    <TextField
                      value={parseTextFieldInput(filter.maxGain)}
                      onChange={(e) => {
                        props.onConfigFilterChanged({ maxGain: parseTextFieldOutput(e.target.value) }, i);
                      }}
                      label='Max gain' size='small' sx={{width: '100%'}} type='number'
                      inputProps={{step: 0.1}}
                    />
                  </Grid>
                </Grid>
              </Grid>
            ))}
            <Grid item>
              <Button onClick={props.onAddFilterClick} variant='outlined'>
                Add filter
              </Button>
            </Grid>
          </Grid>
        </Grid>
      )}
      {!!props.uiConfig?.showPreampControl && (
        <Grid item>
          <InputSlider
            label='Preamp' value={props.preamp}
            min={-20} max={20} step={0.5}
            onChange={(v) => { props.onEqParamChanged({ preamp: v }) }}
          />
        </Grid>
      )}
      <Grid item>
        <Table size='small'>
          <TableHead>
            <TableRow>
              {!('fixedBands' in props && props.fixedBands !== false) && (
                <CompactTableCell align='left'>Filter Type</CompactTableCell>
              )}
              <CompactTableCell align='center'>{columnNames.fc}</CompactTableCell>
              {!('fixedBands' in props && props.fixedBands !== false) && (
                <CompactTableCell align='center'>{columnNames.q}</CompactTableCell>
              )}
              <CompactTableCell align='center'>{columnNames.gain}</CompactTableCell>
            </TableRow>
          </TableHead>
          {!!props.parametricEq?.filters && (
            <TableBody>
              {props.parametricEq.filters.map((filt, i) => {
                return (
                  <TableRow key={i}>
                    {!('fixedBands' in props && props.fixedBands !== false) && (
                      <CompactTableCell align='left'>{filterNames[filt.type]}</CompactTableCell>
                    )}
                    <CompactTableCell align='center'>{filt.fc.toFixed(0)}</CompactTableCell>
                    {!('fixedBands' in props && props.fixedBands !== false) && (
                      <CompactTableCell align='center'>
                        {(props.uiConfig?.bw ? bandwidth(filt.q) : filt.q).toFixed(2)}
                      </CompactTableCell>
                    )}
                    <CompactTableCell align='center'>{filt.gain.toFixed(1)}</CompactTableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          )}
        </Table>
      </Grid>
      <Grid item>
        <Typography><b>{filterNames.PREAMP}:</b> {props.parametricEq?.preamp?.toFixed(1)} dB</Typography>
      </Grid>
      {!!props.uiConfig?.showDownload && (
        <Grid item container direction='row' columnSpacing={1} justifyContent='center'>
          <Grid item>
            <IconButton onClick={onDownloadClick}><DownloadIcon /></IconButton>
          </Grid>
        </Grid>
      )}

    </Grid>
  );
};

export default EqAppParametricEq;
