# Shure SE310
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.3; 25 -1.3; 28 -1.4; 31 -1.6; 34 -1.7; 37 -1.7; 41 -1.9; 45 -2.2; 49 -2.4; 54 -2.6; 60 -2.8; 66 -3.2; 72 -3.7; 79 -4.0; 87 -4.3; 96 -4.6; 106 -4.9; 116 -5.1; 128 -5.4; 141 -5.7; 155 -5.9; 170 -6.1; 187 -6.2; 206 -6.3; 227 -6.3; 249 -6.4; 274 -6.4; 302 -6.3; 332 -6.1; 365 -5.9; 402 -5.8; 442 -5.6; 486 -5.4; 535 -5.3; 588 -5.1; 647 -5.1; 712 -5.1; 783 -5.2; 861 -5.5; 947 -6.1; 1042 -6.8; 1146 -7.5; 1261 -8.3; 1387 -9.3; 1526 -10.1; 1678 -10.7; 1846 -10.6; 2031 -10.2; 2234 -9.1; 2457 -7.2; 2703 -4.4; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -1.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE310 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE310 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.62 | 4.3 dB  |
| Peaking | 41 Hz   | 0.56 | 3.5 dB  |
| Peaking | 1908 Hz | 1.79 | -6.2 dB |
| Peaking | 3423 Hz | 1.61 | 7.1 dB  |
| Peaking | 5736 Hz | 2.98 | 5.2 dB  |
| Peaking | 693 Hz  | 1.37 | 1.8 dB  |
| Peaking | 1242 Hz | 4    | -0.7 dB |
| Peaking | 1450 Hz | 5.9  | -1.0 dB |
| Peaking | 6592 Hz | 7.76 | 2.1 dB  |
| Peaking | 7828 Hz | 2.24 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE310/Shure%20SE310.png)