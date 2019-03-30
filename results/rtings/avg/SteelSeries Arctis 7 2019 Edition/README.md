# SteelSeries Arctis 7 2019 Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.2; 31 -1.2; 34 -1.3; 37 -1.4; 41 -1.8; 45 -2.4; 49 -3.0; 54 -3.7; 60 -4.5; 66 -5.2; 72 -5.8; 79 -6.3; 87 -6.8; 96 -7.1; 106 -7.4; 116 -7.7; 128 -8.0; 141 -8.1; 155 -8.2; 170 -8.1; 187 -7.9; 206 -7.5; 227 -7.2; 249 -7.2; 274 -7.2; 302 -6.7; 332 -6.0; 365 -5.7; 402 -5.7; 442 -5.8; 486 -5.8; 535 -5.4; 588 -4.9; 647 -4.3; 712 -3.3; 783 -3.0; 861 -3.1; 947 -2.7; 1042 -2.0; 1146 -1.5; 1261 -1.5; 1387 -1.9; 1526 -2.0; 1678 -3.1; 1846 -4.1; 2031 -3.9; 2234 -3.3; 2457 -2.8; 2703 -2.8; 2973 -2.7; 3270 -2.4; 3597 -2.5; 3957 -1.7; 4353 -1.8; 4788 -2.5; 5267 -6.7; 5793 -8.2; 6373 -7.0; 7010 -7.2; 7711 -8.6; 8482 -10.6; 9330 -10.9; 10263 -7.2; 11289 -5.3; 12418 -8.0; 13660 -10.2; 15026 -9.7; 16529 -7.7; 18182 -5.4; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis 7 2019 Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis 7 2019 Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.61 | 5.1 dB  |
| Peaking | 1205 Hz  | 1.59 | 3.9 dB  |
| Peaking | 3718 Hz  | 1.74 | 3.7 dB  |
| Peaking | 8420 Hz  | 1.94 | -5.3 dB |
| Peaking | 14562 Hz | 2.11 | -5.2 dB |
| Peaking | 20 Hz    | 3.33 | 1.9 dB  |
| Peaking | 46 Hz    | 2.33 | 2.2 dB  |
| Peaking | 148 Hz   | 0.75 | -3.1 dB |
| Peaking | 5210 Hz  | 2.29 | 2.8 dB  |
| Peaking | 5592 Hz  | 5.26 | -6.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%207%202019%20Edition/SteelSeries%20Arctis%207%202019%20Edition.png)