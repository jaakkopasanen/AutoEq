# Sennheiser HD 219
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.6; 25 -3.3; 28 -4.1; 31 -4.9; 34 -5.6; 37 -6.2; 41 -6.9; 45 -7.5; 49 -8.0; 54 -8.6; 60 -9.1; 66 -9.6; 72 -10.0; 79 -10.3; 87 -10.5; 96 -10.8; 106 -10.9; 116 -10.9; 128 -10.6; 141 -10.1; 155 -9.8; 170 -9.7; 187 -9.5; 206 -8.7; 227 -7.9; 249 -7.8; 274 -7.2; 302 -6.0; 332 -4.9; 365 -4.1; 402 -3.9; 442 -3.6; 486 -3.9; 535 -4.2; 588 -4.3; 647 -4.6; 712 -4.2; 783 -4.1; 861 -4.9; 947 -5.6; 1042 -5.9; 1146 -5.9; 1261 -5.7; 1387 -5.6; 1526 -5.1; 1678 -6.3; 1846 -7.0; 2031 -6.5; 2234 -6.1; 2457 -5.3; 2703 -5.4; 2973 -5.2; 3270 -5.3; 3597 -5.3; 3957 -5.7; 4353 -7.5; 4788 -6.5; 5267 -3.1; 5793 -0.9; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -7.6; 9330 -6.1; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 219 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 219 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.61 | 5.8 dB  |
| Peaking | 130 Hz  | 0.35 | -3.5 dB |
| Peaking | 228 Hz  | 0.19 | -3.3 dB |
| Peaking | 431 Hz  | 0.62 | 6.7 dB  |
| Peaking | 6127 Hz | 4.79 | 6.3 dB  |
| Peaking | 1590 Hz | 5.93 | 2.0 dB  |
| Peaking | 1749 Hz | 3.63 | -2.0 dB |
| Peaking | 4414 Hz | 1.19 | 1.8 dB  |
| Peaking | 4454 Hz | 4.63 | -4.2 dB |
| Peaking | 8572 Hz | 5.69 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20219/Sennheiser%20HD%20219.png)