# Sennheiser HD 439
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.7; 25 -7.0; 28 -7.5; 31 -7.8; 34 -8.1; 37 -8.3; 41 -8.6; 45 -8.8; 49 -9.0; 54 -9.2; 60 -9.4; 66 -9.4; 72 -9.3; 79 -9.7; 87 -10.0; 96 -8.7; 106 -7.6; 116 -9.4; 128 -10.7; 141 -11.1; 155 -11.3; 170 -11.2; 187 -11.4; 206 -11.5; 227 -11.6; 249 -11.5; 274 -11.1; 302 -10.0; 332 -9.1; 365 -8.6; 402 -8.6; 442 -8.2; 486 -8.0; 535 -8.1; 588 -7.8; 647 -7.9; 712 -8.1; 783 -8.1; 861 -8.4; 947 -8.4; 1042 -8.0; 1146 -8.1; 1261 -8.2; 1387 -9.5; 1526 -9.9; 1678 -9.9; 1846 -8.8; 2031 -7.7; 2234 -6.4; 2457 -4.4; 2703 -3.9; 2973 -3.5; 3270 -3.4; 3597 -3.5; 3957 -0.9; 4353 -0.5; 4788 -0.5; 5267 -1.3; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 439 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 1.02 | -2.4 dB |
| Peaking | 203 Hz  | 0.9  | -5.1 dB |
| Peaking | 873 Hz  | 1.92 | -1.4 dB |
| Peaking | 1603 Hz | 2.71 | -4.1 dB |
| Peaking | 4665 Hz | 1.24 | 6.4 dB  |
| Peaking | 102 Hz  | 2.41 | -2.2 dB |
| Peaking | 105 Hz  | 5.89 | 4.3 dB  |
| Peaking | 2614 Hz | 5.77 | 1.6 dB  |
| Peaking | 6332 Hz | 3.57 | 4.8 dB  |
| Peaking | 7049 Hz | 1.36 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)