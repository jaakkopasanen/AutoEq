# Acoustune HS1501
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.5; 25 -8.7; 28 -8.9; 31 -9.1; 34 -9.2; 37 -9.3; 41 -9.4; 45 -9.5; 49 -9.6; 54 -9.7; 60 -9.8; 66 -10.0; 72 -10.1; 79 -10.3; 87 -10.5; 96 -10.6; 106 -10.8; 116 -10.8; 128 -10.8; 141 -10.8; 155 -10.7; 170 -10.4; 187 -10.2; 206 -9.9; 227 -9.5; 249 -9.1; 274 -8.7; 302 -8.2; 332 -7.8; 365 -7.3; 402 -6.9; 442 -6.5; 486 -6.1; 535 -5.7; 588 -5.4; 647 -5.0; 712 -4.7; 783 -4.4; 861 -4.2; 947 -4.2; 1042 -4.6; 1146 -5.6; 1261 -6.7; 1387 -7.6; 1526 -8.1; 1678 -8.3; 1846 -8.4; 2031 -8.3; 2234 -7.6; 2457 -6.0; 2703 -3.9; 2973 -2.0; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -3.3; 5267 -7.8; 5793 -10.3; 6373 -5.2; 7010 -4.1; 7711 -6.4; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.9; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1501 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1501 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.37 | -2.8 dB |
| Peaking | 155 Hz  | 0.8  | -2.8 dB |
| Peaking | 764 Hz  | 2.11 | 2.7 dB  |
| Peaking | 3810 Hz | 2.27 | 7.1 dB  |
| Peaking | 5625 Hz | 8.86 | -6.3 dB |
| Peaking | 1027 Hz | 3.5  | 1.8 dB  |
| Peaking | 1894 Hz | 1.31 | -3.0 dB |
| Peaking | 2925 Hz | 3.77 | 2.9 dB  |
| Peaking | 6847 Hz | 7.16 | 3.6 dB  |
| Peaking | 7954 Hz | 2.71 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Acoustune%20HS1501/Acoustune%20HS1501.png)