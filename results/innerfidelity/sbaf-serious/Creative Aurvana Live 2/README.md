# Creative Aurvana Live 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -10.0; 25 -10.2; 28 -10.5; 31 -10.7; 34 -10.8; 37 -10.9; 41 -11.0; 45 -11.0; 49 -11.1; 54 -11.0; 60 -11.1; 66 -11.2; 72 -11.1; 79 -11.0; 87 -11.0; 96 -11.3; 106 -11.6; 116 -11.9; 128 -12.1; 141 -12.3; 155 -12.2; 170 -11.6; 187 -11.9; 206 -11.8; 227 -11.4; 249 -11.1; 274 -10.7; 302 -10.0; 332 -9.4; 365 -8.2; 402 -7.6; 442 -6.9; 486 -7.0; 535 -7.0; 588 -7.1; 647 -7.5; 712 -7.8; 783 -7.5; 861 -7.3; 947 -6.9; 1042 -6.1; 1146 -5.4; 1261 -4.6; 1387 -3.9; 1526 -3.2; 1678 -2.8; 1846 -2.2; 2031 -1.4; 2234 -1.0; 2457 -0.7; 2703 -1.2; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -2.9; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.4; 9330 -10.5; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Live 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Live 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.41 | -3.9 dB |
| Peaking | 177 Hz  | 0.69 | -4.8 dB |
| Peaking | 2672 Hz | 0.94 | 6.2 dB  |
| Peaking | 5689 Hz | 3.53 | 5.1 dB  |
| Peaking | 448 Hz  | 3.76 | 1.3 dB  |
| Peaking | 818 Hz  | 1.86 | -1.7 dB |
| Peaking | 2746 Hz | 0.38 | 0.8 dB  |
| Peaking | 2772 Hz | 5.02 | -2.1 dB |
| Peaking | 9147 Hz | 4.39 | -5.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Aurvana%20Live%202/Creative%20Aurvana%20Live%202.png)