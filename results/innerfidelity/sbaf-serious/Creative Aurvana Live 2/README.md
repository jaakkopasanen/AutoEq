# Creative Aurvana Live 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.6; 25 -10.8; 28 -11.1; 31 -11.2; 34 -11.3; 37 -11.4; 41 -11.5; 45 -11.6; 49 -11.6; 54 -11.6; 60 -11.6; 66 -11.7; 72 -11.7; 79 -11.6; 87 -11.5; 96 -11.9; 106 -12.2; 116 -12.4; 128 -12.7; 141 -12.9; 155 -12.7; 170 -12.1; 187 -12.4; 206 -12.3; 227 -12.0; 249 -11.7; 274 -11.2; 302 -10.6; 332 -10.0; 365 -8.8; 402 -8.1; 442 -7.4; 486 -7.6; 535 -7.6; 588 -7.7; 647 -8.1; 712 -8.3; 783 -8.1; 861 -7.8; 947 -7.4; 1042 -6.7; 1146 -6.0; 1261 -5.1; 1387 -4.5; 1526 -3.8; 1678 -3.4; 1846 -2.8; 2031 -2.0; 2234 -1.5; 2457 -1.3; 2703 -1.8; 2973 -1.8; 3270 -0.5; 3597 -0.5; 3957 -1.5; 4353 -3.4; 4788 -2.4; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -8.9; 9330 -11.0; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Live 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Live 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.45 | -4.3 dB |
| Peaking | 173 Hz  | 0.6  | -5.4 dB |
| Peaking | 2152 Hz | 1.57 | 4.6 dB  |
| Peaking | 3498 Hz | 2.72 | 4.7 dB  |
| Peaking | 5720 Hz | 3.61 | 6.1 dB  |
| Peaking | 474 Hz  | 1.67 | 2.7 dB  |
| Peaking | 639 Hz  | 0.75 | -2.2 dB |
| Peaking | 1357 Hz | 2.38 | 1.4 dB  |
| Peaking | 6564 Hz | 5.94 | 1.8 dB  |
| Peaking | 9108 Hz | 4.65 | -5.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Aurvana%20Live%202/Creative%20Aurvana%20Live%202.png)