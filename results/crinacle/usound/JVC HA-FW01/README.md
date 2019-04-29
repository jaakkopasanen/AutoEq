# JVC HA-FW01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.7; 25 -3.1; 28 -3.5; 31 -3.8; 34 -4.1; 37 -4.4; 41 -4.7; 45 -5.0; 49 -5.2; 54 -5.5; 60 -5.8; 66 -6.2; 72 -6.6; 79 -7.0; 87 -7.4; 96 -7.8; 106 -8.2; 116 -8.5; 128 -8.7; 141 -9.0; 155 -9.1; 170 -9.2; 187 -9.2; 206 -9.0; 227 -8.9; 249 -8.6; 274 -8.3; 302 -8.0; 332 -7.6; 365 -7.2; 402 -6.7; 442 -6.2; 486 -5.7; 535 -5.2; 588 -4.7; 647 -3.5; 712 -2.3; 783 -2.1; 861 -1.7; 947 -1.2; 1042 -1.2; 1146 -1.7; 1261 -2.3; 1387 -2.9; 1526 -3.0; 1678 -2.9; 1846 -2.6; 2031 -2.6; 2234 -2.8; 2457 -3.3; 2703 -4.0; 2973 -4.6; 3270 -4.7; 3597 -4.4; 3957 -4.1; 4353 -4.3; 4788 -4.8; 5267 -4.5; 5793 -2.6; 6373 -0.5; 7010 -2.2; 7711 -4.4; 8482 -4.6; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FW01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FW01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.5  | 3.3 dB  |
| Peaking | 179 Hz   | 0.47 | -4.7 dB |
| Peaking | 924 Hz   | 1.21 | 4.2 dB  |
| Peaking | 2053 Hz  | 3.06 | 1.6 dB  |
| Peaking | 6459 Hz  | 5.78 | 4.7 dB  |
| Peaking | 2345 Hz  | 4.31 | 0.3 dB  |
| Peaking | 4008 Hz  | 0.51 | -0.2 dB |
| Peaking | 18190 Hz | 1.46 | 0.4 dB  |
| Peaking | 19956 Hz | 1.36 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JVC%20HA-FW01/JVC%20HA-FW01.png)