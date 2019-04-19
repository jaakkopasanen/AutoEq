# RHA MA750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.2; 25 -8.4; 28 -8.7; 31 -8.8; 34 -8.9; 37 -8.9; 41 -8.9; 45 -8.9; 49 -9.0; 54 -9.2; 60 -9.5; 66 -9.7; 72 -9.8; 79 -10.1; 87 -9.9; 96 -9.8; 106 -10.2; 116 -10.1; 128 -10.4; 141 -10.2; 155 -10.2; 170 -10.4; 187 -10.4; 206 -10.5; 227 -10.5; 249 -10.4; 274 -10.4; 302 -10.2; 332 -10.0; 365 -9.7; 402 -9.5; 442 -9.3; 486 -9.0; 535 -8.7; 588 -8.3; 647 -7.8; 712 -7.3; 783 -6.7; 861 -6.2; 947 -5.8; 1042 -5.7; 1146 -5.7; 1261 -5.6; 1387 -5.1; 1526 -4.3; 1678 -3.4; 1846 -2.4; 2031 -1.3; 2234 -0.5; 2457 -0.5; 2703 -0.7; 2973 -2.1; 3270 -3.7; 3597 -4.8; 3957 -5.5; 4353 -6.3; 4788 -7.9; 5267 -8.5; 5793 -5.1; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -18.5; 15026 -30.8; 16529 -34.6; 18182 -33.3; 20000 -28.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA MA750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA MA750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 170 Hz   | 0.17 | -3.5 dB  |
| Peaking | 535 Hz   | 0.43 | -2.8 dB  |
| Peaking | 2753 Hz  | 0.25 | 14.9 dB  |
| Peaking | 11704 Hz | 0.7  | 26.5 dB  |
| Peaking | 16065 Hz | 0.23 | -44.2 dB |
| Peaking | 1360 Hz  | 2.88 | -1.6 dB  |
| Peaking | 2422 Hz  | 2.33 | 2.9 dB   |
| Peaking | 5416 Hz  | 1.55 | -6.5 dB  |
| Peaking | 6360 Hz  | 3.24 | 9.4 dB   |
| Peaking | 18583 Hz | 2.14 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 10.5 dB  |
| Peaking | 16000 Hz | 1.41 | -35.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/RHA%20MA750/RHA%20MA750.png)