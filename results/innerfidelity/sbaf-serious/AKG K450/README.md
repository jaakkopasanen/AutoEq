# AKG K450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.5; 41 -2.0; 45 -2.4; 49 -2.8; 54 -3.2; 60 -3.5; 66 -3.8; 72 -4.1; 79 -4.4; 87 -4.7; 96 -5.1; 106 -5.4; 116 -5.7; 128 -6.0; 141 -6.5; 155 -6.7; 170 -6.8; 187 -7.0; 206 -7.1; 227 -7.2; 249 -7.4; 274 -7.2; 302 -7.3; 332 -7.4; 365 -7.3; 402 -6.9; 442 -7.0; 486 -7.3; 535 -7.5; 588 -7.0; 647 -6.8; 712 -6.6; 783 -6.5; 861 -6.5; 947 -6.1; 1042 -5.7; 1146 -5.5; 1261 -4.5; 1387 -3.6; 1526 -2.6; 1678 -1.6; 1846 -0.9; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.0; 2973 -3.0; 3270 -5.3; 3597 -6.4; 3957 -5.1; 4353 -3.7; 4788 -0.8; 5267 -0.5; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.36 | 6.2 dB  |
| Peaking | 1385 Hz | 0.09 | -1.5 dB |
| Peaking | 2227 Hz | 0.92 | 7.9 dB  |
| Peaking | 3545 Hz | 3.24 | -4.2 dB |
| Peaking | 5512 Hz | 2.01 | 6.6 dB  |
| Peaking | 198 Hz  | 3.33 | -0.2 dB |
| Peaking | 6525 Hz | 8.57 | 1.9 dB  |
| Peaking | 7610 Hz | 3.73 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K450/AKG%20K450.png)