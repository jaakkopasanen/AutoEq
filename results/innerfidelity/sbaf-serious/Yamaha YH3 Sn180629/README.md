# Yamaha YH3 Sn180629
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.7; 25 -4.0; 28 -4.3; 31 -4.6; 34 -4.8; 37 -5.0; 41 -5.1; 45 -5.3; 49 -5.4; 54 -5.6; 60 -5.9; 66 -6.2; 72 -6.4; 79 -6.6; 87 -6.8; 96 -7.2; 106 -7.7; 116 -7.8; 128 -8.1; 141 -8.4; 155 -8.7; 170 -8.7; 187 -9.0; 206 -9.1; 227 -9.1; 249 -9.2; 274 -9.1; 302 -8.9; 332 -8.7; 365 -8.6; 402 -8.8; 442 -8.7; 486 -8.8; 535 -8.7; 588 -8.5; 647 -8.6; 712 -8.5; 783 -7.7; 861 -7.5; 947 -7.1; 1042 -6.0; 1146 -4.6; 1261 -3.2; 1387 -2.2; 1526 -2.2; 1678 -2.4; 1846 -3.0; 2031 -4.8; 2234 -5.8; 2457 -5.8; 2703 -4.5; 2973 -1.6; 3270 -0.5; 3597 -2.2; 3957 -3.1; 4353 -3.0; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.9; 16529 -7.7; 18182 -6.5; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha YH3 Sn180629 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH3 Sn180629 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.19 | 3.0 dB  |
| Peaking | 894 Hz   | 0.08 | -3.0 dB |
| Peaking | 1483 Hz  | 1.5  | 7.3 dB  |
| Peaking | 3230 Hz  | 3.62 | 6.7 dB  |
| Peaking | 5551 Hz  | 1.76 | 8.4 dB  |
| Peaking | 2379 Hz  | 6.11 | -0.8 dB |
| Peaking | 6899 Hz  | 0.21 | 0.2 dB  |
| Peaking | 7865 Hz  | 5.33 | -1.2 dB |
| Peaking | 13954 Hz | 1.3  | 0.6 dB  |
| Peaking | 15918 Hz | 3.18 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH3%20Sn180629/Yamaha%20YH3%20Sn180629.png)