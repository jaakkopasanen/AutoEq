# Acoustune HS1650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.8; 25 -5.9; 28 -6.1; 31 -6.2; 34 -6.3; 37 -6.4; 41 -6.4; 45 -6.5; 49 -6.6; 54 -6.7; 60 -6.8; 66 -6.9; 72 -7.0; 79 -7.2; 87 -7.3; 96 -7.4; 106 -7.6; 116 -7.6; 128 -7.6; 141 -7.5; 155 -7.3; 170 -7.0; 187 -6.7; 206 -6.2; 227 -5.7; 249 -5.2; 274 -4.5; 302 -3.9; 332 -3.4; 365 -2.8; 402 -2.4; 442 -2.1; 486 -2.2; 535 -2.3; 588 -2.7; 647 -3.0; 712 -3.0; 783 -2.8; 861 -2.6; 947 -2.6; 1042 -2.9; 1146 -3.6; 1261 -4.4; 1387 -4.9; 1526 -5.2; 1678 -5.3; 1846 -5.5; 2031 -6.1; 2234 -6.9; 2457 -7.0; 2703 -5.7; 2973 -3.7; 3270 -1.9; 3597 -0.8; 3957 -0.5; 4353 -1.0; 4788 -2.7; 5267 -5.3; 5793 -5.6; 6373 -2.6; 7010 -1.8; 7711 -3.9; 8482 -5.3; 9330 -4.3; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -6.6; 15026 -8.8; 16529 -9.8; 18182 -9.9; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.64 | -2.5 dB |
| Peaking | 133 Hz   | 1.56 | -2.9 dB |
| Peaking | 2361 Hz  | 2.75 | -3.7 dB |
| Peaking | 3760 Hz  | 2.46 | 4.5 dB  |
| Peaking | 17311 Hz | 1.1  | -6.7 dB |
| Peaking | 460 Hz   | 1.96 | 2.4 dB  |
| Peaking | 895 Hz   | 3.13 | 1.6 dB  |
| Peaking | 5550 Hz  | 6.57 | -3.0 dB |
| Peaking | 6527 Hz  | 4.98 | 1.0 dB  |
| Peaking | 6747 Hz  | 7.74 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Acoustune%20HS1650/Acoustune%20HS1650.png)