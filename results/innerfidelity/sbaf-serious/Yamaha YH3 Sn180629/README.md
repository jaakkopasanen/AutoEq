# Yamaha YH3 Sn180629
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.4; 25 -4.7; 28 -5.0; 31 -5.3; 34 -5.5; 37 -5.7; 41 -5.9; 45 -6.0; 49 -6.1; 54 -6.3; 60 -6.6; 66 -6.9; 72 -7.1; 79 -7.3; 87 -7.5; 96 -8.0; 106 -8.4; 116 -8.5; 128 -8.9; 141 -9.2; 155 -9.4; 170 -9.5; 187 -9.8; 206 -9.9; 227 -9.8; 249 -9.9; 274 -9.8; 302 -9.7; 332 -9.4; 365 -9.4; 402 -9.6; 442 -9.5; 486 -9.5; 535 -9.4; 588 -9.2; 647 -9.3; 712 -9.2; 783 -8.5; 861 -8.2; 947 -7.8; 1042 -6.7; 1146 -5.3; 1261 -3.9; 1387 -2.9; 1526 -2.9; 1678 -3.1; 1846 -3.8; 2031 -5.5; 2234 -6.5; 2457 -6.5; 2703 -5.2; 2973 -2.3; 3270 -0.6; 3597 -3.0; 3957 -3.8; 4353 -3.7; 4788 -2.4; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.5; 9330 -7.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.5; 16529 -8.4; 18182 -6.8; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha YH3 Sn180629 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH3 Sn180629 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 198 Hz  | 0.78 | -3.0 dB |
| Peaking | 654 Hz  | 0.74 | -2.8 dB |
| Peaking | 1372 Hz | 1.89 | 2.8 dB  |
| Peaking | 1545 Hz | 2.28 | 2.1 dB  |
| Peaking | 5167 Hz | 1.42 | 5.5 dB  |
| Peaking | 20 Hz   | 1.01 | 2.4 dB  |
| Peaking | 2570 Hz | 1.73 | -7.1 dB |
| Peaking | 3277 Hz | 1.34 | 11.2 dB |
| Peaking | 4024 Hz | 2.46 | -7.6 dB |
| Peaking | 8910 Hz | 2.37 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH3%20Sn180629/Yamaha%20YH3%20Sn180629.png)