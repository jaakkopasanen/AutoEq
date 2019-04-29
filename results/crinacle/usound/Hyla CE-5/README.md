# Hyla CE-5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -5.9; 25 -6.0; 28 -6.0; 31 -5.9; 34 -5.9; 37 -5.8; 41 -5.8; 45 -5.7; 49 -5.6; 54 -5.6; 60 -5.5; 66 -5.4; 72 -5.4; 79 -5.4; 87 -5.4; 96 -5.4; 106 -5.4; 116 -5.3; 128 -5.1; 141 -4.9; 155 -4.7; 170 -4.4; 187 -4.3; 206 -3.9; 227 -3.5; 249 -3.1; 274 -2.8; 302 -2.4; 332 -2.1; 365 -1.7; 402 -1.5; 442 -1.3; 486 -1.1; 535 -0.9; 588 -0.8; 647 -0.7; 712 -0.6; 783 -0.5; 861 -0.5; 947 -0.8; 1042 -1.5; 1146 -2.7; 1261 -4.0; 1387 -4.9; 1526 -5.4; 1678 -5.5; 1846 -5.4; 2031 -5.3; 2234 -5.0; 2457 -4.4; 2703 -3.6; 2973 -2.8; 3270 -2.5; 3597 -2.8; 3957 -3.5; 4353 -4.3; 4788 -4.1; 5267 -2.6; 5793 -1.0; 6373 -1.1; 7010 -2.3; 7711 -2.7; 8482 -3.0; 9330 -3.7; 10263 -3.6; 11289 -3.0; 12418 -3.0; 13660 -4.8; 15026 -6.1; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hyla CE-5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hyla CE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.37 | -2.8 dB |
| Peaking | 128 Hz   | 0.68 | -1.8 dB |
| Peaking | 1153 Hz  | 0.45 | 5.8 dB  |
| Peaking | 1643 Hz  | 0.93 | -7.9 dB |
| Peaking | 14406 Hz | 4.75 | -4.2 dB |
| Peaking | 3287 Hz  | 3.59 | 1.1 dB  |
| Peaking | 4582 Hz  | 2.85 | -2.2 dB |
| Peaking | 5921 Hz  | 3.49 | 2.7 dB  |
| Peaking | 9765 Hz  | 6.41 | -1.4 dB |
| Peaking | 12427 Hz | 3.24 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hyla%20CE-5/Hyla%20CE-5.png)