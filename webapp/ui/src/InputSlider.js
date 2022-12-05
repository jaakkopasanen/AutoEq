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
                    <Grid item sx={{flexGrow: 1}}>
                        <Slider
                            value={this.props.value}
                            min={this.props.min} max={this.props.max} step={this.props.step}
                            onChange={(e) => this.props.onChange(e.target.value)}
                        />
                    </Grid>
                    <Grid item>
                        <TextField
                            value={this.props.value}
                            onChange={(e) => this.props.onChange(parseFloat(e.target.value))}
                            type='number'
                            size='small'
                            sx={{width: '80px'}}
                            inputProps={{step: this.props.step}}
                        />
                    </Grid>
                </Grid>
            </Grid>
        );
    }
}

export default InputSlider;
