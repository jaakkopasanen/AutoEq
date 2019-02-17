# HiFiMAN HE1000 PreProduction
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.0; 25 -1.2; 28 -1.5; 31 -1.6; 34 -1.7; 37 -1.7; 41 -1.8; 45 -1.9; 49 -2.0; 54 -2.2; 60 -2.5; 66 -2.7; 72 -2.7; 79 -3.0; 87 -3.3; 96 -3.7; 106 -3.9; 116 -4.1; 128 -4.4; 141 -4.6; 155 -5.0; 170 -5.2; 187 -5.1; 206 -4.7; 227 -4.4; 249 -4.7; 274 -5.3; 302 -5.9; 332 -5.8; 365 -4.4; 402 -4.4; 442 -3.5; 486 -4.8; 535 -4.5; 588 -3.8; 647 -4.2; 712 -4.5; 783 -3.9; 861 -4.4; 947 -4.6; 1042 -3.2; 1146 -3.4; 1261 -2.0; 1387 -2.2; 1526 -1.9; 1678 -2.4; 1846 -1.4; 2031 -0.5; 2234 -1.1; 2457 -0.6; 2703 -0.6; 2973 -2.4; 3270 -3.3; 3597 -2.3; 3957 -3.3; 4353 -6.1; 4788 -6.5; 5267 -5.9; 5793 -3.8; 6373 -7.6; 7010 -8.4; 7711 -7.0; 8482 -6.9; 9330 -5.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -5.1; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE1000 PreProduction GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE1000 PreProduction ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.7  | 3.1 dB  |
| Peaking | 1333 Hz |  6.15 | 1.6 dB  |
| Peaking | 2326 Hz |  1.48 | 3.8 dB  |
| Peaking | 4636 Hz |  5.95 | -2.9 dB |
| Peaking | 7156 Hz |  2.86 | -4.4 dB |
| Peaking | 68 Hz   |  1.75 | 0.7 dB  |
| Peaking | 146 Hz  |  1.61 | -0.6 dB |
| Peaking | 174 Hz  |  5.01 | -0.9 dB |
| Peaking | 310 Hz  |  4.13 | -1.9 dB |
| Peaking | 3740 Hz | 11.47 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE1000%20PreProduction/HiFiMAN%20HE1000%20PreProduction.png)