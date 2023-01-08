import React from 'react';
import {Autocomplete, Button, Grid, IconButton, TextField, Typography} from '@mui/material';
import {Download as DownloadIcon, Edit as EditIcon} from '@mui/icons-material';

class CSVAutocomplete extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showEdit: false,
      name: '',
      csvText: this.constructCsvText([]),
      error: null
    };
    this.constructCsvText = this.constructCsvText.bind(this);
    this.onCsvTextChanged = this.onCsvTextChanged.bind(this);
    this.onCsvSaveClick = this.onCsvSaveClick.bind(this);
    this.onOptionSelected = this.onOptionSelected.bind(this);
    this.uploadButtonClick = this.uploadButtonClick.bind(this);
  }

  constructCsvText(data) {
    let csvText = 'frequency,raw\n';
    if (data.length === 0) {
      csvText += '20,0\n20000,0'
    } else {
      for (let i = 0; i < data.length; ++i) {
        csvText += data[i].frequency.toFixed(1)
          + ',' + data[i].raw.toFixed(1) + '\n';
      }
    }
    return csvText;
  }

  onCsvTextChanged(e) {
    this.setState({
      csvText: e.target.value,
      error: null
    });
  }

  onCsvSaveClick() {
    const frequency = [];
    const raw = [];
    const rows = this.state.csvText.trim().split('\n');
    for (const row of rows) {
      if (row.trim() === '') {
        continue;
      }
      const cells = row.trim().split(',');
      if (cells.length !== 2) {
        this.setState({ error: 'Invalid data' });
        return;
      }
      if (cells[0] === 'frequency') {
        continue;
      }
      if (isNaN(parseFloat(cells[0].trim())) || isNaN(parseFloat(cells[1].trim()))) {
        this.setState({ error: true });
        return;
      }
      frequency.push(parseFloat(cells[0].trim()));
      raw.push(parseFloat(cells[1].trim()));
    }
    this.props.onOptionUpdated(this.state.name, frequency, raw);
  }

  onOptionSelected(e, val) {
    if (val !== null) {
      this.setState({
        name: val.label,
        csvText: this.constructCsvText([])
      });
    }
    console.log(val);
    this.props.onChange(val);
  }

  uploadButtonClick() {
    this.setState({ showEdit: !this.state.showEdit });
  }

  render() {
    return (
      <Grid container direction='column' rowSpacing={1}>
        <Grid item container direction='row' alignItems='center'>
          <Grid item sx={{flexGrow: 1}}>
            <Autocomplete
              renderInput={(params) =>
                <TextField
                  sx={{background: (theme) => theme.palette.background.default}}
                  {...params}
                  label='Select headphones'
                />
              }
              options={this.props.options}
              onChange={this.onOptionSelected}
              { ...this.props.autocompleteProps }
            />
          </Grid>
          {this.props.value === null && (
            <Grid item>
              <IconButton onClick={this.uploadButtonClick}>
                <DownloadIcon color={this.state.showEdit ? 'primary' : 'gray'} />
              </IconButton>
            </Grid>
          )}
          {this.props.value !== null && !!this.props.value.frequency && (
            <Grid item>
              <IconButton onClick={this.uploadButtonClick}>
                <EditIcon color={this.state.showEdit ? 'primary' : 'gray'} />
              </IconButton>
            </Grid>
          )}
        </Grid>
        {this.state.showEdit && (
          <Grid item container direction='column' rowSpacing={1}>
            <Grid item container direction='row' alignItems='center' columnSpacing={1}>
              <Grid item sx={{flexGrow: 1}}>
                <TextField
                  value={this.state.name}
                  onChange={(e) => {
                    this.setState({ name: e.target.value });
                  }}
                  size='small'
                  sx={{
                    width: '100%',
                    background: theme => theme.palette.background.default,
                    borderRadius: 0,
                    border: 'none'
                  }}
                  label='Name'
                />
              </Grid>
              <Grid item>
                <Button
                  onClick={this.onCsvSaveClick}
                  variant='contained' size='large' color='primary'
                  disabled={!this.state.name}
                >
                  Save
                </Button>
              </Grid>
            </Grid>
            <Grid item>
              <Grid container direction='row' columnSpacing={1} alignItems='stretch'>
                <Grid item xs={6}>
                  <TextField
                    multiline rows={10} value={this.state.csvText}
                    sx={{width: '100%', background: theme => theme.palette.background.default}}
                    inputProps={{ style: { fontFamily: 'monospace' } }}
                    onChange={this.onCsvTextChanged}
                    label='CSV data'
                  />
                </Grid>
                <Grid
                  item xs={6}
                  sx={{
                    //background: 'rgb(241, 245, 255)',
                    background: 'rgb(241, 245, 255)',
                    border: '2px dashed #5992ff',
                    borderRadius: 1,
                    color: '#5992ff'
                  }}
                  container direction='column' justifyContent='center' alignItems='center'
                >
                  <Grid item>
                    <Typography sx={{textAlign: 'center'}}>
                      Edit values manually<br />
                      OR<br />
                      Click here to open file<br />
                      OR<br />
                      Drag and drop CSV file
                    </Typography>
                  </Grid>
                </Grid>
              </Grid>
            </Grid>
          </Grid>
        )}
      </Grid>
    );
  }
}

export default CSVAutocomplete;
