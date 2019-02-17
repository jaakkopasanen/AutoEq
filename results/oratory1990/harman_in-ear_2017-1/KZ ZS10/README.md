# KZ ZS10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -13.2; 25 -13.6; 28 -13.4; 31 -13.3; 34 -13.4; 37 -13.5; 41 -13.4; 45 -13.4; 49 -13.5; 54 -13.8; 60 -13.9; 66 -14.3; 72 -14.2; 79 -14.4; 87 -14.5; 96 -14.0; 106 -14.3; 116 -13.9; 128 -13.9; 141 -13.7; 155 -13.3; 170 -13.1; 187 -12.8; 206 -12.5; 227 -12.1; 249 -11.7; 274 -11.3; 302 -10.8; 332 -10.1; 365 -9.6; 402 -9.1; 442 -8.6; 486 -8.1; 535 -7.6; 588 -7.2; 647 -6.8; 712 -6.5; 783 -6.4; 861 -6.1; 947 -6.2; 1042 -6.8; 1146 -7.6; 1261 -8.3; 1387 -8.9; 1526 -9.4; 1678 -10.0; 1846 -10.8; 2031 -11.5; 2234 -11.4; 2457 -10.0; 2703 -8.6; 2973 -8.1; 3270 -7.7; 3597 -8.8; 3957 -6.9; 4353 -2.4; 4788 -0.5; 5267 -3.6; 5793 -1.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.9; 13660 -18.8; 15026 -25.4; 16529 -25.0; 18182 -25.3; 20000 -26.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.19 | -6.6 dB  |
| Peaking | 207 Hz   | 0.41 | -2.9 dB  |
| Peaking | 2133 Hz  | 0.78 | -11.0 dB |
| Peaking | 8015 Hz  | 0.19 | 24.1 dB  |
| Peaking | 16601 Hz | 0.21 | -35.2 dB |
| Peaking | 3825 Hz  | 4.28 | -6.5 dB  |
| Peaking | 4316 Hz  | 2.24 | 4.7 dB   |
| Peaking | 8168 Hz  | 3.64 | -3.9 dB  |
| Peaking | 12155 Hz | 3.04 | 6.4 dB   |
| Peaking | 14445 Hz | 3.59 | -6.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 16000 Hz | 1.41 | -26.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZS10/KZ%20ZS10.png)