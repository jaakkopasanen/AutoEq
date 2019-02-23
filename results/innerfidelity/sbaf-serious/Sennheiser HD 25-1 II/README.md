# Sennheiser HD 25-1 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.5; 66 -2.3; 72 -3.1; 79 -3.6; 87 -3.8; 96 -3.9; 106 -5.4; 116 -6.3; 128 -7.4; 141 -8.5; 155 -8.7; 170 -8.7; 187 -9.1; 206 -8.9; 227 -8.7; 249 -8.5; 274 -8.1; 302 -8.1; 332 -8.0; 365 -7.7; 402 -7.3; 442 -7.2; 486 -7.2; 535 -7.0; 588 -6.8; 647 -6.7; 712 -6.8; 783 -6.6; 861 -6.8; 947 -6.9; 1042 -7.0; 1146 -7.2; 1261 -7.5; 1387 -8.2; 1526 -8.9; 1678 -9.7; 1846 -9.9; 2031 -9.9; 2234 -9.5; 2457 -8.1; 2703 -6.2; 2973 -4.4; 3270 -4.5; 3597 -4.8; 3957 -4.2; 4353 -4.6; 4788 -3.1; 5267 -1.8; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.4; 9330 -9.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.27 | 6.7 dB  |
| Peaking | 164 Hz  | 0.76 | -5.5 dB |
| Peaking | 1892 Hz | 2.04 | -4.4 dB |
| Peaking | 6294 Hz | 1.01 | 6.4 dB  |
| Peaking | 8636 Hz | 2.49 | -7.1 dB |
| Peaking | 74 Hz   | 4.06 | -0.7 dB |
| Peaking | 95 Hz   | 6.83 | 1.0 dB  |
| Peaking | 2358 Hz | 7.25 | -1.3 dB |
| Peaking | 2993 Hz | 4.62 | 1.7 dB  |
| Peaking | 4469 Hz | 8.64 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1%20II/Sennheiser%20HD%2025-1%20II.png)