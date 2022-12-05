import React from 'react';
import {Autocomplete, Grid, TextField} from "@mui/material";
import InputSlider from "./InputSlider";

class TargetTab extends React.Component {
    render() {
        return (
            <Grid container direction='row' spacing={2} sx={{p: 1}}>
                <Grid item xs={12} md={6} container direction='column' rowSpacing={1}>
                    {!!this.props.compensations && (
                        <Grid item>
                            <Autocomplete
                                xs={6}
                                renderInput={(params) =>
                                    <TextField {...params} label="Select compensation" />
                                }
                                options={this.props.compensations}
                                onChange={(e, val) => {
                                    this.props.onEqParamChanged('compensation', val?.name)
                                }}
                                sx={{width: '100%'}}
                            />
                        </Grid>
                    )}
                    {!!this.props.measurements && (
                        <Grid item>
                            <Autocomplete
                                xs={6}
                                renderInput={(params) =>
                                    <TextField {...params} label="Select sound signature" />
                                }
                                options={this.props.measurements}
                                onChange={(e, val) => {
                                    this.props.onEqParamChanged('sound_signature', val?.name)
                                }}
                                sx={{width: '100%'}}
                            />
                        </Grid>
                    )}
                </Grid>
                <Grid item xs={12} sm={6} container direction='column' rowSpacing={1}>
                    <Grid item>
                        <InputSlider
                            label='Bass boost' value={this.props.eqParams.bass_boost_gain} min={-10} max={20} step={0.5}
                            onChange={(v) => { this.props.onEqParamChanged('bass_boost_gain', v) }} />
                    </Grid>
                    <Grid>
                        <InputSlider
                            label='Treble boost' value={this.props.eqParams.treble_boost_gain} min={-20} max={20} step={0.5}
                            onChange={(v) => { this.props.onEqParamChanged('treble_boost_gain', v) }} />
                    </Grid>
                    <Grid>
                        <InputSlider
                            label='Tilt' value={this.props.eqParams.tilt} min={-2} max={2} step={0.1}
                            onChange={(v) => { this.props.onEqParamChanged('tilt', v) }} />
                    </Grid>
                    <Grid>
                        <InputSlider
                            label='Max gain' value={this.props.eqParams.max_gain} min={0} max={30} step={0.5}
                            onChange={(v) => { this.props.onEqParamChanged('max_gain', v) }} />
                    </Grid>
                    <Grid>
                        <InputSlider
                            label='Smoothing window size' value={this.props.eqParams.window_size} min={0} max={1} step={0.01}
                            onChange={(v) => { this.props.onEqParamChanged('window_size', v) }} />
                    </Grid>
                </Grid>
            </Grid>
        )
    }
}

export default TargetTab;
