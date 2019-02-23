# Sennheiser HD 800 S sn01067
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.8; 31 -2.2; 34 -2.5; 37 -2.8; 41 -3.1; 45 -3.3; 49 -3.5; 54 -3.7; 60 -3.9; 66 -3.9; 72 -4.1; 79 -4.7; 87 -5.0; 96 -5.7; 106 -6.2; 116 -6.5; 128 -7.0; 141 -7.1; 155 -7.3; 170 -7.3; 187 -7.5; 206 -7.6; 227 -7.6; 249 -7.7; 274 -7.6; 302 -7.5; 332 -7.4; 365 -7.2; 402 -7.1; 442 -6.8; 486 -6.7; 535 -6.6; 588 -6.1; 647 -6.1; 712 -5.9; 783 -5.5; 861 -5.3; 947 -5.1; 1042 -4.7; 1146 -4.6; 1261 -4.1; 1387 -3.8; 1526 -3.3; 1678 -3.5; 1846 -3.6; 2031 -3.3; 2234 -3.5; 2457 -2.9; 2703 -2.5; 2973 -3.1; 3270 -2.7; 3597 -4.1; 3957 -5.3; 4353 -5.2; 4788 -4.6; 5267 -5.4; 5793 -6.5; 6373 -8.9; 7010 -7.9; 7711 -6.2; 8482 -5.8; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.9; 15026 -6.0; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S sn01067 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S sn01067 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 10 Hz   |  0.18 | 5.0 dB  |
| Peaking | 213 Hz  |  0.55 | -2.3 dB |
| Peaking | 1526 Hz |  1.13 | 2.0 dB  |
| Peaking | 2850 Hz |  1.81 | 2.6 dB  |
| Peaking | 6494 Hz |  5.43 | -3.9 dB |
| Peaking | 41 Hz   |  2.67 | -0.6 dB |
| Peaking | 125 Hz  |  4.39 | -0.4 dB |
| Peaking | 4977 Hz | 11.96 | 1.0 dB  |
| Peaking | 7123 Hz | 11.34 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800%20S%20sn01067/Sennheiser%20HD%20800%20S%20sn01067.png)