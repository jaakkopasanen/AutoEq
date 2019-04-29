# Westone UM Pro 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.8; 25 -4.9; 28 -5.0; 31 -5.2; 34 -5.3; 37 -5.4; 41 -5.6; 45 -5.8; 49 -5.9; 54 -6.1; 60 -6.4; 66 -6.7; 72 -7.0; 79 -7.4; 87 -7.9; 96 -8.3; 106 -8.7; 116 -9.1; 128 -9.5; 141 -9.8; 155 -10.1; 170 -10.4; 187 -10.6; 206 -10.6; 227 -10.7; 249 -10.7; 274 -10.7; 302 -10.7; 332 -10.6; 365 -10.5; 402 -10.4; 442 -10.2; 486 -10.1; 535 -9.9; 588 -9.6; 647 -9.3; 712 -8.9; 783 -8.6; 861 -8.3; 947 -8.1; 1042 -8.2; 1146 -8.7; 1261 -9.2; 1387 -9.3; 1526 -8.7; 1678 -7.7; 1846 -6.4; 2031 -5.3; 2234 -4.5; 2457 -3.6; 2703 -2.9; 2973 -2.4; 3270 -2.1; 3597 -1.9; 3957 -1.6; 4353 -0.8; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.4; 20000 -11.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM Pro 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM Pro 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.28 | 2.0 dB  |
| Peaking | 238 Hz   | 0.35 | -4.7 dB |
| Peaking | 1395 Hz  | 2.97 | -2.9 dB |
| Peaking | 4325 Hz  | 0.94 | 6.3 dB  |
| Peaking | 19313 Hz | 1.42 | -6.2 dB |
| Peaking | 2613 Hz  | 3.04 | 0.9 dB  |
| Peaking | 3926 Hz  | 4.24 | -1.2 dB |
| Peaking | 6365 Hz  | 2.67 | 4.5 dB  |
| Peaking | 7421 Hz  | 1.69 | -3.7 dB |
| Peaking | 16836 Hz | 2.8  | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Westone%20UM%20Pro%2010/Westone%20UM%20Pro%2010.png)