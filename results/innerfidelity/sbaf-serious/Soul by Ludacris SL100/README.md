# Soul by Ludacris SL100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.6; 25 -6.0; 28 -6.6; 31 -7.1; 34 -7.5; 37 -7.8; 41 -8.3; 45 -8.6; 49 -8.9; 54 -9.2; 60 -9.1; 66 -9.0; 72 -9.7; 79 -10.9; 87 -11.9; 96 -12.7; 106 -13.0; 116 -13.3; 128 -13.6; 141 -13.7; 155 -13.9; 170 -14.2; 187 -14.4; 206 -14.3; 227 -14.0; 249 -13.7; 274 -13.6; 302 -13.7; 332 -14.1; 365 -13.7; 402 -13.4; 442 -12.9; 486 -12.3; 535 -11.6; 588 -10.3; 647 -8.7; 712 -7.0; 783 -5.5; 861 -5.3; 947 -5.9; 1042 -7.2; 1146 -8.7; 1261 -10.0; 1387 -10.6; 1526 -10.6; 1678 -9.8; 1846 -8.1; 2031 -6.3; 2234 -4.8; 2457 -2.7; 2703 -1.8; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -6.9; 4788 -9.2; 5267 -7.7; 5793 -8.7; 6373 -5.1; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul by Ludacris SL100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul by Ludacris SL100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 2.92 | -0.5 dB |
| Peaking | 155 Hz  | 0.64 | -7.5 dB |
| Peaking | 387 Hz  | 1.62 | -4.8 dB |
| Peaking | 1503 Hz | 3.2  | -4.9 dB |
| Peaking | 3122 Hz | 2.24 | 7.0 dB  |
| Peaking | 21 Hz   | 2.18 | 2.0 dB  |
| Peaking | 833 Hz  | 4.8  | 3.2 dB  |
| Peaking | 4026 Hz | 4.62 | 8.3 dB  |
| Peaking | 4475 Hz | 2.61 | -7.4 dB |
| Peaking | 6771 Hz | 8.94 | 3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.6 dB |
| Peaking | 500 Hz   | 1.41 | -3.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20by%20Ludacris%20SL100/Soul%20by%20Ludacris%20SL100.png)