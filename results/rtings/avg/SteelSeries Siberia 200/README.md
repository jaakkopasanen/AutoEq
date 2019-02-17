# SteelSeries Siberia 200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.6; 25 -5.1; 28 -5.7; 31 -6.2; 34 -6.5; 37 -6.7; 41 -6.9; 45 -7.0; 49 -7.0; 54 -7.0; 60 -7.1; 66 -7.2; 72 -7.3; 79 -7.3; 87 -7.3; 96 -7.4; 106 -7.5; 116 -7.5; 128 -7.6; 141 -7.5; 155 -7.4; 170 -7.1; 187 -7.1; 206 -7.2; 227 -7.3; 249 -7.6; 274 -7.6; 302 -7.3; 332 -7.0; 365 -6.7; 402 -6.5; 442 -6.4; 486 -5.9; 535 -5.3; 588 -4.0; 647 -2.4; 712 -0.9; 783 -0.5; 861 -0.9; 947 -2.3; 1042 -2.1; 1146 -3.1; 1261 -3.2; 1387 -3.0; 1526 -2.8; 1678 -3.7; 1846 -5.3; 2031 -6.8; 2234 -6.7; 2457 -6.1; 2703 -6.2; 2973 -5.8; 3270 -0.8; 3597 -3.2; 3957 -4.2; 4353 -3.0; 4788 -2.3; 5267 -4.0; 5793 -5.1; 6373 -5.3; 7010 -5.5; 7711 -8.1; 8482 -9.7; 9330 -8.0; 10263 -3.9; 11289 -2.4; 12418 -3.5; 13660 -3.2; 15026 -2.4; 16529 -2.4; 18182 -2.6; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Siberia 200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Siberia 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 78 Hz    |  0.29 | -4.8 dB |
| Peaking | 397 Hz   |  0.71 | -3.1 dB |
| Peaking | 759 Hz   |  2.23 | 4.3 dB  |
| Peaking | 2269 Hz  |  2.33 | -4.5 dB |
| Peaking | 8368 Hz  |  2.57 | -7.5 dB |
| Peaking | 2923 Hz  |  7.38 | -2.1 dB |
| Peaking | 3323 Hz  | 12.72 | 4.4 dB  |
| Peaking | 5899 Hz  |  8.36 | -1.7 dB |
| Peaking | 10909 Hz |  7.52 | 1.9 dB  |
| Peaking | 20017 Hz |  2.33 | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Siberia%20200/SteelSeries%20Siberia%20200.png)