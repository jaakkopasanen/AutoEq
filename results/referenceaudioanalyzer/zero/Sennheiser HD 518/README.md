# Sennheiser HD 518
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.1; 28 -2.1; 31 -3.1; 34 -3.9; 37 -4.6; 41 -5.4; 45 -6.0; 49 -6.5; 54 -6.7; 60 -6.7; 66 -6.7; 72 -7.0; 79 -7.5; 87 -7.9; 96 -8.1; 106 -8.3; 116 -8.5; 128 -8.8; 141 -8.9; 155 -8.9; 170 -9.1; 187 -9.2; 206 -9.2; 227 -9.0; 249 -8.9; 274 -8.9; 302 -8.8; 332 -8.6; 365 -8.4; 402 -8.2; 442 -8.0; 486 -7.8; 535 -7.5; 588 -7.2; 647 -6.7; 712 -6.2; 783 -6.0; 861 -6.0; 947 -5.9; 1042 -5.4; 1146 -4.8; 1261 -4.1; 1387 -3.3; 1526 -2.1; 1678 -0.6; 1846 -0.5; 2031 -1.9; 2234 -4.1; 2457 -5.0; 2703 -4.4; 2973 -3.8; 3270 -5.1; 3597 -6.6; 3957 -7.8; 4353 -9.0; 4788 -9.2; 5267 -7.5; 5793 -4.8; 6373 -3.2; 7010 -4.7; 7711 -6.9; 8482 -7.5; 9330 -6.9; 10263 -6.7; 11289 -7.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 518 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 518 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.31 | 6.3 dB  |
| Peaking | 196 Hz  | 0.5  | -2.8 dB |
| Peaking | 1746 Hz | 1.66 | 6.0 dB  |
| Peaking | 4540 Hz | 3.52 | -3.7 dB |
| Peaking | 6254 Hz | 5.44 | 4.1 dB  |
| Peaking | 743 Hz  | 5.99 | 0.6 dB  |
| Peaking | 2364 Hz | 6.48 | -1.3 dB |
| Peaking | 2965 Hz | 6.14 | 1.9 dB  |
| Peaking | 8398 Hz | 5.34 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20HD%20518/Sennheiser%20HD%20518.png)