import React, {createContext, forwardRef, useCallback, useContext} from 'react';
import {
  Autocomplete,
  Box,
  Button,
  ButtonGroup,
  FormControl,
  Grid,
  IconButton,
  InputLabel,
  MenuItem,
  Select,
  TextField,
  Tooltip, Typography,
} from '@mui/material';
import FileOpenOutlinedIcon from '@mui/icons-material/FileOpenOutlined';
import {useDropzone} from 'react-dropzone';
import find from 'lodash/find';
import isEqual from 'lodash/isEqual';
import {parseCSV} from './utils';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import { FixedSizeList } from 'react-window';
import Popper from "@mui/material/Popper";


const LISTBOX_PADDING = 8; // px

const renderRow = (props) => {
  const { data, index, style } = props;
  const liProps = data[index][0];
  const option = data[index][1];
  const renderOptionFn = data[index][2];

  if (renderOptionFn) {
    return renderOptionFn(liProps, option, style);
  } else {
    return (
      <Typography component='li' {...liProps} style={{ ...style, top: (style.top) + LISTBOX_PADDING }}>
        {option.label}
      </Typography>
    );
  }
};

const OuterElementContext = createContext({});

const OuterElementType = forwardRef((props, ref) => {
  const outerProps = useContext(OuterElementContext);
  return <div ref={ref} {...props} {...outerProps} />;
});

const InnerElementType = forwardRef(({ style, ...other }, ref) => (
  <ul
    ref={ref}
    style={{
      ...style,
      paddingLeft: 0,
      marginTop: 0
    }}
    { ...other }
  />
));

const ListboxComponent = forwardRef(function ListboxComponent(props, ref) {
  const { children, showOnlyUniqueLabels, onShowOnlyUniqueLabelsChanged, ...other } = props;
  const itemData = [];
  children.forEach(
    (child) => {
      itemData.push(child);
      itemData.push(...(child.children || []));
    }
  );

  const itemCount = itemData.length;
  const itemSize = 48;

  const getHeight = () => {
    return Math.min(8, itemCount) * itemSize;
  };

  return (
    <div ref={ref}>
      <OuterElementContext.Provider value={other}>
        <FixedSizeList
          itemData={itemData}
          height={getHeight() + 2 * LISTBOX_PADDING}
          width='100%'
          outerElementType={OuterElementType}
          innerElementType={InnerElementType}
          itemSize={itemSize}
          overscanCount={5}
          itemCount={itemCount}
          style={{paddingLeft: 0 }}
          scrollToIndex={30}
        >
          {renderRow}
        </FixedSizeList>
        <Grid container direction='row' alignItems='center' justifyContent='center' sx={{p: 1, borderTop: '1px solid #ddd'}}>
          <Grid item>
            <ButtonGroup variant='text'>
              <Button
                size='small' sx={{height: 22, textTransform: 'none', color: !showOnlyUniqueLabels ? 'primary' : 'gray'}}
                onMouseDown={event => event.preventDefault()}
                onClick={() => onShowOnlyUniqueLabelsChanged(false)}
              >
                all
              </Button>
              <Button
                size='small' sx={{height: 22, textTransform: 'none', color: showOnlyUniqueLabels ? 'primary' : 'gray'}}
                onMouseDown={event => event.preventDefault()}
                onClick={() => onShowOnlyUniqueLabelsChanged(true)}
              >
                uniques
              </Button>
            </ButtonGroup>
          </Grid>
        </Grid>
      </OuterElementContext.Provider>
    </div>
  );
});

const PopperComponent = (props) => {
  return (
    <Popper { ...props } style={{ minWidth: 350, width: props.anchorEl.clientWidth }} placement='bottom' />
  );
};

const CSVAutocomplete = (props) => {
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

  let options = props.options;
  if (props.showOnlyUniqueLabels) {
    options = [];
    for (const option of props.options) {
      if (options.length === 0 || options[options.length - 1].label !== option.label) {
        options.push(option);
      }
    }
  }

  return (
    <Box sx={{position: 'relative'}} { ...getRootProps() }>
      {props.useSelect && (
        <FormControl fullWidth>
          <InputLabel id={`${props.label}-label`}>{props.label}</InputLabel>
          <Select
            label={props.label}
            labelId={`${props.label}-label`}
            onChange={(e) => { props.onChange(find(props.options, (option) => option.label === e.target.value)); }}
            value={props.value}
            sx={{'& .MuiSvgIcon-root': { display: 'none' }}}
          >
            {props.options.map((option) =>
              <MenuItem key={option.label} value={option.label}>{option.label}</MenuItem>
            )}
          </Select>
        </FormControl>
      )}
      {!props.useSelect && 'virtualize' in props && props.virtualize !== false && (
        <Autocomplete
          renderInput={(params) =>
            <TextField
              sx={{
                background: (theme) => 'transparent',
                '& .MuiInputBase-root': (theme) => ({
                  backgroundColor: isDragAccept ? 'rgba(225, 255, 214, 0.2)' : theme.palette.background.default,
                  borderRadius: '4px'
                }),
                '& .MuiAutocomplete-endAdornment': { display: 'none' },
                '& .MuiInputLabel-root': (theme) => ({
                  background: theme.palette.background.default,
                  borderRadius: '4px',
                  padding: '0 4px'
                })
              }}
              {...params}
              label={props.label}
            />
          }
          ListboxComponent={ListboxComponent}
          ListboxProps={{
            showOnlyUniqueLabels: props.showOnlyUniqueLabels,
            onShowOnlyUniqueLabelsChanged: props.onShowOnlyUniqueLabelsChanged
          }}
          PopperComponent={PopperComponent}
          renderOption={(liProps, option) => [liProps, option, props.renderOption || null]}
          value={props.value}
          options={options}
          isOptionEqualToValue={(option, value) => option.label === value.label && isEqual(option, value)}
          onChange={(e, val) => { props.onChange(val); }}
          { ...props.autocompleteProps }
        />
      )}
      {!props.useSelect && !props.virtualize && (
        <Autocomplete
          renderInput={(params) =>
            <TextField
              sx={{
                background: (theme) => 'transparent',
                '& .MuiInputBase-root': (theme) => ({
                  backgroundColor: isDragAccept ? 'rgba(225, 255, 214, 0.2)' : theme.palette.background.default,
                  borderRadius: '4px'
                }),
                '& .MuiAutocomplete-endAdornment': { display: 'none' },
              }}
              {...params}
              label={props.label}
            />
          }
          value={props.value}
          options={options}
          isOptionEqualToValue={(option, value) => option.label === value.label}
          onChange={(e, val) => { props.onChange(val); }}
          { ...props.autocompleteProps }
        />
      )}
      <Tooltip title='Open CSV file' placement='left'>
        <IconButton onClick={open} sx={{position: 'absolute', top: '50%', transform: 'translateY(-50%)', right: '0px'}}>
          <FileOpenOutlinedIcon />
        </IconButton>
      </Tooltip>
      {props.tooltip && (
        <Tooltip
          title={props.tooltip}
          disableFocusListener
          enterTouchDelay={0} leaveTouchDelay={0}
          placement='top'
        >
          <InfoOutlinedIcon sx={{ width: 14, height: 14, position: 'absolute', top: -6, right: 10, background: '#fff' }} />
        </Tooltip>
      )}
      <input { ...getInputProps() } />
    </Box>
  );
};

export default CSVAutocomplete;
