# Sennheiser HD 569
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.5; 25 -3.3; 28 -4.3; 31 -5.2; 34 -5.9; 37 -6.5; 41 -7.2; 45 -7.8; 49 -8.2; 54 -8.6; 60 -9.0; 66 -9.2; 72 -9.3; 79 -9.4; 87 -9.4; 96 -9.5; 106 -9.5; 116 -9.8; 128 -10.6; 141 -11.2; 155 -10.6; 170 -8.6; 187 -9.1; 206 -8.4; 227 -7.3; 249 -6.2; 274 -5.3; 302 -5.0; 332 -5.0; 365 -5.4; 402 -6.0; 442 -6.7; 486 -7.6; 535 -7.8; 588 -7.4; 647 -7.3; 712 -7.3; 783 -7.3; 861 -7.4; 947 -7.3; 1042 -7.2; 1146 -6.8; 1261 -6.4; 1387 -6.4; 1526 -6.7; 1678 -6.8; 1846 -6.8; 2031 -6.8; 2234 -6.6; 2457 -5.3; 2703 -4.5; 2973 -4.6; 3270 -7.0; 3597 -6.5; 3957 -4.6; 4353 -4.1; 4788 -2.9; 5267 -0.5; 5793 -0.7; 6373 -0.9; 7010 -3.8; 7711 -6.0; 8482 -6.8; 9330 -8.8; 10263 -6.4; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -7.3; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 569 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 569 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 18 Hz   |  1.23 | 5.6 dB  |
| Peaking | 52 Hz   |  1.33 | -2.0 dB |
| Peaking | 86 Hz   |  1.46 | -2.1 dB |
| Peaking | 143 Hz  |  2.53 | -4.2 dB |
| Peaking | 5616 Hz |  2.82 | 6.6 dB  |
| Peaking | 206 Hz  |  4.38 | -1.7 dB |
| Peaking | 329 Hz  |  1.26 | 3.8 dB  |
| Peaking | 462 Hz  |  0.83 | -2.8 dB |
| Peaking | 6560 Hz | 10.79 | 2.0 dB  |
| Peaking | 9151 Hz |  5.28 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20569/Sennheiser%20HD%20569.png)