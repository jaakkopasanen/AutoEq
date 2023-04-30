import React, {useState} from 'react';
import {Grid, Slider, TextField, Typography} from "@mui/material";

const InputSlider = (props) => {
  const [value, setValue] = useState(props.initialValue || 0.0);

  const handleChange = (v) => {
    setValue(v);
    props.onChange(v);
  };

  return (
    <Grid item container direction='row' columnSpacing={1} alignItems='center'>
      {Array.isArray(value) && (
        <Grid item>
          <TextField
            value={value[0].toString()}
            onChange={(e) => {
                props.onChange([parseFloat(e.target.value), value[1]])
            }}
            size='small' sx={{width: (props.inputChars || 3) * 10 + 25}}
            error={value[0] > value[1]}
          />
        </Grid>
      )}
      <Grid item sx={{flexGrow: 1, width: 'auto'}} container direction='column'>
        <Grid item>
          <Typography sx={{fontSize: '14px'}}>{props.label}</Typography>
        </Grid>
        <Grid item>
          <Slider
            value={value}
            min={props.min} max={props.max} step={props.step}
            onChange={(e) => handleChange(e.target.value)}
            color={Array.isArray(value) && value[0] > value[1] ? 'error' : 'primary'}
            sx={{padding: '12px 0'}}
          />
        </Grid>
      </Grid>
      <Grid item>
        <TextField
          value={(Array.isArray(value) ? value[1] : value).toString()}
          onChange={(e) => {
            if (Array.isArray(value)) {
              props.onChange([value[0], parseFloat(e.target.value)])
            } else {
              props.onChange(parseFloat(e.target.value))
            }
          }}
          size='small' sx={{width: (props.inputChars || 3) * 10 + 25}}
          error={Array.isArray(value) && value[0] > value[1]}
        />
      </Grid>
    </Grid>
  );
};

export default InputSlider;
