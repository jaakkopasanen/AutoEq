# BÖHM B-66
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.6; 25 -3.3; 28 -4.0; 31 -4.2; 34 -4.2; 37 -4.0; 41 -3.8; 45 -3.6; 49 -3.5; 54 -3.4; 60 -3.3; 66 -3.5; 72 -3.6; 79 -3.8; 87 -4.0; 96 -4.3; 106 -4.6; 116 -5.0; 128 -5.2; 141 -5.5; 155 -5.7; 170 -5.7; 187 -5.7; 206 -5.7; 227 -5.6; 249 -5.7; 274 -5.8; 302 -5.8; 332 -5.8; 365 -5.4; 402 -4.8; 442 -3.9; 486 -2.7; 535 -1.6; 588 -1.0; 647 -1.1; 712 -1.5; 783 -2.1; 861 -2.7; 947 -3.5; 1042 -4.2; 1146 -4.7; 1261 -6.0; 1387 -7.5; 1526 -9.0; 1678 -10.1; 1846 -9.8; 2031 -8.7; 2234 -7.8; 2457 -5.7; 2703 -4.8; 2973 -5.5; 3270 -5.8; 3597 -4.9; 3957 -3.8; 4353 -3.3; 4788 -0.5; 5267 -0.5; 5793 -1.0; 6373 -1.6; 7010 -3.8; 7711 -5.7; 8482 -7.5; 9330 -6.4; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -4.8; 15026 -4.8; 16529 -4.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BÖHM B-66 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BÖHM B-66 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 669 Hz  | 1.97 | 4.3 dB  |
| Peaking | 1752 Hz | 2.16 | -5.9 dB |
| Peaking | 5430 Hz | 2.29 | 5.0 dB  |
| Peaking | 8523 Hz | 4.37 | -3.6 dB |
| Peaking | 18 Hz   | 2.5  | 4.1 dB  |
| Peaking | 63 Hz   | 1.24 | 1.6 dB  |
| Peaking | 241 Hz  | 0.71 | -1.4 dB |
| Peaking | 526 Hz  | 4.13 | 1.6 dB  |
| Peaking | 3298 Hz | 9.07 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/B%C3%96HM%20B-66/B%C3%96HM%20B-66.png)