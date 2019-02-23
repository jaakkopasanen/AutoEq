# Westone UM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.2; 31 -1.8; 34 -2.3; 37 -2.7; 41 -3.2; 45 -3.7; 49 -4.1; 54 -4.6; 60 -5.2; 66 -5.7; 72 -6.2; 79 -6.7; 87 -7.2; 96 -7.6; 106 -8.0; 116 -8.3; 128 -8.6; 141 -9.1; 155 -9.3; 170 -9.5; 187 -9.7; 206 -9.7; 227 -9.8; 249 -9.8; 274 -9.8; 302 -9.7; 332 -9.6; 365 -9.4; 402 -9.3; 442 -9.2; 486 -9.1; 535 -8.9; 588 -8.5; 647 -8.3; 712 -8.1; 783 -8.2; 861 -8.4; 947 -8.8; 1042 -9.2; 1146 -9.6; 1261 -9.9; 1387 -10.4; 1526 -10.8; 1678 -10.8; 1846 -10.4; 2031 -9.5; 2234 -8.4; 2457 -6.8; 2703 -5.2; 2973 -3.6; 3270 -2.2; 3597 -1.9; 3957 -3.0; 4353 -3.1; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.51 | 6.2 dB  |
| Peaking | 216 Hz  | 0.46 | -3.5 dB |
| Peaking | 1684 Hz | 1.13 | -4.7 dB |
| Peaking | 3303 Hz | 2.01 | 5.1 dB  |
| Peaking | 5591 Hz | 2.54 | 6.3 dB  |
| Peaking | 719 Hz  | 6.11 | 0.4 dB  |
| Peaking | 6565 Hz | 7.26 | 2.3 dB  |
| Peaking | 7697 Hz | 2.21 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20UM1/Westone%20UM1.png)