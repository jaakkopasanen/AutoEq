# Shure SE530
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.6; 25 -4.6; 28 -4.8; 31 -4.9; 34 -5.0; 37 -5.1; 41 -5.3; 45 -5.5; 49 -5.7; 54 -5.9; 60 -6.3; 66 -6.6; 72 -7.0; 79 -7.3; 87 -7.8; 96 -8.2; 106 -8.6; 116 -8.8; 128 -9.2; 141 -9.4; 155 -9.7; 170 -9.9; 187 -9.9; 206 -10.1; 227 -9.9; 249 -10.0; 274 -9.9; 302 -9.8; 332 -9.5; 365 -9.4; 402 -9.1; 442 -8.7; 486 -8.5; 535 -8.1; 588 -7.5; 647 -7.2; 712 -7.0; 783 -6.5; 861 -6.5; 947 -6.6; 1042 -6.7; 1146 -6.8; 1261 -7.1; 1387 -7.5; 1526 -7.9; 1678 -8.4; 1846 -8.4; 2031 -8.4; 2234 -7.9; 2457 -6.2; 2703 -4.4; 2973 -2.6; 3270 -1.3; 3597 -0.8; 3957 -1.2; 4353 -2.3; 4788 -1.8; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE530 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.53 | 2.0 dB  |
| Peaking | 205 Hz  | 0.57 | -3.8 dB |
| Peaking | 2012 Hz | 1.98 | -3.3 dB |
| Peaking | 3474 Hz | 1.75 | 5.9 dB  |
| Peaking | 5771 Hz | 3.05 | 5.5 dB  |
| Peaking | 469 Hz  | 1.12 | -1.6 dB |
| Peaking | 608 Hz  | 0.65 | 1.4 dB  |
| Peaking | 1465 Hz | 2.79 | -0.8 dB |
| Peaking | 6574 Hz | 7.89 | 2.0 dB  |
| Peaking | 7779 Hz | 2.23 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE530/Shure%20SE530.png)