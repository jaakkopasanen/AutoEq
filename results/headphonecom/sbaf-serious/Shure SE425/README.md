# Shure SE425
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.0; 25 -1.2; 28 -1.5; 31 -1.8; 34 -2.1; 37 -2.3; 41 -2.6; 45 -3.0; 49 -3.3; 54 -3.7; 60 -4.2; 66 -4.7; 72 -5.2; 79 -5.6; 87 -6.1; 96 -6.5; 106 -6.9; 116 -7.2; 128 -7.6; 141 -8.1; 155 -8.3; 170 -8.5; 187 -8.6; 206 -8.7; 227 -8.7; 249 -8.8; 274 -8.8; 302 -8.4; 332 -8.5; 365 -8.2; 402 -8.0; 442 -7.8; 486 -7.6; 535 -7.3; 588 -7.0; 647 -6.7; 712 -6.4; 783 -6.2; 861 -6.3; 947 -6.5; 1042 -6.8; 1146 -7.0; 1261 -7.3; 1387 -7.8; 1526 -8.3; 1678 -8.6; 1846 -8.7; 2031 -8.8; 2234 -8.8; 2457 -8.1; 2703 -6.9; 2973 -5.3; 3270 -3.5; 3597 -2.3; 3957 -2.3; 4353 -2.9; 4788 -2.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.9; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.4  | 5.6 dB  |
| Peaking | 201 Hz  | 0.69 | -2.7 dB |
| Peaking | 2129 Hz | 1.49 | -3.3 dB |
| Peaking | 3652 Hz | 2.11 | 4.4 dB  |
| Peaking | 5715 Hz | 3.01 | 6.2 dB  |
| Peaking | 805 Hz  | 2.96 | 0.9 dB  |
| Peaking | 1524 Hz | 6.19 | -0.6 dB |
| Peaking | 6613 Hz | 7.13 | 2.3 dB  |
| Peaking | 7642 Hz | 3.32 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE425/Shure%20SE425.png)