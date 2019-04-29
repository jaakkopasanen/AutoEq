# Vsonic GR07 BE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.4; 25 -5.6; 28 -5.9; 31 -6.1; 34 -6.2; 37 -6.3; 41 -6.5; 45 -6.6; 49 -6.7; 54 -6.9; 60 -7.0; 66 -7.2; 72 -7.5; 79 -7.8; 87 -8.1; 96 -8.4; 106 -8.6; 116 -9.0; 128 -9.2; 141 -9.4; 155 -9.7; 170 -9.8; 187 -9.9; 206 -10.0; 227 -10.1; 249 -10.1; 274 -10.1; 302 -10.0; 332 -9.9; 365 -9.7; 402 -9.7; 442 -9.7; 486 -9.5; 535 -9.4; 588 -9.2; 647 -9.0; 712 -8.7; 783 -8.3; 861 -8.0; 947 -7.9; 1042 -7.9; 1146 -8.2; 1261 -8.3; 1387 -8.1; 1526 -7.4; 1678 -6.5; 1846 -5.6; 2031 -5.0; 2234 -3.9; 2457 -2.9; 2703 -1.8; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.0; 5793 -3.6; 6373 -4.4; 7010 -4.1; 7711 -6.2; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.9; 15026 -21.4; 16529 -22.7; 18182 -25.2; 20000 -29.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vsonic GR07 BE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vsonic GR07 BE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 261 Hz   | 0.36 | -3.7 dB  |
| Peaking | 1335 Hz  | 3.18 | -1.6 dB  |
| Peaking | 3124 Hz  | 1.62 | 5.9 dB   |
| Peaking | 4824 Hz  | 2.79 | 4.8 dB   |
| Peaking | 14 Hz    | 0.81 | 2.1 dB   |
| Peaking | 61 Hz    | 1.38 | 0.4 dB   |
| Peaking | 7533 Hz  | 0.57 | 7.9 dB   |
| Peaking | 11943 Hz | 2.14 | 10.0 dB  |
| Peaking | 19764 Hz | 0.12 | -21.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB   |
| Peaking | 62 Hz    | 1.41 | -0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -21.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Vsonic%20GR07%20BE/Vsonic%20GR07%20BE.png)