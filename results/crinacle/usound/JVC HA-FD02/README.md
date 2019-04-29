# JVC HA-FD02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.4; 25 -5.6; 28 -5.8; 31 -6.0; 34 -6.1; 37 -6.2; 41 -6.3; 45 -6.4; 49 -6.4; 54 -6.5; 60 -6.6; 66 -6.8; 72 -6.9; 79 -7.1; 87 -7.3; 96 -7.4; 106 -7.5; 116 -7.6; 128 -7.6; 141 -7.6; 155 -7.5; 170 -7.4; 187 -7.3; 206 -7.0; 227 -6.7; 249 -6.5; 274 -6.3; 302 -6.1; 332 -5.8; 365 -5.6; 402 -5.4; 442 -5.3; 486 -5.2; 535 -5.0; 588 -4.9; 647 -4.7; 712 -4.5; 783 -4.4; 861 -4.3; 947 -4.4; 1042 -4.9; 1146 -5.6; 1261 -6.3; 1387 -6.9; 1526 -7.0; 1678 -7.0; 1846 -6.9; 2031 -7.1; 2234 -7.6; 2457 -8.4; 2703 -9.3; 2973 -9.8; 3270 -9.7; 3597 -9.6; 3957 -9.9; 4353 -9.8; 4788 -7.6; 5267 -3.9; 5793 -0.7; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.8; 15026 -8.2; 16529 -6.0; 18182 -6.3; 20000 -14.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FD02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FD02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 127 Hz   | 0.83 | -1.8 dB |
| Peaking | 754 Hz   | 1.08 | 2.0 dB  |
| Peaking | 4384 Hz  | 0.82 | -6.5 dB |
| Peaking | 5949 Hz  | 2.35 | 11.0 dB |
| Peaking | 19928 Hz | 2.03 | -8.6 dB |
| Peaking | 17 Hz    | 1.6  | 1.0 dB  |
| Peaking | 2841 Hz  | 6.18 | -0.4 dB |
| Peaking | 13030 Hz | 1.7  | 1.0 dB  |
| Peaking | 14474 Hz | 3.03 | -2.9 dB |
| Peaking | 17048 Hz | 1.84 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JVC%20HA-FD02/JVC%20HA-FD02.png)