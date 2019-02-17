# SteelSeries Arctis Pro GameDAC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.6; 25 -10.5; 28 -10.3; 31 -9.9; 34 -9.3; 37 -8.6; 41 -7.7; 45 -7.1; 49 -6.7; 54 -6.7; 60 -6.8; 66 -7.0; 72 -7.1; 79 -7.3; 87 -7.5; 96 -7.7; 106 -7.8; 116 -7.9; 128 -7.9; 141 -8.1; 155 -8.2; 170 -8.2; 187 -8.1; 206 -8.1; 227 -8.2; 249 -8.5; 274 -8.8; 302 -9.1; 332 -9.3; 365 -9.5; 402 -9.6; 442 -9.7; 486 -9.7; 535 -9.7; 588 -9.5; 647 -9.3; 712 -8.4; 783 -7.4; 861 -7.5; 947 -6.9; 1042 -6.4; 1146 -6.1; 1261 -5.7; 1387 -5.1; 1526 -4.6; 1678 -6.4; 1846 -7.3; 2031 -7.5; 2234 -7.0; 2457 -6.3; 2703 -6.5; 2973 -5.9; 3270 -3.1; 3597 -0.5; 3957 -1.0; 4353 -6.1; 4788 -9.1; 5267 -9.7; 5793 -10.2; 6373 -10.7; 7010 -9.8; 7711 -8.5; 8482 -6.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.1; 13660 -11.1; 15026 -9.9; 16529 -8.8; 18182 -7.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis Pro GameDAC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis Pro GameDAC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.23 | -4.4 dB |
| Peaking | 375 Hz   | 0.74 | -3.2 dB |
| Peaking | 3716 Hz  | 4.03 | 8.1 dB  |
| Peaking | 5681 Hz  | 1.88 | -4.8 dB |
| Peaking | 14330 Hz | 2.1  | -4.6 dB |
| Peaking | 119 Hz   | 2.31 | -0.8 dB |
| Peaking | 607 Hz   | 4.04 | -1.1 dB |
| Peaking | 1549 Hz  | 1.93 | 4.0 dB  |
| Peaking | 1826 Hz  | 2.2  | -3.4 dB |
| Peaking | 10145 Hz | 3.1  | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%20Pro%20GameDAC/SteelSeries%20Arctis%20Pro%20GameDAC.png)