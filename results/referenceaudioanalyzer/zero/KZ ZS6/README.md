# KZ ZS6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.3; 25 -9.7; 28 -10.1; 31 -10.4; 34 -10.6; 37 -10.8; 41 -11.0; 45 -11.1; 49 -11.2; 54 -11.2; 60 -11.2; 66 -11.2; 72 -11.2; 79 -11.0; 87 -10.8; 96 -10.7; 106 -10.5; 116 -10.2; 128 -9.9; 141 -9.6; 155 -9.4; 170 -9.2; 187 -8.8; 206 -8.4; 227 -7.9; 249 -7.6; 274 -7.3; 302 -6.9; 332 -6.6; 365 -6.1; 402 -5.7; 442 -5.3; 486 -5.0; 535 -4.6; 588 -4.4; 647 -4.1; 712 -4.0; 783 -3.7; 861 -3.7; 947 -4.0; 1042 -4.4; 1146 -4.9; 1261 -5.6; 1387 -6.2; 1526 -6.3; 1678 -6.4; 1846 -7.1; 2031 -8.5; 2234 -10.5; 2457 -12.3; 2703 -12.8; 2973 -12.0; 3270 -10.8; 3597 -9.3; 3957 -6.9; 4353 -3.9; 4788 -2.0; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.8; 9330 -11.4; 10263 -11.0; 11289 -8.9; 12418 -7.9; 13660 -7.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 61 Hz   | 0.33 | -4.8 dB |
| Peaking | 785 Hz  | 0.64 | 3.1 dB  |
| Peaking | 2828 Hz | 1.52 | -8.4 dB |
| Peaking | 5593 Hz | 1.42 | 8.3 dB  |
| Peaking | 9662 Hz | 2.03 | -6.6 dB |
| Peaking | 917 Hz  | 3.24 | 0.2 dB  |
| Peaking | 1412 Hz | 2.55 | -1.2 dB |
| Peaking | 1728 Hz | 2.16 | 1.3 dB  |
| Peaking | 2360 Hz | 6.21 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/KZ%20ZS6/KZ%20ZS6.png)