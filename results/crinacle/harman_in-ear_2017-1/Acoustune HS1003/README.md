# Acoustune HS1003
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.3; 25 -9.4; 28 -9.5; 31 -9.5; 34 -9.5; 37 -9.5; 41 -9.5; 45 -9.5; 49 -9.5; 54 -9.5; 60 -9.5; 66 -9.6; 72 -9.6; 79 -9.6; 87 -9.7; 96 -9.7; 106 -9.8; 116 -9.7; 128 -9.6; 141 -9.5; 155 -9.2; 170 -9.0; 187 -8.7; 206 -8.2; 227 -7.8; 249 -7.4; 274 -6.9; 302 -6.3; 332 -5.8; 365 -5.2; 402 -4.7; 442 -4.2; 486 -3.7; 535 -3.2; 588 -2.7; 647 -2.2; 712 -1.7; 783 -1.1; 861 -0.7; 947 -0.7; 1042 -1.0; 1146 -1.5; 1261 -2.0; 1387 -2.0; 1526 -1.7; 1678 -1.3; 1846 -1.0; 2031 -0.7; 2234 -0.5; 2457 -0.9; 2703 -1.9; 2973 -2.9; 3270 -3.1; 3597 -2.7; 3957 -2.5; 4353 -3.1; 4788 -5.1; 5267 -8.2; 5793 -9.2; 6373 -5.5; 7010 -2.5; 7711 -4.2; 8482 -7.3; 9330 -7.2; 10263 -4.5; 11289 -4.5; 12418 -5.4; 13660 -13.4; 15026 -19.4; 16529 -20.9; 18182 -21.7; 20000 -22.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1003 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.24 | -4.7 dB  |
| Peaking | 155 Hz   | 0.67 | -3.1 dB  |
| Peaking | 830 Hz   | 1.07 | 3.6 dB   |
| Peaking | 2234 Hz  | 1.26 | 3.5 dB   |
| Peaking | 18544 Hz | 0.63 | -20.0 dB |
| Peaking | 3069 Hz  | 4.3  | -0.9 dB  |
| Peaking | 4014 Hz  | 3.39 | 1.8 dB   |
| Peaking | 5521 Hz  | 6.73 | -5.5 dB  |
| Peaking | 12133 Hz | 1.68 | 7.8 dB   |
| Peaking | 14799 Hz | 1.81 | -8.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -21.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Acoustune%20HS1003/Acoustune%20HS1003.png)