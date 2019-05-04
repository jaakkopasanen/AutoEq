# BÖHM B-66
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -2.1; 25 -2.9; 28 -3.6; 31 -3.9; 34 -3.9; 37 -3.7; 41 -3.5; 45 -3.3; 49 -3.1; 54 -3.0; 60 -3.0; 66 -3.0; 72 -3.1; 79 -3.3; 87 -3.6; 96 -3.9; 106 -4.2; 116 -4.5; 128 -4.8; 141 -5.0; 155 -5.2; 170 -5.3; 187 -5.3; 206 -5.3; 227 -5.3; 249 -5.4; 274 -5.5; 302 -5.5; 332 -5.6; 365 -5.1; 402 -4.5; 442 -3.7; 486 -2.5; 535 -1.4; 588 -0.9; 647 -1.0; 712 -1.4; 783 -2.0; 861 -2.6; 947 -3.4; 1042 -4.1; 1146 -4.6; 1261 -5.9; 1387 -7.5; 1526 -9.1; 1678 -10.1; 1846 -9.9; 2031 -9.0; 2234 -8.4; 2457 -6.4; 2703 -5.1; 2973 -5.3; 3270 -5.3; 3597 -4.4; 3957 -3.3; 4353 -2.7; 4788 -0.8; 5267 -0.7; 5793 -0.7; 6373 -0.5; 7010 -3.7; 7711 -6.3; 8482 -7.0; 9330 -4.8; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BÖHM B-66 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BÖHM B-66 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 672 Hz  | 1.9  | 4.2 dB  |
| Peaking | 1790 Hz | 1.85 | -6.2 dB |
| Peaking | 5771 Hz | 1.63 | 5.2 dB  |
| Peaking | 8038 Hz | 3.42 | -4.5 dB |
| Peaking | 18 Hz   | 2.33 | 3.7 dB  |
| Peaking | 67 Hz   | 1.08 | 1.8 dB  |
| Peaking | 357 Hz  | 0.37 | -1.5 dB |
| Peaking | 520 Hz  | 3.05 | 2.2 dB  |
| Peaking | 1012 Hz | 2.1  | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/B%C3%96HM%20B-66/B%C3%96HM%20B-66.png)