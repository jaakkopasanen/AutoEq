# Sennheiser HD 25-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.6; 25 -4.9; 28 -5.4; 31 -5.6; 34 -5.8; 37 -5.9; 41 -5.9; 45 -6.0; 49 -6.0; 54 -5.9; 60 -6.2; 66 -6.5; 72 -6.5; 79 -7.2; 87 -8.7; 96 -10.4; 106 -11.0; 116 -10.8; 128 -10.2; 141 -9.7; 155 -8.9; 170 -9.0; 187 -8.4; 206 -8.0; 227 -7.2; 249 -6.4; 274 -6.1; 302 -5.7; 332 -5.0; 365 -4.6; 402 -4.6; 442 -4.8; 486 -5.2; 535 -5.4; 588 -5.3; 647 -5.6; 712 -6.0; 783 -6.2; 861 -6.7; 947 -7.1; 1042 -7.5; 1146 -7.9; 1261 -8.4; 1387 -9.2; 1526 -10.0; 1678 -10.7; 1846 -10.9; 2031 -10.6; 2234 -9.5; 2457 -7.6; 2703 -6.1; 2973 -4.6; 3270 -4.7; 3597 -4.1; 3957 -2.6; 4353 -1.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.4; 8482 -11.7; 9330 -11.3; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 122 Hz  | 0.79 | -8.1 dB  |
| Peaking | 129 Hz  | 0.23 | 4.0 dB   |
| Peaking | 1802 Hz | 1.32 | -5.9 dB  |
| Peaking | 5672 Hz | 0.86 | 7.8 dB   |
| Peaking | 8651 Hz | 2.71 | -10.1 dB |
| Peaking | 39 Hz   | 2.92 | -0.6 dB  |
| Peaking | 75 Hz   | 3    | 1.9 dB   |
| Peaking | 109 Hz  | 1.2  | -2.0 dB  |
| Peaking | 137 Hz  | 2.69 | 2.1 dB   |
| Peaking | 6359 Hz | 3.65 | 0.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1/Sennheiser%20HD%2025-1.png)