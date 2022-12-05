import React from 'react';
import {Autocomplete, Grid, TextField} from "@mui/material";

class TargetTab extends React.Component {
    constructor(props) {
        super(props);
        this.state = { compensations: null };
        this.fetchCompensations = this.fetchCompensations.bind(this);
    }

    async fetchCompensations() {
        const data = await fetch('/compensations').then(res => res.json()).catch(err => {
            throw err;
        });
        const compensations = [];
        for (const [name, fr] of Object.entries(data)) {
            compensations.push({ label: name, ...fr });
        }
        this.setState({compensations: compensations});
    }

    componentDidMount() {
        this.fetchCompensations();
    }

    render() {
        if (!this.state.compensations) {
            return null;
        }
        return (
            <Grid container direction='row' spacing={2} sx={{p: 1}}>
                <Grid item container xs={12} md={6}>
                    <Autocomplete
                        xs={6}
                        renderInput={(params) => <TextField {...params} label="Select compensation" />}
                        options={this.state.compensations}
                        onChange={this.props.onCompensationChanged}
                        sx={{width: '100%'}}
                    />
                </Grid>
                <Grid item container xs={12} sm={6}>
                    Hello
                </Grid>
            </Grid>
        )
    }
}

export default TargetTab;
