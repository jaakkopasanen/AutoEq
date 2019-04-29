# KZ ZS5v2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.9; 25 -9.2; 28 -9.6; 31 -10.0; 34 -10.3; 37 -10.5; 41 -10.8; 45 -11.0; 49 -11.1; 54 -11.3; 60 -11.5; 66 -11.8; 72 -12.0; 79 -12.2; 87 -12.4; 96 -12.6; 106 -12.7; 116 -12.8; 128 -12.8; 141 -12.7; 155 -12.6; 170 -12.4; 187 -12.1; 206 -11.8; 227 -11.4; 249 -10.9; 274 -10.5; 302 -9.9; 332 -9.2; 365 -8.6; 402 -8.1; 442 -7.5; 486 -7.0; 535 -6.4; 588 -5.9; 647 -5.4; 712 -4.9; 783 -4.4; 861 -4.1; 947 -4.1; 1042 -4.6; 1146 -5.3; 1261 -6.0; 1387 -6.5; 1526 -6.9; 1678 -7.3; 1846 -7.9; 2031 -8.0; 2234 -7.0; 2457 -5.0; 2703 -3.0; 2973 -1.8; 3270 -1.6; 3597 -2.1; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.6; 8482 -12.3; 9330 -13.2; 10263 -15.1; 11289 -16.7; 12418 -19.8; 13660 -27.7; 15026 -32.7; 16529 -28.6; 18182 -24.9; 20000 -32.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS5v2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS5v2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 63 Hz    | 0.38 | -4.2 dB  |
| Peaking | 172 Hz   | 0.66 | -3.8 dB  |
| Peaking | 788 Hz   | 2.16 | 2.7 dB   |
| Peaking | 5810 Hz  | 0.61 | 20.4 dB  |
| Peaking | 15676 Hz | 0.22 | -27.2 dB |
| Peaking | 2053 Hz  | 1.65 | -7.8 dB  |
| Peaking | 2490 Hz  | 0.94 | 5.7 dB   |
| Peaking | 11683 Hz | 2.17 | 7.6 dB   |
| Peaking | 17880 Hz | 1.38 | 13.9 dB  |
| Peaking | 19255 Hz | 0.2  | -9.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 10.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 16000 Hz | 1.41 | -38.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20ZS5v2/KZ%20ZS5v2.png)