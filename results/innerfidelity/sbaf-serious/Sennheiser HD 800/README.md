# Sennheiser HD 800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.5; 31 -1.8; 34 -2.0; 37 -2.2; 41 -2.3; 45 -2.3; 49 -2.3; 54 -2.0; 60 -2.1; 66 -2.8; 72 -3.7; 79 -4.3; 87 -4.8; 96 -5.3; 106 -5.6; 116 -5.7; 128 -6.1; 141 -6.3; 155 -6.5; 170 -6.6; 187 -6.7; 206 -6.8; 227 -6.7; 249 -6.8; 274 -6.6; 302 -6.5; 332 -6.4; 365 -6.2; 402 -6.1; 442 -5.7; 486 -5.7; 535 -5.5; 588 -5.1; 647 -5.0; 712 -5.0; 783 -4.4; 861 -4.4; 947 -4.0; 1042 -3.6; 1146 -3.2; 1261 -2.5; 1387 -2.4; 1526 -2.3; 1678 -2.6; 1846 -2.8; 2031 -2.3; 2234 -2.5; 2457 -1.8; 2703 -1.4; 2973 -1.9; 3270 -1.7; 3597 -2.6; 3957 -4.1; 4353 -6.1; 4788 -6.5; 5267 -7.1; 5793 -7.9; 6373 -8.9; 7010 -7.5; 7711 -5.3; 8482 -3.9; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.57 | 3.8 dB  |
| Peaking | 60 Hz    | 2.12 | 2.2 dB  |
| Peaking | 217 Hz   | 0.37 | -3.0 dB |
| Peaking | 4079 Hz  | 0.41 | 4.2 dB  |
| Peaking | 5750 Hz  | 1.24 | -8.4 dB |
| Peaking | 1983 Hz  | 1.29 | 1.4 dB  |
| Peaking | 1988 Hz  | 2.35 | -2.0 dB |
| Peaking | 6762 Hz  | 6.86 | -1.3 dB |
| Peaking | 8309 Hz  | 3.98 | 1.2 dB  |
| Peaking | 12984 Hz | 0.91 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)