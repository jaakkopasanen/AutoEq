# AKG N700NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.3; 25 -3.4; 28 -3.5; 31 -3.5; 34 -3.3; 37 -3.2; 41 -2.9; 45 -2.7; 49 -2.6; 54 -2.3; 60 -2.1; 66 -2.0; 72 -1.8; 79 -1.7; 87 -1.6; 96 -1.5; 106 -1.4; 116 -1.4; 128 -1.4; 141 -1.4; 155 -1.4; 170 -1.3; 187 -1.2; 206 -1.0; 227 -0.7; 249 -0.6; 274 -0.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.7; 442 -1.0; 486 -1.3; 535 -1.7; 588 -2.1; 647 -2.1; 712 -1.9; 783 -1.6; 861 -1.2; 947 -0.9; 1042 -0.8; 1146 -0.9; 1261 -1.3; 1387 -2.4; 1526 -3.2; 1678 -3.6; 1846 -3.3; 2031 -3.4; 2234 -2.9; 2457 -4.3; 2703 -6.8; 2973 -8.5; 3270 -7.7; 3597 -5.8; 3957 -5.7; 4353 -6.1; 4788 -6.8; 5267 -6.3; 5793 -6.0; 6373 -6.6; 7010 -3.4; 7711 -2.5; 8482 -3.9; 9330 -4.3; 10263 -2.7; 11289 -4.8; 12418 -7.7; 13660 -6.1; 15026 -3.1; 16529 -2.8; 18182 -2.8; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N700NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N700NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 316 Hz   | 0.29 | 2.0 dB  |
| Peaking | 2992 Hz  | 3.54 | -5.4 dB |
| Peaking | 5252 Hz  | 1.43 | -4.5 dB |
| Peaking | 9522 Hz  | 0.45 | 1.3 dB  |
| Peaking | 12631 Hz | 2.61 | -6.1 dB |
| Peaking | 31 Hz    | 2.05 | -0.9 dB |
| Peaking | 640 Hz   | 2.8  | -1.5 dB |
| Peaking | 1235 Hz  | 1.13 | 1.6 dB  |
| Peaking | 1441 Hz  | 4.54 | -1.2 dB |
| Peaking | 1683 Hz  | 3.98 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | -4.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20N700NC/AKG%20N700NC.png)