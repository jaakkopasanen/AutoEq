# Vsonic GR07 BE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.2; 25 -4.5; 28 -4.8; 31 -4.9; 34 -5.1; 37 -5.2; 41 -5.3; 45 -5.5; 49 -5.6; 54 -5.7; 60 -5.9; 66 -6.1; 72 -6.3; 79 -6.6; 87 -6.9; 96 -7.2; 106 -7.5; 116 -7.8; 128 -8.1; 141 -8.3; 155 -8.5; 170 -8.6; 187 -8.7; 206 -8.8; 227 -8.9; 249 -9.0; 274 -9.0; 302 -8.9; 332 -8.9; 365 -8.9; 402 -8.9; 442 -8.8; 486 -8.7; 535 -8.6; 588 -8.5; 647 -8.3; 712 -8.0; 783 -7.6; 861 -7.3; 947 -7.1; 1042 -7.1; 1146 -7.4; 1261 -7.8; 1387 -7.9; 1526 -7.5; 1678 -6.6; 1846 -5.8; 2031 -5.5; 2234 -5.1; 2457 -4.6; 2703 -3.9; 2973 -2.8; 3270 -1.5; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.8; 5793 -4.7; 6373 -5.9; 7010 -5.4; 7711 -8.4; 8482 -9.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.8; 20000 -17.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vsonic GR07 BE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vsonic GR07 BE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.2  | 2.4 dB  |
| Peaking | 269 Hz  | 0.39 | -2.7 dB |
| Peaking | 1398 Hz | 4.06 | -1.5 dB |
| Peaking | 4038 Hz | 1.34 | 6.7 dB  |
| Peaking | 8133 Hz | 4.64 | -4.3 dB |
| Peaking | 4182 Hz | 4.88 | -1.1 dB |
| Peaking | 5003 Hz | 4.94 | 0.9 dB  |
| Peaking | 5524 Hz | 1.58 | 0.9 dB  |
| Peaking | 6005 Hz | 5.8  | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vsonic%20GR07%20BE/Vsonic%20GR07%20BE.png)