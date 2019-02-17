# Sennheiser HD 439
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.4; 25 -6.6; 28 -6.9; 31 -7.2; 34 -7.4; 37 -7.5; 41 -7.7; 45 -7.8; 49 -8.0; 54 -8.1; 60 -8.2; 66 -8.2; 72 -8.1; 79 -7.7; 87 -8.5; 96 -7.7; 106 -5.2; 116 -6.8; 128 -8.7; 141 -9.2; 155 -9.2; 170 -8.9; 187 -8.9; 206 -9.1; 227 -9.3; 249 -9.0; 274 -8.6; 302 -7.7; 332 -7.8; 365 -6.1; 402 -6.1; 442 -5.9; 486 -5.5; 535 -5.5; 588 -5.8; 647 -6.2; 712 -6.0; 783 -6.3; 861 -6.7; 947 -7.2; 1042 -6.3; 1146 -6.4; 1261 -6.1; 1387 -7.7; 1526 -8.1; 1678 -7.8; 1846 -6.9; 2031 -5.4; 2234 -3.5; 2457 -1.8; 2703 -1.2; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 439 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 1.48 | -1.6 dB |
| Peaking | 212 Hz  | 1.05 | -3.0 dB |
| Peaking | 450 Hz  | 1.83 | 1.6 dB  |
| Peaking | 1629 Hz | 2.47 | -3.8 dB |
| Peaking | 3738 Hz | 0.82 | 7.0 dB  |
| Peaking | 108 Hz  | 5.96 | 5.2 dB  |
| Peaking | 109 Hz  | 2.25 | -2.4 dB |
| Peaking | 3900 Hz | 4.94 | -1.0 dB |
| Peaking | 6268 Hz | 2.43 | 4.6 dB  |
| Peaking | 7574 Hz | 1.6  | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)