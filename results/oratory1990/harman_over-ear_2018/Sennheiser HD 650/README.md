# Sennheiser HD 650
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.3; 45 -1.5; 49 -1.7; 54 -2.1; 60 -2.4; 66 -3.0; 72 -3.8; 79 -4.7; 87 -5.4; 96 -6.1; 106 -6.7; 116 -7.1; 128 -7.5; 141 -7.9; 155 -8.1; 170 -8.2; 187 -8.3; 206 -8.4; 227 -8.3; 249 -8.1; 274 -7.9; 302 -7.7; 332 -7.5; 365 -7.2; 402 -7.0; 442 -6.9; 486 -6.8; 535 -6.5; 588 -6.3; 647 -6.3; 712 -6.3; 783 -6.4; 861 -6.4; 947 -6.3; 1042 -6.6; 1146 -6.5; 1261 -6.3; 1387 -5.9; 1526 -5.5; 1678 -5.2; 1846 -4.7; 2031 -4.4; 2234 -4.3; 2457 -4.9; 2703 -5.7; 2973 -6.2; 3270 -6.1; 3597 -5.0; 3957 -3.5; 4353 -2.2; 4788 -4.2; 5267 -4.5; 5793 -2.5; 6373 -3.5; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.3; 15026 -8.9; 16529 -11.5; 18182 -13.6; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 31 Hz    |  0.92 | 6.8 dB  |
| Peaking | 2021 Hz  |  3.03 | 2.0 dB  |
| Peaking | 5288 Hz  |  1.28 | 3.4 dB  |
| Peaking | 18694 Hz |  0.82 | -7.8 dB |
| Peaking | 22050 Hz |  1.76 | 2.2 dB  |
| Peaking | 63 Hz    |  2.35 | 2.0 dB  |
| Peaking | 179 Hz   |  0.88 | -2.3 dB |
| Peaking | 3139 Hz  |  5.52 | -1.2 dB |
| Peaking | 4230 Hz  | 10.07 | 2.0 dB  |
| Peaking | 12940 Hz |  4.48 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)