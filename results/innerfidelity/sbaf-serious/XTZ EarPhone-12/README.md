# XTZ EarPhone-12
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.7; 25 -5.1; 28 -5.7; 31 -6.2; 34 -6.6; 37 -7.0; 41 -7.4; 45 -7.8; 49 -8.1; 54 -8.5; 60 -9.0; 66 -9.4; 72 -9.7; 79 -10.1; 87 -10.5; 96 -10.9; 106 -11.1; 116 -11.2; 128 -11.3; 141 -11.4; 155 -11.4; 170 -11.2; 187 -11.1; 206 -10.7; 227 -10.4; 249 -10.1; 274 -9.6; 302 -9.1; 332 -8.6; 365 -8.1; 402 -7.5; 442 -6.8; 486 -6.3; 535 -5.7; 588 -4.9; 647 -4.4; 712 -4.1; 783 -3.5; 861 -3.5; 947 -3.8; 1042 -4.2; 1146 -4.5; 1261 -4.8; 1387 -5.3; 1526 -5.9; 1678 -6.5; 1846 -7.0; 2031 -7.5; 2234 -7.4; 2457 -6.7; 2703 -5.6; 2973 -3.5; 3270 -1.6; 3597 -0.5; 3957 -1.2; 4353 -3.2; 4788 -3.6; 5267 -2.8; 5793 -1.6; 6373 -0.6; 7010 -1.6; 7711 -3.8; 8482 -4.1; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`XTZ EarPhone-12 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `XTZ EarPhone-12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.53 | -6.3 dB |
| Peaking | 240 Hz  | 1.04 | -3.3 dB |
| Peaking | 2140 Hz | 2.04 | -3.9 dB |
| Peaking | 3576 Hz | 3.55 | 4.5 dB  |
| Peaking | 6297 Hz | 4.46 | 3.9 dB  |
| Peaking | 16 Hz   | 0.41 | 1.2 dB  |
| Peaking | 38 Hz   | 1.29 | -1.3 dB |
| Peaking | 407 Hz  | 2.53 | -0.7 dB |
| Peaking | 800 Hz  | 1.98 | 1.5 dB  |
| Peaking | 1576 Hz | 4.09 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/XTZ%20EarPhone-12/XTZ%20EarPhone-12.png)