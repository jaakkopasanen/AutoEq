# KZ ZS5v1 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.5; 25 -7.9; 28 -8.4; 31 -8.7; 34 -9.0; 37 -9.2; 41 -9.5; 45 -9.6; 49 -9.7; 54 -9.9; 60 -10.1; 66 -10.3; 72 -10.6; 79 -10.8; 87 -11.1; 96 -11.3; 106 -11.5; 116 -11.7; 128 -11.7; 141 -11.8; 155 -11.8; 170 -11.7; 187 -11.5; 206 -11.3; 227 -11.0; 249 -10.6; 274 -10.2; 302 -9.8; 332 -9.4; 365 -8.9; 402 -8.4; 442 -7.9; 486 -7.4; 535 -7.0; 588 -6.5; 647 -5.9; 712 -5.4; 783 -4.7; 861 -4.3; 947 -4.1; 1042 -4.3; 1146 -4.9; 1261 -5.6; 1387 -6.1; 1526 -6.4; 1678 -6.6; 1846 -7.1; 2031 -7.9; 2234 -8.9; 2457 -9.0; 2703 -8.1; 2973 -7.6; 3270 -7.5; 3597 -5.7; 3957 -0.9; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.5; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -10.1; 13660 -11.1; 15026 -7.0; 16529 -6.5; 18182 -6.5; 20000 -12.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS5v1 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS5v1 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 81 Hz    | 0.53 | -4.0 dB |
| Peaking | 198 Hz   | 1.08 | -3.4 dB |
| Peaking | 2783 Hz  | 1.96 | -4.1 dB |
| Peaking | 4841 Hz  | 1.49 | 7.5 dB  |
| Peaking | 13208 Hz | 2.94 | -5.4 dB |
| Peaking | 911 Hz   | 0.52 | -2.4 dB |
| Peaking | 913 Hz   | 1.11 | 5.1 dB  |
| Peaking | 6350 Hz  | 6.07 | 2.4 dB  |
| Peaking | 8061 Hz  | 4.59 | -2.9 dB |
| Peaking | 11126 Hz | 5.9  | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20ZS5v1%20sample%201/KZ%20ZS5v1%20sample%201.png)