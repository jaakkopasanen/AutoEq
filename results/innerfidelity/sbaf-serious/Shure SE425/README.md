# Shure SE425
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.9; 31 -1.2; 34 -1.4; 37 -1.7; 41 -2.1; 45 -2.4; 49 -2.7; 54 -3.1; 60 -3.6; 66 -4.0; 72 -4.5; 79 -5.0; 87 -5.5; 96 -6.0; 106 -6.5; 116 -6.8; 128 -7.2; 141 -7.6; 155 -7.8; 170 -8.0; 187 -8.1; 206 -8.2; 227 -8.2; 249 -8.3; 274 -8.3; 302 -8.1; 332 -8.0; 365 -7.9; 402 -7.7; 442 -7.4; 486 -7.3; 535 -7.1; 588 -6.6; 647 -6.3; 712 -6.3; 783 -6.0; 861 -6.1; 947 -6.3; 1042 -6.5; 1146 -6.8; 1261 -7.0; 1387 -7.5; 1526 -8.0; 1678 -8.4; 1846 -8.5; 2031 -8.5; 2234 -8.6; 2457 -7.8; 2703 -6.7; 2973 -4.9; 3270 -3.7; 3597 -3.1; 3957 -3.0; 4353 -3.5; 4788 -2.8; 5267 -0.7; 5793 -0.5; 6373 -1.9; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.31 | 6.0 dB  |
| Peaking | 48 Hz   | 1.94 | 2.9 dB  |
| Peaking | 2223 Hz | 1.29 | -3.3 dB |
| Peaking | 3478 Hz | 1.85 | 4.3 dB  |
| Peaking | 5665 Hz | 3.28 | 6.1 dB  |
| Peaking | 76 Hz   | 1.6  | 1.3 dB  |
| Peaking | 233 Hz  | 0.56 | -2.0 dB |
| Peaking | 770 Hz  | 1.56 | 1.2 dB  |
| Peaking | 8099 Hz | 4.33 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE425/Shure%20SE425.png)