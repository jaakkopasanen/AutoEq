# Teac CT-H02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.1; 25 -6.2; 28 -6.3; 31 -6.4; 34 -6.4; 37 -6.5; 41 -6.5; 45 -6.5; 49 -6.5; 54 -6.5; 60 -6.6; 66 -6.8; 72 -7.0; 79 -7.2; 87 -7.1; 96 -6.9; 106 -7.6; 116 -7.7; 128 -7.2; 141 -6.3; 155 -7.9; 170 -7.1; 187 -8.3; 206 -8.9; 227 -9.1; 249 -9.1; 274 -8.8; 302 -8.7; 332 -8.5; 365 -8.3; 402 -7.9; 442 -7.9; 486 -7.8; 535 -8.0; 588 -8.0; 647 -8.0; 712 -7.8; 783 -7.7; 861 -7.4; 947 -6.8; 1042 -6.5; 1146 -7.0; 1261 -7.1; 1387 -7.3; 1526 -7.6; 1678 -7.4; 1846 -6.4; 2031 -4.8; 2234 -4.0; 2457 -2.5; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.8; 8482 -13.2; 9330 -14.1; 10263 -9.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Teac CT-H02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 343 Hz  |  0.48 | -2.2 dB  |
| Peaking | 1438 Hz |  1.94 | -1.9 dB  |
| Peaking | 1751 Hz |  2.99 | -2.2 dB  |
| Peaking | 4716 Hz |  0.49 | 7.6 dB   |
| Peaking | 8955 Hz |  2.68 | -13.3 dB |
| Peaking | 139 Hz  | 10.37 | 1.6 dB   |
| Peaking | 224 Hz  |  5.07 | -0.9 dB  |
| Peaking | 2910 Hz |  3.95 | 1.4 dB   |
| Peaking | 5104 Hz |  0.83 | -1.1 dB  |
| Peaking | 6226 Hz |  3.67 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 9.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)