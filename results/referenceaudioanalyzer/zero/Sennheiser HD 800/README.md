# Sennheiser HD 800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.4; 31 -2.1; 34 -2.6; 37 -3.1; 41 -3.6; 45 -3.8; 49 -3.7; 54 -3.8; 60 -4.4; 66 -5.0; 72 -5.4; 79 -5.8; 87 -6.2; 96 -6.5; 106 -6.7; 116 -6.8; 128 -7.1; 141 -7.1; 155 -7.2; 170 -7.5; 187 -7.5; 206 -7.5; 227 -7.5; 249 -7.5; 274 -7.3; 302 -7.1; 332 -7.1; 365 -7.1; 402 -6.8; 442 -6.8; 486 -6.5; 535 -6.5; 588 -6.5; 647 -6.3; 712 -6.2; 783 -5.9; 861 -5.8; 947 -5.6; 1042 -5.3; 1146 -4.7; 1261 -3.9; 1387 -3.3; 1526 -2.6; 1678 -1.9; 1846 -1.4; 2031 -1.3; 2234 -1.3; 2457 -1.3; 2703 -1.4; 2973 -1.9; 3270 -2.3; 3597 -3.0; 3957 -6.2; 4353 -10.7; 4788 -14.3; 5267 -16.9; 5793 -17.8; 6373 -16.3; 7010 -12.2; 7711 -8.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -6.9; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 0.88 | 6.0 dB   |
| Peaking | 56 Hz   | 1.77 | 1.6 dB   |
| Peaking | 621 Hz  | 0.14 | -1.4 dB  |
| Peaking | 3036 Hz | 0.5  | 9.2 dB   |
| Peaking | 5477 Hz | 1.79 | -18.1 dB |
| Peaking | 1021 Hz | 1.35 | -1.6 dB  |
| Peaking | 1096 Hz | 0.6  | 1.1 dB   |
| Peaking | 6557 Hz | 5.62 | -3.8 dB  |
| Peaking | 7526 Hz | 0.56 | -1.1 dB  |
| Peaking | 7957 Hz | 1.5  | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.5 dB |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)