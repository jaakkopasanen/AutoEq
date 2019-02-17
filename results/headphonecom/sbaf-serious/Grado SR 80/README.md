# Grado SR 80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.1; 66 -2.1; 72 -3.2; 79 -4.4; 87 -5.4; 96 -6.2; 106 -6.6; 116 -7.1; 128 -7.3; 141 -7.6; 155 -7.6; 170 -7.5; 187 -7.3; 206 -7.3; 227 -7.2; 249 -7.0; 274 -6.6; 302 -6.6; 332 -6.4; 365 -6.2; 402 -6.1; 442 -6.0; 486 -5.9; 535 -5.9; 588 -5.8; 647 -5.8; 712 -5.8; 783 -5.9; 861 -6.0; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.6; 1387 -8.5; 1526 -9.7; 1678 -10.6; 1846 -11.5; 2031 -12.4; 2234 -12.6; 2457 -12.1; 2703 -11.7; 2973 -11.0; 3270 -10.6; 3597 -12.1; 3957 -16.7; 4353 -12.9; 4788 -10.7; 5267 -11.0; 5793 -13.8; 6373 -10.1; 7010 -11.9; 7711 -13.8; 8482 -16.2; 9330 -17.4; 10263 -15.0; 11289 -9.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR 80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 35 Hz    |  0.88 | 7.2 dB   |
| Peaking | 2119 Hz  |  1.88 | -5.8 dB  |
| Peaking | 4030 Hz  |  2.73 | -7.3 dB  |
| Peaking | 8950 Hz  |  2.08 | -11.1 dB |
| Peaking | 20119 Hz |  3.2  | -7.2 dB  |
| Peaking | 61 Hz    |  2.92 | 2.6 dB   |
| Peaking | 133 Hz   |  0.89 | -1.8 dB  |
| Peaking | 636 Hz   |  1.14 | 1.1 dB   |
| Peaking | 5716 Hz  | 11.35 | -4.0 dB  |
| Peaking | 12491 Hz |  4    | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | -8.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR%2080/Grado%20SR%2080.png)