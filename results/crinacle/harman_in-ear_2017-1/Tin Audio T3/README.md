# Tin Audio T3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.9; 25 -2.4; 28 -3.0; 31 -3.6; 34 -4.1; 37 -4.4; 41 -4.9; 45 -5.2; 49 -5.5; 54 -5.9; 60 -6.4; 66 -6.8; 72 -7.2; 79 -7.7; 87 -8.1; 96 -8.6; 106 -9.1; 116 -9.5; 128 -9.8; 141 -10.2; 155 -10.4; 170 -10.5; 187 -10.6; 206 -10.7; 227 -10.7; 249 -10.6; 274 -10.4; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.3; 442 -9.0; 486 -8.6; 535 -8.2; 588 -7.7; 647 -7.2; 712 -6.7; 783 -6.1; 861 -5.7; 947 -5.5; 1042 -5.6; 1146 -6.0; 1261 -6.3; 1387 -6.3; 1526 -6.1; 1678 -5.8; 1846 -5.6; 2031 -5.4; 2234 -5.0; 2457 -4.4; 2703 -2.4; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -2.8; 5267 -4.0; 5793 -3.5; 6373 -2.8; 7010 -5.3; 7711 -8.9; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -7.2; 12418 -10.9; 13660 -16.5; 15026 -19.1; 16529 -17.7; 18182 -15.2; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.54 | 6.4 dB   |
| Peaking | 199 Hz   | 0.58 | -4.5 dB  |
| Peaking | 3901 Hz  | 1.02 | 7.1 dB   |
| Peaking | 11083 Hz | 1.72 | 7.3 dB   |
| Peaking | 15207 Hz | 0.63 | -14.2 dB |
| Peaking | 909 Hz   | 2.71 | 1.6 dB   |
| Peaking | 2753 Hz  | 0.97 | -1.9 dB  |
| Peaking | 3018 Hz  | 3.32 | 3.2 dB   |
| Peaking | 6462 Hz  | 5.86 | 3.2 dB   |
| Peaking | 7747 Hz  | 8.27 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB   |
| Peaking | 62 Hz    | 1.41 | -0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 16000 Hz | 1.41 | -15.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Tin%20Audio%20T3/Tin%20Audio%20T3.png)