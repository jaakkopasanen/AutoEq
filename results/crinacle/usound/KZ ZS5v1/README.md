# KZ ZS5v1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.2; 25 -7.6; 28 -8.1; 31 -8.4; 34 -8.7; 37 -8.9; 41 -9.1; 45 -9.3; 49 -9.4; 54 -9.5; 60 -9.7; 66 -9.9; 72 -10.1; 79 -10.3; 87 -10.5; 96 -10.6; 106 -10.8; 116 -10.9; 128 -10.9; 141 -10.9; 155 -10.8; 170 -10.6; 187 -10.4; 206 -10.1; 227 -9.8; 249 -9.5; 274 -9.1; 302 -8.7; 332 -8.4; 365 -7.9; 402 -7.5; 442 -7.2; 486 -6.8; 535 -6.5; 588 -6.1; 647 -5.8; 712 -5.4; 783 -5.0; 861 -4.8; 947 -4.9; 1042 -5.3; 1146 -6.2; 1261 -6.9; 1387 -7.0; 1526 -7.8; 1678 -8.6; 1846 -9.6; 2031 -10.6; 2234 -10.9; 2457 -10.5; 2703 -9.9; 2973 -9.0; 3270 -6.2; 3597 -2.2; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.5; 8482 -8.2; 9330 -6.5; 10263 -6.5; 11289 -8.4; 12418 -11.0; 13660 -9.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS5v1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS5v1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 74 Hz    | 0.56 | -3.3 dB |
| Peaking | 177 Hz   | 1.08 | -2.8 dB |
| Peaking | 2485 Hz  | 1.73 | -7.0 dB |
| Peaking | 4516 Hz  | 1.25 | 8.1 dB  |
| Peaking | 12479 Hz | 2.6  | -5.1 dB |
| Peaking | 861 Hz   | 2.01 | 2.3 dB  |
| Peaking | 1814 Hz  | 3.53 | -1.1 dB |
| Peaking | 6336 Hz  | 5.61 | 2.6 dB  |
| Peaking | 8212 Hz  | 3.75 | -3.4 dB |
| Peaking | 10307 Hz | 3.21 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20ZS5v1/KZ%20ZS5v1.png)