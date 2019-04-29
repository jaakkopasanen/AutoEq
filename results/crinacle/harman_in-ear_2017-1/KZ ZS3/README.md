# KZ ZS3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.3; 23 -11.4; 25 -11.4; 28 -11.4; 31 -11.5; 34 -11.5; 37 -11.5; 41 -11.6; 45 -11.7; 49 -11.7; 54 -11.7; 60 -11.8; 66 -12.0; 72 -12.2; 79 -12.4; 87 -12.6; 96 -12.8; 106 -12.9; 116 -13.0; 128 -13.1; 141 -13.1; 155 -13.1; 170 -13.0; 187 -12.8; 206 -12.4; 227 -12.1; 249 -11.7; 274 -11.3; 302 -10.8; 332 -10.1; 365 -9.5; 402 -8.8; 442 -8.2; 486 -7.5; 535 -6.8; 588 -6.0; 647 -5.3; 712 -4.4; 783 -3.7; 861 -3.0; 947 -2.6; 1042 -2.4; 1146 -2.7; 1261 -2.6; 1387 -2.9; 1526 -2.5; 1678 -2.0; 1846 -1.6; 2031 -1.3; 2234 -1.3; 2457 -1.7; 2703 -2.0; 2973 -1.8; 3270 -1.3; 3597 -1.3; 3957 -2.3; 4353 -5.0; 4788 -8.9; 5267 -7.3; 5793 -1.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -7.8; 15026 -15.7; 16529 -23.4; 18182 -27.7; 20000 -23.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.22 | -5.1 dB  |
| Peaking | 160 Hz   | 0.65 | -5.2 dB  |
| Peaking | 354 Hz   | 0.81 | -4.3 dB  |
| Peaking | 2836 Hz  | 0.08 | 4.5 dB   |
| Peaking | 18371 Hz | 0.76 | -25.6 dB |
| Peaking | 4092 Hz  | 1.39 | 7.8 dB   |
| Peaking | 4941 Hz  | 1.7  | -14.7 dB |
| Peaking | 6054 Hz  | 3.63 | 9.0 dB   |
| Peaking | 13040 Hz | 2.04 | 5.6 dB   |
| Peaking | 16215 Hz | 2.14 | -5.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -6.0 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 16000 Hz | 1.41 | -19.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20ZS3/KZ%20ZS3.png)