# Tin Audio T2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.2; 41 -1.8; 45 -2.2; 49 -2.7; 54 -3.3; 60 -3.8; 66 -4.3; 72 -4.8; 79 -5.3; 87 -5.9; 96 -6.5; 106 -7.1; 116 -7.6; 128 -8.1; 141 -8.6; 155 -9.0; 170 -9.3; 187 -9.6; 206 -9.9; 227 -10.0; 249 -10.2; 274 -10.3; 302 -10.3; 332 -10.1; 365 -10.0; 402 -9.9; 442 -9.7; 486 -9.5; 535 -9.2; 588 -8.9; 647 -8.4; 712 -7.9; 783 -7.4; 861 -6.9; 947 -6.4; 1042 -6.5; 1146 -6.9; 1261 -7.0; 1387 -6.7; 1526 -6.1; 1678 -5.5; 1846 -4.9; 2031 -4.4; 2234 -4.2; 2457 -4.6; 2703 -5.0; 2973 -4.0; 3270 -2.5; 3597 -2.0; 3957 -2.8; 4353 -3.2; 4788 -4.5; 5267 -3.6; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -9.1; 12418 -13.3; 13660 -20.2; 15026 -28.2; 16529 -29.2; 18182 -25.3; 20000 -23.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.43 | 6.3 dB   |
| Peaking | 265 Hz   | 0.43 | -4.2 dB  |
| Peaking | 6168 Hz  | 0.43 | 15.4 dB  |
| Peaking | 11552 Hz | 1.24 | 10.6 dB  |
| Peaking | 15366 Hz | 0.32 | -30.4 dB |
| Peaking | 2817 Hz  | 5.95 | -1.5 dB  |
| Peaking | 3384 Hz  | 3.34 | 1.6 dB   |
| Peaking | 4983 Hz  | 3.97 | -4.5 dB  |
| Peaking | 6014 Hz  | 2.27 | 3.8 dB   |
| Peaking | 7564 Hz  | 4.34 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB   |
| Peaking | 62 Hz    | 1.41 | 1.9 dB   |
| Peaking | 125 Hz   | 1.41 | -1.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 16000 Hz | 1.41 | -31.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Tin%20Audio%20T2/Tin%20Audio%20T2.png)