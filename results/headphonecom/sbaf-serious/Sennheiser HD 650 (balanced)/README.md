# Sennheiser HD 650 (balanced)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.5; 34 -2.0; 37 -2.4; 41 -2.9; 45 -3.1; 49 -3.1; 54 -3.7; 60 -4.7; 66 -4.9; 72 -5.0; 79 -5.7; 87 -6.4; 96 -6.8; 106 -7.1; 116 -7.4; 128 -7.8; 141 -8.0; 155 -8.1; 170 -7.8; 187 -8.0; 206 -7.9; 227 -7.8; 249 -7.7; 274 -7.5; 302 -7.3; 332 -7.0; 365 -6.7; 402 -6.3; 442 -6.1; 486 -5.9; 535 -5.9; 588 -5.7; 647 -5.5; 712 -5.6; 783 -5.7; 861 -5.8; 947 -5.3; 1042 -5.5; 1146 -5.9; 1261 -6.2; 1387 -6.4; 1526 -6.8; 1678 -7.1; 1846 -7.4; 2031 -7.3; 2234 -7.1; 2457 -7.0; 2703 -6.9; 2973 -6.8; 3270 -6.9; 3597 -6.1; 3957 -4.8; 4353 -5.5; 4788 -5.9; 5267 -2.5; 5793 -2.9; 6373 -6.1; 7010 -6.0; 7711 -6.2; 8482 -7.4; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.5
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

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.86 | 5.8 dB  |
| Peaking | 51 Hz   | 0.95 | 1.8 dB  |
| Peaking | 156 Hz  | 0.67 | -2.0 dB |
| Peaking | 650 Hz  | 1.19 | 1.3 dB  |
| Peaking | 5425 Hz | 5.82 | 4.8 dB  |
| Peaking | 1009 Hz | 7.08 | 1.0 dB  |
| Peaking | 1941 Hz | 2.3  | -1.0 dB |
| Peaking | 3870 Hz | 2.46 | -1.4 dB |
| Peaking | 4044 Hz | 5.69 | 3.0 dB  |
| Peaking | 8976 Hz | 8.79 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20650%20(balanced)/Sennheiser%20HD%20650%20(balanced).png)