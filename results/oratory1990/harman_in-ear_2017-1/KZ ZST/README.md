# KZ ZST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.0; 25 -10.2; 28 -10.4; 31 -10.6; 34 -10.7; 37 -10.7; 41 -10.8; 45 -10.9; 49 -10.9; 54 -11.0; 60 -11.0; 66 -11.1; 72 -11.2; 79 -11.2; 87 -11.3; 96 -11.3; 106 -11.3; 116 -11.2; 128 -11.0; 141 -10.7; 155 -10.7; 170 -11.1; 187 -10.7; 206 -10.3; 227 -9.9; 249 -9.5; 274 -9.0; 302 -8.6; 332 -8.1; 365 -7.6; 402 -7.3; 442 -7.0; 486 -6.6; 535 -6.3; 588 -6.1; 647 -5.9; 712 -5.7; 783 -5.7; 861 -6.1; 947 -6.2; 1042 -6.8; 1146 -7.3; 1261 -7.8; 1387 -8.1; 1526 -8.5; 1678 -9.3; 1846 -10.0; 2031 -9.9; 2234 -8.4; 2457 -6.8; 2703 -5.1; 2973 -4.7; 3270 -5.4; 3597 -4.8; 3957 -1.0; 4353 -0.5; 4788 -1.2; 5267 -6.3; 5793 -6.0; 6373 -7.4; 7010 -8.1; 7711 -6.2; 8482 -6.5; 9330 -6.7; 10263 -12.7; 11289 -16.0; 12418 -17.0; 13660 -21.8; 15026 -25.8; 16529 -21.8; 18182 -14.3; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 52 Hz    | 0.37 | -4.6 dB  |
| Peaking | 176 Hz   | 1.17 | -2.5 dB  |
| Peaking | 1860 Hz  | 2.85 | -4.0 dB  |
| Peaking | 4335 Hz  | 2.25 | 7.0 dB   |
| Peaking | 15223 Hz | 1.18 | -20.7 dB |
| Peaking | 696 Hz   | 1.26 | 1.9 dB   |
| Peaking | 2763 Hz  | 5.48 | 2.2 dB   |
| Peaking | 4532 Hz  | 0.07 | -0.8 dB  |
| Peaking | 9085 Hz  | 2.56 | 5.9 dB   |
| Peaking | 10791 Hz | 3.5  | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -24.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZST/KZ%20ZST.png)