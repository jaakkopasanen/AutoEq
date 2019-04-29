# TFZ 5S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.7; 25 -11.8; 28 -11.9; 31 -12.0; 34 -12.0; 37 -12.1; 41 -12.1; 45 -12.2; 49 -12.2; 54 -12.2; 60 -12.3; 66 -12.4; 72 -12.6; 79 -12.7; 87 -12.8; 96 -13.0; 106 -13.0; 116 -13.1; 128 -13.0; 141 -12.9; 155 -12.8; 170 -12.5; 187 -12.2; 206 -11.9; 227 -11.5; 249 -11.0; 274 -10.6; 302 -10.0; 332 -9.4; 365 -8.7; 402 -8.2; 442 -7.6; 486 -7.0; 535 -6.4; 588 -5.9; 647 -5.6; 712 -5.6; 783 -5.8; 861 -6.1; 947 -6.8; 1042 -7.6; 1146 -8.6; 1261 -9.4; 1387 -10.1; 1526 -10.6; 1678 -10.9; 1846 -10.8; 2031 -9.4; 2234 -6.8; 2457 -3.9; 2703 -1.8; 2973 -0.7; 3270 -0.8; 3597 -2.3; 3957 -4.8; 4353 -4.4; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -19.1; 16529 -26.3; 18182 -23.2; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ 5S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ 5S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.25 | -5.3 dB  |
| Peaking | 165 Hz   | 0.75 | -3.8 dB  |
| Peaking | 5510 Hz  | 1.08 | 8.5 dB   |
| Peaking | 13040 Hz | 1.24 | 14.1 dB  |
| Peaking | 16490 Hz | 0.66 | -25.7 dB |
| Peaking | 721 Hz   | 1.56 | 2.6 dB   |
| Peaking | 1824 Hz  | 1.12 | -7.4 dB  |
| Peaking | 2877 Hz  | 1.59 | 8.1 dB   |
| Peaking | 4193 Hz  | 4.38 | -4.9 dB  |
| Peaking | 4710 Hz  | 5.22 | 0.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 16000 Hz | 1.41 | -19.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%205S/TFZ%205S.png)