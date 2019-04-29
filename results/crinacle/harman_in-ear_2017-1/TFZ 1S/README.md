# TFZ 1S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.6; 25 -11.7; 28 -11.9; 31 -12.0; 34 -12.1; 37 -12.2; 41 -12.2; 45 -12.3; 49 -12.3; 54 -12.3; 60 -12.4; 66 -12.4; 72 -12.5; 79 -12.6; 87 -12.7; 96 -12.8; 106 -12.8; 116 -12.7; 128 -12.7; 141 -12.5; 155 -12.3; 170 -12.1; 187 -11.7; 206 -11.4; 227 -11.0; 249 -10.6; 274 -10.1; 302 -9.6; 332 -9.1; 365 -8.7; 402 -8.3; 442 -8.0; 486 -7.7; 535 -7.5; 588 -7.1; 647 -6.8; 712 -6.6; 783 -6.6; 861 -6.8; 947 -7.1; 1042 -7.6; 1146 -8.4; 1261 -9.1; 1387 -9.7; 1526 -9.9; 1678 -9.8; 1846 -9.2; 2031 -7.5; 2234 -5.1; 2457 -2.6; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -2.0; 4353 -2.5; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -18.6; 16529 -21.6; 18182 -15.9; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ 1S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ 1S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.56 | -4.0 dB  |
| Peaking | 120 Hz   | 0.41 | -5.7 dB  |
| Peaking | 4882 Hz  | 0.95 | 7.6 dB   |
| Peaking | 13324 Hz | 1.31 | 12.8 dB  |
| Peaking | 15772 Hz | 0.85 | -22.0 dB |
| Peaking | 1678 Hz  | 1.86 | -5.4 dB  |
| Peaking | 2801 Hz  | 1.93 | 4.5 dB   |
| Peaking | 4292 Hz  | 4.42 | -3.2 dB  |
| Peaking | 6571 Hz  | 3.17 | 2.4 dB   |
| Peaking | 7414 Hz  | 4.27 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -15.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%201S/TFZ%201S.png)