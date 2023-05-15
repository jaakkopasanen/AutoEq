import {Container, Grid, IconButton, Typography, Box} from "@mui/material";
import ClearIcon from "@mui/icons-material/Clear";
import FileOpenOutlinedIcon from "@mui/icons-material/FileOpenOutlined";
import React from "react";
import {
  android as isAndroid,
  ios as isIos,
  linux as isLinux,
  macos as isMacos,
  windows as isWindows
} from "platform-detect";
import LooksOneOutlinedIcon from '@mui/icons-material/LooksOneOutlined';
import LooksTwoOutlinedIcon from '@mui/icons-material/LooksTwoOutlined';
import Looks3OutlinedIcon from '@mui/icons-material/Looks3Outlined';
import Looks4OutlinedIcon from '@mui/icons-material/Looks4Outlined';
import {useTheme} from "@emotion/react";

const InfoPage = (props) => {
  const platform = isWindows ? 'Windows' : isMacos ? 'Mac OS' : isLinux ? 'Linux' : isAndroid ? 'Android' : isIos ? 'OSX' : null;
  const recommendedApp = {
    'Windows': 'EqualizerAPO GraphicEq',
    'Mac OS': 'Sound Source',
    'Linux': 'EasyEffects',
    'Android': 'Wavelet',
    'iOS': null,
  }[platform];

  const theme = useTheme();
  const iconSize = 48;

  return (
    <Container fixed maxWidth='md' sx={{color: theme => theme.palette.grey.A200, pb: 4}}>
      <IconButton
        onClick={props.onCloseClick}
        sx={{
          display: (props.canClose) ? 'inherit' : 'none',
          position: 'absolute', right: 0,
          top: theme => theme.spacing(10),
          color: theme => theme.palette.grey.A200,
        }}
      >
        <ClearIcon />
      </IconButton>
      <Grid
        container direction='column' alignItems='center' rowSpacing={{xs: 2, sm: 6}}
        sx={{'& p': {pb: theme => theme.spacing(1)}, pt: {xs: 4, sm: 8}}}
      >
        <Grid
          item
          sx={{textAlign: 'center'}}
          style={{pt: {xs: 4, sm: 8}, pb: {xs: 2, sm: 4}}}
        >
          <Box sx={{width: {xs: '60vw', sm: 300, xl: 400}, maxWidth: {xs: 300, sm: '60vw'}}}>
            <img src="/autoeq_logo.svg" alt='AutoEq logo' style={{width: '100%'}}/>
            <Typography variant='body2'>four easy steps to make your headphones sound better</Typography>
          </Box>

        </Grid>

        <Grid item container direction='row' columnSpacing={4} rowSpacing={4} justifyContent='center'>
          <Grid item xs={12} sm={6} container direction='row' alignItems='start' sx={{textAlign: 'left'}}>
            <Grid item sx={{width: iconSize + 8}}>
              <LooksOneOutlinedIcon sx={{width: iconSize, height: iconSize}} />
            </Grid>
            <Grid item sx={{width: `calc(100% - ${iconSize + 8}px)`}}>
              <Typography variant='h6' sx={{lineHeight: 1.2, mb: '12px'}}>Select your headphones at the top</Typography>
              <Typography variant='body2'>
                You can also import your own data by dragging and dropping a CSV file to the select field or clicking
                <FileOpenOutlinedIcon sx={{display: 'inline', height: '17px', width: '16px', transform: 'translate(-1px, 3px)'}} />
                to select a CSV file on your device.
              </Typography>
            </Grid>
          </Grid>

          <Grid item xs={12} sm={6} container direction='row' alignItems='start' sx={{textAlign: 'left'}}>
            <Grid item sx={{width: iconSize + 8}}>
              <LooksTwoOutlinedIcon sx={{width: iconSize, height: iconSize}} />
            </Grid>
            <Grid item sx={{width: `calc(100% - ${iconSize + 8}px)`}}>
              <Typography variant='h6' sx={{lineHeight: 1.2, mb: '12px'}}>Select equalizer app</Typography>
              {platform !== 'iOS' && (
                <Typography variant='body2'>
                  <b style={{color: theme.palette.secondary.light}}>{recommendedApp}</b> is recommended for <b>{platform}</b>
                </Typography>
              )}
              {platform === 'iOS' && (
                <Typography variant='body2'>
                  Unfortunately iOS doesn't allow system-wide equalizers. You can use iTunes' built-in equalizer or
                  get a separate device like Qudelix-5K or MiniDSP IL-DSP
                </Typography>
              )}
              <Typography variant='body2'>
                AutoEq doesn't do the live equalization for your device and so you need a separate equalizer app to
                do this. AutoEq will produce optimal settings for the app
              </Typography>

            </Grid>
          </Grid>

          <Grid item xs={12} sm={6} container direction='row' alignItems='start' sx={{textAlign: 'left'}}>
            <Grid item sx={{width: iconSize + 8}}>
              <Looks3OutlinedIcon sx={{width: iconSize, height: iconSize}} />
            </Grid>
            <Grid item sx={{width: `calc(100% - ${iconSize + 8}px)`}}>
              <Typography variant='h6' sx={{lineHeight: 1.2, mb: '12px'}}>Hear the difference with the live demo</Typography>
              <Typography variant='body2'>
                Play some songs with player on the bottom and toggle EQ on and off to hear the difference
              </Typography>
              <Typography variant='body2'>
                Adjust bass and treble to taste and play around with the advanced parameters if you wish to get the
                most out of your headphones
              </Typography>
            </Grid>
          </Grid>

          <Grid item xs={12} sm={6} container direction='row' alignItems='start' sx={{textAlign: 'left'}}>
            <Grid item sx={{width: iconSize + 8}}>
              <Looks4OutlinedIcon sx={{width: iconSize, height: iconSize}} />
            </Grid>
            <Grid item sx={{width: `calc(100% - ${iconSize + 8}px)`}}>
              <Typography variant='h6' sx={{lineHeight: 1.2, mb: '12px'}}>Copy settings to the equalizer app</Typography>
              <Typography variant='body2'>
                Download and import, copy and paste or configure manually, depending on your chosen equalizer
              </Typography>
            </Grid>
          </Grid>


        </Grid>
      </Grid>
    </Container>
  );
};

export default InfoPage;
