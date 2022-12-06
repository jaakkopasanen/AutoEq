import React from 'react';
import {Grid, Slider, TextField, Typography} from "@mui/material";

class InputSlider extends React.Component {
  render() {
    return (
      <Grid container direction='column'>
        <Grid item>
          <Typography>{this.props.label}</Typography>
        </Grid>
        <Grid item container direction='row' columnSpacing={1}>
          {Array.isArray(this.props.value) && (
            <Grid item>
              <TextField
                value={this.props.value[0]}
                onChange={(e) => {
                    this.props.onChange([parseFloat(e.target.value), this.props.value[1]])
                }}
                type='number'
                size='small'
                sx={{width: '100px'}}
                inputProps={{step: this.props.step}}
                error={this.props.value[0] > this.props.value[1]}
              />
            </Grid>
          )}
          <Grid item sx={{flexGrow: 1}}>
            <Slider
              value={this.props.value}
              min={this.props.min} max={this.props.max} step={this.props.step}
              onChange={(e) => this.props.onChange(e.target.value)}
              color={Array.isArray(this.props.value) && this.props.value[0] > this.props.value[1] ? 'error' : 'primary'}
            />
          </Grid>
          <Grid item>
            <TextField
              value={Array.isArray(this.props.value) ? this.props.value[1] : this.props.value}
              onChange={(e) => {
                if (Array.isArray(this.props.value)) {
                  this.props.onChange([this.props.value[0], parseFloat(e.target.value)])
                } else {
                  this.props.onChange(parseFloat(e.target.value))
                }
              }}
              type='number' size='small' sx={{width: '100px'}} inputProps={{step: this.props.step}}
              error={Array.isArray(this.props.value) && this.props.value[0] > this.props.value[1]}
            />
          </Grid>
        </Grid>
      </Grid>
    );
  }
}

export default InputSlider;
