# Sennheiser HD 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.5; 34 -2.1; 37 -2.7; 41 -3.2; 45 -3.7; 49 -4.0; 54 -4.2; 60 -4.9; 66 -5.3; 72 -5.0; 79 -5.7; 87 -6.8; 96 -7.5; 106 -7.9; 116 -8.2; 128 -8.5; 141 -8.7; 155 -8.9; 170 -8.7; 187 -8.9; 206 -9.0; 227 -8.8; 249 -8.7; 274 -8.5; 302 -8.3; 332 -8.2; 365 -7.9; 402 -7.8; 442 -7.5; 486 -7.5; 535 -7.5; 588 -7.1; 647 -7.0; 712 -6.9; 783 -6.7; 861 -7.0; 947 -6.9; 1042 -6.8; 1146 -7.3; 1261 -7.5; 1387 -7.7; 1526 -7.8; 1678 -8.1; 1846 -8.0; 2031 -7.3; 2234 -7.1; 2457 -6.7; 2703 -6.5; 2973 -7.0; 3270 -7.6; 3597 -7.3; 3957 -6.5; 4353 -6.6; 4788 -5.8; 5267 -1.9; 5793 -0.9; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.6  | 6.2 dB  |
| Peaking | 72 Hz   | 3.74 | 1.2 dB  |
| Peaking | 163 Hz  | 0.57 | -2.8 dB |
| Peaking | 3467 Hz | 0.38 | -1.2 dB |
| Peaking | 5836 Hz | 2.9  | 7.0 dB  |
| Peaking | 834 Hz  | 1.96 | 0.4 dB  |
| Peaking | 1659 Hz | 2.43 | -0.9 dB |
| Peaking | 2706 Hz | 2.69 | 1.8 dB  |
| Peaking | 3136 Hz | 2.41 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)