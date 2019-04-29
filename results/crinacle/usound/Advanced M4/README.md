# Advanced M4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.9; 25 -3.0; 28 -3.2; 31 -3.3; 34 -3.4; 37 -3.5; 41 -3.6; 45 -3.8; 49 -4.0; 54 -4.1; 60 -4.4; 66 -4.7; 72 -5.0; 79 -5.4; 87 -5.7; 96 -6.2; 106 -6.5; 116 -6.7; 128 -7.0; 141 -7.1; 155 -7.3; 170 -7.3; 187 -7.3; 206 -7.2; 227 -7.0; 249 -6.7; 274 -6.5; 302 -6.1; 332 -5.8; 365 -5.3; 402 -4.9; 442 -4.5; 486 -4.0; 535 -3.5; 588 -3.0; 647 -2.4; 712 -1.8; 783 -1.2; 861 -0.7; 947 -0.5; 1042 -0.7; 1146 -1.3; 1261 -2.0; 1387 -2.3; 1526 -2.2; 1678 -1.7; 1846 -1.3; 2031 -1.2; 2234 -1.7; 2457 -2.8; 2703 -4.2; 2973 -5.3; 3270 -5.3; 3597 -4.4; 3957 -3.1; 4353 -2.2; 4788 -2.0; 5267 -2.7; 5793 -5.3; 6373 -10.4; 7010 -9.7; 7711 -6.1; 8482 -5.7; 9330 -7.2; 10263 -4.9; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -5.0; 16529 -10.3; 18182 -15.4; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced M4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced M4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 190 Hz   | 0.73 | -3.2 dB  |
| Peaking | 925 Hz   | 1.01 | 3.3 dB   |
| Peaking | 6581 Hz  | 0.12 | 1.2 dB   |
| Peaking | 6749 Hz  | 4.58 | -8.1 dB  |
| Peaking | 18783 Hz | 0.95 | -13.0 dB |
| Peaking | 25 Hz    | 0.86 | 1.7 dB   |
| Peaking | 2077 Hz  | 3.62 | 1.9 dB   |
| Peaking | 3112 Hz  | 2.94 | -2.9 dB  |
| Peaking | 4703 Hz  | 3.34 | 2.4 dB   |
| Peaking | 9319 Hz  | 7.01 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20M4/Advanced%20M4.png)