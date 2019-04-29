# TFZ Tequila 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.3; 25 -4.7; 28 -5.2; 31 -5.7; 34 -6.0; 37 -6.2; 41 -6.5; 45 -6.8; 49 -7.0; 54 -7.3; 60 -7.6; 66 -8.0; 72 -8.3; 79 -8.6; 87 -8.9; 96 -9.2; 106 -9.5; 116 -9.6; 128 -9.7; 141 -9.8; 155 -9.8; 170 -9.6; 187 -9.4; 206 -9.2; 227 -8.8; 249 -8.4; 274 -8.0; 302 -7.5; 332 -7.1; 365 -6.5; 402 -6.0; 442 -5.5; 486 -5.0; 535 -4.4; 588 -3.9; 647 -3.3; 712 -2.7; 783 -2.1; 861 -1.6; 947 -1.0; 1042 -1.2; 1146 -1.8; 1261 -2.4; 1387 -2.8; 1526 -2.6; 1678 -2.4; 1846 -2.3; 2031 -2.2; 2234 -2.4; 2457 -2.5; 2703 -2.2; 2973 -1.6; 3270 -0.9; 3597 -0.5; 3957 -0.7; 4353 -1.8; 4788 -4.1; 5267 -6.1; 5793 -4.1; 6373 -1.1; 7010 -1.9; 7711 -4.9; 8482 -4.4; 9330 -4.4; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Tequila 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Tequila 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 85 Hz    | 0.56 | -1.4 dB |
| Peaking | 170 Hz   | 0.44 | -4.6 dB |
| Peaking | 930 Hz   | 0.78 | 3.5 dB  |
| Peaking | 3525 Hz  | 2.22 | 3.7 dB  |
| Peaking | 22047 Hz | 2.19 | 0.8 dB  |
| Peaking | 19 Hz    | 2.18 | 1.2 dB  |
| Peaking | 1387 Hz  | 3.12 | -1.9 dB |
| Peaking | 1510 Hz  | 1.36 | 1.1 dB  |
| Peaking | 5280 Hz  | 6.86 | -3.3 dB |
| Peaking | 6543 Hz  | 6.99 | 3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%20Tequila%201/TFZ%20Tequila%201.png)