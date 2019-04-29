# Advanced Evo X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.3; 25 -5.5; 28 -5.8; 31 -6.0; 34 -6.2; 37 -6.4; 41 -6.6; 45 -6.8; 49 -7.0; 54 -7.2; 60 -7.5; 66 -7.8; 72 -8.2; 79 -8.5; 87 -8.8; 96 -9.3; 106 -9.5; 116 -9.9; 128 -10.1; 141 -10.3; 155 -10.5; 170 -10.5; 187 -10.5; 206 -10.4; 227 -10.3; 249 -10.0; 274 -9.8; 302 -9.4; 332 -9.0; 365 -8.4; 402 -7.9; 442 -7.3; 486 -6.9; 535 -5.7; 588 -4.8; 647 -5.4; 712 -5.2; 783 -5.0; 861 -4.8; 947 -4.8; 1042 -5.2; 1146 -5.9; 1261 -6.6; 1387 -6.9; 1526 -7.1; 1678 -7.2; 1846 -7.3; 2031 -7.0; 2234 -6.0; 2457 -4.5; 2703 -3.5; 2973 -2.1; 3270 -1.0; 3597 -0.5; 3957 -0.7; 4353 -1.7; 4788 -3.6; 5267 -6.7; 5793 -8.9; 6373 -5.7; 7010 -4.1; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.6; 15026 -20.7; 16529 -23.2; 18182 -16.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced Evo X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced Evo X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.18 | 1.6 dB   |
| Peaking | 430 Hz   | 0.18 | -6.3 dB  |
| Peaking | 705 Hz   | 0.67 | 7.6 dB   |
| Peaking | 3530 Hz  | 1.58 | 7.7 dB   |
| Peaking | 16482 Hz | 1.68 | -19.2 dB |
| Peaking | 4536 Hz  | 4.96 | 1.5 dB   |
| Peaking | 5782 Hz  | 4.1  | -4.6 dB  |
| Peaking | 6764 Hz  | 5.41 | 3.8 dB   |
| Peaking | 12479 Hz | 1.79 | 5.3 dB   |
| Peaking | 14418 Hz | 2.73 | -6.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -17.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20Evo%20X/Advanced%20Evo%20X.png)