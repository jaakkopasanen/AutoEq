# qdc Anole VX All
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.8; 25 -10.0; 28 -10.4; 31 -10.6; 34 -10.7; 37 -10.9; 41 -11.0; 45 -11.2; 49 -11.4; 54 -11.5; 60 -11.7; 66 -11.8; 72 -12.0; 79 -12.1; 87 -12.3; 96 -12.4; 106 -12.5; 116 -12.6; 128 -12.6; 141 -12.4; 155 -12.2; 170 -12.0; 187 -11.6; 206 -11.3; 227 -10.9; 249 -10.4; 274 -9.9; 302 -9.3; 332 -8.8; 365 -8.1; 402 -7.7; 442 -7.3; 486 -6.9; 535 -6.7; 588 -6.5; 647 -6.6; 712 -6.8; 783 -7.1; 861 -7.7; 947 -8.4; 1042 -9.1; 1146 -9.7; 1261 -9.6; 1387 -8.9; 1526 -7.8; 1678 -6.7; 1846 -5.6; 2031 -4.5; 2234 -3.4; 2457 -2.1; 2703 -1.0; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -1.8; 4353 -3.5; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -4.2; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.2; 13660 -16.8; 15026 -25.0; 16529 -27.0; 18182 -23.3; 20000 -16.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole VX All GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole VX All ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.41 | -4.6 dB  |
| Peaking | 156 Hz   | 0.94 | -3.7 dB  |
| Peaking | 3815 Hz  | 0.65 | 11.8 dB  |
| Peaking | 12091 Hz | 0.43 | 28.4 dB  |
| Peaking | 15342 Hz | 0.28 | -41.6 dB |
| Peaking | 624 Hz   | 1.79 | 1.7 dB   |
| Peaking | 1228 Hz  | 2.22 | -2.8 dB  |
| Peaking | 2560 Hz  | 2.47 | 1.6 dB   |
| Peaking | 4269 Hz  | 5.66 | -3.5 dB  |
| Peaking | 5545 Hz  | 5.73 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 16000 Hz | 1.41 | -24.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20VX%20All/qdc%20Anole%20VX%20All.png)