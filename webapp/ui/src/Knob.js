import React, {useRef, useState} from 'react';
import {Box, Typography} from '@mui/material';

const Knob = (props) => {
  const angleOffset = 45;
  const [isMouseDown, setIsMouseDown] = useState(false);

  const newValue = (e) => {
    const cx = elRef.current.getBoundingClientRect().x + parseFloat(props.size) / 2;
    const cy = elRef.current.getBoundingClientRect().y + parseFloat(props.size) / 2;
    // atan2 returns angle from center right with angle increasing counter clockwise
    // transform the angle to be relative to bottom center and clockwise
    const angle = (270 - Math.atan2(cy - e.clientY, e.clientX - cx) * 180 / Math.PI) % 360;
    let value = props.minValue + (angle - angleOffset) / (360 - 2 * angleOffset) * (props.maxValue - props.minValue)  // Value from angle
    if (props.step) {
      let v = props.minValue;
      let closest = null;
      while (v < props.maxValue + props.step) {
        if (closest === null || Math.abs(value - v) < Math.abs(value - closest)) {
          closest = v;
        }
        v += props.step;
      }
      return closest;
    }
    return Math.min(props.maxValue, Math.max(props.minValue, value));  // Clip between min and max values
  };

  const onMouseDown = (e) => {
    setIsMouseDown(true);
    if (props.onChange) {
      props.onChange(newValue(e));
    }
  };

  const onMouseUp = () => {
    setIsMouseDown(false);
  };

  const onMouseMove = (e) => {
    if (isMouseDown && props.onChange) {
      props.onChange(newValue(e));
    }
  };

  const elRef = useRef();

  const angle = angleOffset + (props.value - props.minValue) / (props.maxValue - props.minValue) * (360 - 2 * angleOffset);
  const ticks = [];
  const nTicks = props.nTicks || 8;
  for (let i = 0; i < nTicks; ++i) {
    const value = props.minValue + i * (props.maxValue - props.minValue) / (nTicks - 1);
    ticks.push(angleOffset + (value - props.minValue) / (props.maxValue - props.minValue) * (360 - 2 * angleOffset));
  }
  return (
    <Box
      sx={{
        width: props.size,
        textAlign: 'center',
        margin: 'auto'
      }}
      onMouseDown={onMouseDown}
      onMouseUp={onMouseUp}
      onMouseMove={onMouseMove}
      ref={elRef}
    >
      <Box sx={{
        position: 'relative',
        width: props.size,
        height: props.size,
        padding: '12px',
        boxSizing: 'border-box',
        marginBottom: '-6px'
      }}>
        {ticks.map(a => (
          <Box key={a} sx={{
            position: 'absolute', bottom: 0, left: '50%',
            transform: `translate(-50%) rotate(${a}deg)`,
            width: '2px', height: '10px',
            background: theme => theme.palette.grey.A400,
            borderRadius: '1px',
            transformOrigin: `50% -${parseFloat(props.size) / 2 - 10}px`
          }} />
        ))}
        <Box
          sx={{
            width: '100%', height: '100%',
            borderRadius: '50%',
            border: theme => `1px solid ${theme.palette.primary.main}`,
            boxSizing: 'border-box'
          }}
        />
        <Box sx={{
          position: 'absolute',
          bottom: '18px', left: '50%',
          width: '6px', height: '6px',
          background: theme => theme.palette.primary.main,
          borderRadius: '3px',
          transform: `translate(-50%) rotate(${angle}deg)`,
          transformOrigin: `50% -${parseFloat(props.size) / 2 - 24}px`
        }} />
        <Box
          sx={{
            position: 'absolute',
            top: '50%', left: '50%',
            transform: props.unit ? 'translate(-50%, -14px)' : 'translate(-50%, -7px)',
            textAlign: 'center',
          }}
        >
          <Typography sx={{lineHeight: 1}}>{props.formattedValue}</Typography>
          {props.unit && <Typography variant='caption'>{props.unit}</Typography>}
        </Box>
        {'icon' in props && (
          <Box
            sx={{
              position: 'absolute',
              bottom: '2px', left: '50%',
              width: '16px', height: '16px',
              transform: 'translate(-50%)',
              border: theme => `1px solid ${theme.palette.grey.A400}`,
              borderRadius: '4px',
              background: theme => theme.palette.background.default,
              padding: '1px 3px',
            }}
          >
            <props.icon sx={{color: theme => theme.palette.primary.light, width: 16, height: 16}} />
          </Box>
        )}
      </Box>
      {props.label && <Typography variant='caption' sx={{lineHeight: 1}}>{props.label}</Typography>}
    </Box>
  );
};

export default Knob;
