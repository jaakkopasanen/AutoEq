# Advanced Evo X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.4; 25 -2.6; 28 -2.8; 31 -3.1; 34 -3.3; 37 -3.5; 41 -3.7; 45 -3.9; 49 -4.1; 54 -4.3; 60 -4.5; 66 -4.9; 72 -5.2; 79 -5.6; 87 -5.9; 96 -6.3; 106 -6.6; 116 -7.0; 128 -7.2; 141 -7.4; 155 -7.5; 170 -7.6; 187 -7.6; 206 -7.5; 227 -7.3; 249 -7.1; 274 -6.8; 302 -6.6; 332 -6.2; 365 -5.8; 402 -5.3; 442 -4.7; 486 -4.3; 535 -3.2; 588 -2.3; 647 -3.0; 712 -2.8; 783 -2.5; 861 -2.3; 947 -2.3; 1042 -2.6; 1146 -3.4; 1261 -4.3; 1387 -5.0; 1526 -5.4; 1678 -5.6; 1846 -5.7; 2031 -5.7; 2234 -5.3; 2457 -4.4; 2703 -3.8; 2973 -2.6; 3270 -1.4; 3597 -0.7; 3957 -0.5; 4353 -1.1; 4788 -2.7; 5267 -5.8; 5793 -8.2; 6373 -5.4; 7010 -3.7; 7711 -6.6; 8482 -5.9; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced Evo X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced Evo X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.24 | 2.7 dB  |
| Peaking | 176 Hz  | 0.54 | -3.2 dB |
| Peaking | 694 Hz  | 1.35 | 3.1 dB  |
| Peaking | 3905 Hz | 2.62 | 4.9 dB  |
| Peaking | 5724 Hz | 6.08 | -4.6 dB |
| Peaking | 703 Hz  | 6.44 | -1.1 dB |
| Peaking | 1009 Hz | 3.9  | 1.1 dB  |
| Peaking | 1814 Hz | 1.21 | -3.5 dB |
| Peaking | 1949 Hz | 0.61 | 1.9 dB  |
| Peaking | 8076 Hz | 9.21 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20Evo%20X/Advanced%20Evo%20X.png)