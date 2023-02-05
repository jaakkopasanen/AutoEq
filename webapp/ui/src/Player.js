import React, {useEffect, useState} from 'react';
import {Grid, IconButton, LinearProgress, Slider, Switch, Typography} from "@mui/material";
import {
  PlayArrow as PlayIcon,
  SkipNext as SkipNextIcon,
  SkipPrevious as SkipPreviousIcon,
  Pause as PauseIcon,
  VolumeUp as VolumeIcon
} from "@mui/icons-material";

const playlist = [
  {
    url: 'https://dl.dropboxusercontent.com/s/5p1gayvfmb3fc0z/Eagles%20-%20Hotel%20California%2064%20kbps.mp3?dl=0',
    name: 'Eagles - Hotel California'
  },
  {
    url: 'https://dl.dropboxusercontent.com/s/7jb5cif5o5bda9n/Jennifer%20Warnes%20-%20Bird%20on%20a%20Wire%2064%20kbps.mp3?dl=0',
    name: 'Jennifer Warnes - Bird On a Wire'
  },
  {
    url: 'https://dl.dropboxusercontent.com/s/epvit0keu9w7emp/Wintersun%20-%20Sons%20of%20Winter%20and%20Stars%2064%20kbps.mp3?dl=0',
    name: 'Wintersun - Sons Of Winter And Stars'
  },
];
for (let i = 0; i < playlist.length; ++i) {
  playlist[i].audio = new Audio(playlist[i].url);
  playlist[i].audio.crossOrigin = 'anonymous';
  playlist[i].audio.loop = true;
  playlist[i].sourceNode = null;
}

const Player = (props) => {
  const [trackIx, setTrackIx] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(0);

  const initSourceNode = (ix) => {
    if (playlist[ix].sourceNode === null) {
      playlist[ix].sourceNode = props.audioContext.createMediaElementSource(playlist[ix].audio);
      playlist[ix].sourceNode.connect(props.audioDestination);
    }
  }

  const onSkipPreviousClick = () => {
    playlist[trackIx].audio.pause();
    const newTrackIx = trackIx > 0 ? trackIx - 1 : 0;
    initSourceNode(newTrackIx);
    playlist[newTrackIx].audio.fastSeek(0);
    playlist[newTrackIx].audio.play();
    setTrackIx(newTrackIx);
    setIsPlaying(true);
  };

  const onSkipNextClick = () => {
    playlist[trackIx].audio.pause();
    const newTrackIx = trackIx < playlist.length - 1 ? trackIx + 1 : playlist.length - 1;
    initSourceNode(newTrackIx);
    playlist[newTrackIx].audio.fastSeek(0);
    playlist[newTrackIx].audio.play();
    setTrackIx(newTrackIx);
    setIsPlaying(true);
  };

  const onPlayClick = () => {
    initSourceNode(trackIx);
    if (isPlaying) {
      playlist[trackIx].audio.pause();
    } else {
      playlist[trackIx].audio.play();
    }
    setIsPlaying(!isPlaying);
  };

  useEffect(() => {
    const timer = setInterval(() => {
      setProgress(playlist[trackIx].audio.currentTime / playlist[trackIx].audio.duration * 100);
    }, 10);
    return () => {
      clearInterval(timer);
    };
  }, [trackIx, isPlaying]);

  return (
    <Grid container direction='column' justifyContent='center' alignItems='center'>
      <Grid item>
        <div>
          <Grid
            container direction='row' justifyContent='center' alignItems='center' columnSpacing={1}
            sx={{
              background: theme => theme.palette.grey["800"],
              borderTopLeftRadius: 4, borderTopRightRadius: 4,
              padding: '12px 18px'
            }}
          >
            <Grid item>
              <IconButton onClick={onSkipPreviousClick} disabled={trackIx === 0} color='secondary'>
                <SkipPreviousIcon />
              </IconButton>
            </Grid>
            <Grid item>
              <IconButton onClick={onPlayClick} color='secondary'>
                {isPlaying ? <PauseIcon /> : <PlayIcon />}
              </IconButton>
            </Grid>
            <Grid item>
              <IconButton onClick={onSkipNextClick} disabled={trackIx === playlist.length - 1} color='secondary'>
                <SkipNextIcon />
              </IconButton>
            </Grid>
            <Grid item sx={{width: '200px'}}>
              <LinearProgress
                sx={{ '& .MuiLinearProgress-bar': { transition: 'none' } }}
                variant='determinate'
                color='primary'
                value={progress}
              />
            </Grid>
            <Grid item container direction='row' justifyContent='center' alignItems='center' sx={{width: '120px'}}>
              <Grid item>
                <IconButton color='secondary'>
                  <VolumeIcon />
                </IconButton>
              </Grid>
              <Grid item sx={{flexGrow: 1}}>
                <Slider value={props.gain} onChange={(e, val) => { props.onGainChange(val); }} size='medium' />
              </Grid>
            </Grid>
            <Grid item container direction='row' justifyContent='center' alignItems='center' sx={{width: '120px'}}>
              <Grid item>
                <Typography>EQ</Typography>
              </Grid>
              <Grid item>
                <Switch
                  checked={props.isEqOn}
                  onChange={(e, val) => { props.onIsEqOnChange(val); }}
                  disabled={!props.isEqEnabled}
                />
              </Grid>
            </Grid>
          </Grid>
        </div>
      </Grid>
    </Grid>
  );
};

export default Player;
