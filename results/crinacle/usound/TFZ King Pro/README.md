# TFZ King Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.8; 25 -8.8; 28 -8.7; 31 -8.5; 34 -8.4; 37 -8.2; 41 -8.0; 45 -7.8; 49 -7.6; 54 -7.4; 60 -7.2; 66 -7.1; 72 -7.0; 79 -6.9; 87 -6.8; 96 -6.7; 106 -6.7; 116 -6.5; 128 -6.4; 141 -6.3; 155 -6.1; 170 -5.9; 187 -5.6; 206 -5.3; 227 -5.0; 249 -4.7; 274 -4.5; 302 -4.2; 332 -3.9; 365 -3.8; 402 -3.5; 442 -3.3; 486 -3.2; 535 -3.1; 588 -3.0; 647 -2.9; 712 -2.4; 783 -2.4; 861 -2.5; 947 -2.7; 1042 -3.4; 1146 -4.5; 1261 -5.7; 1387 -6.7; 1526 -7.4; 1678 -7.9; 1846 -8.3; 2031 -8.4; 2234 -7.9; 2457 -6.6; 2703 -5.1; 2973 -3.7; 3270 -2.0; 3597 -0.9; 3957 -1.7; 4353 -3.9; 4788 -4.8; 5267 -2.5; 5793 -0.5; 6373 -0.5; 7010 -4.3; 7711 -9.2; 8482 -8.4; 9330 -5.0; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.9; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ King Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ King Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.22 | -4.1 dB |
| Peaking | 1951 Hz | 2.46 | -4.5 dB |
| Peaking | 3554 Hz | 4.06 | 4.3 dB  |
| Peaking | 6220 Hz | 3.73 | 5.7 dB  |
| Peaking | 7890 Hz | 4.36 | -6.4 dB |
| Peaking | 149 Hz  | 1.45 | -0.8 dB |
| Peaking | 1062 Hz | 0.52 | 3.3 dB  |
| Peaking | 1284 Hz | 2.89 | -2.3 dB |
| Peaking | 1516 Hz | 4.73 | -1.7 dB |
| Peaking | 2153 Hz | 0.79 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%20King%20Pro/TFZ%20King%20Pro.png)