import React, { useEffect, useRef } from 'react';
import FrequencyResponseGraph from './FrequencyResponseGraph';
import {
  Alert, Box,
  Container,
  Grid,
  Paper, Snackbar, styled,
} from '@mui/material';
import TopBar from './TopBar';
import TargetTab from './TargetTab';
import EqTab from './EqTab';
import cloneDeep from 'lodash/cloneDeep';
import find from 'lodash/find';
import findIndex from 'lodash/findIndex';
import merge from 'lodash/merge';
import { transposeArrayToObject } from './utils';
import Player from './Player';
import Waves from './Waves';
import defaultEqualizers from './equalizers';
import ApiClient from './ApiClient';
import useStateRef from './useStateRef';
import InfoPage from "./InfoPage";

const SmPaper = styled(Paper)(({ theme }) => ({
  [theme.breakpoints.down('sm')]: {
    borderRadius: 0,
    boxShadow: 'none',
    borderBottom: '1px dashed #aaa',
    paddingLeft: theme.spacing(1),
    paddingRight: theme.spacing(1),
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  background: 'rgba(255, 255, 255, 0.97)',
  backdropFilter: 'blur(3px)',
}));

const App = (props) => {
  const apiClientRef = useRef();
  const audioContextRef = useRef();
  const gainNodeRef = useRef();
  const preampNodeRef = useRef();
  const eqNodesRef = useRef([]);
  const equalizeTimerRef = useRef(null);

  const [isSnackbarOpen, setIsSnackbarOpen, isSnackbarOpenRef] = useStateRef(false);
  const [snackbarMessage, setSnackbarMessage, snackbarMessageRef] = useStateRef('');
  const [showInfo, setShowInfo, showInfoRef] = useStateRef(true);

  const [measurements, setMeasurements, measurementsRef] = useStateRef(null);  // { label, source, form, rig }
  const [selectedMeasurement, setSelectedMeasurement, selectedMeasurementRef] = useStateRef(null);  // { label, source, form, rig }

  const [graphData, setGraphData, graphDataRef] = useStateRef(null);  // Data for the frequency response graph

  const [soundProfiles, setSoundProfiles, soundProfilesRef] = useStateRef(
    window.localStorage.getItem('soundProfiles')
      ? JSON.parse(window.localStorage.getItem('soundProfiles'))
      : null
  );
  const [selectedSoundProfile, setSelectedSoundProfile, selectedSoundProfileRef] = useStateRef(null);
  const [compensations, setCompensations, compensationsRef] = useStateRef([]);
  // Sound signatures preferred for each measurement rig: {source: {form: {rig: label}}
  const [preferredCompensations, setPreferredCompensations, preferredCompensationsRef] = useStateRef([]);
  // Name (label) of the currently selected compensation.
  const [selectedCompensation, setSelectedCompensation, selectedCompensationRef] = useStateRef(null);
  const [soundSignature, setSoundSignature, soundSignatureRef] = useStateRef(null);  // Sound signature { frequency, raw }
  // Smoothing window size for sound signature
  const [soundSignatureSmoothingWindowSize, setSoundSignatureSmoothingWindowSize, soundSignatureSmoothingWindowSizeRef] = useStateRef(0.0);

  const [equalizers, setEqualizers, equalizersRef] = useStateRef(defaultEqualizers);
  const [selectedEqualizer, setSelectedEqualizer, selectedEqualizerRef] = useStateRef(null);  // Name of the selected equalizer app

  const [smoothed, setSmoothed, smoothedRef] = useStateRef(true);

  const [bassBoostGain, setBassBoostGain, bassBoostGainRef] = useStateRef(0.0);
  const [bassBoostFc, setBassBoostFc, bassBoostFcRef] = useStateRef(105.0);
  const [bassBoostQ, setBassBoostQ, bassBoostQRef] = useStateRef(0.7);
  const [trebleBoostGain, setTrebleBoostGain, trebleBoostGainRef] = useStateRef(0.0);
  const [trebleBoostFc, setTrebleBoostFc, trebleBoostFcRef] = useStateRef(10000.0);
  const [trebleBoostQ, setTrebleBoostQ, trebleBoostQRef] = useStateRef(0.7);
  const [tilt, setTilt, tiltRef] = useStateRef(0.0);
  const [maxGain, setMaxGain, maxGainRef] = useStateRef(12.0);
  const [windowSize, setWindowSize, windowSizeRef] = useStateRef(0.08);
  const [trebleWindowSize, setTrebleWindowSize, trebleWindowSizeRef] = useStateRef(2.0);
  const [trebleFLower, setTrebleFLower, trebleFLowerRef] = useStateRef(6000.0);
  const [trebleFUpper, setTrebleFUpper, trebleFUpperRef] = useStateRef(8000.0);
  const [trebleGainK, setTrebleGainK, trebleGainKRef] = useStateRef(1.0);
  const [fs, setFs, fsRef] = useStateRef(44100);
  const [bitDepth, setBitDepth, bitDepthRef] = useStateRef(16);
  const [phase, setPhase, phaseRef] = useStateRef('minimum');
  const [fRes, setFRes, fResRef] = useStateRef(16.0);
  const [preamp, setPreamp, preampRef] = useStateRef(0.0);
  const [graphicEq, setGraphicEq, graphicEqRef] = useStateRef(null);
  const [parametricEq, setParametricEq, parametricEqRef] = useStateRef(null);
  const [fixedBandEq, setFixedBandEq, fixedBandEqRef] = useStateRef(null);
  const [firAudioBuffer, setFirAudioBuffer, firAudioBufferRef] = useStateRef(null);
  const [gain, setGain, gainRef] = useStateRef(null);
  const [isEqOn, setIsEqOn, isEqOnRef] = useStateRef(false);

  const setState = {
    selectedCompensation: setSelectedCompensation,
    preferredCompensations: setPreferredCompensations,
    soundSignature: setSoundSignature,
    soundSignatureSmoothingWindowSize: setSoundSignatureSmoothingWindowSize,
    bassBoostFc: setBassBoostFc, bassBoostQ: setBassBoostQ, bassBoostGain: setBassBoostGain,
    trebleBoostFc: setTrebleBoostFc, trebleBoostQ: setTrebleBoostQ, trebleBoostGain: setTrebleBoostGain,
    tilt: setTilt, fs: setFs, bitDepth: setBitDepth, phase: setPhase, fRes: setFRes,
    preamp: setPreamp, maxGain: setMaxGain,
    windowSize: setWindowSize, trebleWindowSize: setTrebleWindowSize,
    trebleFLower: setTrebleFLower, trebleFUpper: setTrebleFUpper, trebleGainK: setTrebleGainK,
    smoothed: setSmoothed
  };

  const setUp = async () => {
    setMeasurements(await ApiClient.fetchMeasurements());
    const [compensations, preferredCompensations] = await ApiClient.fetchCompensations();
    setCompensations(compensations);
    setPreferredCompensations(preferredCompensations);

    apiClientRef.current = new ApiClient();
    audioContextRef.current = new AudioContext();
    gainNodeRef.current = audioContextRef.current.createGain();
    gainNodeRef.current.gain.value = 0.5;
    preampNodeRef.current = audioContextRef.current.createGain();
    preampNodeRef.current.gain.value = 1.0;
    preampNodeRef.current.connect(audioContextRef.current.destination);
    gainNodeRef.current.connect(preampNodeRef.current);
    setFs(audioContextRef.current.sampleRate);
    setGain(gainNodeRef.current.gain.value * 100);
  };
  useEffect(() => {
    setUp();
  }, []);

  const equalize = async (skipTimer) => {
    if (!!equalizeTimerRef.current) clearTimeout(equalizeTimerRef.current);
    if (!skipTimer) {
      equalizeTimerRef.current = setTimeout(() => { equalize(true); }, 500);
      return;
    }

    try {
      const res = await apiClientRef.current.equalize({
        selectedMeasurement: selectedMeasurementRef.current,
        equalizer: find(equalizersRef.current, (eq) => eq.label === selectedEqualizerRef.current),
        compensation: selectedCompensationRef.current,
        soundSignature: soundSignatureRef.current,
        soundSignatureSmoothingWindowSize: soundSignatureSmoothingWindowSizeRef.current,
        bassBoostGain: bassBoostGainRef.current,
        bassBoostFc: bassBoostFcRef.current,
        bassBoostQ: bassBoostQRef.current,
        trebleBoostGain: trebleBoostGainRef.current,
        trebleBoostFc: trebleBoostFcRef.current,
        trebleBoostQ: trebleBoostQRef.current,
        tilt: tiltRef.current,
        fs: fsRef.current,
        bitDepth: bitDepthRef.current,
        phase: phaseRef.current,
        fRes: fResRef.current,
        preamp: preampRef.current,
        maxGain: maxGainRef.current,
        windowSize: windowSizeRef.current,
        trebleWindowSize: trebleWindowSizeRef.current,
        trebleFLower: trebleFLowerRef.current,
        trebleFUpper: trebleFUpperRef.current,
        trebleGainK: trebleGainKRef.current,
        smoothed: smoothedRef.current
      }, audioContextRef.current);

      preampNodeRef.current.gain.value = res.preampGain;
      eqNodesRef.current = res.eqNodes;
      if (isEqOnRef.current) {
        connectEqNodes();
      } else {
        disconnectEqNodes();
      }

      setGraphData(res.graphData);
      setGraphicEq(res.graphicEq);
      setParametricEq(res.parametricEq);
      setFixedBandEq(res.fixedBandEq);
      setFirAudioBuffer(res.firAudioBuffer);

    } catch (err) {
      setIsSnackbarOpen(true);
      setSnackbarMessage(err.toString());
    }
  };

  const connectEqNodes = () => {
    const nodes = [preampNodeRef.current, ...eqNodesRef.current, audioContextRef.current.destination];
    for (let i = 0; i < nodes.length - 1; ++i) {
      nodes[i].disconnect();
      nodes[i].connect(nodes[i + 1]);
    }
  };

  const disconnectEqNodes = () => {
    for (const node of [preampNodeRef.current, ...eqNodesRef.current]) {
      node.disconnect();
    }
    preampNodeRef.current.connect(audioContextRef.current.destination);
  };

  const onMeasurementSelected = (measurement) => {
    if (measurement === null) {
      setSelectedMeasurement(null);
      setGraphData(null);
      return;
    }

    // TODO: not preferred for any?
    const compensationLabel = preferredCompensationsRef.current[measurement.source][measurement.form][measurement.rig];
    const compensation = find(compensations, (c) => c.label === compensationLabel);
    setShowInfo(false);
    setSelectedMeasurement(cloneDeep(measurement));
    setSelectedCompensation(compensationLabel);
    setBassBoostFc(compensation.bassBoost.fc);
    setBassBoostQ(compensation.bassBoost.q);
    setBassBoostGain(compensation.bassBoost.gain);
    equalize(true);
  };

  const onMeasurementCreated = (name, dataPoints) => {
    const newMeasurements = cloneDeep(measurementsRef.current);
    const obj = transposeArrayToObject(dataPoints, ['frequency', 'raw']);
    const newMeasurement = {
      label: name,
      form: 'unknown',
      rig: 'unknown',
      source: 'unknown',
      frequency: obj.frequency,
      raw: obj.raw
    };
    newMeasurements.splice(0, 0, newMeasurement);
    setMeasurements(newMeasurements);
    onMeasurementSelected(newMeasurement);
  };

  const onSmoothedChanged = (val) => {
    setSmoothed(val);
  };

  const onSoundProfileSelected = (name) => {
    const newState = cloneDeep(find(soundProfilesRef.current, (p) => p.name === name));
    for (const [key, val] of Object.entries(newState)) {
      try {
        setState[key](val);
      } catch (e) {}
    }
    const newlySelectedSoundProfile = cloneDeep(find(soundProfilesRef.current, (p) => p.name === name));
    delete newlySelectedSoundProfile.name;
    setSelectedSoundProfile(newlySelectedSoundProfile);
    equalize(true);
  };

  const captureSoundProfile = () => {
    return {
      selectedCompensation, preferredCompensations, soundSignature, soundSignatureSmoothingWindowSize,
      bassBoostGain, bassBoostFc, bassBoostQ, trebleBoostGain, trebleBoostFc, trebleBoostQ,
      tilt, maxGain, windowSize, trebleWindowSize, trebleFLower, trebleFUpper, trebleGainK
    };
  };

  const onSoundProfileCreated = () => {
    const newSoundProfile = captureSoundProfile();
    const newSoundProfiles = cloneDeep(soundProfilesRef.current);
    newSoundProfile.name = newSoundProfiles.length;
    newSoundProfiles.push(newSoundProfile);
    window.localStorage.setItem('soundProfiles', JSON.stringify(newSoundProfiles));
    setSoundProfiles(newSoundProfiles);
    onSoundProfileSelected(newSoundProfile.name);
  };

  const onSoundProfileSaved = (name) => {
    const profile = captureSoundProfile();
    profile.name = name;
    const newSoundProfiles = cloneDeep(soundProfilesRef.current);
    const ix = findIndex(newSoundProfiles, (p) => p.name === name);
    newSoundProfiles[ix] = profile;
    window.localStorage.setItem('soundProfiles', JSON.stringify(newSoundProfiles));
    setSoundProfiles(newSoundProfiles);
  };

  const onSoundProfileDeleted = (name) => {
    const newSoundProfiles = cloneDeep(soundProfilesRef.current);
    const ix = findIndex(newSoundProfiles, (p) => p.name === name);
    newSoundProfiles.splice(ix, 1);
    window.localStorage.setItem('soundProfiles', JSON.stringify(newSoundProfiles));
    setSoundProfiles(newSoundProfiles);
  };

  const onCompensationSelected = (compensation) => {
    const newPreferredCompensations = cloneDeep(preferredCompensationsRef.current);
    newPreferredCompensations[selectedMeasurementRef.current.source][selectedMeasurementRef.current.form][selectedMeasurementRef.current.rig] = compensation.label;
    setSelectedCompensation(compensation.label);
    setPreferredCompensations(newPreferredCompensations);
    setBassBoostFc(compensation.bassBoost.fc);
    setBassBoostQ(compensation.bassBoost.q);
    setBassBoostGain(compensation.bassBoost.gain);
    equalize(true);
  };

  const onCompensationCreated = (name, dataPoints) => {
    const newCompensations = cloneDeep(compensationsRef.current);
    const obj = transposeArrayToObject(dataPoints, ['frequency', 'raw'])
    const newCompensation = {
      label: name,
      frequency: obj.frequency,
      raw: obj.raw,
      compatible: [],
      recommended: [],
      bassBoost: { fc: 105, q: 0.7, gain: 0.0 }
    };
    newCompensations.push(newCompensation);
    setCompensations(newCompensations);
    onCompensationSelected(newCompensation);
  };

  const onEqParamChanged = (newParams) => {
    const newPreferredCompensations = cloneDeep(preferredCompensationsRef.current);
    const newCompensations = cloneDeep(compensationsRef.current);
    const compensationLabel = newPreferredCompensations[selectedMeasurementRef.current.source][selectedMeasurementRef.current.form][selectedMeasurementRef.current.rig];
    const ix = findIndex(newCompensations, (c) => c.label === compensationLabel);
    for (const [key, val] of Object.entries(newParams)) {
      if (key === 'bassBoostFc') {
        newCompensations[ix].bassBoost.fc = val;
        setBassBoostFc(val);
      } else  if (key === 'bassBoostQ') {
        newCompensations[ix].bassBoost.q = val;
        setBassBoostQ(val);
      } else if (key === 'bassBoostGain') {
        newCompensations[ix].bassBoost.gain = val;
        setBassBoostGain(val);
      }
      setState[key](val);
    }
    setPreferredCompensations(newPreferredCompensations);
    setCompensations(newCompensations);
    equalize();
  };

  const onEqualizerSelected = (val) => {
    if (val === null) {
      setSelectedEqualizer(null);
    } else {
      setSelectedEqualizer(val);
      equalize(true);
    }
  };

  const updateCustomPeqConfig = (updateFn) => {
    const equalizers = cloneDeep(equalizersRef.current);
    // Find custom parametric eq in the equalizers array
    const ix = findIndex(equalizers, (equalizer) => equalizer.label === 'Custom Parametric Eq');
    const equalizer = equalizers[ix];
    equalizers.splice(ix, 1, equalizer);
    updateFn(equalizer);
    setEqualizers(equalizer);
    equalize();
  };

  const onCustomPeqConfigChanged = (newParams) => {
    updateCustomPeqConfig((equalizer) => {
      equalizer.config = merge(equalizer.config, newParams);
    });
  };

  const onCustomPeqConfigFilterChanged = (newParams, i) => {
    updateCustomPeqConfig((equalizer) => {
      const filter = merge(equalizer.config.filters[i], newParams);
      equalizer.config.filters.splice(i, 1, filter);
    });
  };

  const onCustomPeqAddFilterClick = () => {
    updateCustomPeqConfig((equalizer) => {
      equalizer.config.filters.push({ type: 'PEAKING', fc: null, q: null, gain: null, minFc: null, maxFc: null, minQ: null, maxQ: null, minGain: null, maxGain: null});
    });
  };

  const onCustomPeqDeleteFilterClick = (i) => {
    updateCustomPeqConfig((equalizer) => {
      equalizer.config.filters.splice(i, 1);
    });
  };

  const onGainChange = (val) => {
    gainNodeRef.current.gain.value = val / 100;
    setGain(val);
  };

  const onIsEqOnChange = (val) => {
    setIsEqOn(val);
    if (!val) {
      disconnectEqNodes();
    } else {
      connectEqNodes();
    }
  };

  const onError = (err) => {
    setIsSnackbarOpen(true);
    setSnackbarMessage(err.toString());
  };

  const customPeq = find(equalizersRef.current, (equalizer) => equalizer.label === 'Custom Parametric Eq');
  const customPeqConfig = !!customPeq ? customPeq.config : null;
  //console.log(!!graphData, !!showInfo);
  return (
    <Box sx={{pt: 10, pb: {xs: 12, md: 13}}}>
      <Waves nWaves={10} />

      {(!!graphData && !showInfo) && (
        <Container fixed sx={{ pl: {xs: 0, sm: 2, md: 3}, pr: {xs: 0, sm: 1, md: 3}, }}>
          <Grid
            item
            container direction='row' alignItems='stretch'
            columnSpacing={{xs: 0, sm: 1, md: 2}} rowSpacing={{xs: 0, sm: 1, md: 2}}
          >

            <Grid item xs={12}>
              <SmPaper sx={{ pt: 1, pl: {xs: 1, sm: 0, md: 0}, pr: {xs: 0, sm: 1, md: 0}, pb: {xs: 1, sm: 0.5, md: 0} }}>
                <FrequencyResponseGraph
                  data={graphData}
                  smoothed={smoothed}
                  onSmoothedChanged={onSmoothedChanged}
                />
              </SmPaper>
            </Grid>

            <Grid item xs={12} md={6}>
              <SmPaper sx={{p: {sm: 1, md: 2}}}>
                <TargetTab
                  selectedMeasurement={selectedMeasurement}

                  soundProfiles={soundProfiles}
                  selectedSoundProfile={selectedSoundProfile}
                  onSoundProfileSelected={onSoundProfileSelected}
                  onSoundProfileCreated={onSoundProfileCreated}
                  onSoundProfileSaved={onSoundProfileSaved}
                  onSoundProfileDeleted={onSoundProfileDeleted}
                  captureSoundProfile={captureSoundProfile}

                  compensations={compensations}
                  selectedCompensation={selectedCompensation}
                  onCompensationSelected={onCompensationSelected}
                  onCompensationCreated={onCompensationCreated}

                  soundSignature={soundSignature}
                  soundSignatureSmoothingWindowSize={soundSignatureSmoothingWindowSize}

                  graphData={graphData}
                  smoothed={smoothed}

                  bassBoostGain={bassBoostGain}
                  bassBoostFc={bassBoostFc}
                  bassBoostQ={bassBoostQ}
                  trebleBoostGain={trebleBoostGain}
                  trebleBoostFc={trebleBoostFc}
                  trebleBoostQ={trebleBoostQ}
                  tilt={tilt}
                  maxGain={maxGain}
                  windowSize={windowSize}
                  trebleWindowSize={trebleWindowSize}
                  trebleFLower={trebleFLower}
                  trebleFUpper={trebleFUpper}
                  trebleGainK={trebleGainK}
                  onEqParamChanged={onEqParamChanged}

                  onError={onError}
                />
              </SmPaper>
            </Grid>

            <Grid item xs={12} md={6}>
              <SmPaper sx={{p: {sm: 1, md: 2}}}>
                <EqTab
                  selectedMeasurement={selectedMeasurement?.label}
                  equalizers={equalizers}
                  selectedEqualizer={selectedEqualizer}
                  onEqualizerSelected={onEqualizerSelected}
                  graphicEq={graphicEq}
                  parametricEq={parametricEq}
                  fixedBandEq={fixedBandEq}
                  firAudioBuffer={firAudioBuffer}
                  fs={fs}
                  bitDepth={bitDepth}
                  phase={phase}
                  fRes={fRes}
                  preamp={preamp}
                  onEqParamChanged={onEqParamChanged}
                  customPeqConfig={customPeqConfig}
                  onCustomPeqConfigChanged={onCustomPeqConfigChanged}
                  onCustomPeqConfigFilterChanged={onCustomPeqConfigFilterChanged}
                  onCustomPeqAddFilterClick={onCustomPeqAddFilterClick}
                  onCustomPeqDeleteFilterClick={onCustomPeqDeleteFilterClick}
                />
              </SmPaper>
            </Grid>
          </Grid>
        </Container>
      )}

      <Box sx={{color: theme => theme.palette.grey.A400, display: (!!showInfo || !graphData) ? 'block' : 'none'}}>
        <InfoPage
          canClose={!!graphData}
          onCloseClick={() => { setShowInfo(false); }}
        />
      </Box>

      <Box sx={{position: 'fixed', top: 0, left: 0, width: '100%', padding: 0, background: '#fff'}}>
        <Paper sx={{
          padding: '8px 16px',
          borderRadius: 0,
          background: (theme) => theme.palette.background.default}}
        >
          <TopBar
            onShowInfoClicked={() => setShowInfo(!showInfo)}
            selectedMeasurement={selectedMeasurement}
            isMeasurementSelected={!!selectedMeasurement}
            measurements={measurements}
            onMeasurementSelected={onMeasurementSelected}
            onMeasurementCreated={onMeasurementCreated}
            onError={onError}
          />
        </Paper>
      </Box>

      <Box
        sx={{
          position: 'fixed', bottom: theme => theme.spacing(1),
          width: {xs: '252px', sm: '574px', md: '594px'},
          left: {xs: 'calc((100% - 252px) / 2)', sm: 'calc((100% - 574px) / 2)', md: 'calc((100% - 594px) / 2)'}
        }}>
        <Player
          audioContext={audioContextRef.current}
          audioDestination={gainNodeRef.current}
          gain={gain}
          onGainChange={onGainChange}
          onIsEqOnChange={onIsEqOnChange}
          isEqEnabled={eqNodesRef.current.length > 0 && selectedEqualizer !== null}
        />
      </Box>

      <Box>
        <Snackbar
          open={isSnackbarOpen}
          onClose={() => { setIsSnackbarOpen(false); }}
          sx={{background: theme => theme.palette.background.default}}
          anchorOrigin={{ vertical: 'top', horizontal: 'center'}}
        >
          <Alert
            onClose={() => { setIsSnackbarOpen(false); }}
            severity='error' variant='outlined' sx={{ width: '100%'}}
          >
            {snackbarMessage}
          </Alert>
        </Snackbar>
      </Box>
    </Box>
  );

};

export default App;
