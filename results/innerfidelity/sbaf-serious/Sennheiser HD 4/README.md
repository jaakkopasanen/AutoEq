# Sennheiser HD 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.0; 31 -1.7; 34 -2.3; 37 -2.9; 41 -3.4; 45 -3.8; 49 -4.1; 54 -4.5; 60 -4.9; 66 -5.3; 72 -5.6; 79 -6.0; 87 -6.3; 96 -6.6; 106 -6.9; 116 -7.0; 128 -7.0; 141 -7.3; 155 -8.0; 170 -7.0; 187 -7.6; 206 -7.9; 227 -7.7; 249 -7.3; 274 -7.0; 302 -6.6; 332 -6.2; 365 -5.7; 402 -5.5; 442 -5.7; 486 -6.2; 535 -6.2; 588 -5.9; 647 -6.0; 712 -6.2; 783 -6.0; 861 -6.2; 947 -6.3; 1042 -6.5; 1146 -6.6; 1261 -6.9; 1387 -7.4; 1526 -7.9; 1678 -8.5; 1846 -8.3; 2031 -7.7; 2234 -7.1; 2457 -5.6; 2703 -3.9; 2973 -2.2; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -4.8; 5267 -5.4; 5793 -2.8; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  1.41 | 6.2 dB  |
| Peaking | 42 Hz   |  2.05 | 1.7 dB  |
| Peaking | 1837 Hz |  2.19 | -2.9 dB |
| Peaking | 3597 Hz |  1.92 | 6.9 dB  |
| Peaking | 6354 Hz |  6.7  | 4.9 dB  |
| Peaking | 233 Hz  |  0.9  | -2.5 dB |
| Peaking | 344 Hz  |  0.93 | 2.1 dB  |
| Peaking | 4492 Hz |  8.76 | 2.8 dB  |
| Peaking | 4966 Hz | 11.01 | -4.0 dB |
| Peaking | 8394 Hz |  4.45 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%204/Sennheiser%20HD%204.png)