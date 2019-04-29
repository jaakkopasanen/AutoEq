# TFZ Exclusive 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.2; 25 -10.4; 28 -10.6; 31 -10.7; 34 -10.7; 37 -10.8; 41 -10.8; 45 -10.9; 49 -10.9; 54 -10.8; 60 -10.8; 66 -10.8; 72 -10.8; 79 -10.9; 87 -10.9; 96 -11.0; 106 -11.0; 116 -10.9; 128 -10.8; 141 -10.6; 155 -10.4; 170 -10.1; 187 -9.8; 206 -9.4; 227 -9.0; 249 -8.5; 274 -8.1; 302 -7.6; 332 -7.0; 365 -6.5; 402 -6.0; 442 -5.7; 486 -5.2; 535 -4.8; 588 -4.5; 647 -4.2; 712 -3.8; 783 -3.5; 861 -3.7; 947 -3.9; 1042 -3.2; 1146 -4.8; 1261 -5.4; 1387 -5.0; 1526 -5.5; 1678 -5.6; 1846 -5.8; 2031 -5.9; 2234 -5.9; 2457 -5.8; 2703 -5.3; 2973 -4.3; 3270 -3.4; 3597 -3.2; 3957 -3.9; 4353 -5.7; 4788 -7.7; 5267 -6.4; 5793 -2.6; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -6.5; 9330 -6.5; 10263 -5.9; 11289 -5.9; 12418 -6.3; 13660 -11.5; 15026 -17.5; 16529 -21.0; 18182 -21.0; 20000 -16.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Exclusive 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Exclusive 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.37 | -4.8 dB  |
| Peaking | 151 Hz   | 0.99 | -3.0 dB  |
| Peaking | 8233 Hz  | 0.22 | 22.0 dB  |
| Peaking | 12476 Hz | 1.66 | 10.4 dB  |
| Peaking | 14543 Hz | 0.17 | -31.3 dB |
| Peaking | 811 Hz   | 0.72 | 4.7 dB   |
| Peaking | 1463 Hz  | 0.26 | -3.4 dB  |
| Peaking | 3539 Hz  | 2.17 | 3.7 dB   |
| Peaking | 4876 Hz  | 4.17 | -3.8 dB  |
| Peaking | 6237 Hz  | 4.75 | 5.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 16000 Hz | 1.41 | -17.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%20Exclusive%201/TFZ%20Exclusive%201.png)