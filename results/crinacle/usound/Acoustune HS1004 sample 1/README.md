# Acoustune HS1004 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.3; 28 -6.6; 31 -6.8; 34 -7.0; 37 -7.1; 41 -7.3; 45 -7.5; 49 -7.6; 54 -7.8; 60 -7.9; 66 -8.1; 72 -8.3; 79 -8.5; 87 -8.7; 96 -9.0; 106 -9.1; 116 -9.2; 128 -9.3; 141 -9.3; 155 -9.2; 170 -9.0; 187 -8.9; 206 -8.7; 227 -8.4; 249 -8.0; 274 -7.7; 302 -7.4; 332 -7.0; 365 -6.7; 402 -6.4; 442 -6.1; 486 -5.8; 535 -5.6; 588 -5.3; 647 -5.0; 712 -4.8; 783 -4.5; 861 -4.4; 947 -4.4; 1042 -4.7; 1146 -5.3; 1261 -6.2; 1387 -7.1; 1526 -7.5; 1678 -7.6; 1846 -7.5; 2031 -7.3; 2234 -6.6; 2457 -5.0; 2703 -3.0; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.7; 4788 -5.5; 5267 -7.4; 5793 -10.8; 6373 -11.9; 7010 -8.7; 7711 -8.9; 8482 -11.7; 9330 -9.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.3; 15026 -9.6; 16529 -7.0; 18182 -7.6; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1004 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1004 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 128 Hz   | 0.67 | -2.9 dB |
| Peaking | 754 Hz   | 1.74 | 2.3 dB  |
| Peaking | 3638 Hz  | 2.18 | 7.4 dB  |
| Peaking | 6101 Hz  | 3.92 | -6.6 dB |
| Peaking | 8637 Hz  | 5.48 | -5.6 dB |
| Peaking | 17 Hz    | 1.86 | 0.9 dB  |
| Peaking | 1050 Hz  | 3.24 | 1.4 dB  |
| Peaking | 1783 Hz  | 1.45 | -2.1 dB |
| Peaking | 2872 Hz  | 5.08 | 2.3 dB  |
| Peaking | 20210 Hz | 0.98 | -7.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Acoustune%20HS1004%20sample%201/Acoustune%20HS1004%20sample%201.png)