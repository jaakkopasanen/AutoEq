# AKG K267 Tiesto Club Setting
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.1; 25 -5.1; 28 -5.0; 31 -4.9; 34 -4.9; 37 -4.7; 41 -4.6; 45 -4.4; 49 -4.1; 54 -3.9; 60 -3.8; 66 -3.6; 72 -3.5; 79 -3.5; 87 -4.3; 96 -5.4; 106 -5.5; 116 -6.1; 128 -6.8; 141 -6.9; 155 -6.6; 170 -6.2; 187 -6.6; 206 -6.6; 227 -6.3; 249 -6.0; 274 -5.2; 302 -4.0; 332 -3.0; 365 -3.4; 402 -4.5; 442 -5.3; 486 -5.8; 535 -5.9; 588 -5.7; 647 -5.8; 712 -6.0; 783 -5.8; 861 -6.0; 947 -6.3; 1042 -6.8; 1146 -7.3; 1261 -8.4; 1387 -10.0; 1526 -9.9; 1678 -8.8; 1846 -7.4; 2031 -6.6; 2234 -5.9; 2457 -4.4; 2703 -4.4; 2973 -3.7; 3270 -3.4; 3597 -2.5; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -2.6; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K267 Tiesto Club Setting GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Club Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 1.21 | 3.1 dB  |
| Peaking | 345 Hz  | 3.08 | 3.6 dB  |
| Peaking | 1475 Hz | 3.59 | -4.4 dB |
| Peaking | 4199 Hz | 1.71 | 6.0 dB  |
| Peaking | 6118 Hz | 5.23 | 4.4 dB  |
| Peaking | 26 Hz   | 0.6  | 1.4 dB  |
| Peaking | 75 Hz   | 0.7  | -2.2 dB |
| Peaking | 81 Hz   | 2.11 | 2.7 dB  |
| Peaking | 721 Hz  | 1.84 | 0.7 dB  |
| Peaking | 9127 Hz | 5.07 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Club%20Setting/AKG%20K267%20Tiesto%20Club%20Setting.png)