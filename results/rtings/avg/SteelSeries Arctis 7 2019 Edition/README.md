# SteelSeries Arctis 7 2019 Edition
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.2; 31 -1.3; 34 -1.3; 37 -1.4; 41 -1.8; 45 -2.4; 49 -3.1; 54 -3.8; 60 -4.5; 66 -5.3; 72 -5.8; 79 -6.3; 87 -6.7; 96 -7.1; 106 -7.4; 116 -7.7; 128 -8.0; 141 -8.1; 155 -8.2; 170 -8.1; 187 -7.9; 206 -7.6; 227 -7.3; 249 -7.4; 274 -7.3; 302 -6.8; 332 -6.2; 365 -5.8; 402 -5.8; 442 -6.0; 486 -6.0; 535 -5.7; 588 -5.2; 647 -4.6; 712 -3.6; 783 -3.2; 861 -3.4; 947 -3.0; 1042 -2.3; 1146 -1.8; 1261 -1.9; 1387 -2.3; 1526 -2.4; 1678 -3.5; 1846 -4.6; 2031 -4.6; 2234 -4.3; 2457 -3.9; 2703 -3.6; 2973 -3.1; 3270 -2.4; 3597 -2.5; 3957 -1.5; 4353 -1.7; 4788 -3.1; 5267 -7.3; 5793 -8.2; 6373 -6.2; 7010 -7.5; 7711 -9.6; 8482 -10.4; 9330 -9.3; 10263 -7.0; 11289 -6.6; 12418 -8.4; 13660 -9.7; 15026 -9.6; 16529 -7.8; 18182 -5.6; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis 7 2019 Edition GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis 7 2019 Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 28 Hz    |  1.53 | 5.2 dB  |
| Peaking | 1195 Hz  |  1.69 | 3.8 dB  |
| Peaking | 3865 Hz  |  2.2  | 4.3 dB  |
| Peaking | 8112 Hz  |  1.8  | -4.6 dB |
| Peaking | 14596 Hz |  1.75 | -4.5 dB |
| Peaking | 17 Hz    |  3.07 | 2.6 dB  |
| Peaking | 47 Hz    |  2.18 | 2.0 dB  |
| Peaking | 150 Hz   |  0.67 | -2.9 dB |
| Peaking | 746 Hz   |  4.99 | 1.4 dB  |
| Peaking | 5520 Hz  | 11.01 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%207%202019%20Edition/SteelSeries%20Arctis%207%202019%20Edition.png)