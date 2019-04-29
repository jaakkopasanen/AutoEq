# Advanced M51D
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.2; 37 -1.6; 41 -2.1; 45 -2.5; 49 -2.9; 54 -3.3; 60 -3.7; 66 -4.1; 72 -4.6; 79 -5.1; 87 -5.7; 96 -6.2; 106 -6.7; 116 -7.2; 128 -7.7; 141 -8.1; 155 -8.6; 170 -8.9; 187 -9.2; 206 -9.5; 227 -9.7; 249 -10.0; 274 -10.3; 302 -10.4; 332 -10.5; 365 -10.5; 402 -10.7; 442 -10.7; 486 -10.5; 535 -10.3; 588 -9.8; 647 -9.3; 712 -8.6; 783 -7.8; 861 -7.1; 947 -6.8; 1042 -7.0; 1146 -7.5; 1261 -8.1; 1387 -8.5; 1526 -8.5; 1678 -8.4; 1846 -8.3; 2031 -7.6; 2234 -6.3; 2457 -4.4; 2703 -2.7; 2973 -1.5; 3270 -1.3; 3597 -2.3; 3957 -4.4; 4353 -5.1; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -16.1; 16529 -24.3; 18182 -27.5; 20000 -25.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced M51D GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced M51D ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.35 | 6.2 dB   |
| Peaking | 327 Hz   | 0.41 | -4.2 dB  |
| Peaking | 5648 Hz  | 0.68 | 11.2 dB  |
| Peaking | 13129 Hz | 1.09 | 16.3 dB  |
| Peaking | 17642 Hz | 0.27 | -25.7 dB |
| Peaking | 942 Hz   | 2.47 | 2.4 dB   |
| Peaking | 2001 Hz  | 0.92 | -6.3 dB  |
| Peaking | 3143 Hz  | 0.84 | 7.9 dB   |
| Peaking | 4201 Hz  | 3.2  | -7.5 dB  |
| Peaking | 7648 Hz  | 4.26 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB   |
| Peaking | 62 Hz    | 1.41 | 1.8 dB   |
| Peaking | 125 Hz   | 1.41 | -1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -19.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20M51D/Advanced%20M51D.png)