# Sennheiser HD 800 S sn01070
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -2.0; 31 -2.4; 34 -2.8; 37 -3.1; 41 -3.4; 45 -3.7; 49 -3.9; 54 -4.1; 60 -4.1; 66 -4.2; 72 -4.3; 79 -5.1; 87 -6.0; 96 -6.3; 106 -6.8; 116 -7.2; 128 -7.6; 141 -7.8; 155 -8.0; 170 -8.0; 187 -8.3; 206 -8.4; 227 -8.3; 249 -8.3; 274 -8.2; 302 -8.1; 332 -8.0; 365 -7.8; 402 -7.6; 442 -7.3; 486 -7.3; 535 -7.1; 588 -6.7; 647 -6.5; 712 -6.4; 783 -5.9; 861 -5.8; 947 -5.5; 1042 -5.1; 1146 -4.8; 1261 -4.4; 1387 -3.9; 1526 -3.7; 1678 -4.0; 1846 -4.0; 2031 -3.7; 2234 -4.0; 2457 -3.4; 2703 -3.0; 2973 -3.4; 3270 -2.8; 3597 -3.2; 3957 -5.0; 4353 -5.7; 4788 -5.4; 5267 -6.2; 5793 -6.0; 6373 -8.8; 7010 -9.2; 7711 -7.7; 8482 -6.1; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -7.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S sn01070 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S sn01070 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 213 Hz  | 0.45 | -3.3 dB |
| Peaking | 1548 Hz | 1.38 | 1.7 dB  |
| Peaking | 3046 Hz | 2.23 | 2.4 dB  |
| Peaking | 6867 Hz | 3.77 | -4.5 dB |
| Peaking | 15 Hz   | 0.53 | 5.6 dB  |
| Peaking | 69 Hz   | 2.21 | 1.5 dB  |
| Peaking | 228 Hz  | 1.4  | 0.2 dB  |
| Peaking | 4236 Hz | 8.8  | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800%20S%20sn01070/Sennheiser%20HD%20800%20S%20sn01070.png)