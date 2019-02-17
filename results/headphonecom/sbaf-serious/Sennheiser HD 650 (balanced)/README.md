# Sennheiser HD 650 (balanced)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.3; 28 -2.1; 31 -2.8; 34 -3.3; 37 -3.7; 41 -4.2; 45 -4.4; 49 -4.4; 54 -5.0; 60 -6.0; 66 -6.2; 72 -6.3; 79 -7.0; 87 -7.6; 96 -8.1; 106 -8.4; 116 -8.6; 128 -9.1; 141 -9.3; 155 -9.4; 170 -9.1; 187 -9.3; 206 -9.2; 227 -9.1; 249 -8.9; 274 -8.8; 302 -8.5; 332 -8.3; 365 -8.0; 402 -7.6; 442 -7.4; 486 -7.2; 535 -7.2; 588 -7.0; 647 -6.8; 712 -6.9; 783 -6.9; 861 -7.0; 947 -6.6; 1042 -6.8; 1146 -7.2; 1261 -7.5; 1387 -7.7; 1526 -8.1; 1678 -8.4; 1846 -8.6; 2031 -8.6; 2234 -8.3; 2457 -8.2; 2703 -8.1; 2973 -8.1; 3270 -8.2; 3597 -7.4; 3957 -6.1; 4353 -6.8; 4788 -7.2; 5267 -3.8; 5793 -4.2; 6373 -7.3; 7010 -7.2; 7711 -7.1; 8482 -8.7; 9330 -9.1; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 (balanced) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.41 | 7.0 dB  |
| Peaking | 162 Hz   | 0.6  | -3.3 dB |
| Peaking | 1869 Hz  | 1.82 | -2.3 dB |
| Peaking | 2998 Hz  | 3.78 | -1.4 dB |
| Peaking | 8898 Hz  | 6.04 | -3.4 dB |
| Peaking | 5535 Hz  | 5.69 | 5.3 dB  |
| Peaking | 5959 Hz  | 2.06 | -1.9 dB |
| Peaking | 10038 Hz | 2.33 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20650%20(balanced)/Sennheiser%20HD%20650%20(balanced).png)