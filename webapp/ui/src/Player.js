import React, {useEffect, useState} from 'react';
import {Grid, IconButton, LinearProgress, Slider, Switch, Typography} from "@mui/material";
import {
  PlayArrow as PlayIcon,
  SkipNext as SkipNextIcon,
  SkipPrevious as SkipPreviousIcon,
  Pause as PauseIcon,
  VolumeUp as VolumeIcon
} from "@mui/icons-material";

const Player = (props) => {
  const [trackIx, setTrackIx] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [progressInterval, setProgressInterval] = useState(null);
  const [progress, setProgress] = useState(0);
  const [playlist, setPlaylist] = useState([]);

  const initSourceNode = (ix) => {
    if (playlist[ix].audio === null) {
      const newPlaylist = [ ...playlist ];
      newPlaylist[ix].audio = new Audio(newPlaylist[ix].url);
      newPlaylist[ix].audio.crossOrigin = 'anonymous';
      newPlaylist[ix].audio.loop = true;
      newPlaylist[ix].sourceNode = props.audioContext.createMediaElementSource(newPlaylist[ix].audio);
      newPlaylist[ix].sourceNode.connect(props.audioDestination);
      setPlaylist(newPlaylist);
    }
  }

  const onSkipPreviousClick = () => {
    playlist[trackIx].audio.pause();
    const newTrackIx = trackIx > 0 ? trackIx - 1 : playlist.length - 1;
    initSourceNode(newTrackIx);
    playlist[newTrackIx].audio.fastSeek(0);
    playlist[newTrackIx].audio.play();
    setTrackIx(newTrackIx);
    setIsPlaying(true);
  };

  const onSkipNextClick = () => {
    playlist[trackIx].audio.pause();
    const newTrackIx = trackIx < playlist.length - 1 ? trackIx + 1 : 0;
    initSourceNode(newTrackIx);
    playlist[newTrackIx].audio.fastSeek(0);
    playlist[newTrackIx].audio.play();
    setTrackIx(newTrackIx);
    setIsPlaying(true);
  };

  const onPlayClick = () => {
    if (!playlist.length) return;
    initSourceNode(trackIx);
    if (isPlaying) {
      playlist[trackIx].audio.pause();
    } else {
      playlist[trackIx].audio.play();
    }
    setIsPlaying(!isPlaying);
  };

  useEffect(() => {
    console.log('useEffect', trackIx, isPlaying);
    if (!playlist.length) return;
    if (isPlaying) {
      setProgressInterval(setInterval(() => {
        setProgress(playlist[trackIx].audio.currentTime / playlist[trackIx].audio.duration * 100);
      }, 10));
    } else {
      clearInterval(progressInterval);
    }
    return () => {
      clearInterval(progressInterval);
    };
  }, [trackIx, isPlaying]);

  useEffect(() => {
    if (playlist.length) return;
    fetch('/playlist').then(async res => {
      const playlist = await res.json();
      for (let i = 0; i < playlist.length; ++i) {
        playlist[i].audio = null;
        playlist[i].sourceNode = null;
      }
      setPlaylist(playlist);
    });
  }, []);

  if (!playlist.length) return null;

  return (
    <Grid container direction='column' justifyContent='center' alignItems='center'>
      <Grid item>
        <div>
          <Grid
            item container direction='column' justifyContent='center' alignItems='center'
            sx={{
              background: 'rgba(255, 255, 255, 0.8)',
              borderRadius: 2,
              padding: '12px 18px',
              borderStyle: 'solid', borderWidth: 1, borderColor: theme => theme.palette.grey.A400,
              backdropFilter: 'blur(2px)'
            }}
          >
            <Grid item>
              <Typography>{playlist[trackIx].name}</Typography>
            </Grid>
            <Grid item>
              <Grid
                container direction='row' justifyContent='center' alignItems='center' columnSpacing={1}
              >
                <Grid item>
                  <IconButton onClick={onSkipPreviousClick} color='secondary'>
                    <SkipPreviousIcon />
                  </IconButton>
                </Grid>
                <Grid item>
                  <IconButton onClick={onPlayClick} color='secondary'>
                    {isPlaying ? <PauseIcon /> : <PlayIcon />}
                  </IconButton>
                </Grid>
                <Grid item>
                  <IconButton onClick={onSkipNextClick} color='secondary'>
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
            </Grid>
          </Grid>
        </div>
      </Grid>
    </Grid>
  );
};

export default Player;
