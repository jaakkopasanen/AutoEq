# KZ ZS6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.5; 25 -12.8; 28 -12.9; 31 -13.0; 34 -13.2; 37 -13.2; 41 -13.3; 45 -13.4; 49 -13.5; 54 -13.8; 60 -13.9; 66 -14.2; 72 -14.2; 79 -14.5; 87 -14.3; 96 -14.1; 106 -14.3; 116 -14.0; 128 -14.1; 141 -13.7; 155 -13.5; 170 -13.4; 187 -13.2; 206 -12.9; 227 -12.6; 249 -12.3; 274 -11.8; 302 -11.3; 332 -10.8; 365 -10.3; 402 -9.8; 442 -9.4; 486 -8.9; 535 -8.4; 588 -7.9; 647 -7.5; 712 -7.0; 783 -6.6; 861 -6.4; 947 -6.4; 1042 -6.7; 1146 -7.3; 1261 -7.7; 1387 -7.8; 1526 -7.4; 1678 -6.8; 1846 -6.3; 2031 -6.4; 2234 -7.0; 2457 -7.5; 2703 -7.1; 2973 -6.6; 3270 -6.7; 3597 -6.8; 3957 -2.4; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -9.3; 8482 -11.4; 9330 -11.1; 10263 -12.4; 11289 -14.0; 12418 -17.5; 13660 -26.3; 15026 -33.5; 16529 -31.9; 18182 -26.8; 20000 -25.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 49 Hz    | 0.23 | -6.5 dB  |
| Peaking | 641 Hz   | 0.21 | -7.3 dB  |
| Peaking | 3416 Hz  | 0.56 | -11.1 dB |
| Peaking | 5027 Hz  | 0.29 | 34.2 dB  |
| Peaking | 15558 Hz | 0.31 | -41.3 dB |
| Peaking | 1349 Hz  | 4.64 | -1.4 dB  |
| Peaking | 1945 Hz  | 3.84 | 1.2 dB   |
| Peaking | 6603 Hz  | 5.76 | 2.3 dB   |
| Peaking | 8090 Hz  | 5.11 | -3.8 dB  |
| Peaking | 11646 Hz | 4.1  | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 16000 Hz | 1.41 | -38.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZS6/KZ%20ZS6.png)