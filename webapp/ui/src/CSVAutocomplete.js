import React, {useCallback, useEffect, useState} from 'react';
import {Autocomplete, Button, Grid, IconButton, TextField, Typography} from '@mui/material';
import {Download as DownloadIcon, Edit as EditIcon} from '@mui/icons-material';
import {useDropzone} from 'react-dropzone';

function CSVAutocomplete(props) {
  const constructCsvText = (data) => {
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
  };

  const [showEdit, setShowEdit] = useState(false);
  const [name, setName] = useState('');
  const [csvText, setCsvText] = useState(constructCsvText([]));
  const [error, setError] = useState('');

  useEffect(() => {
    if (props.newData?.length > 0) {
      const newCsvText = constructCsvText(props.newData);
      if (newCsvText !== csvText) {
        setCsvText(newCsvText);
      }
    }
  }, [props.newData])

  const onDrop = useCallback((acceptedFiles) => {
    acceptedFiles.forEach((file) => {
      const reader = new FileReader();
      reader.onabort = () => console.log('file reading was aborted');
      reader.onerror = () => console.log('file reading has failed');
      reader.onload = () => {
        setName(file.name.replace(/\.\w+/, ''))
        setCsvText(reader.result);
      }
      reader.readAsText(file);
    });
  }, [])
  const {getRootProps, getInputProps, isDragAccept} = useDropzone({onDrop})

  const onCsvTextChanged = (e) => {
    setCsvText(e.target.value);
    setError('');
  };

  const findCsvSeparators = () => {
    const rows = csvText.trim().split('\n')
    const columnSeparatorCounts = { ',': 0, ';': 0, '\t': 0, '|': 0 };
    let nNumericRows = 0;
    for (const row of rows) {
      if (!/^\d/.test(row)) {
        // Skip rows which don't start with numbers
        continue;
      }
      nNumericRows++;
      for (const columnSeparator of Object.keys(columnSeparatorCounts)) {
        if (row.includes(columnSeparator)) {
          columnSeparatorCounts[columnSeparator] += 1;
        }
      }
    }
    const columnSeparatorCandidates = [];
    for (const [sep, count] of Object.entries(columnSeparatorCounts)) {
      if (count === nNumericRows) {
        columnSeparatorCandidates.push(sep)
      }
    }
    let columnSeparator = '';
    if (columnSeparatorCandidates.includes('\t')) {
      columnSeparator = '\t';
    } else if (columnSeparatorCandidates.includes(';')) {
      columnSeparator = ';';
    } else if (columnSeparatorCandidates.includes('|')) {
      columnSeparator = '|';
    } else if (columnSeparatorCandidates.includes(',')) {
      return [',', '.'];
    } else {
      return [null, null];
    }
    if (columnSeparatorCandidates.includes(',')) {
      return [columnSeparator, ','];
    }
    return [columnSeparator, '.'];
  }

  const onSaveClick = () => {
    let csv = csvText.trim();

    const [columnSeparator, decimalDelimiter] = findCsvSeparators();
    if (columnSeparator === null) {
      setError('Column separator couldn\'t be detected');
      return;
    }
    if (decimalDelimiter === ',') {
      csv = csv.replace(',', '.')
    }

    const rows = csv.split('\n');
    const frequency = [];
    const raw = [];
    for (const row of rows) {
      if (!/^\d/.test(row)) {
        // Skip rows which don't start with numbers
        continue;
      }
      const cells = row.trim().split(columnSeparator);
      if (cells.length < 2) {
        setError('CSV data has row(s) with less than 2 values')
      }
      frequency.push(parseFloat(cells[0].trim()));
      raw.push(parseFloat(cells[1].trim()));
      if (isNaN(frequency[frequency.length - 1]) || isNaN(raw[raw.length - 1])) {
        setError('Non-numbers detected in CSV data');
        return;
      }
    }
    const freqSet = new Set();
    for (const freq of frequency) {
      if ( freqSet.has(freq)) {
        setError(`Duplicate frequency "${freq}" in CSV data`);
        return;
      }
      freqSet.add(freq);
    }
    if (!!props.value) {
      props.onOptionUpdated(props.value.label, name, frequency, raw);
    } else {
      props.onOptionCreated(name, frequency, raw);
    }
    setShowEdit(false);
  };

  const onOptionSelected = (e, val) => {
    if (val !== null) {
      setName(val.label);
      if (val.frequency?.length > 0) {
        setCsvText(constructCsvText(val.frequency.map((f, i) => ({
          frequency: f,
          raw: val.raw[i]
        }))));
      }
      props.onChange({ ...val });
    } else {
      props.onChange(null);
    }
  };

  const uploadButtonClick = () => {
    if ('showEdit' in props) {
      props.onShowEditChanged(!props.showEdit);
    } else {
      setShowEdit(!showEdit);
    }
  };

  return (
    <Grid container direction='column' rowSpacing={1}>
      <Grid item container direction='row' alignItems='center'>
        <Grid item sx={{flexGrow: 1}}>
          <Autocomplete
            renderInput={(params) =>
              <TextField
                sx={{background: (theme) => theme.palette.background.default}}
                {...params}
                label={props.autocompleteLabel}
              />
            }
            value={props.value}
            options={props.options}
            isOptionEqualToValue={(option, value) => option.label === value.label}
            onChange={onOptionSelected}
            { ...props.autocompleteProps }
          />
        </Grid>
        {props.value === null && (
          <Grid item>
            <IconButton onClick={uploadButtonClick}>
              <DownloadIcon color={!!props.showEdit || showEdit ? 'primary' : 'gray'} />
            </IconButton>
          </Grid>
        )}
        {props.value !== null && !!props.value.frequency && (
          <Grid item>
            <IconButton onClick={uploadButtonClick}>
              <EditIcon color={!!props.showEdit || showEdit ? 'primary' : 'gray'} />
            </IconButton>
          </Grid>
        )}
      </Grid>
      {(props.showEdit || showEdit) && (
        <Grid item container direction='column' rowSpacing={1}>
          <Grid item container direction='row' alignItems='center' columnSpacing={1}>
            <Grid item sx={{flexGrow: 1}}>
              <TextField
                value={name}
                onChange={(e) => {
                  setName(e.target.value);
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
              <Button onClick={onSaveClick} variant='contained' size='large' color='primary' disabled={!name}>
                Save
              </Button>
            </Grid>
          </Grid>
          <Grid item container direction='row' alignItems='stretch' columnSpacing={1}>
            <Grid item xs={6}>
              <TextField
                multiline rows={10} value={csvText}
                sx={{width: '100%', background: theme => theme.palette.background.default}}
                inputProps={{ style: { fontFamily: 'monospace' } }}
                onChange={onCsvTextChanged}
                label='CSV data'
                error={!!error}
              />
            </Grid>
            <Grid
              item xs={6}
              sx={{
                background: 'rgb(243,246,255)',
                borderStyle: 'dashed',
                borderWidth: 2,
                borderColor: isDragAccept ? '#447ae5' : '#a6c4ff',
                borderRadius: 1,
                color: isDragAccept ? '#447ae5' : '#a6c4ff'
              }}
              container direction='column' justifyContent='center' alignItems='center'
              { ...getRootProps() }
            >
              <input { ...getInputProps() } />
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
          {!!error && (
            <Grid item>
              <Typography color='error'>Error: {error}</Typography>
            </Grid>
          )}
        </Grid>
      )}
    </Grid>
  );
}

export default CSVAutocomplete;
