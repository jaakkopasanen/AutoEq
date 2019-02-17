# AKG K267 Tiesto Studio Setting
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -2.8; 25 -2.8; 28 -2.7; 31 -2.6; 34 -2.5; 37 -2.3; 41 -2.2; 45 -2.0; 49 -1.7; 54 -1.5; 60 -1.7; 66 -1.9; 72 -2.0; 79 -1.9; 87 -2.8; 96 -4.1; 106 -4.9; 116 -5.7; 128 -6.4; 141 -6.5; 155 -6.3; 170 -5.9; 187 -6.6; 206 -6.4; 227 -6.5; 249 -6.2; 274 -5.7; 302 -4.7; 332 -4.0; 365 -4.3; 402 -5.1; 442 -5.7; 486 -6.1; 535 -6.2; 588 -5.9; 647 -6.0; 712 -6.2; 783 -6.0; 861 -6.2; 947 -6.3; 1042 -6.7; 1146 -6.8; 1261 -7.8; 1387 -9.1; 1526 -8.7; 1678 -7.7; 1846 -6.6; 2031 -5.8; 2234 -5.0; 2457 -3.4; 2703 -3.5; 2973 -2.7; 3270 -2.4; 3597 -1.8; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -3.9; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K267 Tiesto Studio Setting GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Studio Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.66 | 4.0 dB  |
| Peaking | 69 Hz   | 1.78 | 3.2 dB  |
| Peaking | 1462 Hz | 3.82 | -3.5 dB |
| Peaking | 3946 Hz | 1.31 | 5.8 dB  |
| Peaking | 6170 Hz | 5.71 | 4.1 dB  |
| Peaking | 153 Hz  | 1.25 | -0.9 dB |
| Peaking | 341 Hz  | 3.26 | 2.4 dB  |
| Peaking | 354 Hz  | 0.05 | 0.1 dB  |
| Peaking | 6726 Hz | 8.25 | 1.5 dB  |
| Peaking | 7971 Hz | 1.99 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Studio%20Setting/AKG%20K267%20Tiesto%20Studio%20Setting.png)