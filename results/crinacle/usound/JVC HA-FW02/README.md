# JVC HA-FW02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.0; 25 -2.5; 28 -3.2; 31 -3.7; 34 -4.2; 37 -4.5; 41 -5.0; 45 -5.4; 49 -5.7; 54 -6.1; 60 -6.5; 66 -6.9; 72 -7.3; 79 -7.6; 87 -8.1; 96 -8.5; 106 -8.8; 116 -9.0; 128 -9.2; 141 -9.3; 155 -9.4; 170 -9.3; 187 -9.3; 206 -9.1; 227 -8.8; 249 -8.5; 274 -8.1; 302 -7.7; 332 -7.2; 365 -6.8; 402 -6.3; 442 -5.8; 486 -5.3; 535 -4.8; 588 -4.2; 647 -3.6; 712 -3.0; 783 -2.5; 861 -1.8; 947 -1.1; 1042 -1.4; 1146 -1.8; 1261 -2.7; 1387 -2.7; 1526 -1.7; 1678 -2.1; 1846 -2.3; 2031 -2.7; 2234 -3.4; 2457 -4.6; 2703 -5.9; 2973 -6.4; 3270 -5.9; 3597 -5.4; 3957 -5.4; 4353 -6.3; 4788 -6.9; 5267 -5.3; 5793 -2.3; 6373 -0.5; 7010 -2.4; 7711 -4.7; 8482 -4.9; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FW02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FW02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.97 | 4.3 dB  |
| Peaking | 153 Hz  | 0.54 | -4.6 dB |
| Peaking | 925 Hz  | 1.45 | 4.0 dB  |
| Peaking | 1705 Hz | 3.23 | 2.5 dB  |
| Peaking | 6421 Hz | 6.42 | 5.0 dB  |
| Peaking | 2172 Hz | 4.11 | 1.2 dB  |
| Peaking | 2885 Hz | 3.37 | -1.9 dB |
| Peaking | 4851 Hz | 3.78 | -2.6 dB |
| Peaking | 5739 Hz | 5.52 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JVC%20HA-FW02/JVC%20HA-FW02.png)