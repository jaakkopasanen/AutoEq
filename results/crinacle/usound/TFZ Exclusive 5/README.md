# TFZ Exclusive 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.1; 31 -2.6; 34 -2.9; 37 -3.2; 41 -3.6; 45 -3.9; 49 -4.2; 54 -4.5; 60 -4.8; 66 -5.1; 72 -5.4; 79 -5.8; 87 -6.1; 96 -6.4; 106 -6.6; 116 -6.8; 128 -6.9; 141 -6.9; 155 -6.9; 170 -6.8; 187 -6.6; 206 -6.3; 227 -6.0; 249 -5.7; 274 -5.3; 302 -4.8; 332 -4.4; 365 -4.0; 402 -3.6; 442 -3.3; 486 -2.9; 535 -2.5; 588 -2.1; 647 -1.8; 712 -1.5; 783 -1.0; 861 -0.6; 947 -0.7; 1042 -1.6; 1146 -2.5; 1261 -3.5; 1387 -4.4; 1526 -4.9; 1678 -5.3; 1846 -5.7; 2031 -6.5; 2234 -7.3; 2457 -7.5; 2703 -6.1; 2973 -3.9; 3270 -2.1; 3597 -1.1; 3957 -1.0; 4353 -1.8; 4788 -4.4; 5267 -9.0; 5793 -8.4; 6373 -3.5; 7010 -2.3; 7711 -5.5; 8482 -6.0; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -4.3; 16529 -4.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Exclusive 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Exclusive 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 2.48 | 3.7 dB  |
| Peaking | 851 Hz  | 1.62 | 4.1 dB  |
| Peaking | 2474 Hz | 1.44 | -5.9 dB |
| Peaking | 3593 Hz | 1.38 | 6.1 dB  |
| Peaking | 5426 Hz | 5.86 | -7.7 dB |
| Peaking | 35 Hz   | 1.01 | 1.0 dB  |
| Peaking | 140 Hz  | 0.64 | -2.8 dB |
| Peaking | 458 Hz  | 1.59 | 1.2 dB  |
| Peaking | 6861 Hz | 7.57 | 2.8 dB  |
| Peaking | 8112 Hz | 6.58 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%20Exclusive%205/TFZ%20Exclusive%205.png)