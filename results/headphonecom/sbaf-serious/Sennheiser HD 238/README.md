# Sennheiser HD 238
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -2.0; 28 -2.8; 31 -3.5; 34 -4.1; 37 -4.6; 41 -5.0; 45 -5.3; 49 -5.7; 54 -6.3; 60 -6.7; 66 -6.7; 72 -7.2; 79 -7.7; 87 -8.2; 96 -8.5; 106 -8.8; 116 -9.0; 128 -9.2; 141 -9.2; 155 -9.2; 170 -9.3; 187 -9.2; 206 -9.1; 227 -8.9; 249 -8.7; 274 -8.4; 302 -8.0; 332 -7.6; 365 -7.2; 402 -6.8; 442 -6.6; 486 -6.3; 535 -6.0; 588 -5.6; 647 -5.2; 712 -5.0; 783 -4.8; 861 -4.7; 947 -4.7; 1042 -4.8; 1146 -4.9; 1261 -5.4; 1387 -6.0; 1526 -6.8; 1678 -6.2; 1846 -6.1; 2031 -5.0; 2234 -3.5; 2457 -2.6; 2703 -4.2; 2973 -6.7; 3270 -8.3; 3597 -4.8; 3957 -3.7; 4353 -8.6; 4788 -7.2; 5267 -4.6; 5793 -5.7; 6373 -6.6; 7010 -5.8; 7711 -6.3; 8482 -6.7; 9330 -7.4; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.8; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 238 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 238 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 15 Hz    |  0.71 | 7.6 dB  |
| Peaking | 152 Hz   |  0.61 | -3.0 dB |
| Peaking | 799 Hz   |  1.17 | 2.3 dB  |
| Peaking | 2402 Hz  |  5.11 | 4.1 dB  |
| Peaking | 15553 Hz |  2.97 | -0.3 dB |
| Peaking | 1512 Hz  |  8.94 | -1.0 dB |
| Peaking | 3228 Hz  |  8.69 | -2.7 dB |
| Peaking | 3808 Hz  | 12.05 | 4.0 dB  |
| Peaking | 5367 Hz  | 12.28 | 2.3 dB  |
| Peaking | 9104 Hz  | 10.55 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20238/Sennheiser%20HD%20238.png)