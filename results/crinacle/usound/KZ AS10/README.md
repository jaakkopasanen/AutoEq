# KZ AS10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.3; 25 -7.5; 28 -7.8; 31 -8.0; 34 -8.1; 37 -8.2; 41 -8.3; 45 -8.4; 49 -8.5; 54 -8.6; 60 -8.7; 66 -8.9; 72 -9.1; 79 -9.2; 87 -9.3; 96 -9.5; 106 -9.6; 116 -9.6; 128 -9.7; 141 -9.5; 155 -9.4; 170 -9.1; 187 -8.9; 206 -8.5; 227 -8.1; 249 -7.7; 274 -7.3; 302 -6.8; 332 -6.3; 365 -5.7; 402 -5.2; 442 -4.7; 486 -4.2; 535 -3.6; 588 -3.1; 647 -2.5; 712 -1.9; 783 -1.2; 861 -0.8; 947 -0.5; 1042 -0.6; 1146 -1.0; 1261 -1.5; 1387 -1.7; 1526 -1.5; 1678 -1.2; 1846 -1.1; 2031 -1.5; 2234 -2.4; 2457 -4.4; 2703 -7.4; 2973 -9.0; 3270 -7.4; 3597 -6.0; 3957 -5.7; 4353 -2.0; 4788 -6.1; 5267 -7.4; 5793 -2.5; 6373 -1.5; 7010 -3.1; 7711 -5.5; 8482 -4.8; 9330 -4.8; 10263 -4.8; 11289 -5.0; 12418 -4.9; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ AS10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ AS10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.42 | -2.6 dB |
| Peaking | 145 Hz  | 0.57 | -4.1 dB |
| Peaking | 859 Hz  | 1.1  | 3.7 dB  |
| Peaking | 2427 Hz | 0.94 | 6.0 dB  |
| Peaking | 2914 Hz | 2.25 | -9.7 dB |
| Peaking | 4454 Hz | 9.95 | 4.2 dB  |
| Peaking | 5102 Hz | 4.59 | -6.0 dB |
| Peaking | 6140 Hz | 3.25 | 4.6 dB  |
| Peaking | 7819 Hz | 4.73 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20AS10/KZ%20AS10.png)