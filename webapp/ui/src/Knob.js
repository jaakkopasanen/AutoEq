import React, {useEffect, useRef, useState} from 'react';
import {Box, TextField, Tooltip, Typography, useMediaQuery} from '@mui/material';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import {useTheme} from '@emotion/react';

const Knob = (props) => {
  const angleOffset = 45;
  const [value, setValue] = useState(props.formatter(props.initialValue));

  const newFloatValue = (e) => {
    const clientX = e.clientX || e.touches[0].clientX;
    const clientY = e.clientY || e.touches[0].clientY;
    const cx = elRef.current.getBoundingClientRect().x + parseFloat(props.size) / 2;
    const cy = elRef.current.getBoundingClientRect().y + parseFloat(props.size) / 2;
    // atan2 returns angle from center right with angle increasing counter clockwise
    // transform the angle to be relative to bottom center and clockwise
    const angle = (270 - Math.atan2(cy - clientY, clientX - cx) * 180 / Math.PI) % 360;
    let val = props.minValue + (angle - angleOffset) / (360 - 2 * angleOffset) * (props.maxValue - props.minValue)  // Value from angle
    if (props.step) {
      let v = props.minValue;
      let closest = null;
      while (v < props.maxValue + props.step) {
        if (closest === null || Math.abs(val - v) < Math.abs(val - closest)) {
          closest = v;
        }
        v += props.step;
      }
      return closest;
    }
    return Math.min(props.maxValue, Math.max(props.minValue, val));  // Clip between min and max values
  };

  const update = (e) => {
    const newVal = newFloatValue(e);
    setValue(props.formatter(newVal));
    if (props.onChange) {
      props.onChange(newVal);
    }
  }

  const onPointerDown = (e) => {
    e.preventDefault();
    update(e);
    const moveHandler = (e) => { update(e); };
    if (e.type === 'mousedown') {
      document.addEventListener('mousemove', moveHandler);
      document.addEventListener('mouseup', (e) => {
        document.removeEventListener('mousemove', moveHandler);
      });
    } else if (e.type === 'touchstart') {
      document.addEventListener('touchmove', moveHandler);
      document.addEventListener('touchend', (e) => {
        document.removeEventListener('touchmove', moveHandler);
      });
    }
  };

  const handleChange = (e) => {
    setValue(e.target.value);
    if (props.onChange) {
      props.onChange(parseFloat(e.target.value));
    }
  };

  useEffect(() => {
    if (props.initialValue !== value) {
      setValue(props.formatter(props.initialValue));
    }
  }, [props.initialValue]);

  const elRef = useRef();
  const theme = useTheme();
  const isXs = useMediaQuery(theme.breakpoints.down('sm'));

  // Calculate angle of the cursor
  const floatValue = value === null || value === undefined ? props.minValue : parseFloat(value);
  const clippedValue = Math.min(props.maxValue, Math.max(props.minValue, floatValue));
  const angle = angleOffset + (clippedValue - props.minValue) / (props.maxValue - props.minValue) * (360 - 2 * angleOffset);

  // Generate ticks
  const ticks = [];
  if (props.tickStep) {
    for (let val = props.minValue; val < props.maxValue + props.tickStep * 0.5; val += props.tickStep) {
      ticks.push(angleOffset + (val - props.minValue) / (props.maxValue - props.minValue) * (360 - 2 * angleOffset));
    }
  } else {
    const nTicks = props.nTicks || 8;
    for (let i = 0; i < nTicks; ++i) {
      const val = props.minValue + i * (props.maxValue - props.minValue) / (nTicks - 1);
      ticks.push(angleOffset + (val - props.minValue) / (props.maxValue - props.minValue) * (360 - 2 * angleOffset));
    }
  }

  return (
    <Box
      sx={{
        width: props.size,
        textAlign: 'center',
        margin: 'auto'
      }}
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
            background: '#666',
            borderRadius: '1px',
            transformOrigin: `50% -${parseFloat(props.size) / 2 - 10}px`
          }} />
        ))}
        <Box
          sx={{
            width: '100%', height: '100%',
            borderRadius: '50%',
            border: theme => `2px solid ${theme.palette.primary.main}`,
            boxSizing: 'border-box'
          }}
          onMouseDown={onPointerDown} onTouchStart={onPointerDown}
        />
        <Box sx={{
          position: 'absolute',
          bottom: '20px', left: '50%',
          width: '6px', height: '6px',
          background: theme => theme.palette.primary.main,
          borderRadius: '3px',
          transform: `translate(-50%) rotate(${angle}deg)`,
          transformOrigin: `50% -${parseFloat(props.size) / 2 - 26}px`
        }} />
        <Box
          sx={{
            position: 'absolute',
            top: isXs ? '50%' : '45%',
            left: '50%',
            transform: props.unit ? 'translate(-50%, -14px)' : 'translate(-50%, -7px)',
            textAlign: 'center',
          }}
        >
          {/*TODO: Use text only on mobile*/}
          {isXs && (
            <Typography sx={{lineHeight: 1}}>{value}</Typography>
          )}
          {!isXs && (
            <TextField
              variant='standard'
              value={value}
              size='small'
              inputProps={{
                style: { textAlign: 'center' }
              }}
              onChange={handleChange}
            />
          )}
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
      {props.label && props.tooltip && (
        <Tooltip
          title={props.tooltip}
          disableFocusListener
          enterTouchDelay={0} leaveTouchDelay={0}
          placement='top'
        >
          <Typography variant='caption' sx={{lineHeight: 1}}>
            {props.label}
            <InfoOutlinedIcon sx={{width: 16, height: 16, verticalAlign: 'middle'}} />
          </Typography>
        </Tooltip>
      )}
      {props.label && !props.tooltip && (
        <Typography variant='caption' sx={{lineHeight: 1}}>{props.label}</Typography>
      )}
    </Box>
  );
};

export default Knob;
