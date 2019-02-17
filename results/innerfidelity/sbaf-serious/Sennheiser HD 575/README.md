# Sennheiser HD 575
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -1.7; 41 -2.4; 45 -2.9; 49 -3.4; 54 -3.7; 60 -4.3; 66 -5.0; 72 -5.7; 79 -6.3; 87 -7.2; 96 -8.0; 106 -8.5; 116 -8.8; 128 -9.3; 141 -9.7; 155 -9.9; 170 -10.0; 187 -10.1; 206 -10.2; 227 -10.0; 249 -9.6; 274 -9.5; 302 -9.3; 332 -9.1; 365 -8.8; 402 -8.5; 442 -8.0; 486 -7.9; 535 -7.5; 588 -7.0; 647 -6.9; 712 -6.7; 783 -6.3; 861 -6.5; 947 -6.6; 1042 -6.6; 1146 -6.4; 1261 -6.7; 1387 -6.8; 1526 -7.1; 1678 -6.7; 1846 -5.3; 2031 -5.7; 2234 -6.5; 2457 -7.9; 2703 -10.1; 2973 -10.9; 3270 -11.0; 3597 -9.8; 3957 -7.9; 4353 -7.2; 4788 -6.6; 5267 -5.0; 5793 -6.4; 6373 -4.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 575 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 575 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.48 | 6.4 dB  |
| Peaking | 169 Hz  | 0.6  | -4.3 dB |
| Peaking | 1989 Hz | 4.28 | 2.0 dB  |
| Peaking | 3076 Hz | 2.83 | -5.2 dB |
| Peaking | 6768 Hz | 6.3  | 3.5 dB  |
| Peaking | 364 Hz  | 2.83 | -0.4 dB |
| Peaking | 762 Hz  | 2.18 | 0.6 dB  |
| Peaking | 5267 Hz | 6.46 | 2.8 dB  |
| Peaking | 5610 Hz | 2.99 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20575/Sennheiser%20HD%20575.png)