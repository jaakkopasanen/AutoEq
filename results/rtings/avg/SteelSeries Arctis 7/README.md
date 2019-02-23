# SteelSeries Arctis 7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.9; 28 -3.9; 31 -3.7; 34 -3.5; 37 -3.2; 41 -3.0; 45 -3.3; 49 -3.8; 54 -4.5; 60 -5.4; 66 -6.3; 72 -7.1; 79 -7.7; 87 -8.3; 96 -8.8; 106 -9.1; 116 -9.4; 128 -9.5; 141 -9.7; 155 -9.7; 170 -9.6; 187 -9.3; 206 -9.0; 227 -8.9; 249 -8.8; 274 -8.4; 302 -8.1; 332 -8.0; 365 -7.9; 402 -7.6; 442 -7.1; 486 -6.6; 535 -6.0; 588 -5.4; 647 -5.0; 712 -4.1; 783 -3.5; 861 -3.5; 947 -3.3; 1042 -2.7; 1146 -2.7; 1261 -3.2; 1387 -4.1; 1526 -4.9; 1678 -6.4; 1846 -7.5; 2031 -7.7; 2234 -7.1; 2457 -6.4; 2703 -5.9; 2973 -6.1; 3270 -6.3; 3597 -6.8; 3957 -5.4; 4353 -3.1; 4788 -0.5; 5267 -5.0; 5793 -6.6; 6373 -4.7; 7010 -4.2; 7711 -6.0; 8482 -6.6; 9330 -6.5; 10263 -6.3; 11289 -6.8; 12418 -8.6; 13660 -7.9; 15026 -6.4; 16529 -6.6; 18182 -6.4; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis 7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis 7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.65 | 6.2 dB  |
| Peaking | 100 Hz   | 0.41 | -5.2 dB |
| Peaking | 972 Hz   | 1.33 | 4.5 dB  |
| Peaking | 4732 Hz  | 5.2  | 6.5 dB  |
| Peaking | 4922 Hz  | 0.11 | -0.6 dB |
| Peaking | 941 Hz   | 4.23 | -1.7 dB |
| Peaking | 1211 Hz  | 1.07 | 1.3 dB  |
| Peaking | 1902 Hz  | 3.59 | -2.5 dB |
| Peaking | 6924 Hz  | 6.92 | 2.6 dB  |
| Peaking | 12810 Hz | 5.77 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%207/SteelSeries%20Arctis%207.png)