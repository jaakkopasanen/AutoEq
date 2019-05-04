# Sennheiser HD 820
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.0; 25 -5.0; 28 -5.0; 31 -5.0; 34 -4.9; 37 -4.8; 41 -4.7; 45 -4.7; 49 -4.8; 54 -4.9; 60 -5.0; 66 -5.3; 72 -5.6; 79 -6.1; 87 -6.7; 96 -7.4; 106 -7.9; 116 -8.4; 128 -8.7; 141 -9.0; 155 -9.0; 170 -8.7; 187 -8.0; 206 -6.6; 227 -4.5; 249 -1.8; 274 -0.5; 302 -0.5; 332 -1.6; 365 -3.7; 402 -5.2; 442 -6.2; 486 -7.1; 535 -7.6; 588 -8.2; 647 -8.9; 712 -9.7; 783 -10.2; 861 -10.3; 947 -10.3; 1042 -10.1; 1146 -9.7; 1261 -9.3; 1387 -8.7; 1526 -8.1; 1678 -7.3; 1846 -7.4; 2031 -8.3; 2234 -8.4; 2457 -7.6; 2703 -6.8; 2973 -4.9; 3270 -0.9; 3597 -0.5; 3957 -1.4; 4353 -3.7; 4788 -5.6; 5267 -6.8; 5793 -8.0; 6373 -8.2; 7010 -6.7; 7711 -7.5; 8482 -7.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -9.0; 15026 -7.3; 16529 -6.5; 18182 -6.5; 20000 -8.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 820 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 820 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 162 Hz   | 1.66 | -3.8 dB |
| Peaking | 286 Hz   | 2.04 | 7.7 dB  |
| Peaking | 840 Hz   | 1.19 | -3.9 dB |
| Peaking | 3637 Hz  | 2.25 | 10.5 dB |
| Peaking | 3650 Hz  | 0.61 | -3.7 dB |
| Peaking | 39 Hz    | 1.02 | 2.1 dB  |
| Peaking | 1761 Hz  | 4.37 | 2.0 dB  |
| Peaking | 2009 Hz  | 2.2  | -1.2 dB |
| Peaking | 11941 Hz | 1.74 | 1.3 dB  |
| Peaking | 13604 Hz | 3.28 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | 5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -4.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20820/Sennheiser%20HD%20820.png)