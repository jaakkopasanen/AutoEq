# KZ ZST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.2; 25 -8.4; 28 -8.6; 31 -8.7; 34 -8.8; 37 -8.9; 41 -9.0; 45 -9.0; 49 -9.1; 54 -9.1; 60 -9.2; 66 -9.3; 72 -9.3; 79 -9.4; 87 -9.5; 96 -9.5; 106 -9.5; 116 -9.4; 128 -9.1; 141 -8.9; 155 -8.8; 170 -9.3; 187 -8.9; 206 -8.4; 227 -8.0; 249 -7.6; 274 -7.2; 302 -6.8; 332 -6.4; 365 -6.1; 402 -5.8; 442 -5.5; 486 -5.2; 535 -4.9; 588 -4.8; 647 -4.6; 712 -4.3; 783 -4.3; 861 -4.7; 947 -4.7; 1042 -5.3; 1146 -5.9; 1261 -6.6; 1387 -7.2; 1526 -7.9; 1678 -8.8; 1846 -9.5; 2031 -9.7; 2234 -8.9; 2457 -7.9; 2703 -6.5; 2973 -6.3; 3270 -7.0; 3597 -6.1; 3957 -1.8; 4353 -0.5; 4788 -1.3; 5267 -6.4; 5793 -6.4; 6373 -8.3; 7010 -9.8; 7711 -6.6; 8482 -6.5; 9330 -6.5; 10263 -9.7; 11289 -13.9; 12418 -13.7; 13660 -12.2; 15026 -8.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 73 Hz    | 0.51 | -3.2 dB |
| Peaking | 1975 Hz  | 3.31 | -3.7 dB |
| Peaking | 4384 Hz  | 4.36 | 7.2 dB  |
| Peaking | 6765 Hz  | 8.61 | -3.9 dB |
| Peaking | 12306 Hz | 2.22 | -8.4 dB |
| Peaking | 25 Hz    | 2.11 | -0.6 dB |
| Peaking | 184 Hz   | 2.55 | -1.2 dB |
| Peaking | 687 Hz   | 1.04 | 2.7 dB  |
| Peaking | 3667 Hz  | 0.16 | -0.5 dB |
| Peaking | 8908 Hz  | 3.8  | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ZST/KZ%20ZST.png)