# KZ S4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.0; 23 -15.7; 25 -15.5; 28 -15.1; 31 -14.8; 34 -14.5; 37 -14.2; 41 -13.8; 45 -13.4; 49 -13.1; 54 -12.7; 60 -12.3; 66 -12.1; 72 -11.8; 79 -11.5; 87 -11.3; 96 -11.1; 106 -10.9; 116 -10.5; 128 -10.2; 141 -10.0; 155 -9.6; 170 -9.2; 187 -8.8; 206 -8.2; 227 -7.7; 249 -7.2; 274 -6.6; 302 -6.1; 332 -5.5; 365 -5.0; 402 -4.5; 442 -4.0; 486 -3.6; 535 -3.1; 588 -2.7; 647 -2.2; 712 -1.6; 783 -0.9; 861 -0.5; 947 -0.5; 1042 -1.0; 1146 -2.1; 1261 -3.2; 1387 -3.8; 1526 -4.0; 1678 -4.0; 1846 -4.0; 2031 -4.5; 2234 -5.5; 2457 -7.3; 2703 -9.6; 2973 -10.3; 3270 -8.8; 3597 -7.2; 3957 -6.7; 4353 -8.0; 4788 -12.9; 5267 -13.4; 5793 -5.5; 6373 -0.8; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -6.0; 16529 -7.8; 18182 -5.9; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ S4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ S4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.56 | -9.1 dB  |
| Peaking | 95 Hz    | 0.37 | -4.4 dB  |
| Peaking | 1301 Hz  | 0.48 | 7.8 dB   |
| Peaking | 1370 Hz  | 2.4  | -3.9 dB  |
| Peaking | 2985 Hz  | 0.93 | -7.7 dB  |
| Peaking | 2894 Hz  | 5.21 | -2.5 dB  |
| Peaking | 3945 Hz  | 2.06 | 3.7 dB   |
| Peaking | 5071 Hz  | 4.45 | -10.8 dB |
| Peaking | 6358 Hz  | 4.25 | 7.4 dB   |
| Peaking | 20843 Hz | 0.39 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -1.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20S4/KZ%20S4.png)