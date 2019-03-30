# Sennheiser HD 599
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.3; 28 -2.2; 31 -3.0; 34 -3.7; 37 -4.3; 41 -5.0; 45 -5.6; 49 -5.9; 54 -6.2; 60 -6.5; 66 -6.9; 72 -7.2; 79 -7.5; 87 -7.8; 96 -8.0; 106 -8.3; 116 -8.3; 128 -8.3; 141 -8.3; 155 -8.3; 170 -8.2; 187 -8.0; 206 -7.9; 227 -7.6; 249 -7.4; 274 -7.3; 302 -7.1; 332 -7.0; 365 -6.7; 402 -6.4; 442 -6.1; 486 -5.9; 535 -5.6; 588 -5.3; 647 -4.8; 712 -4.4; 783 -4.4; 861 -4.1; 947 -3.9; 1042 -3.7; 1146 -3.3; 1261 -2.9; 1387 -2.4; 1526 -1.8; 1678 -1.3; 1846 -1.2; 2031 -1.9; 2234 -2.7; 2457 -3.5; 2703 -4.7; 2973 -6.7; 3270 -8.7; 3597 -9.7; 3957 -10.7; 4353 -11.6; 4788 -12.3; 5267 -13.4; 5793 -14.4; 6373 -13.6; 7010 -10.1; 7711 -6.3; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 599 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 599 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.07 | 6.0 dB  |
| Peaking | 130 Hz  | 0.7  | -2.3 dB |
| Peaking | 1682 Hz | 0.88 | 5.5 dB  |
| Peaking | 5105 Hz | 1.45 | -8.5 dB |
| Peaking | 676 Hz  | 4.03 | 0.8 dB  |
| Peaking | 3547 Hz | 2.57 | -3.1 dB |
| Peaking | 5420 Hz | 0.91 | 3.3 dB  |
| Peaking | 6320 Hz | 2.84 | -6.2 dB |
| Peaking | 7668 Hz | 3.13 | 2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20599/Sennheiser%20HD%20599.png)