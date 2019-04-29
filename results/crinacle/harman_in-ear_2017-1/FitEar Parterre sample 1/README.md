# FitEar Parterre sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.5; 25 -12.4; 28 -12.4; 31 -12.4; 34 -12.5; 37 -12.5; 41 -12.6; 45 -12.7; 49 -12.8; 54 -12.9; 60 -13.1; 66 -13.3; 72 -13.6; 79 -13.8; 87 -14.1; 96 -14.4; 106 -14.6; 116 -14.8; 128 -15.0; 141 -15.1; 155 -15.1; 170 -15.1; 187 -15.0; 206 -14.7; 227 -14.4; 249 -14.1; 274 -13.7; 302 -13.2; 332 -12.6; 365 -12.0; 402 -11.4; 442 -10.8; 486 -10.2; 535 -9.4; 588 -8.6; 647 -7.8; 712 -6.9; 783 -5.9; 861 -5.1; 947 -4.5; 1042 -4.2; 1146 -4.2; 1261 -4.0; 1387 -3.4; 1526 -2.4; 1678 -1.5; 1846 -0.8; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -5.5; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.8; 15026 -20.8; 16529 -17.2; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Parterre sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Parterre sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.16 | -5.4 dB  |
| Peaking | 194 Hz   | 0.44 | -7.7 dB  |
| Peaking | 2378 Hz  | 0.52 | 6.4 dB   |
| Peaking | 5447 Hz  | 2.56 | 3.6 dB   |
| Peaking | 15544 Hz | 2.63 | -16.9 dB |
| Peaking | 871 Hz   | 5.38 | 1.0 dB   |
| Peaking | 6049 Hz  | 3.18 | 1.5 dB   |
| Peaking | 7442 Hz  | 4.6  | -3.6 dB  |
| Peaking | 12906 Hz | 3.57 | 3.6 dB   |
| Peaking | 14272 Hz | 5.78 | -4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -7.0 dB  |
| Peaking | 250 Hz   | 1.41 | -6.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -12.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20Parterre%20sample%201/FitEar%20Parterre%20sample%201.png)