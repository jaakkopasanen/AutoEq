# Sennheiser HD 595
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.2; 45 -1.8; 49 -2.4; 54 -2.5; 60 -2.8; 66 -3.1; 72 -2.3; 79 -3.9; 87 -5.0; 96 -5.7; 106 -6.1; 116 -6.4; 128 -6.9; 141 -7.3; 155 -7.5; 170 -7.5; 187 -7.7; 206 -7.7; 227 -7.7; 249 -7.9; 274 -7.9; 302 -7.7; 332 -7.6; 365 -7.1; 402 -6.9; 442 -6.5; 486 -6.7; 535 -6.8; 588 -6.9; 647 -6.6; 712 -5.9; 783 -6.2; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.1; 1261 -5.7; 1387 -5.3; 1526 -5.1; 1678 -4.9; 1846 -5.0; 2031 -5.6; 2234 -6.0; 2457 -5.5; 2703 -4.6; 2973 -5.1; 3270 -5.5; 3597 -4.8; 3957 -4.0; 4353 -2.7; 4788 -3.9; 5267 -3.0; 5793 -0.6; 6373 -1.8; 7010 -6.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 595 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.24 | 6.4 dB  |
| Peaking | 144 Hz  | 0.56 | -3.4 dB |
| Peaking | 718 Hz  | 2.89 | 0.4 dB  |
| Peaking | 3140 Hz | 0.65 | 1.6 dB  |
| Peaking | 5820 Hz | 4.54 | 5.5 dB  |
| Peaking | 1639 Hz | 3.19 | 0.9 dB  |
| Peaking | 2240 Hz | 6.14 | -1.2 dB |
| Peaking | 3249 Hz | 7.49 | -0.9 dB |
| Peaking | 4307 Hz | 7.2  | 2.0 dB  |
| Peaking | 8071 Hz | 2.01 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20595/Sennheiser%20HD%20595.png)