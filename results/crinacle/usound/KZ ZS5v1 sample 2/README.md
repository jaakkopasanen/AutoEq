# KZ ZS5v1 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -7.0; 25 -7.4; 28 -7.8; 31 -8.2; 34 -8.4; 37 -8.6; 41 -8.8; 45 -8.9; 49 -9.0; 54 -9.1; 60 -9.3; 66 -9.4; 72 -9.6; 79 -9.7; 87 -9.9; 96 -10.0; 106 -10.0; 116 -10.0; 128 -10.0; 141 -10.0; 155 -9.8; 170 -9.6; 187 -9.3; 206 -9.0; 227 -8.7; 249 -8.3; 274 -8.1; 302 -7.7; 332 -7.4; 365 -7.0; 402 -6.7; 442 -6.4; 486 -6.2; 535 -5.9; 588 -5.7; 647 -5.6; 712 -5.4; 783 -5.3; 861 -5.3; 947 -5.6; 1042 -6.3; 1146 -7.5; 1261 -8.2; 1387 -7.9; 1526 -9.2; 1678 -10.6; 1846 -12.0; 2031 -13.3; 2234 -12.9; 2457 -11.9; 2703 -11.7; 2973 -10.4; 3270 -4.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -8.9; 9330 -7.4; 10263 -7.8; 11289 -11.1; 12418 -12.0; 13660 -7.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS5v1 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS5v1 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 66 Hz    | 0.64 | -2.8 dB  |
| Peaking | 153 Hz   | 1.22 | -2.4 dB  |
| Peaking | 2397 Hz  | 1.48 | -10.5 dB |
| Peaking | 4257 Hz  | 1.07 | 9.6 dB   |
| Peaking | 11732 Hz | 2.01 | -6.1 dB  |
| Peaking | 776 Hz   | 1.71 | 1.9 dB   |
| Peaking | 1810 Hz  | 4.55 | -1.5 dB  |
| Peaking | 6261 Hz  | 6.24 | 2.4 dB   |
| Peaking | 8255 Hz  | 6.06 | -3.4 dB  |
| Peaking | 14314 Hz | 4.59 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20ZS5v1%20sample%202/KZ%20ZS5v1%20sample%202.png)