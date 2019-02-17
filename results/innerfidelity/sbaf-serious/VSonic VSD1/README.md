# VSonic VSD1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.1; 25 -7.4; 28 -7.8; 31 -8.1; 34 -8.4; 37 -8.6; 41 -8.8; 45 -9.0; 49 -9.2; 54 -9.4; 60 -9.6; 66 -9.8; 72 -10.0; 79 -10.3; 87 -10.5; 96 -10.7; 106 -10.8; 116 -10.7; 128 -10.8; 141 -10.8; 155 -10.7; 170 -10.5; 187 -10.3; 206 -10.0; 227 -9.7; 249 -9.5; 274 -9.1; 302 -8.8; 332 -8.5; 365 -8.1; 402 -7.8; 442 -7.4; 486 -7.2; 535 -6.9; 588 -6.4; 647 -6.2; 712 -6.2; 783 -5.9; 861 -6.0; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.8; 1526 -8.5; 1678 -9.0; 1846 -8.6; 2031 -8.7; 2234 -8.4; 2457 -7.1; 2703 -5.3; 2973 -2.5; 3270 -0.6; 3597 -0.5; 3957 -0.9; 4353 -4.1; 4788 -6.8; 5267 -8.5; 5793 -6.7; 6373 -3.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 87 Hz    | 0.55 | -3.6 dB |
| Peaking | 197 Hz   | 1.03 | -2.0 dB |
| Peaking | 1976 Hz  | 1.86 | -3.2 dB |
| Peaking | 3445 Hz  | 2.73 | 7.4 dB  |
| Peaking | 22046 Hz | 2.19 | 1.0 dB  |
| Peaking | 789 Hz   | 2.13 | 1.1 dB  |
| Peaking | 1510 Hz  | 5.68 | -0.7 dB |
| Peaking | 4055 Hz  | 6.35 | 2.4 dB  |
| Peaking | 5366 Hz  | 2.47 | -3.7 dB |
| Peaking | 6501 Hz  | 5.23 | 5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD1/VSonic%20VSD1.png)