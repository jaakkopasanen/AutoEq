# qdc Anole VX Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.8; 25 -11.1; 28 -11.4; 31 -11.6; 34 -11.7; 37 -11.8; 41 -12.0; 45 -12.1; 49 -12.3; 54 -12.4; 60 -12.5; 66 -12.6; 72 -12.8; 79 -12.9; 87 -13.1; 96 -13.2; 106 -13.3; 116 -13.4; 128 -13.3; 141 -13.2; 155 -13.0; 170 -12.7; 187 -12.4; 206 -12.1; 227 -11.6; 249 -11.1; 274 -10.7; 302 -10.1; 332 -9.5; 365 -8.9; 402 -8.4; 442 -8.0; 486 -7.6; 535 -7.2; 588 -7.0; 647 -6.9; 712 -6.8; 783 -6.8; 861 -7.0; 947 -7.2; 1042 -7.7; 1146 -8.2; 1261 -8.4; 1387 -8.0; 1526 -7.1; 1678 -6.2; 1846 -5.2; 2031 -4.1; 2234 -2.9; 2457 -1.4; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.6; 4353 -3.0; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -3.9; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.5; 15026 -22.4; 16529 -26.7; 18182 -24.8; 20000 -17.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole VX Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole VX Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.45 | -3.9 dB  |
| Peaking | 137 Hz   | 0.49 | -5.9 dB  |
| Peaking | 4580 Hz  | 0.71 | 9.5 dB   |
| Peaking | 12214 Hz | 1.2  | 14.1 dB  |
| Peaking | 16410 Hz | 0.45 | -25.0 dB |
| Peaking | 1200 Hz  | 3.74 | -2.0 dB  |
| Peaking | 1496 Hz  | 2.77 | -1.8 dB  |
| Peaking | 2683 Hz  | 2.56 | 2.5 dB   |
| Peaking | 4307 Hz  | 6.63 | -3.2 dB  |
| Peaking | 5702 Hz  | 7.03 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -22.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20VX%20Bass/qdc%20Anole%20VX%20Bass.png)