# Shure SE110
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.8; 25 -2.9; 28 -3.1; 31 -3.2; 34 -3.4; 37 -3.5; 41 -3.7; 45 -3.9; 49 -4.2; 54 -4.4; 60 -4.8; 66 -5.2; 72 -5.5; 79 -5.8; 87 -6.4; 96 -6.6; 106 -6.9; 116 -7.1; 128 -7.7; 141 -8.0; 155 -8.2; 170 -8.4; 187 -8.5; 206 -8.6; 227 -8.6; 249 -8.8; 274 -8.9; 302 -8.8; 332 -8.6; 365 -8.5; 402 -8.3; 442 -8.3; 486 -8.2; 535 -8.1; 588 -8.0; 647 -7.8; 712 -7.8; 783 -7.9; 861 -8.1; 947 -8.5; 1042 -9.0; 1146 -9.4; 1261 -10.1; 1387 -11.4; 1526 -12.9; 1678 -13.6; 1846 -13.5; 2031 -12.1; 2234 -10.4; 2457 -9.3; 2703 -6.8; 2973 -3.9; 3270 -1.4; 3597 -0.5; 3957 -1.4; 4353 -2.9; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE110 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE110 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  0.34 | 3.8 dB  |
| Peaking | 219 Hz  |  0.52 | -2.5 dB |
| Peaking | 1785 Hz |  1.42 | -7.7 dB |
| Peaking | 3475 Hz |  2.46 | 7.1 dB  |
| Peaking | 5655 Hz |  2.66 | 6.3 dB  |
| Peaking | 2496 Hz | 10.59 | -0.5 dB |
| Peaking | 6617 Hz |  7.68 | 2.1 dB  |
| Peaking | 7762 Hz |  2.39 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -7.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE110/Shure%20SE110.png)