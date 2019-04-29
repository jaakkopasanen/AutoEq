# TFZ Secret Garden
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.6; 25 -2.8; 28 -3.1; 31 -3.3; 34 -3.5; 37 -3.6; 41 -3.7; 45 -3.8; 49 -3.8; 54 -4.0; 60 -4.1; 66 -4.2; 72 -4.4; 79 -4.6; 87 -4.7; 96 -4.9; 106 -5.1; 116 -5.1; 128 -5.1; 141 -5.1; 155 -5.0; 170 -4.8; 187 -4.7; 206 -4.4; 227 -4.1; 249 -3.8; 274 -3.5; 302 -3.2; 332 -2.9; 365 -2.6; 402 -2.3; 442 -2.0; 486 -1.8; 535 -1.5; 588 -1.3; 647 -1.0; 712 -0.7; 783 -0.6; 861 -0.5; 947 -0.6; 1042 -1.3; 1146 -2.4; 1261 -3.9; 1387 -5.4; 1526 -5.9; 1678 -6.0; 1846 -6.4; 2031 -7.3; 2234 -8.2; 2457 -7.9; 2703 -6.2; 2973 -4.1; 3270 -2.7; 3597 -2.2; 3957 -2.8; 4353 -4.8; 4788 -8.3; 5267 -8.6; 5793 -4.8; 6373 -3.5; 7010 -7.4; 7711 -6.2; 8482 -3.7; 9330 -3.8; 10263 -3.8; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Secret Garden GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Secret Garden ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 812 Hz  | 1.1  | 4.3 dB  |
| Peaking | 2395 Hz | 1    | -9.3 dB |
| Peaking | 3426 Hz | 0.94 | 7.8 dB  |
| Peaking | 4963 Hz | 4    | -8.1 dB |
| Peaking | 7274 Hz | 7.82 | -5.0 dB |
| Peaking | 17 Hz   | 1.05 | 1.7 dB  |
| Peaking | 132 Hz  | 0.82 | -1.5 dB |
| Peaking | 388 Hz  | 1.72 | 0.8 dB  |
| Peaking | 1419 Hz | 7.2  | -1.1 dB |
| Peaking | 1844 Hz | 6.74 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%20Secret%20Garden/TFZ%20Secret%20Garden.png)