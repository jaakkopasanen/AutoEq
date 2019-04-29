# KZ S4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.4; 23 -17.2; 25 -16.9; 28 -16.6; 31 -16.3; 34 -15.9; 37 -15.6; 41 -15.2; 45 -14.9; 49 -14.5; 54 -14.2; 60 -13.8; 66 -13.5; 72 -13.3; 79 -13.0; 87 -12.7; 96 -12.6; 106 -12.3; 116 -12.0; 128 -11.7; 141 -11.4; 155 -11.0; 170 -10.7; 187 -10.2; 206 -9.7; 227 -9.2; 249 -8.7; 274 -8.1; 302 -7.5; 332 -6.8; 365 -6.2; 402 -5.6; 442 -5.2; 486 -4.6; 535 -4.1; 588 -3.6; 647 -3.2; 712 -2.6; 783 -1.8; 861 -1.5; 947 -1.6; 1042 -2.2; 1146 -3.1; 1261 -4.0; 1387 -4.3; 1526 -4.3; 1678 -4.1; 1846 -4.1; 2031 -4.2; 2234 -4.6; 2457 -5.9; 2703 -7.8; 2973 -8.3; 3270 -6.9; 3597 -5.5; 3957 -5.4; 4353 -7.2; 4788 -12.4; 5267 -12.9; 5793 -4.7; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -8.1; 15026 -22.3; 16529 -27.0; 18182 -22.7; 20000 -21.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ S4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ S4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.61 | -9.7 dB  |
| Peaking | 481 Hz   | 0.11 | -12.6 dB |
| Peaking | 2940 Hz  | 0.08 | 19.3 dB  |
| Peaking | 3778 Hz  | 0.62 | -11.0 dB |
| Peaking | 16880 Hz | 0.62 | -32.0 dB |
| Peaking | 3905 Hz  | 3.4  | 5.2 dB   |
| Peaking | 5087 Hz  | 5.22 | -9.1 dB  |
| Peaking | 6251 Hz  | 4.14 | 7.9 dB   |
| Peaking | 12721 Hz | 2.74 | 7.4 dB   |
| Peaking | 19808 Hz | 0.05 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 16000 Hz | 1.41 | -22.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20S4/KZ%20S4.png)