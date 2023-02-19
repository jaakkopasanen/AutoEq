import React from 'react';
import {Grid, Slider, TextField, Typography} from "@mui/material";

const InputSlider = (props) => {
  return (
    <Grid item container direction='row' columnSpacing={1} alignItems='center'>
      {Array.isArray(props.value) && (
        <Grid item>
          <TextField
            value={props.value[0].toString()}
            onChange={(e) => {
                props.onChange([parseFloat(e.target.value), props.value[1]])
            }}
            size='small' sx={{width: '65px'}}
            error={props.value[0] > props.value[1]}
          />
        </Grid>
      )}
      <Grid item sx={{flexGrow: 1, width: 'auto'}} container direction='column'>
        <Grid item>
          <Typography sx={{fontSize: '14px'}}>{props.label}</Typography>
        </Grid>
        <Grid item>
          <Slider
            value={props.value}
            min={props.min} max={props.max} step={props.step}
            onChange={(e) => props.onChange(e.target.value)}
            color={Array.isArray(props.value) && props.value[0] > props.value[1] ? 'error' : 'primary'}
            sx={{padding: '12px 0'}}
          />
        </Grid>
      </Grid>
      <Grid item>
        <TextField
          value={(Array.isArray(props.value) ? props.value[1] : props.value).toString()}
          onChange={(e) => {
            if (Array.isArray(props.value)) {
              props.onChange([props.value[0], parseFloat(e.target.value)])
            } else {
              props.onChange(parseFloat(e.target.value))
            }
          }}
          size='small' sx={{width: '65px'}}
          error={Array.isArray(props.value) && props.value[0] > props.value[1]}
        />
      </Grid>
    </Grid>
  );
};

export default InputSlider;
