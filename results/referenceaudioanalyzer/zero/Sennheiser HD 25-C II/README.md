# Sennheiser HD 25-C II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -2.2; 34 -3.1; 37 -3.9; 41 -4.7; 45 -5.4; 49 -6.1; 54 -6.9; 60 -7.7; 66 -8.2; 72 -8.5; 79 -8.7; 87 -9.0; 96 -9.3; 106 -9.7; 116 -10.0; 128 -10.2; 141 -10.1; 155 -9.7; 170 -9.1; 187 -8.3; 206 -7.3; 227 -6.0; 249 -5.3; 274 -5.6; 302 -6.0; 332 -6.1; 365 -5.8; 402 -5.5; 442 -5.3; 486 -5.1; 535 -5.0; 588 -5.0; 647 -5.0; 712 -5.0; 783 -5.0; 861 -5.0; 947 -5.0; 1042 -5.2; 1146 -5.3; 1261 -5.3; 1387 -5.6; 1526 -5.8; 1678 -6.2; 1846 -6.7; 2031 -7.5; 2234 -8.4; 2457 -8.9; 2703 -8.7; 2973 -8.6; 3270 -8.8; 3597 -8.6; 3957 -7.9; 4353 -6.3; 4788 -3.8; 5267 -2.4; 5793 -2.4; 6373 -3.6; 7010 -5.6; 7711 -7.0; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -7.0; 12418 -6.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-C II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-C II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.22 | 6.6 dB  |
| Peaking | 121 Hz   | 0.82 | -5.1 dB |
| Peaking | 678 Hz   | 0.19 | 2.3 dB  |
| Peaking | 3807 Hz  | 0.65 | -5.7 dB |
| Peaking | 5390 Hz  | 1.92 | 8.4 dB  |
| Peaking | 12 Hz    | 1.43 | 1.1 dB  |
| Peaking | 246 Hz   | 3.21 | 2.9 dB  |
| Peaking | 258 Hz   | 1.43 | -1.6 dB |
| Peaking | 3181 Hz  | 3.96 | 0.2 dB  |
| Peaking | 14357 Hz | 2.5  | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%2025-C%20II/Sennheiser%20HD%2025-C%20II.png)