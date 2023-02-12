import React, {useCallback} from 'react';
import {Autocomplete, Box, IconButton, TextField,} from '@mui/material';
import FileOpenOutlinedIcon from '@mui/icons-material/FileOpenOutlined';
import {useDropzone} from 'react-dropzone';
import {parseCSV} from './utils';

function CSVAutocomplete(props) {
  const onDrop = useCallback((acceptedFiles) => {
    acceptedFiles.forEach((file) => {
      const reader = new FileReader();
      reader.onabort = () => console.log('file reading was aborted');
      reader.onerror = () => console.log('file reading has failed');
      reader.onload = () => {
        try {
          const dataPoints = parseCSV(reader.result);
          props.onOptionCreated(file.name.replace(/\.\w+$/, ''), dataPoints);
        } catch (err) {
          props.onError(err);
        }
      }
      reader.readAsText(file);
    });
  }, [])
  const {getRootProps, getInputProps, open, isDragAccept} = useDropzone({onDrop, noClick: true, noKeyboard: true})

  return (
    <Box sx={{position: 'relative'}} { ...getRootProps() }>
      <Autocomplete
        renderInput={(params) =>
          <TextField
            sx={{
              background: (theme) => theme.palette.background.default,
              '& .MuiInputBase-root': (theme) => ({
                backgroundColor: isDragAccept ? 'rgb(228, 246, 229)' : theme.palette.background.default,
                borderRadius: '4px'
              }),
              '& .MuiAutocomplete-endAdornment': { display: 'none' },
            }}
            {...params}
            label={props.label}
          />
        }
        value={props.value}
        options={props.options}
        isOptionEqualToValue={(option, value) => option.label === value.label}
        onChange={(e, val) => { props.onChange(val); }}
        { ...props.autocompleteProps }
      />
      <IconButton onClick={open} sx={{position: 'absolute', top: '50%', transform: 'translateY(-50%)', right: '0px'}}>
        <FileOpenOutlinedIcon />
      </IconButton>
      <input { ...getInputProps() } />
    </Box>
  );
}

export default CSVAutocomplete;
