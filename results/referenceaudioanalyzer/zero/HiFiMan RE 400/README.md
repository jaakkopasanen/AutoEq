# HiFiMan RE 400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.3; 25 -4.4; 28 -4.4; 31 -4.3; 34 -4.1; 37 -3.9; 41 -3.9; 45 -4.0; 49 -4.2; 54 -4.2; 60 -4.0; 66 -3.9; 72 -3.8; 79 -3.7; 87 -3.5; 96 -3.4; 106 -3.2; 116 -3.2; 128 -3.1; 141 -2.9; 155 -2.8; 170 -2.6; 187 -2.4; 206 -2.2; 227 -1.9; 249 -2.3; 274 -3.0; 302 -3.2; 332 -3.0; 365 -2.6; 402 -2.5; 442 -2.3; 486 -2.2; 535 -2.2; 588 -2.1; 647 -2.1; 712 -2.2; 783 -2.2; 861 -2.5; 947 -2.7; 1042 -3.0; 1146 -3.6; 1261 -4.3; 1387 -5.3; 1526 -6.5; 1678 -8.1; 1846 -9.9; 2031 -11.1; 2234 -11.0; 2457 -9.6; 2703 -7.4; 2973 -5.0; 3270 -2.6; 3597 -0.9; 3957 -0.7; 4353 -1.5; 4788 -2.6; 5267 -4.0; 5793 -4.4; 6373 -2.6; 7010 -0.5; 7711 -2.6; 8482 -2.8; 9330 -2.8; 10263 -2.9; 11289 -2.9; 12418 -2.9; 13660 -2.9; 15026 -2.9; 16529 -2.9; 18182 -2.9; 20000 -2.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan RE 400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan RE 400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 33 Hz   |  0.54 | -1.5 dB  |
| Peaking | 1267 Hz |  0.57 | 3.2 dB   |
| Peaking | 2122 Hz |  1.06 | -11.3 dB |
| Peaking | 3575 Hz |  2.34 | 5.9 dB   |
| Peaking | 6942 Hz | 10.32 | 3.3 dB   |
| Peaking | 229 Hz  |  2.59 | 1.1 dB   |
| Peaking | 293 Hz  |  3.55 | -1.0 dB  |
| Peaking | 5547 Hz |  1.81 | 1.3 dB   |
| Peaking | 5555 Hz |  4.4  | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20RE%20400/HiFiMan%20RE%20400.png)