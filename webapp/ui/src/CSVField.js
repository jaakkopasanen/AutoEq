import React, {useCallback, useState} from 'react';
import {Box, Grid, IconButton, TextField, Typography} from '@mui/material';
import FileOpenOutlinedIcon from '@mui/icons-material/FileOpenOutlined';
import {useDropzone} from 'react-dropzone';

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

const CSVField = (props) => {
  const [csvText, setCsvText] = useState(constructCsvText([]));
  const [error, setError] = useState('');

  const findCsvSeparators = (csv) => {
    const rows = csv.trim().split('\n')
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

  const parseCSV = (csv) => {
    csv = csv.trim();

    const [columnSeparator, decimalDelimiter] = findCsvSeparators(csv);
    if (columnSeparator === null) {
      throw new Error('Column separator couldn\'t be detected');
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
        throw new Error('CSV data has row(s) with less than 2 values');
      }
      frequency.push(parseFloat(cells[0].trim()));
      raw.push(parseFloat(cells[1].trim()));
      if (isNaN(frequency[frequency.length - 1]) || isNaN(raw[raw.length - 1])) {
        throw new Error('Non-numbers detected in CSV data');
      }
    }
    const freqSet = new Set();
    for (const freq of frequency) {
      if ( freqSet.has(freq)) {
        throw new Error(`Duplicate frequency "${freq}" in CSV data`);
      }
      freqSet.add(freq);
    }

    return [frequency, raw];
  };

  const onCsvTextChanged = (csv) => {
    setCsvText(csv);
    try {
      const [frequency, raw] = parseCSV(csv);
      props.onChange(frequency, raw);
    } catch (e) {
      setError(e);
    }
  };

  const onDrop = useCallback((acceptedFiles) => {
    acceptedFiles.forEach((file) => {
      const reader = new FileReader();
      reader.onabort = () => console.log('file reading was aborted');
      reader.onerror = () => console.log('file reading has failed');
      reader.onload = () => {
        if ('onFileUploaded' in props) {
          props.onFileUploaded(file.name);
        }
        onCsvTextChanged(reader.result);
      }
      reader.readAsText(file);
    });
  }, [])
  const {getRootProps, getInputProps, isDragAccept, open} = useDropzone({onDrop, noClick: true, noKeyboard: true});

  const rows = Math.min(10, csvText.split('\n').length);
  return (
    <Grid container direction='column'>
      <Grid item>
        <Box { ...getRootProps() } sx={{position: 'relative'}}>
          <Box
            sx={{
              position: 'absolute', top: '50%', transform: 'translateY(-50%)',
              right: {xs: '20%', sm: '30px', md: '20%'},
              left: {xs: '40%', sm: '50%', md: '40%'},
              color: isDragAccept ? theme => theme.palette.info : theme => theme.palette.text.secondary,
              textAlign: 'center'
            }}
          >
            <Typography variant='body2' sx={{display: 'inline'}}>Edit the text directly, drop a CSV file or click </Typography>
            <FileOpenOutlinedIcon sx={{display: 'inline', height: '17px', width: '16px', transform: 'translate(-1px, 3px)'}} />
            <Typography variant='body2' sx={{display: 'inline'}}> to open a file.</Typography>
          </Box>
          <TextField
            multiline rows={rows} value={csvText}
            inputProps={{ style: { fontFamily: 'monospace' } }}
            onChange={e => { onCsvTextChanged(e.target.value); }}
            label={props.label || 'CSV Data'}
            error={!!error}
            sx={{width: '100%'}}
          />
          <Box sx={{position: 'absolute', top: 0, right: 0}}>
            <IconButton onClick={open}>
              <FileOpenOutlinedIcon />
            </IconButton>
          </Box>
          <input { ...getInputProps() } />
        </Box>
      </Grid>
      {!!error && (
        <Grid item>
          <Typography color='error'>Error: {error}</Typography>
        </Grid>
      )}
    </Grid>

  );
};

export default CSVField;
