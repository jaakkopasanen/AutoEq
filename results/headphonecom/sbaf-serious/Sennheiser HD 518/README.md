# Sennheiser HD 518
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.8; 28 -2.7; 31 -3.5; 34 -4.1; 37 -4.7; 41 -5.3; 45 -5.8; 49 -6.3; 54 -6.9; 60 -7.5; 66 -8.0; 72 -8.4; 79 -8.8; 87 -8.7; 96 -8.0; 106 -9.1; 116 -9.8; 128 -10.4; 141 -10.6; 155 -10.9; 170 -10.6; 187 -11.0; 206 -10.8; 227 -10.7; 249 -10.7; 274 -10.5; 302 -10.3; 332 -9.9; 365 -9.7; 402 -9.4; 442 -9.1; 486 -8.9; 535 -8.2; 588 -7.8; 647 -7.9; 712 -7.9; 783 -6.8; 861 -7.1; 947 -6.5; 1042 -6.2; 1146 -5.0; 1261 -4.5; 1387 -3.2; 1526 -2.4; 1678 -1.4; 1846 -2.0; 2031 -3.4; 2234 -4.4; 2457 -4.0; 2703 -4.9; 2973 -6.0; 3270 -6.6; 3597 -5.0; 3957 -5.0; 4353 -8.3; 4788 -8.2; 5267 -6.7; 5793 -4.8; 6373 -3.2; 7010 -4.1; 7711 -6.0; 8482 -7.2; 9330 -6.5; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -8.8; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 518 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 518 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.95 | 6.2 dB  |
| Peaking | 194 Hz   | 0.91 | -1.2 dB |
| Peaking | 202 Hz   | 0.36 | -3.6 dB |
| Peaking | 1669 Hz  | 1.77 | 5.2 dB  |
| Peaking | 19348 Hz | 1.47 | -3.9 dB |
| Peaking | 139 Hz   | 5.85 | -0.3 dB |
| Peaking | 3876 Hz  | 6.52 | 3.5 dB  |
| Peaking | 4454 Hz  | 2.69 | -3.6 dB |
| Peaking | 6349 Hz  | 3.42 | 3.7 dB  |
| Peaking | 8663 Hz  | 7.21 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20518/Sennheiser%20HD%20518.png)