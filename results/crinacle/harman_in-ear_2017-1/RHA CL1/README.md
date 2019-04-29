# RHA CL1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.2; 25 -3.4; 28 -3.5; 31 -3.7; 34 -3.7; 37 -3.8; 41 -3.9; 45 -4.1; 49 -4.1; 54 -4.2; 60 -4.3; 66 -4.5; 72 -4.8; 79 -5.1; 87 -5.3; 96 -5.7; 106 -6.0; 116 -6.3; 128 -6.6; 141 -6.8; 155 -7.0; 170 -7.1; 187 -7.2; 206 -7.2; 227 -7.2; 249 -7.1; 274 -7.0; 302 -6.8; 332 -6.5; 365 -6.2; 402 -5.9; 442 -5.6; 486 -5.2; 535 -4.8; 588 -4.3; 647 -3.8; 712 -3.2; 783 -2.6; 861 -2.1; 947 -1.8; 1042 -1.8; 1146 -2.1; 1261 -2.1; 1387 -1.9; 1526 -1.5; 1678 -1.0; 1846 -0.7; 2031 -0.5; 2234 -0.6; 2457 -1.3; 2703 -2.4; 2973 -2.8; 3270 -2.1; 3597 -1.6; 3957 -1.9; 4353 -3.4; 4788 -7.4; 5267 -12.0; 5793 -8.9; 6373 -5.8; 7010 -6.1; 7711 -11.1; 8482 -13.2; 9330 -11.8; 10263 -12.4; 11289 -13.5; 12418 -16.1; 13660 -26.3; 15026 -36.6; 16529 -37.6; 18182 -33.8; 20000 -30.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA CL1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA CL1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 5265 Hz  | 5.54 | -8.8 dB  |
| Peaking | 7499 Hz  | 0.19 | 5.7 dB   |
| Peaking | 7933 Hz  | 0.2  | 7.0 dB   |
| Peaking | 15662 Hz | 0.54 | -37.8 dB |
| Peaking | 19083 Hz | 0.6  | -13.2 dB |
| Peaking | 15 Hz    | 0.31 | 1.9 dB   |
| Peaking | 199 Hz   | 0.8  | -2.7 dB  |
| Peaking | 2850 Hz  | 7.58 | -1.8 dB  |
| Peaking | 8236 Hz  | 7.18 | -4.7 dB  |
| Peaking | 11876 Hz | 4.66 | 4.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB   |
| Peaking | 62 Hz    | 1.41 | 0.7 dB   |
| Peaking | 125 Hz   | 1.41 | -1.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 16000 Hz | 1.41 | -47.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/RHA%20CL1/RHA%20CL1.png)