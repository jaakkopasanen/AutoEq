# Sennheiser HD 239
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.8; 25 -3.3; 28 -3.9; 31 -4.3; 34 -4.7; 37 -5.0; 41 -5.5; 45 -5.8; 49 -6.1; 54 -6.4; 60 -6.7; 66 -7.0; 72 -7.2; 79 -7.4; 87 -7.6; 96 -8.0; 106 -8.3; 116 -8.4; 128 -8.7; 141 -8.8; 155 -8.7; 170 -8.5; 187 -8.4; 206 -8.3; 227 -8.0; 249 -7.7; 274 -7.5; 302 -7.2; 332 -7.0; 365 -6.6; 402 -6.3; 442 -6.0; 486 -5.9; 535 -5.7; 588 -5.2; 647 -5.1; 712 -5.0; 783 -4.8; 861 -4.9; 947 -4.9; 1042 -5.0; 1146 -5.1; 1261 -5.5; 1387 -5.6; 1526 -6.2; 1678 -7.1; 1846 -6.7; 2031 -5.1; 2234 -3.3; 2457 -2.0; 2703 -2.7; 2973 -4.5; 3270 -7.1; 3597 -3.2; 3957 -0.5; 4353 -6.4; 4788 -7.0; 5267 -5.4; 5793 -4.6; 6373 -3.9; 7010 -4.3; 7711 -4.6; 8482 -7.2; 9330 -10.2; 10263 -8.6; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 239 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 239 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.45 | 3.1 dB  |
| Peaking | 141 Hz  | 0.55 | -3.8 dB |
| Peaking | 2531 Hz | 6.86 | 3.7 dB  |
| Peaking | 6965 Hz | 3.76 | 1.6 dB  |
| Peaking | 9479 Hz | 4.47 | -6.0 dB |
| Peaking | 759 Hz  | 2.09 | 0.6 dB  |
| Peaking | 1693 Hz | 4.8  | -2.5 dB |
| Peaking | 3334 Hz | 6.77 | -4.9 dB |
| Peaking | 3887 Hz | 3.63 | 7.2 dB  |
| Peaking | 4476 Hz | 4.73 | -5.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20239/Sennheiser%20HD%20239.png)