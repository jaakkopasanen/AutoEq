# RHA MA750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.2; 25 -4.4; 28 -4.7; 31 -4.9; 34 -5.0; 37 -5.1; 41 -5.2; 45 -5.3; 49 -5.4; 54 -5.5; 60 -5.7; 66 -5.9; 72 -6.0; 79 -6.3; 87 -6.5; 96 -6.8; 106 -7.1; 116 -7.4; 128 -7.6; 141 -7.8; 155 -8.0; 170 -8.1; 187 -8.2; 206 -8.2; 227 -8.2; 249 -8.1; 274 -8.1; 302 -8.0; 332 -7.9; 365 -7.7; 402 -7.6; 442 -7.4; 486 -7.1; 535 -6.8; 588 -6.5; 647 -6.0; 712 -5.5; 783 -4.9; 861 -4.3; 947 -3.9; 1042 -3.7; 1146 -3.8; 1261 -4.0; 1387 -3.8; 1526 -3.3; 1678 -2.4; 1846 -1.4; 2031 -0.8; 2234 -0.5; 2457 -0.8; 2703 -1.7; 2973 -3.2; 3270 -4.9; 3597 -5.7; 3957 -6.0; 4353 -6.3; 4788 -7.6; 5267 -8.3; 5793 -5.1; 6373 -1.8; 7010 -2.8; 7711 -5.7; 8482 -6.1; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -8.5; 15026 -13.4; 16529 -14.7; 18182 -16.0; 20000 -16.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA MA750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA MA750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.85 | 2.2 dB   |
| Peaking | 215 Hz   | 0.6  | -3.1 dB  |
| Peaking | 2090 Hz  | 1.74 | 5.2 dB   |
| Peaking | 6638 Hz  | 7.82 | 4.9 dB   |
| Peaking | 18762 Hz | 0.62 | -12.4 dB |
| Peaking | 976 Hz   | 3.48 | 1.6 dB   |
| Peaking | 2604 Hz  | 8.35 | 1.3 dB   |
| Peaking | 4935 Hz  | 3.81 | -3.4 dB  |
| Peaking | 12864 Hz | 1.5  | 4.9 dB   |
| Peaking | 14876 Hz | 2.05 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB   |
| Peaking | 62 Hz    | 1.41 | -0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -11.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/RHA%20MA750/RHA%20MA750.png)