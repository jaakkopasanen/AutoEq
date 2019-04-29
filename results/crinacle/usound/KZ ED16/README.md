# KZ ED16
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.0; 25 -12.0; 28 -12.0; 31 -12.0; 34 -11.9; 37 -11.9; 41 -11.8; 45 -11.8; 49 -11.7; 54 -11.6; 60 -11.5; 66 -11.5; 72 -11.5; 79 -11.5; 87 -11.5; 96 -11.5; 106 -11.5; 116 -11.5; 128 -11.3; 141 -11.2; 155 -11.0; 170 -10.7; 187 -10.4; 206 -10.0; 227 -9.5; 249 -9.1; 274 -8.7; 302 -8.2; 332 -7.8; 365 -7.3; 402 -6.9; 442 -6.5; 486 -6.1; 535 -5.7; 588 -5.4; 647 -5.0; 712 -4.7; 783 -4.3; 861 -4.1; 947 -4.3; 1042 -4.9; 1146 -6.0; 1261 -7.1; 1387 -8.2; 1526 -9.1; 1678 -9.8; 1846 -10.1; 2031 -9.3; 2234 -7.4; 2457 -5.4; 2703 -4.2; 2973 -4.5; 3270 -5.4; 3597 -5.6; 3957 -3.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.3; 7711 -10.8; 8482 -12.0; 9330 -9.4; 10263 -8.3; 11289 -8.1; 12418 -8.2; 13660 -10.2; 15026 -9.6; 16529 -6.5; 18182 -6.5; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ED16 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ED16 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.16 | -5.3 dB  |
| Peaking | 177 Hz   | 0.67 | -2.8 dB  |
| Peaking | 1776 Hz  | 1.65 | -7.2 dB  |
| Peaking | 6429 Hz  | 0.38 | 35.1 dB  |
| Peaking | 7825 Hz  | 0.44 | -34.7 dB |
| Peaking | 868 Hz   | 4.18 | 1.1 dB   |
| Peaking | 3617 Hz  | 5.23 | -3.3 dB  |
| Peaking | 4279 Hz  | 5.25 | 2.4 dB   |
| Peaking | 10230 Hz | 3.96 | 1.4 dB   |
| Peaking | 14244 Hz | 4.32 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20ED16/KZ%20ED16.png)