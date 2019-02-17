# NuForce Stride
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.7; 25 -7.1; 28 -7.5; 31 -7.9; 34 -8.3; 37 -8.6; 41 -8.9; 45 -9.1; 49 -9.4; 54 -9.7; 60 -9.9; 66 -10.2; 72 -10.5; 79 -10.8; 87 -11.0; 96 -11.3; 106 -11.5; 116 -11.6; 128 -11.6; 141 -11.5; 155 -11.1; 170 -10.5; 187 -10.6; 206 -11.4; 227 -11.1; 249 -10.7; 274 -10.1; 302 -9.5; 332 -8.8; 365 -8.1; 402 -7.5; 442 -6.9; 486 -6.3; 535 -5.6; 588 -5.0; 647 -4.3; 712 -3.7; 783 -3.1; 861 -2.7; 947 -2.6; 1042 -2.7; 1146 -3.0; 1261 -3.0; 1387 -2.7; 1526 -2.3; 1678 -1.8; 1846 -1.4; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -1.4; 2973 -2.7; 3270 -4.3; 3597 -5.1; 3957 -5.4; 4353 -5.6; 4788 -6.3; 5267 -8.1; 5793 -10.1; 6373 -7.9; 7010 -3.5; 7711 -2.4; 8482 -2.7; 9330 -6.6; 10263 -9.2; 11289 -8.3; 12418 -10.3; 13660 -18.8; 15026 -25.7; 16529 -24.5; 18182 -19.5; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce Stride GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce Stride ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.46 | -4.8 dB  |
| Peaking | 119 Hz   | 0.71 | -5.7 dB  |
| Peaking | 274 Hz   | 1.02 | -5.2 dB  |
| Peaking | 5620 Hz  | 5.64 | -5.6 dB  |
| Peaking | 16392 Hz | 0.99 | -24.9 dB |
| Peaking | 2512 Hz  | 1.37 | 5.6 dB   |
| Peaking | 3290 Hz  | 1.1  | -4.2 dB  |
| Peaking | 7396 Hz  | 6.67 | 3.6 dB   |
| Peaking | 8447 Hz  | 4.31 | 4.5 dB   |
| Peaking | 20057 Hz | 0.82 | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -7.1 dB  |
| Peaking | 250 Hz   | 1.41 | -6.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 16000 Hz | 1.41 | -31.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/NuForce%20Stride/NuForce%20Stride.png)