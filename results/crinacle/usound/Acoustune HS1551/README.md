# Acoustune HS1551
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.5; 25 -5.8; 28 -6.2; 31 -6.5; 34 -6.8; 37 -7.0; 41 -7.2; 45 -7.4; 49 -7.6; 54 -7.9; 60 -8.2; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.3; 96 -9.7; 106 -10.0; 116 -10.2; 128 -10.4; 141 -10.5; 155 -10.5; 170 -10.5; 187 -10.4; 206 -10.2; 227 -9.9; 249 -9.6; 274 -9.2; 302 -8.8; 332 -8.4; 365 -7.9; 402 -7.5; 442 -7.1; 486 -6.6; 535 -6.2; 588 -5.8; 647 -5.3; 712 -4.9; 783 -4.5; 861 -4.4; 947 -4.4; 1042 -5.0; 1146 -6.0; 1261 -7.1; 1387 -8.1; 1526 -8.8; 1678 -9.1; 1846 -9.0; 2031 -8.4; 2234 -7.0; 2457 -5.0; 2703 -3.0; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -2.7; 5267 -7.3; 5793 -10.4; 6373 -5.7; 7010 -4.2; 7711 -6.8; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1551 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1551 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 156 Hz   | 0.57 | -4.2 dB |
| Peaking | 894 Hz   | 1.08 | 3.5 dB  |
| Peaking | 1763 Hz  | 1.18 | -5.8 dB |
| Peaking | 3523 Hz  | 1.14 | 8.0 dB  |
| Peaking | 5656 Hz  | 6.64 | -7.6 dB |
| Peaking | 20 Hz    | 1.86 | 1.6 dB  |
| Peaking | 6763 Hz  | 9.66 | 2.3 dB  |
| Peaking | 7349 Hz  | 6.29 | 1.4 dB  |
| Peaking | 7823 Hz  | 3.47 | -2.5 dB |
| Peaking | 19261 Hz | 1.52 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Acoustune%20HS1551/Acoustune%20HS1551.png)