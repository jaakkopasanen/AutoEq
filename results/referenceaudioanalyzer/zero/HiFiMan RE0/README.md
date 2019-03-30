# HiFiMan RE0
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.1; 25 -2.3; 28 -2.5; 31 -2.6; 34 -2.8; 37 -2.8; 41 -2.9; 45 -2.9; 49 -3.0; 54 -3.2; 60 -3.1; 66 -2.9; 72 -2.9; 79 -2.9; 87 -2.9; 96 -3.1; 106 -3.2; 116 -3.1; 128 -2.9; 141 -2.9; 155 -2.9; 170 -2.9; 187 -3.0; 206 -3.4; 227 -3.5; 249 -3.5; 274 -3.4; 302 -3.2; 332 -3.2; 365 -3.0; 402 -2.9; 442 -2.8; 486 -2.5; 535 -2.3; 588 -2.0; 647 -1.7; 712 -1.5; 783 -1.2; 861 -1.0; 947 -0.9; 1042 -1.0; 1146 -1.3; 1261 -2.0; 1387 -3.1; 1526 -4.4; 1678 -5.7; 1846 -8.2; 2031 -10.8; 2234 -12.0; 2457 -11.4; 2703 -9.7; 2973 -7.8; 3270 -6.2; 3597 -5.4; 3957 -5.8; 4353 -7.7; 4788 -9.3; 5267 -8.9; 5793 -5.4; 6373 -0.5; 7010 -1.6; 7711 -3.8; 8482 -4.2; 9330 -8.4; 10263 -10.0; 11289 -9.1; 12418 -5.9; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan RE0 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan RE0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 2279 Hz  | 1.4  | -14.8 dB |
| Peaking | 2675 Hz  | 0.26 | 7.3 dB   |
| Peaking | 5042 Hz  | 2.07 | -9.4 dB  |
| Peaking | 6506 Hz  | 5.18 | 5.3 dB   |
| Peaking | 10375 Hz | 2.08 | -8.7 dB  |
| Peaking | 13 Hz    | 0.5  | 2.6 dB   |
| Peaking | 145 Hz   | 0.53 | 1.4 dB   |
| Peaking | 290 Hz   | 0.56 | -1.1 dB  |
| Peaking | 1119 Hz  | 1.7  | 1.0 dB   |
| Peaking | 1435 Hz  | 1.51 | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20RE0/HiFiMan%20RE0.png)