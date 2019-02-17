# Grado GR8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.2; 25 -4.2; 28 -4.3; 31 -4.4; 34 -4.5; 37 -4.7; 41 -4.8; 45 -4.9; 49 -5.1; 54 -5.5; 60 -5.8; 66 -6.1; 72 -6.4; 79 -6.7; 87 -7.0; 96 -7.3; 106 -7.6; 116 -8.1; 128 -8.3; 141 -8.6; 155 -8.9; 170 -9.1; 187 -9.2; 206 -9.3; 227 -9.3; 249 -9.2; 274 -9.1; 302 -9.0; 332 -8.8; 365 -8.6; 402 -8.0; 442 -7.8; 486 -7.6; 535 -7.3; 588 -7.1; 647 -6.7; 712 -6.5; 783 -6.3; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.5; 1261 -6.7; 1387 -7.1; 1526 -7.9; 1678 -8.3; 1846 -8.2; 2031 -8.1; 2234 -7.7; 2457 -6.2; 2703 -2.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -4.8; 4353 -4.9; 4788 -3.0; 5267 -0.7; 5793 -0.5; 6373 -2.5; 7010 -8.2; 7711 -7.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 26 Hz   |  0.6  | 2.5 dB  |
| Peaking | 204 Hz  |  0.78 | -3.1 dB |
| Peaking | 3210 Hz |  2.25 | 11.3 dB |
| Peaking | 3565 Hz |  0.63 | -4.9 dB |
| Peaking | 5537 Hz |  3.12 | 8.9 dB  |
| Peaking | 1039 Hz |  1.34 | 1.3 dB  |
| Peaking | 2072 Hz |  1.19 | -1.3 dB |
| Peaking | 2786 Hz | 10.16 | 2.6 dB  |
| Peaking | 7119 Hz |  2.05 | 2.6 dB  |
| Peaking | 7236 Hz |  5.71 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GR8/Grado%20GR8.png)