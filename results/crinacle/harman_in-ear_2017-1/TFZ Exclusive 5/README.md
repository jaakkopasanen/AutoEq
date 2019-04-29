# TFZ Exclusive 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.5; 25 -4.0; 28 -4.6; 31 -5.1; 34 -5.4; 37 -5.7; 41 -6.1; 45 -6.4; 49 -6.7; 54 -7.0; 60 -7.3; 66 -7.6; 72 -7.9; 79 -8.2; 87 -8.6; 96 -8.9; 106 -9.1; 116 -9.3; 128 -9.4; 141 -9.4; 155 -9.4; 170 -9.3; 187 -9.1; 206 -8.8; 227 -8.5; 249 -8.2; 274 -7.8; 302 -7.3; 332 -6.7; 365 -6.2; 402 -5.8; 442 -5.4; 486 -5.0; 535 -4.6; 588 -4.2; 647 -3.8; 712 -3.5; 783 -3.0; 861 -2.7; 947 -2.9; 1042 -3.7; 1146 -4.5; 1261 -5.3; 1387 -5.9; 1526 -6.2; 1678 -6.5; 1846 -6.8; 2031 -7.3; 2234 -7.5; 2457 -7.1; 2703 -5.3; 2973 -3.0; 3270 -1.2; 3597 -0.5; 3957 -0.7; 4353 -2.0; 4788 -4.8; 5267 -9.5; 5793 -8.6; 6373 -3.3; 7010 -3.1; 7711 -5.4; 8482 -5.6; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.9; 13660 -14.5; 15026 -20.7; 16529 -22.9; 18182 -21.4; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Exclusive 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Exclusive 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.52 | 3.0 dB   |
| Peaking | 136 Hz   | 0.64 | -4.0 dB  |
| Peaking | 769 Hz   | 1.75 | 3.3 dB   |
| Peaking | 3709 Hz  | 3.52 | 6.3 dB   |
| Peaking | 17207 Hz | 1.16 | -19.9 dB |
| Peaking | 2143 Hz  | 2.68 | -2.7 dB  |
| Peaking | 5511 Hz  | 4.59 | -10.7 dB |
| Peaking | 5989 Hz  | 1.67 | 6.2 dB   |
| Peaking | 12185 Hz | 2.2  | 6.2 dB   |
| Peaking | 14501 Hz | 2.33 | -7.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -20.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%20Exclusive%205/TFZ%20Exclusive%205.png)