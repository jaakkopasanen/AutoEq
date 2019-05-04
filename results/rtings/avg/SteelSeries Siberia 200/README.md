# SteelSeries Siberia 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.2; 25 -4.7; 28 -5.4; 31 -5.9; 34 -6.2; 37 -6.4; 41 -6.6; 45 -6.7; 49 -6.7; 54 -6.7; 60 -6.8; 66 -6.9; 72 -6.9; 79 -6.9; 87 -7.0; 96 -7.0; 106 -7.1; 116 -7.2; 128 -7.2; 141 -7.2; 155 -7.1; 170 -6.8; 187 -6.8; 206 -6.9; 227 -7.0; 249 -7.4; 274 -7.4; 302 -7.1; 332 -6.8; 365 -6.5; 402 -6.4; 442 -6.2; 486 -5.8; 535 -5.2; 588 -4.0; 647 -2.3; 712 -0.9; 783 -0.5; 861 -1.0; 947 -2.2; 1042 -2.2; 1146 -3.1; 1261 -3.4; 1387 -3.0; 1526 -2.9; 1678 -3.8; 1846 -5.5; 2031 -7.1; 2234 -7.4; 2457 -6.9; 2703 -6.7; 2973 -5.6; 3270 -0.7; 3597 -2.7; 3957 -3.9; 4353 -2.4; 4788 -2.6; 5267 -4.2; 5793 -5.0; 6373 -4.1; 7010 -5.6; 7711 -8.8; 8482 -9.2; 9330 -6.2; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Siberia 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Siberia 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 794 Hz  |  3.4  | 4.4 dB  |
| Peaking | 2417 Hz |  1.64 | -8.2 dB |
| Peaking | 2539 Hz |  0.67 | 5.5 dB  |
| Peaking | 3350 Hz | 11.17 | 4.2 dB  |
| Peaking | 8121 Hz |  4.26 | -5.5 dB |
| Peaking | 20 Hz   |  2.11 | 2.2 dB  |
| Peaking | 186 Hz  |  0.17 | -2.2 dB |
| Peaking | 855 Hz  |  0.86 | 1.8 dB  |
| Peaking | 4411 Hz |  2.58 | -1.5 dB |
| Peaking | 4505 Hz |  5.84 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Siberia%20200/SteelSeries%20Siberia%20200.png)