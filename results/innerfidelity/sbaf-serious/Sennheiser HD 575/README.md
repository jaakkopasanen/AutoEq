# Sennheiser HD 575
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.9; 41 -1.5; 45 -2.1; 49 -2.5; 54 -2.8; 60 -3.5; 66 -4.2; 72 -4.8; 79 -5.5; 87 -6.3; 96 -7.1; 106 -7.7; 116 -8.0; 128 -8.5; 141 -8.8; 155 -9.1; 170 -9.1; 187 -9.2; 206 -9.3; 227 -9.1; 249 -8.7; 274 -8.7; 302 -8.5; 332 -8.3; 365 -8.0; 402 -7.7; 442 -7.2; 486 -7.0; 535 -6.6; 588 -6.1; 647 -6.0; 712 -5.9; 783 -5.5; 861 -5.7; 947 -5.7; 1042 -5.7; 1146 -5.6; 1261 -5.8; 1387 -6.0; 1526 -6.2; 1678 -5.8; 1846 -4.4; 2031 -4.8; 2234 -5.6; 2457 -7.1; 2703 -9.2; 2973 -10.1; 3270 -10.2; 3597 -8.9; 3957 -7.1; 4353 -6.4; 4788 -5.8; 5267 -4.1; 5793 -5.6; 6373 -4.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 575 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 575 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.36 | 6.6 dB  |
| Peaking | 150 Hz  | 0.51 | -4.2 dB |
| Peaking | 2002 Hz | 0.32 | 1.7 dB  |
| Peaking | 3083 Hz | 2.78 | -5.8 dB |
| Peaking | 6650 Hz | 8.15 | 3.3 dB  |
| Peaking | 1589 Hz | 2.92 | -1.4 dB |
| Peaking | 1915 Hz | 4.29 | 1.9 dB  |
| Peaking | 4811 Hz | 1.36 | -0.4 dB |
| Peaking | 5246 Hz | 6.86 | 2.2 dB  |
| Peaking | 9106 Hz | 1.8  | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20575/Sennheiser%20HD%20575.png)