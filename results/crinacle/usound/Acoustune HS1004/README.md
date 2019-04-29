# Acoustune HS1004
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.8; 25 -6.1; 28 -6.5; 31 -6.8; 34 -7.1; 37 -7.4; 41 -7.6; 45 -7.9; 49 -8.1; 54 -8.3; 60 -8.5; 66 -8.8; 72 -9.0; 79 -9.3; 87 -9.5; 96 -9.8; 106 -10.0; 116 -10.1; 128 -10.1; 141 -10.2; 155 -10.1; 170 -10.0; 187 -9.8; 206 -9.5; 227 -9.2; 249 -8.8; 274 -8.5; 302 -8.1; 332 -7.7; 365 -7.4; 402 -7.0; 442 -6.7; 486 -6.3; 535 -6.0; 588 -5.7; 647 -5.3; 712 -5.0; 783 -4.7; 861 -4.4; 947 -4.5; 1042 -4.9; 1146 -5.7; 1261 -6.6; 1387 -7.4; 1526 -7.6; 1678 -7.5; 1846 -7.0; 2031 -6.4; 2234 -5.4; 2457 -3.8; 2703 -2.0; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -4.6; 5267 -5.9; 5793 -8.2; 6373 -9.6; 7010 -8.0; 7711 -8.7; 8482 -11.1; 9330 -8.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.3; 15026 -9.6; 16529 -7.3; 18182 -8.2; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1004 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1004 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 130 Hz   | 0.59 | -3.8 dB |
| Peaking | 776 Hz   | 2.12 | 2.3 dB  |
| Peaking | 3553 Hz  | 1.87 | 7.1 dB  |
| Peaking | 6172 Hz  | 4.04 | -4.0 dB |
| Peaking | 8595 Hz  | 4.94 | -5.1 dB |
| Peaking | 20 Hz    | 2.23 | 1.5 dB  |
| Peaking | 1025 Hz  | 3.37 | 1.4 dB  |
| Peaking | 1591 Hz  | 1.75 | -2.1 dB |
| Peaking | 2766 Hz  | 5.59 | 2.0 dB  |
| Peaking | 20416 Hz | 0.74 | -7.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Acoustune%20HS1004/Acoustune%20HS1004.png)