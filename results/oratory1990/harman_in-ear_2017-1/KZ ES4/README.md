# KZ ES4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -14.2; 25 -14.4; 28 -14.3; 31 -14.2; 34 -14.2; 37 -14.1; 41 -14.1; 45 -13.9; 49 -13.9; 54 -14.0; 60 -14.0; 66 -14.2; 72 -14.0; 79 -14.3; 87 -14.0; 96 -13.6; 106 -13.6; 116 -13.2; 128 -13.2; 141 -12.7; 155 -12.3; 170 -12.0; 187 -11.7; 206 -11.3; 227 -10.9; 249 -10.4; 274 -9.9; 302 -9.4; 332 -8.8; 365 -8.2; 402 -7.7; 442 -7.2; 486 -6.7; 535 -6.3; 588 -5.9; 647 -5.5; 712 -5.1; 783 -4.7; 861 -4.5; 947 -4.5; 1042 -5.0; 1146 -5.8; 1261 -6.6; 1387 -7.1; 1526 -7.5; 1678 -8.1; 1846 -8.8; 2031 -9.6; 2234 -10.1; 2457 -9.4; 2703 -7.7; 2973 -6.4; 3270 -6.4; 3597 -7.8; 3957 -7.1; 4353 -1.8; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.4; 13660 -16.4; 15026 -20.9; 16529 -23.4; 18182 -26.9; 20000 -26.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ES4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ES4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.17 | -7.8 dB  |
| Peaking | 831 Hz   | 0.81 | 3.3 dB   |
| Peaking | 2405 Hz  | 0.65 | -11.1 dB |
| Peaking | 5961 Hz  | 0.31 | 14.3 dB  |
| Peaking | 18305 Hz | 0.28 | -23.9 dB |
| Peaking | 3833 Hz  | 4.97 | -6.6 dB  |
| Peaking | 4461 Hz  | 1.54 | 3.6 dB   |
| Peaking | 7611 Hz  | 4.54 | -3.1 dB  |
| Peaking | 8752 Hz  | 3.74 | -1.3 dB  |
| Peaking | 11631 Hz | 4.71 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.8 dB  |
| Peaking | 62 Hz    | 1.41 | -5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 16000 Hz | 1.41 | -23.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ES4/KZ%20ES4.png)