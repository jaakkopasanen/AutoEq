# AKG N700NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.1; 25 -3.3; 28 -3.3; 31 -3.3; 34 -3.2; 37 -3.0; 41 -2.8; 45 -2.6; 49 -2.4; 54 -2.2; 60 -2.0; 66 -1.8; 72 -1.6; 79 -1.5; 87 -1.4; 96 -1.3; 106 -1.2; 116 -1.2; 128 -1.2; 141 -1.2; 155 -1.2; 170 -1.1; 187 -1.0; 206 -0.8; 227 -0.7; 249 -0.6; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.6; 402 -0.7; 442 -1.0; 486 -1.4; 535 -1.8; 588 -2.2; 647 -2.3; 712 -2.1; 783 -1.8; 861 -1.3; 947 -1.0; 1042 -1.0; 1146 -1.1; 1261 -1.5; 1387 -2.6; 1526 -3.5; 1678 -3.9; 1846 -3.7; 2031 -3.8; 2234 -3.9; 2457 -5.3; 2703 -7.5; 2973 -8.6; 3270 -7.5; 3597 -5.6; 3957 -5.4; 4353 -5.9; 4788 -7.2; 5267 -6.8; 5793 -6.1; 6373 -5.6; 7010 -3.6; 7711 -2.9; 8482 -3.5; 9330 -2.9; 10263 -2.9; 11289 -5.9; 12418 -8.0; 13660 -5.4; 15026 -2.9; 16529 -2.9; 18182 -2.9; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N700NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N700NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 224 Hz   | 0.41 | 2.1 dB  |
| Peaking | 2928 Hz  | 2.35 | -6.0 dB |
| Peaking | 4824 Hz  | 0.17 | 1.0 dB  |
| Peaking | 5228 Hz  | 2.08 | -4.7 dB |
| Peaking | 12369 Hz | 3.11 | -6.1 dB |
| Peaking | 28 Hz    | 2.17 | -0.6 dB |
| Peaking | 645 Hz   | 2.83 | -1.3 dB |
| Peaking | 1218 Hz  | 1.13 | 1.9 dB  |
| Peaking | 1577 Hz  | 2.25 | -2.6 dB |
| Peaking | 2307 Hz  | 7.94 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | -4.4 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20N700NC/AKG%20N700NC.png)