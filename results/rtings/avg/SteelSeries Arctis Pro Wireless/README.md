# SteelSeries Arctis Pro Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.5; 25 -5.7; 28 -5.7; 31 -5.5; 34 -5.0; 37 -4.5; 41 -3.9; 45 -3.7; 49 -3.9; 54 -4.4; 60 -4.8; 66 -5.1; 72 -5.3; 79 -5.4; 87 -5.6; 96 -5.7; 106 -5.8; 116 -5.9; 128 -6.0; 141 -5.9; 155 -5.9; 170 -5.7; 187 -5.5; 206 -5.2; 227 -4.9; 249 -4.8; 274 -4.7; 302 -4.7; 332 -4.5; 365 -4.1; 402 -4.2; 442 -4.8; 486 -5.1; 535 -5.1; 588 -5.3; 647 -5.3; 712 -5.5; 783 -5.5; 861 -5.2; 947 -4.8; 1042 -4.1; 1146 -3.8; 1261 -4.1; 1387 -4.3; 1526 -4.4; 1678 -6.6; 1846 -8.3; 2031 -8.6; 2234 -8.8; 2457 -8.6; 2703 -8.1; 2973 -7.5; 3270 -5.0; 3597 -0.5; 3957 -1.1; 4353 -4.1; 4788 -5.1; 5267 -6.3; 5793 -8.1; 6373 -8.0; 7010 -8.6; 7711 -7.2; 8482 -5.3; 9330 -5.4; 10263 -5.4; 11289 -5.6; 12418 -9.9; 13660 -11.0; 15026 -10.5; 16529 -8.0; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis Pro Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis Pro Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 1389 Hz  | 1.4  | 3.9 dB  |
| Peaking | 2135 Hz  | 1.11 | -5.5 dB |
| Peaking | 3750 Hz  | 4.43 | 7.6 dB  |
| Peaking | 6458 Hz  | 3.34 | -3.0 dB |
| Peaking | 14266 Hz | 1.92 | -6.4 dB |
| Peaking | 46 Hz    | 2.84 | 1.8 dB  |
| Peaking | 124 Hz   | 1.68 | -0.7 dB |
| Peaking | 351 Hz   | 2.3  | 1.2 dB  |
| Peaking | 10962 Hz | 2.34 | 2.0 dB  |
| Peaking | 12527 Hz | 5.11 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -5.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%20Pro%20Wireless/SteelSeries%20Arctis%20Pro%20Wireless.png)