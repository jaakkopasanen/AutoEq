# Grado GR8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.6; 25 -4.6; 28 -4.7; 31 -4.8; 34 -4.9; 37 -5.1; 41 -5.2; 45 -5.3; 49 -5.5; 54 -5.9; 60 -6.2; 66 -6.5; 72 -6.8; 79 -7.1; 87 -7.4; 96 -7.7; 106 -8.0; 116 -8.4; 128 -8.7; 141 -9.0; 155 -9.3; 170 -9.4; 187 -9.6; 206 -9.7; 227 -9.7; 249 -9.6; 274 -9.5; 302 -9.4; 332 -9.2; 365 -9.0; 402 -8.4; 442 -8.2; 486 -8.0; 535 -7.7; 588 -7.5; 647 -7.1; 712 -6.9; 783 -6.7; 861 -6.7; 947 -6.8; 1042 -6.9; 1146 -6.9; 1261 -7.1; 1387 -7.5; 1526 -8.3; 1678 -8.7; 1846 -8.6; 2031 -8.5; 2234 -8.1; 2457 -6.6; 2703 -3.0; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -5.2; 4353 -5.3; 4788 -3.4; 5267 -1.0; 5793 -0.6; 6373 -2.9; 7010 -8.6; 7711 -8.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 26 Hz   |  0.64 | 2.1 dB  |
| Peaking | 205 Hz  |  0.7  | -3.4 dB |
| Peaking | 3204 Hz |  2.28 | 11.9 dB |
| Peaking | 3354 Hz |  0.62 | -5.3 dB |
| Peaking | 5544 Hz |  3.43 | 8.7 dB  |
| Peaking | 1045 Hz |  0.89 | 3.6 dB  |
| Peaking | 1266 Hz |  0.54 | -2.8 dB |
| Peaking | 2806 Hz | 10.62 | 2.7 dB  |
| Peaking | 7067 Hz |  1.65 | 2.5 dB  |
| Peaking | 7318 Hz |  5.33 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GR8/Grado%20GR8.png)