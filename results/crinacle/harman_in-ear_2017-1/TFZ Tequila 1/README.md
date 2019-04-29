# TFZ Tequila 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.4; 25 -7.8; 28 -8.4; 31 -8.8; 34 -9.1; 37 -9.4; 41 -9.7; 45 -9.9; 49 -10.2; 54 -10.5; 60 -10.8; 66 -11.1; 72 -11.4; 79 -11.7; 87 -12.0; 96 -12.4; 106 -12.6; 116 -12.7; 128 -12.9; 141 -12.9; 155 -12.9; 170 -12.7; 187 -12.6; 206 -12.3; 227 -12.0; 249 -11.6; 274 -11.2; 302 -10.6; 332 -10.0; 365 -9.4; 402 -8.9; 442 -8.3; 486 -7.7; 535 -7.1; 588 -6.5; 647 -6.0; 712 -5.3; 783 -4.7; 861 -4.3; 947 -3.8; 1042 -4.0; 1146 -4.5; 1261 -4.9; 1387 -5.0; 1526 -4.5; 1678 -4.3; 1846 -4.1; 2031 -3.7; 2234 -3.2; 2457 -2.7; 2703 -2.1; 2973 -1.3; 3270 -0.6; 3597 -0.5; 3957 -1.1; 4353 -2.6; 4788 -5.2; 5267 -7.2; 5793 -4.9; 6373 -1.6; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.4; 13660 -13.2; 15026 -17.4; 16529 -16.8; 18182 -15.0; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Tequila 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Tequila 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 95 Hz    | 0.46 | -5.2 dB  |
| Peaking | 220 Hz   | 0.86 | -3.2 dB  |
| Peaking | 5378 Hz  | 0.25 | 5.7 dB   |
| Peaking | 12226 Hz | 1.69 | 9.0 dB   |
| Peaking | 14834 Hz | 0.57 | -16.7 dB |
| Peaking | 916 Hz   | 1.38 | 3.4 dB   |
| Peaking | 1230 Hz  | 0.63 | -2.5 dB  |
| Peaking | 3669 Hz  | 1.81 | 3.2 dB   |
| Peaking | 5228 Hz  | 3.13 | -5.1 dB  |
| Peaking | 6407 Hz  | 6.48 | 4.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -13.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%20Tequila%201/TFZ%20Tequila%201.png)