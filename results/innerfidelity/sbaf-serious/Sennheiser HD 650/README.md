# Sennheiser HD 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.1; 34 -1.7; 37 -2.2; 41 -2.8; 45 -3.3; 49 -3.6; 54 -3.8; 60 -4.4; 66 -4.8; 72 -4.6; 79 -5.2; 87 -6.4; 96 -7.0; 106 -7.4; 116 -7.7; 128 -8.0; 141 -8.2; 155 -8.4; 170 -8.3; 187 -8.5; 206 -8.5; 227 -8.3; 249 -8.3; 274 -8.0; 302 -7.9; 332 -7.7; 365 -7.5; 402 -7.4; 442 -7.1; 486 -7.0; 535 -7.0; 588 -6.6; 647 -6.5; 712 -6.4; 783 -6.2; 861 -6.5; 947 -6.5; 1042 -6.3; 1146 -6.8; 1261 -7.0; 1387 -7.3; 1526 -7.3; 1678 -7.6; 1846 -7.5; 2031 -6.8; 2234 -6.7; 2457 -6.3; 2703 -6.0; 2973 -6.5; 3270 -7.1; 3597 -6.9; 3957 -6.0; 4353 -6.1; 4788 -5.3; 5267 -1.4; 5793 -0.6; 6373 -1.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.58 | 6.2 dB  |
| Peaking | 73 Hz   | 3.72 | 1.2 dB  |
| Peaking | 162 Hz  | 0.65 | -2.4 dB |
| Peaking | 5440 Hz | 0.73 | -1.7 dB |
| Peaking | 5826 Hz | 2.57 | 7.9 dB  |
| Peaking | 790 Hz  | 1.98 | 0.5 dB  |
| Peaking | 1637 Hz | 2.44 | -1.0 dB |
| Peaking | 2605 Hz | 5.43 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)