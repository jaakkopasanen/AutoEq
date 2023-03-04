import React, {useEffect, useState} from 'react';

const Waves = (props) => {
  const [paths, setPaths] = useState(null);

  const sine = (wavelength, amplitude, y) => {
    const cx = (8 / 3 - Math.sqrt(3)) * wavelength / 2;  // Control point X coordinate
    const cy = 2 * Math.sqrt(3) * amplitude / 6;  // Control point Y coordinate
    return `M 0 ${y} c ${cx} ${-cy}, ${wavelength - cx} ${cy}, ${wavelength} 0 c ${cx} ${-cy}, ${wavelength - cx} ${cy}, ${wavelength} 0 v 100 h ${-2*wavelength} Z`
  };

  const createPaths = () => {
    const alpha = 1.0;
    const palette = [
      `rgba(255, 91, 61, ${alpha})`,
      `rgba(37, 31, 27, ${alpha})`,
      `rgba(20, 104, 153, ${alpha})`,
      `rgba(222, 212, 0, ${alpha})`,
      `rgba(153, 131, 0, ${alpha})`,
      `rgba(247, 217, 203, ${alpha})`,
    ];
    const paths = [];
    for (let i = 0; i < props.nWaves; ++i) {
      const swellDuration = 12 + ((i / props.nWaves * 1.5)**2 - 3 * i / props.nWaves) * 6;
      const swellDelay = -props.nWaves + i * 0.3
      const waveDuration = 15;
      const waveDelay = ((i / props.nWaves * 1.5)**2 - 3 * i / props.nWaves) * 6;
      paths.push(
        <svg key={i} style={{animation: `swell ${swellDuration}s ease ${swellDelay}s infinite`}}>
          <path
            d={`${sine(100, 100, 50 + i * 7)}`}
            fill={palette[i % palette.length]}
            //stroke={palette[i % palette.length]} fill='transparent'
            style={{
              animation: `wave ${waveDuration}s cubic-bezier( 0.36, 0.45, 0.63, 0.53) ${waveDelay}s infinite`
            }}
          />
        </svg>
      );
    }
    return paths;
  };

  useEffect(() => {
    const paths = createPaths();
    setPaths(paths);
  }, [props.nWaves]);

  return (
    <svg
      width='100%' viewBox='0 0 100 100'
      preserveAspectRatio='none'
      style={{
        position: 'fixed', bottom: 0, left: 0, right: 0, height: '300px', maxHeight: '40vw'
      }}
    >
      {paths}
    </svg>
  );
};

export default Waves;
