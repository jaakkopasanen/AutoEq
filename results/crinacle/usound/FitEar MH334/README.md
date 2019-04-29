# FitEar MH334
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.2; 28 -4.7; 31 -5.0; 34 -5.3; 37 -5.6; 41 -5.9; 45 -6.1; 49 -6.4; 54 -6.7; 60 -7.0; 66 -7.4; 72 -7.7; 79 -8.1; 87 -8.5; 96 -9.0; 106 -9.4; 116 -9.8; 128 -10.1; 141 -10.4; 155 -10.7; 170 -10.8; 187 -10.9; 206 -10.9; 227 -10.8; 249 -10.8; 274 -10.6; 302 -10.4; 332 -10.2; 365 -9.9; 402 -9.7; 442 -9.4; 486 -9.0; 535 -8.6; 588 -8.1; 647 -7.6; 712 -7.1; 783 -6.5; 861 -5.9; 947 -5.6; 1042 -5.7; 1146 -6.3; 1261 -6.9; 1387 -7.4; 1526 -7.3; 1678 -6.8; 1846 -5.9; 2031 -4.9; 2234 -4.4; 2457 -4.2; 2703 -3.2; 2973 -2.3; 3270 -1.9; 3597 -1.7; 3957 -2.0; 4353 -0.8; 4788 -0.5; 5267 -3.5; 5793 -3.4; 6373 -1.2; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar MH334 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar MH334 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.28 | 3.4 dB  |
| Peaking | 236 Hz  | 0.36 | -4.9 dB |
| Peaking | 1349 Hz | 0.59 | 4.1 dB  |
| Peaking | 1503 Hz | 1.68 | -4.7 dB |
| Peaking | 4330 Hz | 1.19 | 4.7 dB  |
| Peaking | 3036 Hz | 7.48 | 0.7 dB  |
| Peaking | 5523 Hz | 8.93 | -2.1 dB |
| Peaking | 6469 Hz | 4.46 | 4.1 dB  |
| Peaking | 7692 Hz | 1.9  | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20MH334/FitEar%20MH334.png)