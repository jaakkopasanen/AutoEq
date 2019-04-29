# KZ ED16
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.1; 23 -13.1; 25 -13.2; 28 -13.2; 31 -13.1; 34 -13.1; 37 -13.0; 41 -13.0; 45 -12.9; 49 -12.9; 54 -12.8; 60 -12.7; 66 -12.6; 72 -12.7; 79 -12.7; 87 -12.7; 96 -12.7; 106 -12.7; 116 -12.6; 128 -12.5; 141 -12.3; 155 -12.1; 170 -11.8; 187 -11.5; 206 -11.1; 227 -10.7; 249 -10.3; 274 -9.9; 302 -9.3; 332 -8.7; 365 -8.2; 402 -7.7; 442 -7.3; 486 -6.8; 535 -6.4; 588 -6.0; 647 -5.7; 712 -5.3; 783 -4.9; 861 -4.8; 947 -5.1; 1042 -5.7; 1146 -6.7; 1261 -7.6; 1387 -8.4; 1526 -9.0; 1678 -9.6; 1846 -9.9; 2031 -8.7; 2234 -6.3; 2457 -3.7; 2703 -2.1; 2973 -2.2; 3270 -3.2; 3597 -3.6; 3957 -1.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.9; 8482 -10.3; 9330 -10.4; 10263 -10.6; 11289 -9.5; 12418 -10.8; 13660 -19.1; 15026 -26.0; 16529 -22.3; 18182 -16.0; 20000 -18.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ED16 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ED16 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.24 | -6.5 dB  |
| Peaking | 162 Hz   | 0.88 | -3.3 dB  |
| Peaking | 4419 Hz  | 1.5  | 6.3 dB   |
| Peaking | 6147 Hz  | 3.42 | 5.1 dB   |
| Peaking | 15835 Hz | 1.04 | -19.8 dB |
| Peaking | 864 Hz   | 1.52 | 2.9 dB   |
| Peaking | 1854 Hz  | 1.23 | -5.0 dB  |
| Peaking | 2620 Hz  | 2.98 | 5.6 dB   |
| Peaking | 8474 Hz  | 5.5  | -2.3 dB  |
| Peaking | 11925 Hz | 5.12 | 5.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -22.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20ED16/KZ%20ED16.png)