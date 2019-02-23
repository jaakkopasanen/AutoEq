# Sennheiser HD 598
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.9; 41 -1.5; 45 -2.0; 49 -2.5; 54 -3.0; 60 -3.4; 66 -3.4; 72 -4.2; 79 -4.0; 87 -4.1; 96 -5.3; 106 -6.0; 116 -6.3; 128 -6.9; 141 -7.2; 155 -7.5; 170 -7.5; 187 -7.8; 206 -7.8; 227 -7.6; 249 -7.8; 274 -7.9; 302 -7.8; 332 -7.6; 365 -7.4; 402 -7.3; 442 -7.2; 486 -7.1; 535 -6.8; 588 -6.7; 647 -6.5; 712 -5.5; 783 -6.1; 861 -6.2; 947 -5.7; 1042 -6.0; 1146 -5.7; 1261 -6.0; 1387 -6.0; 1526 -5.7; 1678 -4.6; 1846 -4.7; 2031 -5.0; 2234 -5.0; 2457 -4.0; 2703 -5.4; 2973 -5.6; 3270 -6.3; 3597 -6.0; 3957 -6.1; 4353 -9.1; 4788 -9.3; 5267 -7.0; 5793 -5.9; 6373 -6.0; 7010 -5.6; 7711 -6.2; 8482 -6.7; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.9; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  0.34 | 6.2 dB  |
| Peaking | 189 Hz   |  0.69 | -2.1 dB |
| Peaking | 2090 Hz  |  0.95 | 1.8 dB  |
| Peaking | 4592 Hz  |  5.56 | -4.1 dB |
| Peaking | 6384 Hz  |  3.08 | 0.8 dB  |
| Peaking | 57 Hz    |  3.89 | -0.3 dB |
| Peaking | 691 Hz   | 13.59 | 1.6 dB  |
| Peaking | 955 Hz   |  7.34 | 0.4 dB  |
| Peaking | 1375 Hz  |  6.57 | -0.6 dB |
| Peaking | 19434 Hz |  1.34 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)