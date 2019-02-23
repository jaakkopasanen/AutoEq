# Sennheiser HD 595
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -1.4; 66 -2.1; 72 -2.6; 79 -3.0; 87 -4.0; 96 -5.0; 106 -5.6; 116 -6.0; 128 -6.6; 141 -7.0; 155 -7.3; 170 -7.5; 187 -7.7; 206 -7.9; 227 -7.9; 249 -7.9; 274 -8.0; 302 -8.0; 332 -8.0; 365 -7.9; 402 -7.9; 442 -7.7; 486 -7.9; 535 -7.6; 588 -7.1; 647 -7.2; 712 -7.4; 783 -7.3; 861 -7.5; 947 -7.7; 1042 -7.9; 1146 -7.9; 1261 -8.3; 1387 -8.2; 1526 -8.0; 1678 -7.4; 1846 -6.4; 2031 -5.8; 2234 -6.3; 2457 -6.6; 2703 -6.9; 2973 -6.2; 3270 -5.4; 3597 -4.5; 3957 -2.9; 4353 -3.6; 4788 -4.6; 5267 -4.1; 5793 -2.8; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.7; 9330 -9.2; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.6; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 595 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.53 | 7.4 dB  |
| Peaking | 245 Hz   | 0.21 | -1.9 dB |
| Peaking | 4008 Hz  | 3.47 | 3.4 dB  |
| Peaking | 6308 Hz  | 3.71 | 5.0 dB  |
| Peaking | 9278 Hz  | 5.38 | -3.0 dB |
| Peaking | 73 Hz    | 4.37 | 0.7 dB  |
| Peaking | 642 Hz   | 2.14 | 1.0 dB  |
| Peaking | 1590 Hz  | 1.32 | -1.4 dB |
| Peaking | 1975 Hz  | 3.59 | 2.1 dB  |
| Peaking | 18695 Hz | 1.95 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20595/Sennheiser%20HD%20595.png)