# Creative Aurvana
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.6; 25 -4.1; 28 -4.6; 31 -5.1; 34 -5.4; 37 -5.7; 41 -5.9; 45 -6.2; 49 -6.4; 54 -6.7; 60 -7.0; 66 -7.1; 72 -7.2; 79 -7.7; 87 -8.1; 96 -8.4; 106 -8.6; 116 -8.5; 128 -8.7; 141 -8.7; 155 -8.5; 170 -8.2; 187 -8.0; 206 -7.8; 227 -7.5; 249 -7.2; 274 -6.9; 302 -6.6; 332 -6.2; 365 -5.9; 402 -5.6; 442 -5.2; 486 -5.1; 535 -5.0; 588 -4.8; 647 -5.2; 712 -5.8; 783 -6.2; 861 -6.0; 947 -5.9; 1042 -6.0; 1146 -5.7; 1261 -5.6; 1387 -5.6; 1526 -5.8; 1678 -5.8; 1846 -5.3; 2031 -4.7; 2234 -4.2; 2457 -3.7; 2703 -4.8; 2973 -5.8; 3270 -2.3; 3597 -1.1; 3957 -4.1; 4353 -6.2; 4788 -5.0; 5267 -1.8; 5793 -0.5; 6373 -0.8; 7010 -3.7; 7711 -6.0; 8482 -6.2; 9330 -7.0; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.4; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.1  | 4.1 dB  |
| Peaking | 134 Hz  | 0.73 | -3.2 dB |
| Peaking | 574 Hz  | 0.19 | 1.0 dB  |
| Peaking | 3475 Hz | 7.31 | 5.4 dB  |
| Peaking | 5982 Hz | 3.96 | 6.3 dB  |
| Peaking | 541 Hz  | 1.38 | 2.6 dB  |
| Peaking | 635 Hz  | 0.78 | -2.0 dB |
| Peaking | 2450 Hz | 3.23 | 2.1 dB  |
| Peaking | 2904 Hz | 7.16 | -2.0 dB |
| Peaking | 9176 Hz | 3.31 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Aurvana/Creative%20Aurvana.png)