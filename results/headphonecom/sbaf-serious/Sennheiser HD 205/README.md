# Sennheiser HD 205
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.7; 25 -3.1; 28 -3.5; 31 -3.9; 34 -4.3; 37 -4.7; 41 -5.1; 45 -5.2; 49 -5.5; 54 -6.4; 60 -6.7; 66 -6.7; 72 -6.8; 79 -7.6; 87 -8.2; 96 -8.8; 106 -9.1; 116 -9.2; 128 -9.4; 141 -8.8; 155 -7.9; 170 -8.7; 187 -8.7; 206 -8.3; 227 -7.6; 249 -8.0; 274 -7.8; 302 -7.4; 332 -6.8; 365 -5.7; 402 -4.6; 442 -4.5; 486 -6.1; 535 -7.8; 588 -8.0; 647 -6.4; 712 -4.2; 783 -4.9; 861 -6.7; 947 -8.2; 1042 -9.1; 1146 -9.5; 1261 -10.0; 1387 -10.4; 1526 -10.9; 1678 -10.9; 1846 -10.4; 2031 -9.8; 2234 -8.8; 2457 -7.4; 2703 -5.6; 2973 -5.2; 3270 -4.4; 3597 -2.7; 3957 -1.8; 4353 -0.5; 4788 -5.5; 5267 -8.4; 5793 -2.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.4; 10263 -8.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 205 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 205 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.58 | 4.8 dB  |
| Peaking | 119 Hz   | 1.04 | -3.1 dB |
| Peaking | 1590 Hz  | 1.72 | -5.0 dB |
| Peaking | 3982 Hz  | 3.31 | 6.0 dB  |
| Peaking | 6306 Hz  | 7.29 | 6.1 dB  |
| Peaking | 433 Hz   | 2.65 | 5.8 dB  |
| Peaking | 533 Hz   | 1.04 | -4.2 dB |
| Peaking | 724 Hz   | 3.78 | 5.5 dB  |
| Peaking | 9926 Hz  | 5.84 | -3.0 dB |
| Peaking | 10385 Hz | 2.85 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20205/Sennheiser%20HD%20205.png)