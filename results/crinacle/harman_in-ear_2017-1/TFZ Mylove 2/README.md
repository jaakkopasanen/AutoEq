# TFZ Mylove 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.4; 25 -10.4; 28 -10.3; 31 -10.1; 34 -9.9; 37 -9.7; 41 -9.5; 45 -9.3; 49 -9.0; 54 -8.8; 60 -8.6; 66 -8.5; 72 -8.3; 79 -8.2; 87 -8.1; 96 -8.0; 106 -7.8; 116 -7.7; 128 -7.5; 141 -7.4; 155 -7.2; 170 -6.9; 187 -6.6; 206 -6.2; 227 -5.9; 249 -5.6; 274 -5.3; 302 -4.9; 332 -4.4; 365 -4.1; 402 -3.8; 442 -3.5; 486 -3.2; 535 -3.0; 588 -2.8; 647 -2.5; 712 -2.4; 783 -2.3; 861 -2.2; 947 -2.4; 1042 -3.1; 1146 -3.9; 1261 -4.6; 1387 -5.2; 1526 -5.5; 1678 -5.8; 1846 -6.2; 2031 -6.4; 2234 -6.0; 2457 -4.7; 2703 -2.9; 2973 -1.3; 3270 -0.5; 3597 -0.7; 3957 -2.0; 4353 -4.5; 4788 -6.5; 5267 -4.9; 5793 -2.0; 6373 -1.0; 7010 -4.5; 7711 -4.6; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -12.0; 16529 -18.6; 18182 -16.6; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Mylove 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Mylove 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.34 | -6.1 dB  |
| Peaking | 134 Hz   | 1.26 | -2.0 dB  |
| Peaking | 6202 Hz  | 6.23 | 4.0 dB   |
| Peaking | 13396 Hz | 0.86 | 10.2 dB  |
| Peaking | 16714 Hz | 0.74 | -20.1 dB |
| Peaking | 232 Hz   | 2.02 | -0.8 dB  |
| Peaking | 840 Hz   | 0.83 | 3.1 dB   |
| Peaking | 2204 Hz  | 0.77 | -5.2 dB  |
| Peaking | 3249 Hz  | 1.52 | 7.6 dB   |
| Peaking | 4743 Hz  | 5.24 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -13.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%20Mylove%202/TFZ%20Mylove%202.png)