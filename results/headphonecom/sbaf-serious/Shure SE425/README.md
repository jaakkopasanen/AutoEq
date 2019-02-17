# Shure SE425
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.1; 28 -1.4; 31 -1.7; 34 -1.9; 37 -2.2; 41 -2.5; 45 -2.8; 49 -3.2; 54 -3.5; 60 -4.1; 66 -4.6; 72 -5.0; 79 -5.5; 87 -5.9; 96 -6.4; 106 -6.8; 116 -7.1; 128 -7.4; 141 -7.9; 155 -8.2; 170 -8.4; 187 -8.5; 206 -8.6; 227 -8.6; 249 -8.6; 274 -8.6; 302 -8.3; 332 -8.3; 365 -8.0; 402 -7.9; 442 -7.7; 486 -7.5; 535 -7.2; 588 -6.8; 647 -6.5; 712 -6.2; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.7; 1526 -8.2; 1678 -8.5; 1846 -8.6; 2031 -8.6; 2234 -8.6; 2457 -8.0; 2703 -6.8; 2973 -5.2; 3270 -3.4; 3597 -2.2; 3957 -2.2; 4353 -2.8; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.45 | 5.8 dB  |
| Peaking | 45 Hz   | 2.05 | 2.9 dB  |
| Peaking | 2390 Hz | 0.96 | -3.6 dB |
| Peaking | 3566 Hz | 1.83 | 5.8 dB  |
| Peaking | 5706 Hz | 2.89 | 6.2 dB  |
| Peaking | 71 Hz   | 1.43 | 1.2 dB  |
| Peaking | 224 Hz  | 0.57 | -2.3 dB |
| Peaking | 800 Hz  | 1.63 | 1.3 dB  |
| Peaking | 6638 Hz | 7.11 | 2.3 dB  |
| Peaking | 7656 Hz | 3.12 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE425/Shure%20SE425.png)