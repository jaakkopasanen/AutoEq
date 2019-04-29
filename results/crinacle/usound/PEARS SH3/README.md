# PEARS SH3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -1.0; 28 -1.5; 31 -1.9; 34 -2.3; 37 -2.6; 41 -3.0; 45 -3.3; 49 -3.6; 54 -3.9; 60 -4.3; 66 -4.7; 72 -5.2; 79 -5.6; 87 -6.1; 96 -6.6; 106 -7.1; 116 -7.4; 128 -7.8; 141 -8.2; 155 -8.5; 170 -8.7; 187 -8.9; 206 -8.9; 227 -9.0; 249 -9.0; 274 -9.0; 302 -8.9; 332 -8.8; 365 -8.7; 402 -8.5; 442 -8.4; 486 -8.1; 535 -7.9; 588 -7.5; 647 -7.1; 712 -6.7; 783 -6.2; 861 -5.7; 947 -5.5; 1042 -5.6; 1146 -6.2; 1261 -6.9; 1387 -7.5; 1526 -7.9; 1678 -8.1; 1846 -8.0; 2031 -6.9; 2234 -5.3; 2457 -4.0; 2703 -3.5; 2973 -3.7; 3270 -4.4; 3597 -5.2; 3957 -5.6; 4353 -5.4; 4788 -4.9; 5267 -3.7; 5793 -1.9; 6373 -1.0; 7010 -6.4; 7711 -8.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PEARS SH3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PEARS SH3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.68 | 5.9 dB  |
| Peaking | 56 Hz   | 1.16 | 1.3 dB  |
| Peaking | 227 Hz  | 0.63 | -2.9 dB |
| Peaking | 2826 Hz | 3.37 | 3.4 dB  |
| Peaking | 6011 Hz | 4.9  | 5.9 dB  |
| Peaking | 482 Hz  | 2.24 | -0.5 dB |
| Peaking | 931 Hz  | 2.34 | 1.6 dB  |
| Peaking | 1643 Hz | 3.18 | -2.2 dB |
| Peaking | 6638 Hz | 5.93 | 2.7 dB  |
| Peaking | 7329 Hz | 6.24 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/PEARS%20SH3/PEARS%20SH3.png)