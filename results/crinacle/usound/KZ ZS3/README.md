# KZ ZS3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.0; 25 -10.1; 28 -10.1; 31 -10.1; 34 -10.2; 37 -10.2; 41 -10.3; 45 -10.3; 49 -10.4; 54 -10.4; 60 -10.5; 66 -10.7; 72 -10.9; 79 -11.0; 87 -11.3; 96 -11.5; 106 -11.6; 116 -11.7; 128 -11.8; 141 -11.8; 155 -11.8; 170 -11.6; 187 -11.4; 206 -11.1; 227 -10.8; 249 -10.4; 274 -10.0; 302 -9.5; 332 -9.0; 365 -8.4; 402 -7.8; 442 -7.2; 486 -6.6; 535 -5.9; 588 -5.2; 647 -4.4; 712 -3.6; 783 -2.8; 861 -2.1; 947 -1.7; 1042 -1.4; 1146 -1.7; 1261 -2.0; 1387 -2.5; 1526 -2.4; 1678 -1.9; 1846 -1.6; 2031 -1.7; 2234 -2.2; 2457 -3.2; 2703 -4.0; 2973 -3.9; 3270 -3.4; 3597 -3.1; 3957 -3.7; 4353 -6.0; 4788 -9.6; 5267 -8.0; 5793 -2.8; 6373 -0.5; 7010 -3.3; 7711 -6.7; 8482 -6.4; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.9; 18182 -11.0; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.66 | -1.9 dB |
| Peaking | 41 Hz    | 0.19 | -2.0 dB |
| Peaking | 181 Hz   | 0.38 | -4.9 dB |
| Peaking | 1118 Hz  | 0.57 | 5.1 dB  |
| Peaking | 6365 Hz  | 8.71 | 5.7 dB  |
| Peaking | 3932 Hz  | 2.52 | 2.8 dB  |
| Peaking | 4914 Hz  | 3.42 | -7.0 dB |
| Peaking | 5706 Hz  | 6.28 | 2.7 dB  |
| Peaking | 5861 Hz  | 4.39 | 1.0 dB  |
| Peaking | 19311 Hz | 1.37 | -7.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20ZS3/KZ%20ZS3.png)