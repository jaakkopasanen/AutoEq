# KZ ZS5v1 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.6; 25 -9.0; 28 -9.5; 31 -9.9; 34 -10.1; 37 -10.4; 41 -10.7; 45 -10.8; 49 -10.8; 54 -11.0; 60 -11.3; 66 -11.5; 72 -11.7; 79 -12.0; 87 -12.2; 96 -12.4; 106 -12.7; 116 -12.8; 128 -12.9; 141 -12.9; 155 -13.0; 170 -12.8; 187 -12.7; 206 -12.4; 227 -12.1; 249 -11.8; 274 -11.4; 302 -10.9; 332 -10.3; 365 -9.7; 402 -9.2; 442 -8.8; 486 -8.2; 535 -7.7; 588 -7.1; 647 -6.6; 712 -6.1; 783 -5.4; 861 -5.0; 947 -4.9; 1042 -5.1; 1146 -5.6; 1261 -6.0; 1387 -6.3; 1526 -6.4; 1678 -6.5; 1846 -6.9; 2031 -7.4; 2234 -7.8; 2457 -7.3; 2703 -6.0; 2973 -5.3; 3270 -5.3; 3597 -3.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.2; 12418 -12.6; 13660 -20.0; 15026 -22.8; 16529 -20.4; 18182 -20.4; 20000 -24.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS5v1 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS5v1 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.64 | -2.4 dB  |
| Peaking | 155 Hz   | 0.47 | -6.2 dB  |
| Peaking | 838 Hz   | 2.25 | 2.5 dB   |
| Peaking | 6227 Hz  | 0.81 | 9.1 dB   |
| Peaking | 18468 Hz | 0.28 | -16.6 dB |
| Peaking | 2348 Hz  | 2.22 | -2.5 dB  |
| Peaking | 4186 Hz  | 4.31 | 2.6 dB   |
| Peaking | 7642 Hz  | 4.42 | -3.3 dB  |
| Peaking | 11179 Hz | 2.45 | 5.7 dB   |
| Peaking | 14263 Hz | 2.95 | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 16000 Hz | 1.41 | -22.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20ZS5v1%20sample%201/KZ%20ZS5v1%20sample%201.png)