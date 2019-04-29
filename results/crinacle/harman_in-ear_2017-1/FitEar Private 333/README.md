# FitEar Private 333
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -2.7; 25 -2.8; 28 -3.1; 31 -3.2; 34 -3.4; 37 -3.6; 41 -3.7; 45 -3.9; 49 -4.1; 54 -4.3; 60 -4.6; 66 -4.9; 72 -5.3; 79 -5.6; 87 -6.0; 96 -6.5; 106 -6.9; 116 -7.3; 128 -7.6; 141 -7.9; 155 -8.1; 170 -8.3; 187 -8.3; 206 -8.4; 227 -8.4; 249 -8.3; 274 -8.2; 302 -8.0; 332 -7.6; 365 -7.3; 402 -7.1; 442 -6.8; 486 -6.4; 535 -6.0; 588 -5.6; 647 -5.2; 712 -4.7; 783 -4.2; 861 -3.9; 947 -3.8; 1042 -4.0; 1146 -4.5; 1261 -4.9; 1387 -4.9; 1526 -4.6; 1678 -4.2; 1846 -3.9; 2031 -3.6; 2234 -3.5; 2457 -3.2; 2703 -1.9; 2973 -0.7; 3270 -0.5; 3597 -1.0; 3957 -1.5; 4353 -2.8; 4788 -5.5; 5267 -7.6; 5793 -8.4; 6373 -9.5; 7010 -5.0; 7711 -5.1; 8482 -5.3; 9330 -6.0; 10263 -7.4; 11289 -5.4; 12418 -5.4; 13660 -9.2; 15026 -16.7; 16529 -14.2; 18182 -6.6; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Private 333 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Private 333 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.4  | 2.9 dB   |
| Peaking | 194 Hz   | 0.73 | -3.4 dB  |
| Peaking | 4299 Hz  | 0.76 | 7.2 dB   |
| Peaking | 5631 Hz  | 1.88 | -9.4 dB  |
| Peaking | 15516 Hz | 2.24 | -13.1 dB |
| Peaking | 861 Hz   | 3.45 | 1.6 dB   |
| Peaking | 7324 Hz  | 8.09 | 2.3 dB   |
| Peaking | 11852 Hz | 0.99 | -2.2 dB  |
| Peaking | 12486 Hz | 2.89 | 4.8 dB   |
| Peaking | 16866 Hz | 7.61 | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB   |
| Peaking | 62 Hz    | 1.41 | 0.7 dB   |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -10.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20Private%20333/FitEar%20Private%20333.png)