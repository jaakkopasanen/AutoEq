# Grado RS2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.0; 45 -2.0; 49 -2.9; 54 -4.0; 60 -5.0; 66 -5.6; 72 -6.6; 79 -7.4; 87 -8.0; 96 -8.5; 106 -8.7; 116 -8.8; 128 -8.9; 141 -8.7; 155 -8.6; 170 -8.4; 187 -8.0; 206 -8.2; 227 -8.1; 249 -7.8; 274 -7.4; 302 -7.0; 332 -7.3; 365 -7.1; 402 -6.8; 442 -6.7; 486 -6.6; 535 -6.4; 588 -6.2; 647 -6.0; 712 -6.0; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.5; 1146 -6.7; 1261 -7.1; 1387 -7.9; 1526 -8.9; 1678 -9.9; 1846 -11.4; 2031 -14.6; 2234 -14.4; 2457 -12.5; 2703 -10.7; 2973 -8.9; 3270 -7.5; 3597 -9.5; 3957 -14.8; 4353 -12.5; 4788 -10.0; 5267 -10.1; 5793 -10.3; 6373 -11.8; 7010 -13.4; 7711 -11.8; 8482 -13.0; 9330 -17.1; 10263 -15.7; 11289 -8.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 31 Hz    |  0.53 | 7.2 dB  |
| Peaking | 99 Hz    |  0.69 | -4.4 dB |
| Peaking | 2137 Hz  |  2.95 | -8.5 dB |
| Peaking | 4117 Hz  |  4.36 | -6.8 dB |
| Peaking | 9139 Hz  |  1.86 | -9.8 dB |
| Peaking | 753 Hz   |  1.88 | 0.9 dB  |
| Peaking | 3363 Hz  | 10.87 | 2.4 dB  |
| Peaking | 6671 Hz  |  6.29 | -3.3 dB |
| Peaking | 11772 Hz |  7.95 | 3.0 dB  |
| Peaking | 13557 Hz |  3.14 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | -7.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS2/Grado%20RS2.png)