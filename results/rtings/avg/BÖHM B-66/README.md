# BÖHM B-66
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.6; 25 -3.3; 28 -4.0; 31 -4.2; 34 -4.2; 37 -4.0; 41 -3.8; 45 -3.6; 49 -3.5; 54 -3.4; 60 -3.3; 66 -3.5; 72 -3.6; 79 -3.8; 87 -4.0; 96 -4.3; 106 -4.6; 116 -5.0; 128 -5.2; 141 -5.5; 155 -5.7; 170 -5.7; 187 -5.7; 206 -5.7; 227 -5.6; 249 -5.7; 274 -5.8; 302 -5.8; 332 -5.8; 365 -5.4; 402 -4.8; 442 -3.9; 486 -2.7; 535 -1.6; 588 -1.0; 647 -1.1; 712 -1.5; 783 -2.1; 861 -2.7; 947 -3.5; 1042 -4.2; 1146 -4.7; 1261 -6.0; 1387 -7.5; 1526 -9.0; 1678 -10.1; 1846 -9.8; 2031 -8.7; 2234 -7.8; 2457 -5.7; 2703 -4.8; 2973 -5.5; 3270 -5.8; 3597 -4.9; 3957 -3.8; 4353 -3.3; 4788 -0.5; 5267 -0.5; 5793 -1.0; 6373 -1.6; 7010 -3.8; 7711 -5.7; 8482 -7.5; 9330 -6.4; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BÖHM B-66 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BÖHM B-66 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 367 Hz  | 0.6  | -3.8 dB |
| Peaking | 608 Hz  | 1.05 | 6.0 dB  |
| Peaking | 1742 Hz | 1.66 | -6.6 dB |
| Peaking | 5409 Hz | 2.64 | 4.3 dB  |
| Peaking | 8530 Hz | 4.21 | -4.3 dB |
| Peaking | 64 Hz   | 1.18 | 0.8 dB  |
| Peaking | 138 Hz  | 2.42 | -0.7 dB |
| Peaking | 2712 Hz | 5.41 | 1.4 dB  |
| Peaking | 3212 Hz | 4.55 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/B%C3%96HM%20B-66/B%C3%96HM%20B-66.png)