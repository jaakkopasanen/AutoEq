# FitEar Private 222
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.3; 25 -1.5; 28 -1.7; 31 -1.9; 34 -2.0; 37 -2.1; 41 -2.3; 45 -2.5; 49 -2.7; 54 -2.9; 60 -3.1; 66 -3.4; 72 -3.7; 79 -4.1; 87 -4.5; 96 -4.9; 106 -5.3; 116 -5.6; 128 -5.8; 141 -6.1; 155 -6.3; 170 -6.4; 187 -6.5; 206 -6.4; 227 -6.3; 249 -6.1; 274 -6.0; 302 -5.7; 332 -5.4; 365 -5.1; 402 -4.7; 442 -4.3; 486 -3.9; 535 -3.5; 588 -3.0; 647 -2.5; 712 -1.9; 783 -1.3; 861 -0.8; 947 -0.5; 1042 -0.6; 1146 -1.1; 1261 -1.7; 1387 -2.1; 1526 -2.2; 1678 -2.1; 1846 -2.5; 2031 -3.3; 2234 -3.6; 2457 -2.5; 2703 -1.1; 2973 -0.5; 3270 -0.5; 3597 -0.9; 3957 -1.5; 4353 -2.3; 4788 -3.9; 5267 -7.2; 5793 -9.2; 6373 -7.4; 7010 -2.6; 7711 -3.0; 8482 -3.3; 9330 -3.3; 10263 -3.3; 11289 -3.3; 12418 -3.3; 13660 -3.3; 15026 -3.3; 16529 -3.3; 18182 -3.3; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Private 222 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Private 222 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.22 | 2.2 dB  |
| Peaking | 183 Hz  |  0.54 | -3.5 dB |
| Peaking | 921 Hz  |  1.45 | 3.2 dB  |
| Peaking | 3391 Hz |  2.11 | 3.2 dB  |
| Peaking | 5742 Hz |  4.55 | -7.0 dB |
| Peaking | 2215 Hz |  4.4  | -2.9 dB |
| Peaking | 2282 Hz |  2.28 | 1.5 dB  |
| Peaking | 7231 Hz | 13.44 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20Private%20222/FitEar%20Private%20222.png)