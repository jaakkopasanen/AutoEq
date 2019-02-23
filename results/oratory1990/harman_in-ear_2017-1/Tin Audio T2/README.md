# Tin Audio T2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -2.0; 31 -2.4; 34 -2.8; 37 -3.2; 41 -3.6; 45 -4.0; 49 -4.3; 54 -4.7; 60 -5.2; 66 -5.6; 72 -6.0; 79 -6.5; 87 -7.0; 96 -7.5; 106 -8.0; 116 -8.4; 128 -8.8; 141 -9.2; 155 -9.5; 170 -9.6; 187 -9.7; 206 -9.7; 227 -9.9; 249 -10.1; 274 -10.1; 302 -10.0; 332 -9.8; 365 -9.6; 402 -9.4; 442 -9.3; 486 -9.0; 535 -8.7; 588 -8.4; 647 -8.0; 712 -7.6; 783 -7.2; 861 -6.8; 947 -7.2; 1042 -7.1; 1146 -6.8; 1261 -6.4; 1387 -5.8; 1526 -4.9; 1678 -4.0; 1846 -3.1; 2031 -2.1; 2234 -1.4; 2457 -1.3; 2703 -2.0; 2973 -2.4; 3270 -2.4; 3597 -2.4; 3957 -2.8; 4353 -3.9; 4788 -5.9; 5267 -6.5; 5793 -3.6; 6373 -1.4; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -7.9; 12418 -11.2; 13660 -17.0; 15026 -24.6; 16529 -25.7; 18182 -22.2; 20000 -24.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.25 | 6.1 dB   |
| Peaking | 1802 Hz  | 0.14 | 11.8 dB  |
| Peaking | 2929 Hz  | 0.32 | 17.2 dB  |
| Peaking | 6643 Hz  | 0.04 | -26.0 dB |
| Peaking | 10123 Hz | 0.87 | 13.1 dB  |
| Peaking | 5104 Hz  | 4.12 | -3.6 dB  |
| Peaking | 6381 Hz  | 4.37 | 4.9 dB   |
| Peaking | 8891 Hz  | 1.45 | -4.6 dB  |
| Peaking | 14463 Hz | 0.45 | 5.9 dB   |
| Peaking | 15342 Hz | 1.8  | -10.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB   |
| Peaking | 62 Hz    | 1.41 | 0.6 dB   |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 16000 Hz | 1.41 | -25.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Tin%20Audio%20T2/Tin%20Audio%20T2.png)