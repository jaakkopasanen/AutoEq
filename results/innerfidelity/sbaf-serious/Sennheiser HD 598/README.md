# Sennheiser HD 598
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.9; 37 -1.5; 41 -2.3; 45 -2.9; 49 -3.3; 54 -4.0; 60 -4.5; 66 -4.5; 72 -5.1; 79 -5.7; 87 -6.3; 96 -7.4; 106 -7.9; 116 -8.2; 128 -8.7; 141 -9.0; 155 -9.2; 170 -9.1; 187 -9.1; 206 -9.1; 227 -8.9; 249 -8.7; 274 -8.5; 302 -8.4; 332 -8.1; 365 -7.8; 402 -7.6; 442 -7.2; 486 -7.2; 535 -7.0; 588 -5.5; 647 -6.0; 712 -5.8; 783 -5.6; 861 -5.6; 947 -5.5; 1042 -5.4; 1146 -5.0; 1261 -4.9; 1387 -4.5; 1526 -4.0; 1678 -3.1; 1846 -2.8; 2031 -3.8; 2234 -4.8; 2457 -5.1; 2703 -5.3; 2973 -4.8; 3270 -6.0; 3597 -6.2; 3957 -6.2; 4353 -8.5; 4788 -8.6; 5267 -6.5; 5793 -4.6; 6373 -3.9; 7010 -4.2; 7711 -6.2; 8482 -7.2; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.48 | 6.3 dB  |
| Peaking | 162 Hz  | 0.67 | -3.4 dB |
| Peaking | 1709 Hz | 1.04 | 3.1 dB  |
| Peaking | 4615 Hz | 5.42 | -3.4 dB |
| Peaking | 6459 Hz | 4.7  | 3.1 dB  |
| Peaking | 606 Hz  | 8.95 | 1.4 dB  |
| Peaking | 1340 Hz | 6.92 | -0.5 dB |
| Peaking | 5672 Hz | 5.71 | 0.5 dB  |
| Peaking | 9166 Hz | 5.77 | -2.7 dB |
| Peaking | 9708 Hz | 3.33 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)