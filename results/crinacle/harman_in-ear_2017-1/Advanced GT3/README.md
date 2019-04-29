# Advanced GT3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.3; 25 -9.2; 28 -9.1; 31 -9.0; 34 -9.0; 37 -9.0; 41 -8.9; 45 -8.8; 49 -8.7; 54 -8.7; 60 -8.6; 66 -8.7; 72 -8.9; 79 -9.0; 87 -9.2; 96 -9.5; 106 -9.7; 116 -9.9; 128 -10.0; 141 -10.1; 155 -10.2; 170 -10.3; 187 -10.2; 206 -10.1; 227 -10.0; 249 -9.9; 274 -9.6; 302 -9.3; 332 -8.9; 365 -8.5; 402 -8.1; 442 -7.7; 486 -7.2; 535 -6.6; 588 -6.1; 647 -5.5; 712 -4.9; 783 -4.2; 861 -3.7; 947 -3.4; 1042 -3.4; 1146 -3.7; 1261 -3.9; 1387 -3.7; 1526 -3.0; 1678 -2.3; 1846 -1.7; 2031 -1.1; 2234 -0.5; 2457 -0.5; 2703 -0.7; 2973 -1.6; 3270 -3.0; 3597 -4.4; 3957 -4.7; 4353 -5.2; 4788 -7.2; 5267 -9.8; 5793 -11.2; 6373 -8.8; 7010 -6.5; 7711 -8.4; 8482 -11.7; 9330 -10.7; 10263 -6.8; 11289 -6.5; 12418 -10.1; 13660 -21.4; 15026 -30.8; 16529 -33.1; 18182 -33.4; 20000 -36.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 134 Hz   | 0.34 | -3.7 dB  |
| Peaking | 2358 Hz  | 0.59 | 7.3 dB   |
| Peaking | 11699 Hz | 1.34 | 20.8 dB  |
| Peaking | 15264 Hz | 0.47 | -25.2 dB |
| Peaking | 20205 Hz | 0.47 | -22.5 dB |
| Peaking | 22 Hz    | 1.84 | -2.2 dB  |
| Peaking | 860 Hz   | 2.11 | 1.5 dB   |
| Peaking | 1380 Hz  | 3.1  | -1.6 dB  |
| Peaking | 5646 Hz  | 5.93 | -3.6 dB  |
| Peaking | 7068 Hz  | 7.04 | 4.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -36.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20GT3/Advanced%20GT3.png)