import React, {useEffect, useState} from 'react';
import {Grid, IconButton, Tooltip, Typography} from '@mui/material';
import FileCopyIcon from '@mui/icons-material/FileCopy';
import DownloadIcon from '@mui/icons-material/Download';
import { downloadAsFile } from "./utils";

const EqAppEqualizerApoGraphicEq = (props) => {
  const [copyToClipboardTooltipOpen, setCopyToClipboardTooltipOpen] = useState(false);

  const onDownloadClick = () => {
    downloadAsFile(props.graphicEq, 'text/plain', `${props.selectedMeasurement} GraphicEq.txt`);
  };

  useEffect(() => {
    if (copyToClipboardTooltipOpen) {
      setTimeout(() => {
        setCopyToClipboardTooltipOpen(false);
      }, 2000)
    }
  }, [copyToClipboardTooltipOpen]);

  const onCopyToClipboardClick = () => {
    navigator.clipboard.writeText(props.graphicEq).then(() => {
      setCopyToClipboardTooltipOpen(true);
    }, (err) => {
      console.error('Async: Could not copy text: ', err);
    });
  };

  return (
    <Grid container direction='column' rowSpacing={1}>
      {props.instructions && (
        <Grid
          item
          sx={{
            padding: '8px 12px',
            background: '#e5f3f7',
            borderStyle: 'solid',
            borderWidth: '1px',
            borderColor: '#9abac3',
            borderRadius: '4px',
            marginTop: '8px',
          }}
        >
          <Typography variant='caption'>
            {props.instructions}
          </Typography>
        </Grid>
      )}
      <Grid item container direction='row' sx={{flexWrap: 'nowrap'}}>
        <Grid
          item
          sx={{
            fontFamily: 'monospace',
            borderStyle: 'solid',
            borderWidth: '1px',
            borderColor: 'primary.main',
            borderRadius: 1,
            padding: 1,
            display: !!props.graphicEq ? 'block' : 'none'
          }}
        >
          <div>{props.graphicEq}</div>
        </Grid>
      </Grid>
      <Grid item container direction='row' columnSpacing={1} justifyContent='center'>
        <Grid item>
          <IconButton onClick={onDownloadClick}><DownloadIcon /></IconButton>
        </Grid>
        <Grid item>
          <Tooltip
            PopperProps={{disablePortal: true}}
            open={copyToClipboardTooltipOpen}
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
            <IconButton onClick={onCopyToClipboardClick}><FileCopyIcon /></IconButton>
          </Tooltip>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default EqAppEqualizerApoGraphicEq;
