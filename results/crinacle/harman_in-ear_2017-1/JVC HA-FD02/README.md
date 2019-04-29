# JVC HA-FD02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.2; 28 -7.4; 31 -7.5; 34 -7.7; 37 -7.7; 41 -7.8; 45 -7.9; 49 -8.0; 54 -8.1; 60 -8.2; 66 -8.4; 72 -8.5; 79 -8.6; 87 -8.8; 96 -9.0; 106 -9.1; 116 -9.2; 128 -9.1; 141 -9.1; 155 -9.1; 170 -9.0; 187 -8.8; 206 -8.5; 227 -8.3; 249 -8.0; 274 -7.8; 302 -7.6; 332 -7.2; 365 -6.9; 402 -6.7; 442 -6.5; 486 -6.3; 535 -6.1; 588 -6.0; 647 -5.7; 712 -5.6; 783 -5.5; 861 -5.4; 947 -5.6; 1042 -6.1; 1146 -6.8; 1261 -7.2; 1387 -7.4; 1526 -7.4; 1678 -7.2; 1846 -7.1; 2031 -7.0; 2234 -6.9; 2457 -7.1; 2703 -7.6; 2973 -7.9; 3270 -7.9; 3597 -8.1; 3957 -8.7; 4353 -9.1; 4788 -7.1; 5267 -3.4; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.6; 13660 -15.9; 15026 -24.9; 16529 -24.8; 18182 -22.8; 20000 -26.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FD02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FD02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 69 Hz    | 0.5  | -1.6 dB  |
| Peaking | 160 Hz   | 0.92 | -1.9 dB  |
| Peaking | 3154 Hz  | 1.21 | -3.4 dB  |
| Peaking | 10355 Hz | 0.28 | 24.2 dB  |
| Peaking | 16099 Hz | 0.26 | -35.9 dB |
| Peaking | 1516 Hz  | 2.22 | -2.0 dB  |
| Peaking | 4509 Hz  | 2.38 | -6.5 dB  |
| Peaking | 6008 Hz  | 0.92 | 21.4 dB  |
| Peaking | 7152 Hz  | 0.66 | -16.4 dB |
| Peaking | 12312 Hz | 3.96 | 6.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 16000 Hz | 1.41 | -24.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JVC%20HA-FD02/JVC%20HA-FD02.png)