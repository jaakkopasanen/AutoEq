# FitEar Private 222
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.7; 25 -4.9; 28 -5.1; 31 -5.3; 34 -5.4; 37 -5.6; 41 -5.8; 45 -5.9; 49 -6.1; 54 -6.3; 60 -6.5; 66 -6.8; 72 -7.2; 79 -7.5; 87 -7.9; 96 -8.3; 106 -8.7; 116 -9.0; 128 -9.3; 141 -9.5; 155 -9.7; 170 -9.8; 187 -9.9; 206 -9.8; 227 -9.7; 249 -9.6; 274 -9.4; 302 -9.0; 332 -8.7; 365 -8.2; 402 -7.8; 442 -7.4; 486 -6.9; 535 -6.5; 588 -5.9; 647 -5.4; 712 -4.8; 783 -4.2; 861 -3.8; 947 -3.6; 1042 -3.7; 1146 -4.2; 1261 -4.5; 1387 -4.6; 1526 -4.4; 1678 -4.3; 1846 -4.6; 2031 -5.1; 2234 -4.8; 2457 -3.1; 2703 -1.3; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -2.2; 4353 -3.4; 4788 -5.4; 5267 -8.6; 5793 -10.4; 6373 -8.2; 7010 -3.8; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Private 222 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Private 222 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 195 Hz  |  0.57 | -4.5 dB |
| Peaking | 898 Hz  |  1.56 | 2.5 dB  |
| Peaking | 3299 Hz |  1.78 | 5.6 dB  |
| Peaking | 5734 Hz |  3.76 | -6.3 dB |
| Peaking | 7008 Hz |  8.02 | 2.8 dB  |
| Peaking | 21 Hz   |  1    | 1.3 dB  |
| Peaking | 2212 Hz |  4.54 | -2.5 dB |
| Peaking | 2284 Hz |  2.32 | 1.3 dB  |
| Peaking | 4455 Hz | 10.5  | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20Private%20222/FitEar%20Private%20222.png)