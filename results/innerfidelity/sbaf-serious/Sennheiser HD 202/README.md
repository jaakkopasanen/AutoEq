# Sennheiser HD 202
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.6; 31 -2.6; 34 -3.4; 37 -4.1; 41 -4.8; 45 -5.5; 49 -6.1; 54 -6.9; 60 -7.5; 66 -7.9; 72 -8.4; 79 -8.4; 87 -8.0; 96 -7.9; 106 -8.4; 116 -8.5; 128 -8.5; 141 -8.5; 155 -8.3; 170 -7.5; 187 -7.3; 206 -6.5; 227 -4.7; 249 -3.4; 274 -3.6; 302 -3.7; 332 -3.3; 365 -2.7; 402 -2.6; 442 -3.3; 486 -3.9; 535 -4.3; 588 -4.6; 647 -5.1; 712 -5.5; 783 -5.6; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -6.9; 1261 -7.2; 1387 -7.6; 1526 -8.1; 1678 -8.2; 1846 -7.3; 2031 -5.7; 2234 -4.4; 2457 -2.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.6; 4788 -4.4; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 2.14 | 6.6 dB  |
| Peaking | 261 Hz  | 5.26 | 2.5 dB  |
| Peaking | 401 Hz  | 2.21 | 4.0 dB  |
| Peaking | 3249 Hz | 2.03 | 6.8 dB  |
| Peaking | 5880 Hz | 3.55 | 5.8 dB  |
| Peaking | 108 Hz  | 1.12 | -2.4 dB |
| Peaking | 1619 Hz | 2.79 | -2.8 dB |
| Peaking | 2563 Hz | 6.38 | 2.4 dB  |
| Peaking | 6669 Hz | 7.45 | 1.8 dB  |
| Peaking | 7729 Hz | 2.41 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20202/Sennheiser%20HD%20202.png)