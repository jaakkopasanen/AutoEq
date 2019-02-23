# KZ ZS6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -11.2; 25 -11.5; 28 -11.6; 31 -11.7; 34 -11.9; 37 -11.9; 41 -12.0; 45 -12.0; 49 -12.2; 54 -12.5; 60 -12.6; 66 -12.9; 72 -12.9; 79 -13.2; 87 -13.0; 96 -12.8; 106 -13.0; 116 -12.7; 128 -12.8; 141 -12.4; 155 -12.2; 170 -12.1; 187 -11.8; 206 -11.6; 227 -11.3; 249 -11.0; 274 -10.5; 302 -10.0; 332 -9.5; 365 -8.9; 402 -8.5; 442 -8.1; 486 -7.6; 535 -7.0; 588 -6.6; 647 -6.1; 712 -5.7; 783 -5.3; 861 -5.0; 947 -5.0; 1042 -5.4; 1146 -6.0; 1261 -6.4; 1387 -6.5; 1526 -6.1; 1678 -5.5; 1846 -5.0; 2031 -5.1; 2234 -5.7; 2457 -6.2; 2703 -5.8; 2973 -5.3; 3270 -5.4; 3597 -5.5; 3957 -1.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.0; 8482 -10.1; 9330 -9.8; 10263 -11.1; 11289 -12.7; 12418 -16.2; 13660 -25.0; 15026 -32.2; 16529 -30.6; 18182 -25.5; 20000 -24.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.57 | -2.9 dB  |
| Peaking | 111 Hz   | 0.35 | -6.0 dB  |
| Peaking | 761 Hz   | 1.75 | 2.0 dB   |
| Peaking | 6439 Hz  | 0.64 | 13.3 dB  |
| Peaking | 16079 Hz | 0.47 | -28.2 dB |
| Peaking | 3616 Hz  | 2.1  | -5.6 dB  |
| Peaking | 4117 Hz  | 2.36 | 5.7 dB   |
| Peaking | 8167 Hz  | 3.62 | -5.4 dB  |
| Peaking | 12481 Hz | 1.03 | 5.4 dB   |
| Peaking | 14278 Hz | 2.81 | -7.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 16000 Hz | 1.41 | -36.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZS6/KZ%20ZS6.png)