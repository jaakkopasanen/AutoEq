# KZ ES4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.3; 25 -12.4; 28 -12.5; 31 -12.6; 34 -12.6; 37 -12.6; 41 -12.6; 45 -12.6; 49 -12.6; 54 -12.6; 60 -12.6; 66 -12.6; 72 -12.6; 79 -12.7; 87 -12.7; 96 -12.8; 106 -12.8; 116 -12.8; 128 -12.7; 141 -12.5; 155 -12.3; 170 -12.0; 187 -11.7; 206 -11.3; 227 -10.9; 249 -10.4; 274 -9.9; 302 -9.4; 332 -8.8; 365 -8.2; 402 -7.7; 442 -7.3; 486 -6.8; 535 -6.3; 588 -5.9; 647 -5.5; 712 -5.1; 783 -4.7; 861 -4.5; 947 -4.5; 1042 -5.1; 1146 -5.8; 1261 -6.6; 1387 -7.1; 1526 -7.5; 1678 -8.1; 1846 -8.8; 2031 -9.6; 2234 -10.1; 2457 -9.4; 2703 -7.8; 2973 -6.4; 3270 -6.4; 3597 -7.8; 3957 -7.3; 4353 -1.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.6; 13660 -16.8; 15026 -19.9; 16529 -20.6; 18182 -25.5; 20000 -27.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ES4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ES4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 64 Hz    | 0.17 | -6.5 dB  |
| Peaking | 837 Hz   | 0.7  | 5.2 dB   |
| Peaking | 2995 Hz  | 0.44 | -12.6 dB |
| Peaking | 5268 Hz  | 0.52 | 17.0 dB  |
| Peaking | 19132 Hz | 0.33 | -21.8 dB |
| Peaking | 3856 Hz  | 5.23 | -7.2 dB  |
| Peaking | 4004 Hz  | 1.96 | 3.9 dB   |
| Peaking | 7765 Hz  | 3.71 | -3.2 dB  |
| Peaking | 11695 Hz | 2.54 | 4.8 dB   |
| Peaking | 14184 Hz | 2.98 | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 16000 Hz | 1.41 | -21.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20ES4/KZ%20ES4.png)