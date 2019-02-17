# Sennheiser HD 25-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.7; 25 -4.1; 28 -4.5; 31 -4.8; 34 -4.9; 37 -5.0; 41 -5.0; 45 -5.1; 49 -5.1; 54 -5.0; 60 -5.3; 66 -5.6; 72 -5.6; 79 -6.3; 87 -7.8; 96 -9.5; 106 -10.1; 116 -9.9; 128 -9.3; 141 -8.8; 155 -8.1; 170 -8.1; 187 -7.5; 206 -7.1; 227 -6.3; 249 -5.5; 274 -5.2; 302 -4.8; 332 -4.1; 365 -3.7; 402 -3.8; 442 -3.9; 486 -4.3; 535 -4.5; 588 -4.5; 647 -4.7; 712 -5.1; 783 -5.3; 861 -5.8; 947 -6.2; 1042 -6.6; 1146 -7.0; 1261 -7.5; 1387 -8.3; 1526 -9.1; 1678 -9.9; 1846 -10.0; 2031 -9.7; 2234 -8.6; 2457 -6.7; 2703 -5.2; 2973 -3.8; 3270 -3.8; 3597 -3.2; 3957 -1.7; 4353 -0.8; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -10.8; 9330 -10.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 121 Hz  | 1.95 | -4.0 dB |
| Peaking | 438 Hz  | 0.84 | 2.7 dB  |
| Peaking | 1837 Hz | 1.64 | -5.3 dB |
| Peaking | 5369 Hz | 0.81 | 7.3 dB  |
| Peaking | 8676 Hz | 2.8  | -8.7 dB |
| Peaking | 16 Hz   | 0.75 | 3.9 dB  |
| Peaking | 63 Hz   | 1.5  | 1.4 dB  |
| Peaking | 98 Hz   | 3.73 | -0.2 dB |
| Peaking | 98 Hz   | 5.31 | -1.6 dB |
| Peaking | 5086 Hz | 4.48 | -0.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1/Sennheiser%20HD%2025-1.png)