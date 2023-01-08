import React, {useCallback, useEffect, useState} from 'react';
import {Autocomplete, Button, Grid, IconButton, TextField, Typography} from '@mui/material';
import {Download as DownloadIcon, Edit as EditIcon} from '@mui/icons-material';
import {useDropzone} from "react-dropzone";

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

  const onSaveClick = () => {
    const frequency = [];
    const raw = [];
    const rows = csvText.trim().split('\n');
    for (const row of rows) {
      if (row.trim() === '') {
        continue;
      }
      const cells = row.trim().split(',');
      if (cells.length !== 2) {
        setError('Invalid data');
        return;
      }
      if (cells[0] === 'frequency') {
        continue;
      }
      if (isNaN(parseFloat(cells[0].trim())) || isNaN(parseFloat(cells[1].trim()))) {
        setError('Invalid data');
        return;
      }
      frequency.push(parseFloat(cells[0].trim()));
      raw.push(parseFloat(cells[1].trim()));
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
        </Grid>
      )}
    </Grid>
  );
}

export default CSVAutocomplete;
