# Sennheiser HD 800 Balanced
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.6; 31 -1.9; 34 -2.2; 37 -2.3; 41 -2.4; 45 -2.3; 49 -2.1; 54 -2.1; 60 -3.1; 66 -3.8; 72 -3.7; 79 -4.4; 87 -4.9; 96 -5.3; 106 -5.5; 116 -5.7; 128 -6.1; 141 -6.4; 155 -6.6; 170 -6.5; 187 -6.8; 206 -6.7; 227 -6.5; 249 -6.5; 274 -6.5; 302 -6.4; 332 -5.9; 365 -5.8; 402 -5.5; 442 -5.3; 486 -5.2; 535 -4.8; 588 -4.6; 647 -4.4; 712 -4.2; 783 -4.0; 861 -4.0; 947 -3.5; 1042 -3.4; 1146 -2.5; 1261 -2.4; 1387 -2.2; 1526 -2.6; 1678 -2.3; 1846 -2.0; 2031 -1.9; 2234 -2.6; 2457 -2.1; 2703 -1.5; 2973 -3.5; 3270 -1.9; 3597 -1.3; 3957 -2.9; 4353 -5.5; 4788 -6.1; 5267 -6.7; 5793 -6.8; 6373 -8.2; 7010 -8.8; 7711 -8.9; 8482 -5.7; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 Balanced GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 Balanced ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.74 | 4.4 dB  |
| Peaking | 51 Hz   | 1.58 | 2.0 dB  |
| Peaking | 201 Hz  | 0.56 | -2.3 dB |
| Peaking | 3660 Hz | 0.3  | 3.7 dB  |
| Peaking | 6580 Hz | 1.23 | -7.2 dB |
| Peaking | 3638 Hz | 7.98 | 1.9 dB  |
| Peaking | 4498 Hz | 7.47 | -2.0 dB |
| Peaking | 7724 Hz | 7.71 | -1.7 dB |
| Peaking | 8732 Hz | 7.61 | 0.9 dB  |
| Peaking | 9030 Hz | 4.14 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%20Balanced/Sennheiser%20HD%20800%20Balanced.png)