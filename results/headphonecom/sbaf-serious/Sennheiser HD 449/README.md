# Sennheiser HD 449
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.2; 25 -3.8; 28 -4.6; 31 -5.3; 34 -5.9; 37 -6.5; 41 -7.1; 45 -7.7; 49 -8.1; 54 -8.6; 60 -9.1; 66 -9.3; 72 -9.3; 79 -9.1; 87 -9.1; 96 -8.3; 106 -6.4; 116 -7.2; 128 -9.8; 141 -10.5; 155 -9.3; 170 -8.6; 187 -10.2; 206 -9.6; 227 -9.8; 249 -9.5; 274 -8.1; 302 -6.9; 332 -6.2; 365 -5.7; 402 -5.3; 442 -4.7; 486 -5.0; 535 -4.8; 588 -5.2; 647 -5.9; 712 -6.1; 783 -6.3; 861 -6.2; 947 -6.6; 1042 -6.4; 1146 -6.4; 1261 -7.2; 1387 -8.2; 1526 -8.8; 1678 -8.6; 1846 -8.1; 2031 -6.9; 2234 -5.1; 2457 -3.8; 2703 -3.5; 2973 -2.8; 3270 -2.9; 3597 -2.4; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 449 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 449 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 1.74 | -1.8 dB |
| Peaking | 19 Hz   | 1.38 | 4.6 dB  |
| Peaking | 64 Hz   | 1.36 | -3.0 dB |
| Peaking | 187 Hz  | 1.76 | -3.5 dB |
| Peaking | 4695 Hz | 1.39 | 6.9 dB  |
| Peaking | 248 Hz  | 5.37 | -1.8 dB |
| Peaking | 457 Hz  | 1.47 | 2.1 dB  |
| Peaking | 1693 Hz | 2.07 | -3.5 dB |
| Peaking | 2538 Hz | 2.2  | 2.2 dB  |
| Peaking | 8486 Hz | 3.89 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20449/Sennheiser%20HD%20449.png)