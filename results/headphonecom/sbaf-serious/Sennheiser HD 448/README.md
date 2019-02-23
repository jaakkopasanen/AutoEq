# Sennheiser HD 448
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.7; 106 -3.1; 116 -4.0; 128 -5.1; 141 -6.6; 155 -8.7; 170 -9.0; 187 -8.0; 206 -6.4; 227 -5.0; 249 -6.5; 274 -6.8; 302 -6.1; 332 -6.7; 365 -6.6; 402 -6.2; 442 -6.4; 486 -6.2; 535 -6.9; 588 -7.2; 647 -7.5; 712 -8.3; 783 -8.8; 861 -8.5; 947 -8.0; 1042 -8.7; 1146 -8.4; 1261 -9.5; 1387 -9.3; 1526 -9.9; 1678 -10.2; 1846 -10.8; 2031 -11.1; 2234 -9.4; 2457 -7.6; 2703 -7.9; 2973 -7.4; 3270 -7.1; 3597 -7.1; 3957 -5.9; 4353 -0.5; 4788 -0.8; 5267 -5.7; 5793 -5.4; 6373 -2.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 448 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 448 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.31 | 6.6 dB  |
| Peaking | 161 Hz  | 2.44 | -5.8 dB |
| Peaking | 1620 Hz | 0.74 | -3.7 dB |
| Peaking | 4510 Hz | 5.37 | 7.6 dB  |
| Peaking | 6564 Hz | 7.18 | 4.9 dB  |
| Peaking | 85 Hz   | 6.46 | 1.2 dB  |
| Peaking | 755 Hz  | 6.77 | -1.2 dB |
| Peaking | 2017 Hz | 4.04 | -3.9 dB |
| Peaking | 2123 Hz | 2.01 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 6.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20448/Sennheiser%20HD%20448.png)