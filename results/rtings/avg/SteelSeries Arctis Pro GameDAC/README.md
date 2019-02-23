# SteelSeries Arctis Pro GameDAC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.7; 25 -9.6; 28 -9.4; 31 -9.0; 34 -8.4; 37 -7.7; 41 -6.8; 45 -6.2; 49 -5.8; 54 -5.8; 60 -5.9; 66 -6.1; 72 -6.2; 79 -6.4; 87 -6.6; 96 -6.8; 106 -6.9; 116 -7.0; 128 -7.0; 141 -7.2; 155 -7.3; 170 -7.3; 187 -7.2; 206 -7.2; 227 -7.3; 249 -7.6; 274 -7.9; 302 -8.2; 332 -8.4; 365 -8.6; 402 -8.7; 442 -8.8; 486 -8.8; 535 -8.8; 588 -8.6; 647 -8.4; 712 -7.5; 783 -6.5; 861 -6.6; 947 -6.0; 1042 -5.5; 1146 -5.2; 1261 -4.8; 1387 -4.2; 1526 -3.7; 1678 -5.5; 1846 -6.4; 2031 -6.6; 2234 -6.1; 2457 -5.4; 2703 -5.6; 2973 -5.0; 3270 -2.1; 3597 -0.5; 3957 -0.6; 4353 -5.2; 4788 -8.2; 5267 -8.8; 5793 -9.3; 6373 -9.8; 7010 -8.9; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.2; 13660 -10.2; 15026 -9.0; 16529 -7.9; 18182 -6.7; 20000 -6.5
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
| Peaking | 25 Hz    | 1.87 | -3.6 dB |
| Peaking | 1430 Hz  | 4.01 | 2.8 dB  |
| Peaking | 3718 Hz  | 3.3  | 7.9 dB  |
| Peaking | 5544 Hz  | 1.81 | -4.0 dB |
| Peaking | 14100 Hz | 2.62 | -3.8 dB |
| Peaking | 54 Hz    | 1.17 | 2.0 dB  |
| Peaking | 61 Hz    | 0.32 | -1.0 dB |
| Peaking | 375 Hz   | 1.61 | -1.9 dB |
| Peaking | 561 Hz   | 3.18 | -1.7 dB |
| Peaking | 9944 Hz  | 2.64 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%20Pro%20GameDAC/SteelSeries%20Arctis%20Pro%20GameDAC.png)