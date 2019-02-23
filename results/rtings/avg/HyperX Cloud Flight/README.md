# HyperX Cloud Flight
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.3; 25 -4.7; 28 -5.2; 31 -5.4; 34 -5.6; 37 -5.7; 41 -6.0; 45 -6.3; 49 -6.5; 54 -6.7; 60 -6.9; 66 -7.2; 72 -7.4; 79 -7.6; 87 -7.8; 96 -8.0; 106 -8.2; 116 -8.2; 128 -8.2; 141 -7.9; 155 -7.6; 170 -7.2; 187 -6.6; 206 -5.8; 227 -4.9; 249 -4.1; 274 -3.3; 302 -2.4; 332 -1.7; 365 -1.1; 402 -0.5; 442 -1.0; 486 -2.0; 535 -3.1; 588 -4.0; 647 -4.2; 712 -4.8; 783 -6.4; 861 -6.2; 947 -5.9; 1042 -5.0; 1146 -4.2; 1261 -3.2; 1387 -3.8; 1526 -4.6; 1678 -5.0; 1846 -5.6; 2031 -6.2; 2234 -5.0; 2457 -3.7; 2703 -3.4; 2973 -4.5; 3270 -4.6; 3597 -5.8; 3957 -6.3; 4353 -7.5; 4788 -8.2; 5267 -6.5; 5793 -4.1; 6373 -4.7; 7010 -7.3; 7711 -9.3; 8482 -10.8; 9330 -11.7; 10263 -10.3; 11289 -8.1; 12418 -7.4; 13660 -6.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Flight GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Flight ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 114 Hz  | 0.83 | -3.2 dB |
| Peaking | 378 Hz  | 1.59 | 5.3 dB  |
| Peaking | 4661 Hz | 2.26 | -7.6 dB |
| Peaking | 5615 Hz | 0.9  | 7.5 dB  |
| Peaking | 8731 Hz | 1.38 | -9.4 dB |
| Peaking | 20 Hz   | 2.31 | 1.9 dB  |
| Peaking | 840 Hz  | 4.23 | -1.9 dB |
| Peaking | 1284 Hz | 4.42 | 2.0 dB  |
| Peaking | 2040 Hz | 3.52 | -1.8 dB |
| Peaking | 2493 Hz | 4.73 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Flight/HyperX%20Cloud%20Flight.png)