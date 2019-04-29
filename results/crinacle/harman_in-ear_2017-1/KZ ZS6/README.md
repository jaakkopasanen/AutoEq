# KZ ZS6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.4; 25 -9.6; 28 -9.9; 31 -10.2; 34 -10.3; 37 -10.5; 41 -10.7; 45 -10.8; 49 -10.9; 54 -11.0; 60 -11.2; 66 -11.3; 72 -11.5; 79 -11.7; 87 -11.9; 96 -12.1; 106 -12.2; 116 -12.3; 128 -12.3; 141 -12.3; 155 -12.3; 170 -12.1; 187 -11.9; 206 -11.6; 227 -11.3; 249 -11.0; 274 -10.6; 302 -10.1; 332 -9.5; 365 -9.0; 402 -8.5; 442 -8.1; 486 -7.6; 535 -7.1; 588 -6.6; 647 -6.2; 712 -5.7; 783 -5.4; 861 -5.1; 947 -5.1; 1042 -5.5; 1146 -6.0; 1261 -6.5; 1387 -6.6; 1526 -6.1; 1678 -5.5; 1846 -5.0; 2031 -5.1; 2234 -5.7; 2457 -6.2; 2703 -5.9; 2973 -5.3; 3270 -5.5; 3597 -5.5; 3957 -1.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.1; 8482 -10.2; 9330 -9.8; 10263 -11.2; 11289 -12.7; 12418 -16.2; 13660 -25.0; 15026 -32.3; 16529 -30.5; 18182 -25.5; 20000 -25.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 49 Hz    | 0.4  | -3.9 dB  |
| Peaking | 142 Hz   | 0.89 | -3.6 dB  |
| Peaking | 265 Hz   | 1.5  | -2.2 dB  |
| Peaking | 6661 Hz  | 0.55 | 14.5 dB  |
| Peaking | 15938 Hz | 0.42 | -29.1 dB |
| Peaking | 833 Hz   | 3.08 | 1.6 dB   |
| Peaking | 3545 Hz  | 1.55 | -6.4 dB  |
| Peaking | 4236 Hz  | 1.63 | 6.7 dB   |
| Peaking | 8085 Hz  | 5.07 | -4.7 dB  |
| Peaking | 11646 Hz | 3.83 | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 16000 Hz | 1.41 | -36.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20ZS6/KZ%20ZS6.png)