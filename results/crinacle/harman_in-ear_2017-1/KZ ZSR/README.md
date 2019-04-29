# KZ ZSR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.1; 25 -8.5; 28 -9.0; 31 -9.4; 34 -9.7; 37 -10.0; 41 -10.2; 45 -10.5; 49 -10.7; 54 -10.9; 60 -11.1; 66 -11.3; 72 -11.6; 79 -11.8; 87 -12.0; 96 -12.2; 106 -12.4; 116 -12.5; 128 -12.4; 141 -12.4; 155 -12.3; 170 -12.1; 187 -11.8; 206 -11.5; 227 -11.2; 249 -10.7; 274 -10.3; 302 -9.8; 332 -9.2; 365 -8.6; 402 -8.2; 442 -7.8; 486 -7.3; 535 -6.9; 588 -6.4; 647 -6.1; 712 -5.7; 783 -5.3; 861 -5.1; 947 -5.3; 1042 -5.4; 1146 -5.9; 1261 -6.7; 1387 -7.1; 1526 -7.3; 1678 -7.2; 1846 -6.7; 2031 -5.5; 2234 -3.7; 2457 -2.0; 2703 -0.8; 2973 -0.5; 3270 -0.9; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -0.8; 5267 -0.9; 5793 -0.5; 6373 -1.1; 7010 -5.6; 7711 -11.3; 8482 -12.5; 9330 -12.3; 10263 -13.4; 11289 -13.6; 12418 -16.2; 13660 -24.3; 15026 -28.2; 16529 -24.5; 18182 -25.3; 20000 -38.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZSR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZSR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 75 Hz    | 0.46 | -4.6 dB  |
| Peaking | 186 Hz   | 0.91 | -3.3 dB  |
| Peaking | 4491 Hz  | 0.9  | 9.1 dB   |
| Peaking | 14633 Hz | 2.76 | -10.3 dB |
| Peaking | 20221 Hz | 0.33 | -31.5 dB |
| Peaking | 1700 Hz  | 3.31 | -2.5 dB  |
| Peaking | 2697 Hz  | 3.37 | 2.9 dB   |
| Peaking | 6410 Hz  | 2.98 | 10.3 dB  |
| Peaking | 7118 Hz  | 1.32 | -7.4 dB  |
| Peaking | 11501 Hz | 2.6  | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 9.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -33.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20ZSR/KZ%20ZSR.png)