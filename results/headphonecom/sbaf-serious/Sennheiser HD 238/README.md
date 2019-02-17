# Sennheiser HD 238
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -1.9; 28 -2.8; 31 -3.5; 34 -4.0; 37 -4.5; 41 -5.0; 45 -5.2; 49 -5.6; 54 -6.3; 60 -6.6; 66 -6.7; 72 -7.1; 79 -7.7; 87 -8.1; 96 -8.4; 106 -8.8; 116 -9.0; 128 -9.2; 141 -9.2; 155 -9.1; 170 -9.3; 187 -9.1; 206 -9.0; 227 -8.8; 249 -8.6; 274 -8.3; 302 -8.0; 332 -7.6; 365 -7.1; 402 -6.8; 442 -6.5; 486 -6.2; 535 -6.0; 588 -5.5; 647 -5.1; 712 -4.9; 783 -4.7; 861 -4.6; 947 -4.6; 1042 -4.8; 1146 -4.9; 1261 -5.3; 1387 -6.0; 1526 -6.8; 1678 -6.1; 1846 -6.0; 2031 -4.9; 2234 -3.5; 2457 -2.6; 2703 -4.2; 2973 -6.7; 3270 -8.2; 3597 -4.7; 3957 -3.6; 4353 -8.5; 4788 -7.2; 5267 -4.5; 5793 -5.7; 6373 -6.6; 7010 -5.8; 7711 -5.0; 8482 -6.4; 9330 -7.4; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -6.7; 16529 -6.0; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 238 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 238 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.29 | 4.8 dB  |
| Peaking | 124 Hz   | 0.65 | -3.9 dB |
| Peaking | 260 Hz   | 1.03 | -2.0 dB |
| Peaking | 6164 Hz  | 0.54 | -1.4 dB |
| Peaking | 20869 Hz | 1.67 | -1.1 dB |
| Peaking | 1714 Hz  | 2.61 | -2.4 dB |
| Peaking | 2584 Hz  | 2.03 | 4.0 dB  |
| Peaking | 2901 Hz  | 5.48 | -3.1 dB |
| Peaking | 3234 Hz  | 9.61 | -3.7 dB |
| Peaking | 15437 Hz | 4.46 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20238/Sennheiser%20HD%20238.png)