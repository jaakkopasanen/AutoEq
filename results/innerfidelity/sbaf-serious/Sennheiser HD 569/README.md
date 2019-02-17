# Sennheiser HD 569
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.7; 25 -2.5; 28 -3.5; 31 -4.4; 34 -5.1; 37 -5.7; 41 -6.4; 45 -6.9; 49 -7.4; 54 -7.8; 60 -8.2; 66 -8.4; 72 -8.5; 79 -8.5; 87 -8.6; 96 -8.6; 106 -8.7; 116 -9.0; 128 -9.8; 141 -10.4; 155 -9.8; 170 -7.8; 187 -8.3; 206 -7.6; 227 -6.5; 249 -5.4; 274 -4.5; 302 -4.2; 332 -4.2; 365 -4.6; 402 -5.2; 442 -5.9; 486 -6.7; 535 -7.0; 588 -6.6; 647 -6.4; 712 -6.5; 783 -6.4; 861 -6.5; 947 -6.5; 1042 -6.4; 1146 -6.0; 1261 -5.6; 1387 -5.5; 1526 -5.9; 1678 -6.0; 1846 -6.0; 2031 -5.9; 2234 -5.7; 2457 -4.5; 2703 -3.7; 2973 -3.8; 3270 -6.2; 3597 -5.7; 3957 -3.8; 4353 -3.2; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.8; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 569 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 569 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.45 | 6.0 dB  |
| Peaking | 147 Hz  | 0.5  | -3.7 dB |
| Peaking | 295 Hz  | 1.48 | 4.8 dB  |
| Peaking | 2704 Hz | 4.19 | 2.7 dB  |
| Peaking | 5514 Hz | 2.45 | 6.7 dB  |
| Peaking | 107 Hz  | 3.98 | 0.8 dB  |
| Peaking | 141 Hz  | 8.74 | -1.4 dB |
| Peaking | 1322 Hz | 3.98 | 1.0 dB  |
| Peaking | 6486 Hz | 9.68 | 2.0 dB  |
| Peaking | 8882 Hz | 2.76 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20569/Sennheiser%20HD%20569.png)