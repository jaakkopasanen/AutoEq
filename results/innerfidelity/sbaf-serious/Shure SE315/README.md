# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -0.8; 25 -0.9; 28 -1.0; 31 -1.1; 34 -1.2; 37 -1.3; 41 -1.5; 45 -1.7; 49 -1.8; 54 -2.0; 60 -2.3; 66 -2.6; 72 -2.9; 79 -3.3; 87 -3.7; 96 -4.2; 106 -4.5; 116 -4.7; 128 -5.0; 141 -5.2; 155 -5.4; 170 -5.6; 187 -5.6; 206 -5.7; 227 -5.6; 249 -5.6; 274 -5.5; 302 -5.4; 332 -5.3; 365 -5.1; 402 -5.0; 442 -4.8; 486 -4.9; 535 -4.8; 588 -4.5; 647 -4.5; 712 -4.7; 783 -4.8; 861 -5.4; 947 -6.0; 1042 -6.9; 1146 -7.6; 1261 -8.4; 1387 -9.5; 1526 -10.6; 1678 -11.1; 1846 -10.7; 2031 -9.3; 2234 -6.9; 2457 -3.7; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.61 | 4.6 dB  |
| Peaking | 109 Hz  | 0.04 | 1.3 dB  |
| Peaking | 1776 Hz | 1.64 | -8.6 dB |
| Peaking | 3074 Hz | 1.2  | 7.5 dB  |
| Peaking | 5675 Hz | 2.92 | 4.7 dB  |
| Peaking | 203 Hz  | 1.27 | -0.9 dB |
| Peaking | 822 Hz  | 0.9  | 1.5 dB  |
| Peaking | 1137 Hz | 1.78 | -1.6 dB |
| Peaking | 6585 Hz | 7.26 | 2.2 dB  |
| Peaking | 7922 Hz | 2.12 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE315/Shure%20SE315.png)