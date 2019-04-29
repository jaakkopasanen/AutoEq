# TFZ Exclusive 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.5; 25 -10.5; 28 -10.5; 31 -10.4; 34 -10.3; 37 -10.3; 41 -10.2; 45 -10.1; 49 -9.9; 54 -9.8; 60 -9.7; 66 -9.6; 72 -9.5; 79 -9.4; 87 -9.4; 96 -9.3; 106 -9.2; 116 -9.0; 128 -8.8; 141 -8.6; 155 -8.3; 170 -8.0; 187 -7.6; 206 -7.2; 227 -6.7; 249 -6.2; 274 -5.7; 302 -5.2; 332 -4.7; 365 -4.2; 402 -3.7; 442 -3.3; 486 -2.9; 535 -2.4; 588 -2.0; 647 -1.6; 712 -1.2; 783 -0.7; 861 -0.5; 947 -0.7; 1042 -1.4; 1146 -2.5; 1261 -3.5; 1387 -4.3; 1526 -4.7; 1678 -4.9; 1846 -5.3; 2031 -6.1; 2234 -7.0; 2457 -7.1; 2703 -5.7; 2973 -3.7; 3270 -2.1; 3597 -1.4; 3957 -1.7; 4353 -3.4; 4788 -7.7; 5267 -11.0; 5793 -5.5; 6373 -1.7; 7010 -2.5; 7711 -6.2; 8482 -4.7; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Exclusive 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Exclusive 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.11 | -5.8 dB  |
| Peaking | 784 Hz  | 0.82 | 4.5 dB   |
| Peaking | 2520 Hz | 1.1  | -8.0 dB  |
| Peaking | 3417 Hz | 1.02 | 8.1 dB   |
| Peaking | 5105 Hz | 5.8  | -10.0 dB |
| Peaking | 678 Hz  | 1.9  | -1.9 dB  |
| Peaking | 772 Hz  | 1.04 | 1.6 dB   |
| Peaking | 1312 Hz | 3.5  | -1.2 dB  |
| Peaking | 6642 Hz | 6.87 | 3.7 dB   |
| Peaking | 7771 Hz | 5.22 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%20Exclusive%203/TFZ%20Exclusive%203.png)