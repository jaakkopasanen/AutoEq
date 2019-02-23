# Creative Aurvana
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.1; 25 -4.6; 28 -5.2; 31 -5.6; 34 -6.0; 37 -6.2; 41 -6.5; 45 -6.7; 49 -7.0; 54 -7.3; 60 -7.6; 66 -7.6; 72 -7.8; 79 -8.2; 87 -8.6; 96 -8.9; 106 -9.1; 116 -9.1; 128 -9.2; 141 -9.2; 155 -9.0; 170 -8.8; 187 -8.5; 206 -8.3; 227 -8.0; 249 -7.8; 274 -7.5; 302 -7.2; 332 -6.8; 365 -6.4; 402 -6.1; 442 -5.7; 486 -5.7; 535 -5.6; 588 -5.4; 647 -5.7; 712 -6.4; 783 -6.8; 861 -6.5; 947 -6.5; 1042 -6.6; 1146 -6.3; 1261 -6.1; 1387 -6.2; 1526 -6.3; 1678 -6.3; 1846 -5.8; 2031 -5.2; 2234 -4.8; 2457 -4.3; 2703 -5.4; 2973 -6.4; 3270 -2.8; 3597 -1.5; 3957 -4.7; 4353 -6.8; 4788 -5.6; 5267 -2.4; 5793 -0.7; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -6.0; 9330 -7.5; 10263 -6.4; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.2; 16529 -6.7; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  1.89 | 2.8 dB  |
| Peaking | 109 Hz  |  0.83 | -3.0 dB |
| Peaking | 196 Hz  |  1.54 | -1.2 dB |
| Peaking | 3464 Hz |  8.62 | 5.5 dB  |
| Peaking | 6085 Hz |  4.43 | 6.5 dB  |
| Peaking | 563 Hz  |  1.61 | 2.3 dB  |
| Peaking | 672 Hz  |  0.99 | -1.7 dB |
| Peaking | 2347 Hz |  5.56 | 1.6 dB  |
| Peaking | 4441 Hz | 10.9  | -2.0 dB |
| Peaking | 9373 Hz |  5.54 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Aurvana/Creative%20Aurvana.png)