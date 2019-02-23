# AKG K267 Tiesto Studio Setting
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.5; 25 -4.4; 28 -4.4; 31 -4.3; 34 -4.1; 37 -4.0; 41 -3.9; 45 -3.7; 49 -3.4; 54 -3.2; 60 -3.3; 66 -3.6; 72 -3.7; 79 -3.6; 87 -4.4; 96 -5.7; 106 -6.5; 116 -7.4; 128 -8.0; 141 -8.1; 155 -8.0; 170 -7.6; 187 -8.2; 206 -8.1; 227 -8.1; 249 -7.8; 274 -7.4; 302 -6.3; 332 -5.7; 365 -6.0; 402 -6.8; 442 -7.3; 486 -7.8; 535 -7.9; 588 -7.5; 647 -7.6; 712 -7.8; 783 -7.6; 861 -7.8; 947 -8.0; 1042 -8.3; 1146 -8.5; 1261 -9.5; 1387 -10.7; 1526 -10.3; 1678 -9.4; 1846 -8.3; 2031 -7.5; 2234 -6.6; 2457 -5.1; 2703 -5.2; 2973 -4.4; 3270 -4.1; 3597 -3.5; 3957 -2.4; 4353 -0.5; 4788 -0.8; 5267 -5.6; 5793 -1.9; 6373 -1.7; 7010 -3.9; 7711 -6.1; 8482 -6.5; 9330 -7.7; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K267 Tiesto Studio Setting GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Studio Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  1.29 | 2.5 dB  |
| Peaking | 64 Hz   |  2.53 | 2.9 dB  |
| Peaking | 2230 Hz |  0.56 | -6.2 dB |
| Peaking | 2466 Hz |  1.74 | 4.8 dB  |
| Peaking | 4383 Hz |  1.19 | 7.8 dB  |
| Peaking | 184 Hz  |  1.22 | -1.9 dB |
| Peaking | 335 Hz  |  4.74 | 1.8 dB  |
| Peaking | 1430 Hz | 10.25 | -1.4 dB |
| Peaking | 6532 Hz |  4.67 | 5.1 dB  |
| Peaking | 7073 Hz |  1.42 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Studio%20Setting/AKG%20K267%20Tiesto%20Studio%20Setting.png)