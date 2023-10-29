import React, {useEffect, useRef, useState} from 'react';
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
    //borderRadius: 0,
    boxShadow: 'none',
    paddingLeft: theme.spacing(1),
    paddingRight: theme.spacing(1),
    paddingTop: theme.spacing(2),
    paddingBottom: theme.spacing(2),
  },
  background: theme.palette.background.default,
  backdropFilter: 'blur(3px)',
}));

const App = (props) => {
  const apiClientRef = useRef();
  const audioContextRef = useRef(null);
  const gainNodeRef = useRef();
  const preampNodeRef = useRef();
  const eqNodesRef = useRef([]);
  const equalizeTimerRef = useRef(null);

  const [isSnackbarOpen, setIsSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState('');
  const [showInfo, setShowInfo] = useState(true);

  const [measurements, setMeasurements, measurementsRef] = useStateRef(null);  // { label, source, form, rig }
  const [selectedMeasurement, setSelectedMeasurement, selectedMeasurementRef] = useStateRef(null);  // { label, source, form, rig }

  const [graphData, setGraphData] = useState(null);  // Data for the frequency response graph

  const [soundProfiles, setSoundProfiles, soundProfilesRef] = useStateRef(
    window.localStorage.getItem('soundProfiles')
      ? JSON.parse(window.localStorage.getItem('soundProfiles'))
      : []
  );
  const [selectedSoundProfile, setSelectedSoundProfile] = useState(null);
  const [targets, setTargets, targetsRef] = useStateRef([]);
  const targetsBassBoostsRef = useRef({});
  // Sound signatures preferred for each measurement rig: {source: {form: {rig: label}}
  const [preferredTargets, setPreferredTargets, preferredTargetsRef] = useStateRef([]);
  // Name (label) of the currently selected target.
  const [selectedTarget, setSelectedTarget, selectedTargetRef] = useStateRef(null);
  const [soundSignature, setSoundSignature, soundSignatureRef] = useStateRef(null);  // Sound signature { frequency, raw }
  // Smoothing window size for sound signature
  const [soundSignatureSmoothingWindowSize, setSoundSignatureSmoothingWindowSize, soundSignatureSmoothingWindowSizeRef] = useStateRef(1.0);

  const [equalizers, setEqualizers, equalizersRef] = useStateRef(defaultEqualizers);
  const [selectedEqualizer, setSelectedEqualizer, selectedEqualizerRef] = useStateRef(null);  // Name of the selected equalizer app

  const [smoothed, setSmoothed, smoothedRef] = useStateRef(true);

  const bassBoostGainRef = useRef(0.0);
  const bassBoostFcRef = useRef(105.0);
  const bassBoostQRef = useRef(0.7);
  const trebleBoostGainRef = useRef(0.0);
  const trebleBoostFcRef = useRef(10000.0);
  const trebleBoostQRef = useRef(0.7);
  const tiltRef = useRef(0.0);
  const maxGainRef = useRef(12.0);
  const windowSizeRef = useRef(0.08);
  const trebleWindowSizeRef = useRef(2.0);
  const trebleFLowerRef = useRef(6000.0);
  const trebleFUpperRef = useRef(8000.0);
  const trebleGainKRef = useRef(1.0);
  const fsRef = useRef(44100);
  const bitDepthRef = useRef(16);
  const phaseRef = useRef('minimum');
  const fResRef = useRef(16.0);
  const preampRef = useRef(0.0);
  const [graphicEq, setGraphicEq] = useState(null);
  const [parametricEq, setParametricEq] = useState(null);
  const [fixedBandEq, setFixedBandEq] = useState(null);
  const [firAudioBuffer, setFirAudioBuffer] = useState(null);
  const [isEqOn, setIsEqOn, isEqOnRef] = useStateRef(false);
  const maxSlopeRef = useRef(18);

  const setState = {
    selectedTarget: setSelectedTarget,
    preferredTargets: setPreferredTargets,
    soundSignature: setSoundSignature,
    soundSignatureSmoothingWindowSize: (v) => { soundSignatureSmoothingWindowSizeRef.current = v; },
    bassBoostFc: (v) => { bassBoostFcRef.current = v; },
    bassBoostQ: (v) => { bassBoostQRef.current = v; },
    bassBoostGain: (v) => { bassBoostGainRef.current = v; },
    trebleBoostFc: (v) => { trebleBoostFcRef.current = v; },
    trebleBoostQ: (v) => { trebleBoostQRef.current = v; },
    trebleBoostGain: (v) => { trebleBoostGainRef.current = v; },
    tilt: (v) => { tiltRef.current = v; },
    fs: (v) => { fsRef.current = v; },
    bitDepth: (v) => { bitDepthRef.current = v; },
    phase: (v) => { phaseRef.current = v; },
    fRes: (v) => { fResRef.current = v; },
    preamp: (v) => { preampRef.current = v; },
    maxGain: (v) => { maxGainRef.current = v; },
    windowSize: (v) => { windowSizeRef.current = v; },
    trebleWindowSize: (v) => { trebleWindowSizeRef.current = v; },
    trebleFLower: (v) => { trebleFLowerRef.current = v; },
    trebleFUpper: (v) => { trebleFUpperRef.current = v; },
    trebleGainK: (v) => { trebleGainKRef.current = v; },
    smoothed: setSmoothed,
    maxSlope: (v) => { maxSlopeRef.current = v; },
  };

  const setUp = async () => {
    const presetMeasurements = await ApiClient.fetchMeasurements()
    presetMeasurements.splice(0, 0, {
      label: 'Flat',
      form: 'unknown',
      rig: 'unknown',
      source: 'unknown',
      frequency: [20.0, 20000.0],
      raw: [0.0, 0.0]
    });
    setMeasurements(presetMeasurements);
    const [targets, preferredTargets] = await ApiClient.fetchTargets();
    const targetsBassBoosts = {};
    for (const target of targets) {
      targetsBassBoosts[target.label] = cloneDeep(target.bassBoost);
      delete target.bassBoost;
    }
    targetsBassBoostsRef.current = targetsBassBoosts;
    setTargets(targets);
    setPreferredTargets(preferredTargets);
    apiClientRef.current = new ApiClient();

    document.addEventListener('click', () => {
      setUpAudioContext();
    }, { once: true });
  };
  useEffect(() => {
    setUp();
  }, []);

  const setUpAudioContext = () => {
    if (audioContextRef.current !== null) {
      return;
    }
    audioContextRef.current = new AudioContext();
    gainNodeRef.current = audioContextRef.current.createGain();
    gainNodeRef.current.gain.value = 0.5;
    preampNodeRef.current = audioContextRef.current.createGain();
    preampNodeRef.current.gain.value = 1.0;
    preampNodeRef.current.connect(audioContextRef.current.destination);
    gainNodeRef.current.connect(preampNodeRef.current);
    fsRef.current = audioContextRef.current.sampleRate;
  };

  const equalize = async (skipTimer) => {
    if (!!equalizeTimerRef.current) clearTimeout(equalizeTimerRef.current);
    if (!skipTimer) {
      equalizeTimerRef.current = setTimeout(() => { equalize(true); }, 500);
      return;
    }

    const selectedEqualizerObj = find(equalizers, (equalizer) => equalizer.label === selectedEqualizerRef.current);

    let target = find(
      targetsRef.current,
      (target) => target.label === selectedTargetRef.current);
    if (target.frequency) {
      target = { frequency: target.frequency, raw: target.raw };
    } else{
      target = target.label;
    }

    const eqParams = {
      selectedMeasurement: selectedMeasurementRef.current,
      equalizer: find(equalizersRef.current, (eq) => eq.label === selectedEqualizerRef.current),
      target: target,
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
      maxSlope: maxSlopeRef.current,
      windowSize: windowSizeRef.current,
      trebleWindowSize: trebleWindowSizeRef.current,
      trebleFLower: trebleFLowerRef.current,
      trebleFUpper: trebleFUpperRef.current,
      trebleGainK: trebleGainKRef.current,
      smoothed: smoothedRef.current
    };
    if (selectedEqualizerObj?.eqParams) {
      Object.assign(eqParams, selectedEqualizerObj.eqParams);
    }

    try {
      const res = await apiClientRef.current.equalize(eqParams, audioContextRef.current);

      if (res === undefined) {
        return;
      }

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
      throw err;
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

  const getPreferredTarget = (source, form, rig) => {
    let targetLabel = preferredTargetsRef.current[source][form];
    if (typeof(targetLabel) !== 'string') {
      // Preferred target defines rig level
      targetLabel = targetLabel[rig];
    }
    return targetLabel;
  };

  const onMeasurementSelected = (measurement) => {
    if (measurement === null) {
      setSelectedMeasurement(null);
      setGraphData(null);
      return;
    }
    const targetLabel = getPreferredTarget(measurement.source, measurement.form, measurement.rig);
    setShowInfo(false);
    setSelectedMeasurement(cloneDeep(measurement));
    setSelectedTarget(targetLabel);
    bassBoostFcRef.current = targetsBassBoostsRef.current[targetLabel].fc;
    bassBoostQRef.current = targetsBassBoostsRef.current[targetLabel].q;
    bassBoostGainRef.current = targetsBassBoostsRef.current[targetLabel].gain;
    equalize(true);
  };

  const onMeasurementCreated = (name, dataPoints) => {
    setUpAudioContext();
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
    equalize(true);
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
      selectedTarget, preferredTargets, soundSignature, soundSignatureSmoothingWindowSize,
      bassBoostGain: bassBoostGainRef.current, bassBoostFc: bassBoostFcRef.current, bassBoostQ: bassBoostQRef.current,
      trebleBoostGain: trebleBoostGainRef.current, trebleBoostFc: trebleBoostFcRef.current, trebleBoostQ: trebleBoostQRef.current,
      tilt: tiltRef.current, maxGain: maxGainRef.current, maxSlope: maxSlopeRef.current,
      windowSize: windowSizeRef.current, trebleWindowSize: trebleWindowSizeRef.current,
      trebleFLower: trebleFLowerRef.current, trebleFUpper: trebleFUpperRef.current, trebleGainK: trebleGainKRef.current
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

  const onTargetSelected = (target) => {
    const newPreferredTarget = cloneDeep(preferredTargetsRef.current);
    if (typeof(newPreferredTarget[selectedMeasurementRef.current.source][selectedMeasurementRef.current.form]) !== 'string') {
      newPreferredTarget[selectedMeasurementRef.current.source][selectedMeasurementRef.current.form][selectedMeasurementRef.current.rig] = target.label;
    } else {
      newPreferredTarget[selectedMeasurementRef.current.source][selectedMeasurementRef.current.form] = target.label;
    }
    setSelectedTarget(target.label);
    setPreferredTargets(newPreferredTarget);
    bassBoostFcRef.current = targetsBassBoostsRef.current[target.label].fc;
    bassBoostQRef.current = targetsBassBoostsRef.current[target.label].q;
    bassBoostGainRef.current = targetsBassBoostsRef.current[target.label].gain;
    equalize(true);
  };

  const onTargetCreated = (name, dataPoints) => {
    const newTargets = cloneDeep(targetsRef.current);
    const newTargetsBassBoosts = cloneDeep(targetsBassBoostsRef.current);
    const obj = transposeArrayToObject(dataPoints, ['frequency', 'raw'])
    const newTarget = {
      label: name,
      frequency: obj.frequency,
      raw: obj.raw,
      compatible: [],
      recommended: [],
      bassBoost: { fc: 105, q: 0.7, gain: 0.0 }
    };
    newTargets.push(newTarget);
    newTargetsBassBoosts[name] = { fc: 105, q: 0.7, gain: 0.0 };
    targetsBassBoostsRef.current = newTargetsBassBoosts;
    setTargets(newTargets);
    onTargetSelected(newTarget);

  };

  const onEqParamChanged = (newParams) => {
    const newTargetsBassBoosts = cloneDeep(targetsBassBoostsRef.current);
    const targetLabel = getPreferredTarget(
      selectedMeasurementRef.current.source,
      selectedMeasurementRef.current.form,
      selectedMeasurementRef.current.rig
    );
    for (const [key, val] of Object.entries(newParams)) {
      if (key === 'bassBoostFc') {
        newTargetsBassBoosts[targetLabel].fc = val;
      } else  if (key === 'bassBoostQ') {
        newTargetsBassBoosts[targetLabel].q = val;
      } else if (key === 'bassBoostGain') {
        newTargetsBassBoosts[targetLabel].gain = val;
      }
      setState[key](val);
    }
    targetsBassBoostsRef.current = newTargetsBassBoosts;
    equalize();
  };

  const onEqualizerSelected = (val) => {
    if (val === null) {
      selectedEqualizerRef.current = null;
      setSelectedEqualizer(null);
    } else {
      selectedEqualizerRef.current = val;
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
    setEqualizers(equalizers);
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

  return (
    <Box sx={{pt: 0, pb: {xs: 10.25, sm: 14}, background: '#2c2424', minHeight: '100vh', boxSizing: 'border-box'}}>
      <Waves nWaves={10} />

      <Box sx={{padding: [1, 1.5]}}>
        <TopBar
          onShowInfoClicked={() => setShowInfo(!showInfo)}
          selectedMeasurement={selectedMeasurement}
          isMeasurementSelected={!!selectedMeasurement}
          measurements={measurements}
          onMeasurementSelected={onMeasurementSelected}
          onMeasurementCreated={onMeasurementCreated}
          onError={onError}
          showLogo={!showInfo && graphData}
        />
      </Box>

      <Container fixed sx={{ pl: {xs: '1px', sm: 1, md: 3}, pr: {xs: '1px', sm: 1, md: 3}, }} maxWidth='xxl'>
        <Grid
          container direction='row' alignItems='stretch'
          columnSpacing={{xs: 0.5, sm: 1, md: 2}} rowSpacing={{xs: 0.5, sm: 1, md: 2}}
        >

          <Grid item xs={12} xxl={6} sx={{display: !!graphData && !showInfo ? 'block' : 'none'}} order={{ xxl: 1}}>
            <SmPaper sx={{ pt: 1, pl: {xs: 1, sm: 0, md: 0}, pr: {xs: 0, sm: 1, md: 0}, pb: {xs: 1, sm: 0.5, md: 0} }}>
              <FrequencyResponseGraph
                data={graphData}
                smoothed={smoothed}
                onSmoothedChanged={onSmoothedChanged}
              />
            </SmPaper>
          </Grid>

          <Grid item xs={12} md={6} xxl={3} sx={{display: !!graphData && !showInfo ? 'block' : 'none'}} order={{ xxl: 0}}>
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

                targets={targets}
                selectedTarget={selectedTarget}
                onTargetSelected={onTargetSelected}
                onTargetCreated={onTargetCreated}

                soundSignature={soundSignature}
                soundSignatureSmoothingWindowSize={soundSignatureSmoothingWindowSize}

                graphData={graphData}
                smoothed={smoothed}

                bassBoostGain={bassBoostGainRef.current}
                bassBoostFc={bassBoostFcRef.current}
                bassBoostQ={bassBoostQRef.current}
                trebleBoostGain={trebleBoostGainRef.current}
                trebleBoostFc={trebleBoostFcRef.current}
                trebleBoostQ={trebleBoostQRef.current}
                tilt={tiltRef.current}
                maxGain={maxGainRef.current}
                windowSize={windowSizeRef.current}
                trebleWindowSize={trebleWindowSizeRef.current}
                trebleFLower={trebleFLowerRef.current}
                trebleFUpper={trebleFUpperRef.current}
                trebleGainK={trebleGainKRef.current}
                maxSlope={maxSlopeRef.current}

                onEqParamChanged={onEqParamChanged}
                onError={onError}
              />
            </SmPaper>
          </Grid>

          <Grid item xs={12} md={6} xxl={3} sx={{display: !!graphData && !showInfo ? 'block' : 'none'}} order={{ xxl: 2}}>
            <SmPaper sx={{p: {sm: 1, md: 2}}}>
              <EqTab
                audioContext={audioContextRef.current}
                selectedMeasurement={selectedMeasurement?.label}
                equalizers={equalizers}
                selectedEqualizer={selectedEqualizer}
                onEqualizerSelected={onEqualizerSelected}
                graphicEq={graphicEq}
                parametricEq={parametricEq}
                fixedBandEq={fixedBandEq}
                firAudioBuffer={firAudioBuffer}
                fs={fsRef.current}
                bitDepth={bitDepthRef.current}
                phase={phaseRef.current}
                fRes={fResRef.current}
                preamp={preampRef.current}
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

      <Box sx={{color: theme => theme.palette.grey.A400, display: (!!showInfo || !graphData) ? 'block' : 'none'}}>
        <InfoPage
          canClose={!!graphData}
          onCloseClick={() => { setShowInfo(false); }}
        />
      </Box>

      <Box sx={{ position: 'fixed', bottom: {xs: 0, sm: 8}, left: 0, right: 0 }}>
        <Container fixed maxWidth='sm' sx={{padding: '0 !important'}}>
          <Player
            audioContext={audioContextRef.current}
            audioDestination={gainNodeRef.current}
            onGainChange={onGainChange}
            onIsEqOnChange={onIsEqOnChange}
            isEqEnabled={eqNodesRef.current.length > 0 && selectedEqualizer !== null}
          />
        </Container>
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
