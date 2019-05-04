# SteelSeries Arctis Pro GameDAC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.6; 25 -9.5; 28 -9.2; 31 -8.8; 34 -8.3; 37 -7.6; 41 -6.7; 45 -6.1; 49 -5.7; 54 -5.6; 60 -5.7; 66 -5.9; 72 -6.0; 79 -6.1; 87 -6.4; 96 -6.5; 106 -6.6; 116 -6.8; 128 -6.9; 141 -6.9; 155 -7.0; 170 -7.1; 187 -7.0; 206 -7.1; 227 -7.2; 249 -7.5; 274 -7.9; 302 -8.2; 332 -8.3; 365 -8.5; 402 -8.7; 442 -8.8; 486 -8.9; 535 -8.8; 588 -8.7; 647 -8.5; 712 -7.6; 783 -6.6; 861 -6.6; 947 -6.1; 1042 -5.6; 1146 -5.3; 1261 -4.9; 1387 -4.4; 1526 -4.0; 1678 -5.6; 1846 -6.7; 2031 -7.0; 2234 -6.9; 2457 -6.4; 2703 -6.2; 2973 -5.0; 3270 -1.7; 3597 -0.5; 3957 -0.5; 4353 -4.9; 4788 -8.6; 5267 -9.2; 5793 -9.3; 6373 -8.8; 7010 -8.9; 7711 -8.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.5; 13660 -9.4; 15026 -8.5; 16529 -7.7; 18182 -6.6; 20000 -6.5
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
| Peaking | 23 Hz    | 2.21 | -3.5 dB |
| Peaking | 428 Hz   | 1.36 | -2.6 dB |
| Peaking | 3777 Hz  | 2.88 | 8.9 dB  |
| Peaking | 5174 Hz  | 1.69 | -4.8 dB |
| Peaking | 14002 Hz | 2.42 | -3.0 dB |
| Peaking | 57 Hz    | 2.63 | 1.3 dB  |
| Peaking | 631 Hz   | 4.6  | -1.2 dB |
| Peaking | 1545 Hz  | 1.62 | 4.1 dB  |
| Peaking | 1893 Hz  | 1.79 | -3.3 dB |
| Peaking | 10203 Hz | 3.39 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%20Pro%20GameDAC/SteelSeries%20Arctis%20Pro%20GameDAC.png)