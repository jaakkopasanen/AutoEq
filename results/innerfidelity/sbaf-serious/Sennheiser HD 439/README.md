# Sennheiser HD 439
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -4.9; 25 -5.2; 28 -5.6; 31 -6.0; 34 -6.3; 37 -6.5; 41 -6.8; 45 -7.0; 49 -7.2; 54 -7.4; 60 -7.6; 66 -7.6; 72 -7.5; 79 -7.9; 87 -8.2; 96 -6.9; 106 -5.7; 116 -7.6; 128 -8.9; 141 -9.2; 155 -9.5; 170 -9.4; 187 -9.6; 206 -9.6; 227 -9.7; 249 -9.7; 274 -9.2; 302 -8.1; 332 -7.3; 365 -6.7; 402 -6.8; 442 -6.4; 486 -6.2; 535 -6.2; 588 -6.0; 647 -6.1; 712 -6.2; 783 -6.3; 861 -6.6; 947 -6.5; 1042 -6.2; 1146 -6.2; 1261 -6.3; 1387 -7.7; 1526 -8.1; 1678 -8.1; 1846 -7.0; 2031 -5.9; 2234 -4.5; 2457 -2.6; 2703 -2.1; 2973 -1.7; 3270 -1.6; 3597 -1.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 439 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.44 | 2.1 dB  |
| Peaking | 61 Hz   | 1.65 | -1.1 dB |
| Peaking | 197 Hz  | 1.35 | -3.6 dB |
| Peaking | 1627 Hz | 3.24 | -3.3 dB |
| Peaking | 4128 Hz | 0.91 | 6.5 dB  |
| Peaking | 105 Hz  | 5.8  | 4.3 dB  |
| Peaking | 105 Hz  | 2.45 | -2.2 dB |
| Peaking | 2577 Hz | 6.45 | 1.6 dB  |
| Peaking | 6170 Hz | 2.51 | 6.1 dB  |
| Peaking | 6897 Hz | 1.19 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)