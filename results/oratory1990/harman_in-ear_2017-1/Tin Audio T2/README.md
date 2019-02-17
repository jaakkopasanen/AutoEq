# Tin Audio T2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.1; 31 -1.5; 34 -1.9; 37 -2.3; 41 -2.7; 45 -3.1; 49 -3.4; 54 -3.8; 60 -4.3; 66 -4.7; 72 -5.1; 79 -5.6; 87 -6.1; 96 -6.6; 106 -7.1; 116 -7.5; 128 -7.9; 141 -8.3; 155 -8.6; 170 -8.7; 187 -8.8; 206 -8.8; 227 -9.0; 249 -9.2; 274 -9.2; 302 -9.1; 332 -8.9; 365 -8.7; 402 -8.5; 442 -8.4; 486 -8.1; 535 -7.8; 588 -7.5; 647 -7.1; 712 -6.7; 783 -6.3; 861 -5.9; 947 -6.3; 1042 -6.2; 1146 -5.9; 1261 -5.5; 1387 -4.9; 1526 -4.0; 1678 -3.1; 1846 -2.2; 2031 -1.2; 2234 -0.5; 2457 -0.5; 2703 -1.1; 2973 -1.5; 3270 -1.5; 3597 -1.5; 3957 -1.9; 4353 -2.9; 4788 -5.0; 5267 -5.6; 5793 -2.7; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.1; 12418 -10.3; 13660 -16.1; 15026 -23.7; 16529 -24.8; 18182 -21.3; 20000 -23.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.65 | 6.0 dB   |
| Peaking | 2388 Hz  | 0.28 | 24.7 dB  |
| Peaking | 6727 Hz  | 0.54 | 20.1 dB  |
| Peaking | 7727 Hz  | 0.09 | -33.5 dB |
| Peaking | 11284 Hz | 1.72 | 11.9 dB  |
| Peaking | 735 Hz   | 3.07 | 1.3 dB   |
| Peaking | 3871 Hz  | 4.1  | 1.3 dB   |
| Peaking | 5088 Hz  | 8.29 | -3.0 dB  |
| Peaking | 15612 Hz | 3.95 | -4.2 dB  |
| Peaking | 18327 Hz | 2.17 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 1.4 dB   |
| Peaking | 125 Hz   | 1.41 | -1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 16000 Hz | 1.41 | -23.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Tin%20Audio%20T2/Tin%20Audio%20T2.png)