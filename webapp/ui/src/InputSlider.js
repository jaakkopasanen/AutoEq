import React from 'react';
import {Grid, Slider, TextField, Typography} from "@mui/material";

class InputSlider extends React.Component {
  render() {
    return (
      <Grid item container direction='row' columnSpacing={1} alignItems='center'>
        {Array.isArray(this.props.value) && (
          <Grid item>
            <TextField
              value={this.props.value[0].toString()}
              onChange={(e) => {
                  this.props.onChange([parseFloat(e.target.value), this.props.value[1]])
              }}
              size='small' sx={{width: '75px'}} inputProps={{step: this.props.step}}
              error={this.props.value[0] > this.props.value[1]}
            />
          </Grid>
        )}
        <Grid item sx={{flexGrow: 1, width: 'auto'}} container direction='column'>
          <Grid item>
            <Typography sx={{fontSize: '14px'}}>{this.props.label}</Typography>
          </Grid>
          <Grid item>
            <Slider
              value={this.props.value}
              min={this.props.min} max={this.props.max} step={this.props.step}
              onChange={(e) => this.props.onChange(e.target.value)}
              color={Array.isArray(this.props.value) && this.props.value[0] > this.props.value[1] ? 'error' : 'primary'}
              sx={{padding: '12px 0'}}
            />
          </Grid>
        </Grid>
        <Grid item>
          <TextField
            value={(Array.isArray(this.props.value) ? this.props.value[1] : this.props.value).toString()}
            onChange={(e) => {
              if (Array.isArray(this.props.value)) {
                this.props.onChange([this.props.value[0], parseFloat(e.target.value)])
              } else {
                this.props.onChange(parseFloat(e.target.value))
              }
            }}
            size='small' sx={{width: '75px'}} inputProps={{step: this.props.step}}
            error={Array.isArray(this.props.value) && this.props.value[0] > this.props.value[1]}
          />
        </Grid>
      </Grid>
    );
  }
}

export default InputSlider;
