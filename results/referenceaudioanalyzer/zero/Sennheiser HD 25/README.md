# Sennheiser HD 25
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.9; 28 -2.8; 31 -3.6; 34 -4.2; 37 -4.8; 41 -5.4; 45 -5.9; 49 -6.3; 54 -6.7; 60 -7.0; 66 -7.0; 72 -7.1; 79 -7.3; 87 -7.4; 96 -7.6; 106 -7.9; 116 -8.2; 128 -8.5; 141 -8.6; 155 -8.3; 170 -7.9; 187 -7.3; 206 -6.5; 227 -5.4; 249 -4.7; 274 -4.4; 302 -4.2; 332 -4.0; 365 -3.6; 402 -3.3; 442 -3.1; 486 -3.0; 535 -2.8; 588 -2.8; 647 -2.8; 712 -2.8; 783 -2.9; 861 -3.1; 947 -3.1; 1042 -3.4; 1146 -3.8; 1261 -4.1; 1387 -4.2; 1526 -4.4; 1678 -4.7; 1846 -5.0; 2031 -5.3; 2234 -5.8; 2457 -6.6; 2703 -7.2; 2973 -7.5; 3270 -7.3; 3597 -7.0; 3957 -5.8; 4353 -3.7; 4788 -2.5; 5267 -2.5; 5793 -2.2; 6373 -2.6; 7010 -3.1; 7711 -4.3; 8482 -4.6; 9330 -4.6; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.59 | 4.4 dB  |
| Peaking | 70 Hz   | 1.04 | -2.6 dB |
| Peaking | 141 Hz  | 2.06 | -3.7 dB |
| Peaking | 3179 Hz | 2.07 | -3.9 dB |
| Peaking | 5322 Hz | 1.8  | 3.1 dB  |
| Peaking | 190 Hz  | 4.25 | -1.3 dB |
| Peaking | 603 Hz  | 0.73 | 2.0 dB  |
| Peaking | 2353 Hz | 2.88 | -0.7 dB |
| Peaking | 8626 Hz | 4.27 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%2025/Sennheiser%20HD%2025.png)