# Grado SR 80
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.8; 87 -2.7; 96 -3.5; 106 -4.0; 116 -4.4; 128 -4.7; 141 -4.9; 155 -5.0; 170 -4.8; 187 -4.7; 206 -4.6; 227 -4.6; 249 -4.4; 274 -4.0; 302 -4.0; 332 -3.8; 365 -3.6; 402 -3.5; 442 -3.4; 486 -3.3; 535 -3.3; 588 -3.1; 647 -3.1; 712 -3.2; 783 -3.2; 861 -3.4; 947 -3.7; 1042 -4.1; 1146 -4.4; 1261 -5.0; 1387 -5.9; 1526 -7.0; 1678 -8.0; 1846 -8.9; 2031 -9.8; 2234 -10.0; 2457 -9.5; 2703 -9.1; 2973 -8.4; 3270 -8.0; 3597 -9.5; 3957 -14.1; 4353 -10.2; 4788 -8.0; 5267 -8.4; 5793 -11.1; 6373 -7.5; 7010 -9.2; 7711 -11.2; 8482 -13.6; 9330 -14.8; 10263 -12.4; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR 80 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 37 Hz    |  0.5  | 6.7 dB  |
| Peaking | 697 Hz   |  0.51 | 3.7 dB  |
| Peaking | 2093 Hz  |  1.56 | -4.6 dB |
| Peaking | 3985 Hz  |  6.12 | -6.9 dB |
| Peaking | 9023 Hz  |  2.49 | -8.7 dB |
| Peaking | 39 Hz    |  2.52 | -0.8 dB |
| Peaking | 70 Hz    |  3.45 | 1.5 dB  |
| Peaking | 123 Hz   |  2.16 | -0.7 dB |
| Peaking | 5726 Hz  | 12.46 | -3.6 dB |
| Peaking | 11948 Hz |  4.86 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | -5.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR%2080/Grado%20SR%2080.png)