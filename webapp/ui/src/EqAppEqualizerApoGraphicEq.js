import React from 'react';
import {Grid, IconButton, Tooltip} from '@mui/material';
import { FileCopy as CopyIcon, Download as DownloadIcon } from '@mui/icons-material';
import { downloadAsFile } from "./utils";

class EqAppEqualizerApoGraphicEq extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      copyToClipboardTooltipOpen: false
    };
    this.onDownloadClick = this.onDownloadClick.bind(this);
    this.onCopyToClipboardClick = this.onCopyToClipboardClick.bind(this);
  }

  onDownloadClick() {
    downloadAsFile(this.props.graphicEq, 'text/plain', `${this.props.selectedMeasurement} GraphicEq.txt`)
  }

  onCopyToClipboardClick() {
    navigator.clipboard.writeText(this.props.graphicEq).then(() => {
      this.setState({copyToClipboardTooltipOpen: true}, () => {
        setTimeout(() => {
          this.setState({copyToClipboardTooltipOpen: false})
        }, 2000);
      });
    }, (err) => {
      console.error('Async: Could not copy text: ', err);
    });
  }

  render() {
    return (
      <Grid container direction='column' rowSpacing={1}>
        <Grid item />
        <Grid item container direction='row' sx={{flexWrap: 'nowrap'}}>
          <Grid item sx={{
            fontFamily: 'monospace',
            borderStyle: 'solid',
            borderWidth: '1px',
            borderColor: 'primary.main',
            borderRadius: 1,
            padding: 1,
            display: !!this.props.graphicEq ? 'block' : 'none'
          }}
          >
            <div>{this.props.graphicEq}</div>
          </Grid>
        </Grid>
        <Grid item container direction='row' columnSpacing={1} justifyContent='center'>
          <Grid item>
            <IconButton onClick={this.onDownloadClick}><DownloadIcon /></IconButton>
          </Grid>
          <Grid item>
            <Tooltip
              PopperProps={{disablePortal: true}}
              open={this.state.copyToClipboardTooltipOpen}
              leaveDelay={500}
              disableFocusListener
              disableHoverListener
              disableTouchListener
              title='Coped to clipboard!'
              componentsProps={{
                tooltip: {
                  sx: {p: [1, 1.5]}
                }
              }}
            >
              <IconButton onClick={this.onCopyToClipboardClick}><CopyIcon /></IconButton>
            </Tooltip>
          </Grid>
        </Grid>
      </Grid>
    );
  }
}

export default EqAppEqualizerApoGraphicEq;
