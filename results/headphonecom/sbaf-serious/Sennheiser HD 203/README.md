# Sennheiser HD 203
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.5; 25 -2.2; 28 -3.1; 31 -3.7; 34 -4.3; 37 -5.2; 41 -6.6; 45 -7.5; 49 -7.9; 54 -8.5; 60 -9.4; 66 -9.9; 72 -9.9; 79 -9.4; 87 -9.6; 96 -10.5; 106 -10.5; 116 -10.1; 128 -9.7; 141 -9.0; 155 -8.0; 170 -6.7; 187 -4.4; 206 -0.9; 227 -0.8; 249 -1.0; 274 -1.8; 302 -2.8; 332 -4.5; 365 -6.0; 402 -6.4; 442 -6.7; 486 -7.1; 535 -7.0; 588 -6.7; 647 -6.5; 712 -6.3; 783 -6.5; 861 -6.7; 947 -6.6; 1042 -7.1; 1146 -7.3; 1261 -7.5; 1387 -7.8; 1526 -7.9; 1678 -7.5; 1846 -6.0; 2031 -4.9; 2234 -3.4; 2457 -1.9; 2703 -0.9; 2973 -0.8; 3270 -0.8; 3597 -0.8; 3957 -0.8; 4353 -4.8; 4788 -5.2; 5267 -1.7; 5793 -0.9; 6373 -1.4; 7010 -4.3; 7711 -6.5; 8482 -6.8; 9330 -6.8; 10263 -6.8; 11289 -6.8; 12418 -6.8; 13660 -6.8; 15026 -6.8; 16529 -6.8; 18182 -6.8; 20000 -6.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 203 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 203 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.89 | 7.0 dB  |
| Peaking | 152 Hz  |  0.41 | -7.1 dB |
| Peaking | 233 Hz  |  1.3  | 12.6 dB |
| Peaking | 3138 Hz |  1.8  | 6.8 dB  |
| Peaking | 5957 Hz |  4.03 | 5.8 dB  |
| Peaking | 1533 Hz |  3.45 | -2.0 dB |
| Peaking | 2384 Hz |  5.76 | 1.5 dB  |
| Peaking | 4072 Hz |  7.78 | 2.9 dB  |
| Peaking | 4501 Hz | 10.84 | -4.0 dB |
| Peaking | 8275 Hz |  4.65 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 7.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20203/Sennheiser%20HD%20203.png)