# SteelSeries Arctis 7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.0; 25 -3.1; 28 -3.1; 31 -2.9; 34 -2.7; 37 -2.4; 41 -2.3; 45 -2.5; 49 -3.0; 54 -3.7; 60 -4.7; 66 -5.5; 72 -6.2; 79 -6.8; 87 -7.4; 96 -7.9; 106 -8.3; 116 -8.5; 128 -8.8; 141 -8.9; 155 -8.9; 170 -8.9; 187 -8.6; 206 -8.3; 227 -8.2; 249 -8.1; 274 -7.8; 302 -7.5; 332 -7.4; 365 -7.2; 402 -7.0; 442 -6.5; 486 -6.0; 535 -5.4; 588 -4.8; 647 -4.5; 712 -3.7; 783 -3.1; 861 -3.0; 947 -2.8; 1042 -2.3; 1146 -2.2; 1261 -2.8; 1387 -3.7; 1526 -4.5; 1678 -6.0; 1846 -7.3; 2031 -7.6; 2234 -7.3; 2457 -6.7; 2703 -5.9; 2973 -5.6; 3270 -5.5; 3597 -6.0; 3957 -4.5; 4353 -2.1; 4788 -0.5; 5267 -4.7; 5793 -6.0; 6373 -3.3; 7010 -3.5; 7711 -5.4; 8482 -5.8; 9330 -5.7; 10263 -5.7; 11289 -7.2; 12418 -8.2; 13660 -6.4; 15026 -5.7; 16529 -5.8; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis 7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis 7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.65 | 6.4 dB  |
| Peaking | 101 Hz   | 0.35 | -4.8 dB |
| Peaking | 1090 Hz  | 0.91 | 4.3 dB  |
| Peaking | 1979 Hz  | 1.97 | -3.7 dB |
| Peaking | 4697 Hz  | 5.57 | 5.5 dB  |
| Peaking | 86 Hz    | 1.94 | -0.1 dB |
| Peaking | 5621 Hz  | 9.15 | -2.4 dB |
| Peaking | 6637 Hz  | 5.37 | 2.7 dB  |
| Peaking | 12275 Hz | 4.08 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%207/SteelSeries%20Arctis%207.png)