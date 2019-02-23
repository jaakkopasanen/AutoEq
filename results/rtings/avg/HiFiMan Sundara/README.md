# HiFiMan Sundara
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.3; 31 -1.8; 34 -2.1; 37 -2.4; 41 -2.7; 45 -3.0; 49 -3.2; 54 -3.5; 60 -3.7; 66 -4.0; 72 -4.2; 79 -4.4; 87 -4.7; 96 -5.0; 106 -5.3; 116 -5.6; 128 -5.8; 141 -6.1; 155 -6.2; 170 -6.4; 187 -6.5; 206 -6.6; 227 -6.6; 249 -6.6; 274 -6.7; 302 -6.9; 332 -7.1; 365 -7.3; 402 -7.3; 442 -6.6; 486 -6.2; 535 -6.7; 588 -7.0; 647 -7.0; 712 -6.9; 783 -6.8; 861 -6.7; 947 -5.6; 1042 -5.0; 1146 -5.0; 1261 -4.8; 1387 -4.7; 1526 -4.3; 1678 -4.4; 1846 -4.0; 2031 -3.8; 2234 -2.3; 2457 -3.7; 2703 -4.4; 2973 -7.1; 3270 -8.0; 3597 -8.8; 3957 -9.0; 4353 -8.5; 4788 -10.7; 5267 -8.3; 5793 -2.8; 6373 -7.3; 7010 -9.7; 7711 -9.6; 8482 -10.1; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -7.9; 13660 -10.2; 15026 -10.1; 16529 -9.5; 18182 -9.7; 20000 -12.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Sundara GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Sundara ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 18 Hz    |  0.39 | 6.0 dB  |
| Peaking | 2364 Hz  |  1.11 | 4.8 dB  |
| Peaking | 3589 Hz  |  1.67 | -5.0 dB |
| Peaking | 7996 Hz  |  4.18 | -3.3 dB |
| Peaking | 20089 Hz |  0.26 | -4.6 dB |
| Peaking | 365 Hz   |  1.01 | -0.8 dB |
| Peaking | 4853 Hz  |  7.8  | -3.2 dB |
| Peaking | 5741 Hz  | 10.35 | 5.6 dB  |
| Peaking | 11425 Hz |  3.41 | 2.3 dB  |
| Peaking | 13691 Hz |  2.48 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Sundara/HiFiMan%20Sundara.png)