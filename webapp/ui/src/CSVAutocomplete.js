import React, {useCallback} from 'react';
import {Autocomplete, Box, IconButton, TextField, Tooltip,} from '@mui/material';
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
  }, [props])
  const {getRootProps, getInputProps, open, isDragAccept} = useDropzone({onDrop, noClick: true, noKeyboard: true})

  return (
    <Box sx={{position: 'relative'}} { ...getRootProps() }>
      <Autocomplete
        renderInput={(params) =>
          <TextField
            sx={{
              background: (theme) => 'transparent',
              '& .MuiInputBase-root': (theme) => ({
                backgroundColor: isDragAccept ? 'rgba(225, 255, 214, 0.2)' : 'rgba(0, 0, 0, 0.0)',
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
      <Tooltip title='Open CSV file' placement='left'>
        <IconButton onClick={open} sx={{position: 'absolute', top: '50%', transform: 'translateY(-50%)', right: '0px'}}>
          <FileOpenOutlinedIcon />
        </IconButton>
      </Tooltip>
      <input { ...getInputProps() } />
    </Box>
  );
}

export default CSVAutocomplete;
