# Sennheiser HD 239
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.8; 25 -3.3; 28 -3.9; 31 -4.3; 34 -4.7; 37 -5.0; 41 -5.5; 45 -5.8; 49 -6.1; 54 -6.4; 60 -6.7; 66 -7.0; 72 -7.2; 79 -7.4; 87 -7.6; 96 -8.0; 106 -8.3; 116 -8.4; 128 -8.7; 141 -8.8; 155 -8.7; 170 -8.5; 187 -8.4; 206 -8.3; 227 -8.0; 249 -7.7; 274 -7.5; 302 -7.2; 332 -7.0; 365 -6.6; 402 -6.3; 442 -6.0; 486 -5.9; 535 -5.7; 588 -5.2; 647 -5.1; 712 -5.0; 783 -4.8; 861 -4.9; 947 -4.9; 1042 -5.0; 1146 -5.1; 1261 -5.5; 1387 -5.6; 1526 -6.2; 1678 -7.1; 1846 -6.7; 2031 -5.1; 2234 -3.3; 2457 -2.0; 2703 -2.7; 2973 -4.5; 3270 -7.1; 3597 -3.2; 3957 -0.5; 4353 -6.4; 4788 -7.0; 5267 -5.4; 5793 -4.6; 6373 -3.9; 7010 -4.3; 7711 -5.8; 8482 -7.2; 9330 -10.2; 10263 -8.6; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 239 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 239 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.23 | 4.0 dB  |
| Peaking | 141 Hz  |  0.86 | -2.9 dB |
| Peaking | 2500 Hz |  5.83 | 3.9 dB  |
| Peaking | 5763 Hz |  0.47 | 1.5 dB  |
| Peaking | 9501 Hz |  4.17 | -5.8 dB |
| Peaking | 838 Hz  |  1.24 | 1.4 dB  |
| Peaking | 1795 Hz |  2.84 | -2.1 dB |
| Peaking | 2170 Hz |  5.98 | 1.4 dB  |
| Peaking | 3898 Hz | 10.17 | 5.8 dB  |
| Peaking | 4560 Hz |  5.6  | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20239/Sennheiser%20HD%20239.png)