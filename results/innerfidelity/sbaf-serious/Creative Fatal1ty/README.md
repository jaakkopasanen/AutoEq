# Creative Fatal1ty
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.9; 25 -6.5; 28 -7.3; 31 -7.9; 34 -8.4; 37 -8.9; 41 -9.4; 45 -9.7; 49 -10.0; 54 -10.2; 60 -10.5; 66 -10.6; 72 -10.7; 79 -10.9; 87 -11.1; 96 -11.0; 106 -10.8; 116 -10.8; 128 -10.9; 141 -10.8; 155 -10.6; 170 -10.1; 187 -9.9; 206 -9.5; 227 -8.9; 249 -8.3; 274 -7.8; 302 -6.9; 332 -6.2; 365 -5.4; 402 -5.0; 442 -4.4; 486 -4.3; 535 -4.7; 588 -5.1; 647 -5.8; 712 -6.4; 783 -6.1; 861 -6.5; 947 -6.6; 1042 -6.4; 1146 -6.1; 1261 -6.0; 1387 -6.2; 1526 -6.0; 1678 -5.4; 1846 -4.3; 2031 -2.8; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Fatal1ty GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Fatal1ty ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.12 | 3.6 dB  |
| Peaking | 57 Hz   | 0.31 | -2.1 dB |
| Peaking | 287 Hz  | 0.18 | -3.9 dB |
| Peaking | 446 Hz  | 0.92 | 5.9 dB  |
| Peaking | 3403 Hz | 0.73 | 7.4 dB  |
| Peaking | 1649 Hz | 3.6  | -1.1 dB |
| Peaking | 2354 Hz | 3.3  | 1.5 dB  |
| Peaking | 3438 Hz | 2.39 | -1.2 dB |
| Peaking | 6258 Hz | 2.14 | 5.6 dB  |
| Peaking | 7404 Hz | 1.47 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Fatal1ty/Creative%20Fatal1ty.png)