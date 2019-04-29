# FitEar Aya
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.1; 25 -6.3; 28 -6.6; 31 -6.8; 34 -6.9; 37 -7.1; 41 -7.3; 45 -7.5; 49 -7.6; 54 -7.7; 60 -8.0; 66 -8.3; 72 -8.6; 79 -9.0; 87 -9.4; 96 -9.7; 106 -10.1; 116 -10.4; 128 -10.6; 141 -10.9; 155 -11.1; 170 -11.2; 187 -11.3; 206 -11.1; 227 -11.0; 249 -10.9; 274 -10.7; 302 -10.5; 332 -10.2; 365 -9.9; 402 -9.5; 442 -9.1; 486 -8.7; 535 -8.3; 588 -7.8; 647 -7.3; 712 -6.7; 783 -6.1; 861 -5.6; 947 -5.4; 1042 -5.4; 1146 -5.8; 1261 -6.3; 1387 -6.4; 1526 -6.0; 1678 -5.3; 1846 -4.5; 2031 -3.9; 2234 -3.6; 2457 -3.6; 2703 -3.4; 2973 -3.6; 3270 -5.0; 3597 -5.8; 3957 -2.3; 4353 -0.5; 4788 -0.6; 5267 -2.5; 5793 -4.1; 6373 -6.7; 7010 -7.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Aya GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Aya ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 116 Hz  |  0.81 | -3.0 dB |
| Peaking | 218 Hz  |  1.13 | -3.0 dB |
| Peaking | 381 Hz  |  1.76 | -1.9 dB |
| Peaking | 2325 Hz |  1.69 | 3.0 dB  |
| Peaking | 4606 Hz |  3.56 | 6.4 dB  |
| Peaking | 16 Hz   |  1.54 | 1.1 dB  |
| Peaking | 970 Hz  |  1.68 | 3.6 dB  |
| Peaking | 1130 Hz |  0.88 | -2.8 dB |
| Peaking | 1822 Hz |  1.11 | 0.9 dB  |
| Peaking | 6702 Hz | 10.87 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20Aya/FitEar%20Aya.png)