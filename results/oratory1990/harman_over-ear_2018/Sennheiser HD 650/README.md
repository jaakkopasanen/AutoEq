# Sennheiser HD 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.1; 37 -1.6; 41 -2.0; 45 -2.3; 49 -2.5; 54 -2.8; 60 -3.2; 66 -3.8; 72 -4.6; 79 -5.5; 87 -6.2; 96 -6.9; 106 -7.5; 116 -7.9; 128 -8.2; 141 -8.6; 155 -8.9; 170 -8.9; 187 -9.0; 206 -9.1; 227 -9.0; 249 -8.8; 274 -8.6; 302 -8.4; 332 -8.2; 365 -7.9; 402 -7.7; 442 -7.6; 486 -7.4; 535 -7.2; 588 -7.0; 647 -7.0; 712 -7.0; 783 -7.1; 861 -7.1; 947 -7.0; 1042 -7.2; 1146 -7.2; 1261 -6.9; 1387 -6.6; 1526 -6.2; 1678 -5.8; 1846 -5.5; 2031 -5.1; 2234 -5.0; 2457 -5.6; 2703 -6.4; 2973 -6.9; 3270 -6.7; 3597 -5.7; 3957 -4.1; 4353 -2.9; 4788 -4.8; 5267 -4.9; 5793 -3.3; 6373 -4.2; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.4; 15026 -9.7; 16529 -12.0; 18182 -14.1; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.61 | 6.2 dB  |
| Peaking | 60 Hz    | 1.45 | 1.9 dB  |
| Peaking | 170 Hz   | 0.55 | -3.0 dB |
| Peaking | 5338 Hz  | 1.12 | 2.7 dB  |
| Peaking | 18699 Hz | 0.73 | -8.3 dB |
| Peaking | 2180 Hz  | 1.78 | 4.6 dB  |
| Peaking | 2498 Hz  | 1.04 | -3.6 dB |
| Peaking | 4194 Hz  | 6.61 | 2.7 dB  |
| Peaking | 8125 Hz  | 7.82 | -0.6 dB |
| Peaking | 12156 Hz | 3.77 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)