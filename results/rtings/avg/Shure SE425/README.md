# Shure SE425
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.8; 49 -1.2; 54 -1.7; 60 -2.2; 66 -2.6; 72 -3.1; 79 -3.6; 87 -4.2; 96 -4.9; 106 -5.1; 116 -5.7; 128 -6.2; 141 -6.5; 155 -6.8; 170 -7.0; 187 -7.2; 206 -7.4; 227 -7.5; 249 -7.6; 274 -7.8; 302 -7.8; 332 -7.8; 365 -7.7; 402 -7.6; 442 -7.5; 486 -7.2; 535 -6.8; 588 -6.4; 647 -6.0; 712 -5.8; 783 -5.7; 861 -6.1; 947 -7.0; 1042 -7.9; 1146 -8.5; 1261 -8.8; 1387 -8.8; 1526 -8.7; 1678 -8.7; 1846 -8.9; 2031 -8.9; 2234 -8.6; 2457 -7.4; 2703 -6.2; 2973 -5.6; 3270 -5.9; 3597 -6.8; 3957 -7.0; 4353 -5.8; 4788 -4.1; 5267 -2.3; 5793 -1.8; 6373 -3.5; 7010 -7.7; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 31 Hz   |  0.46 | 6.4 dB  |
| Peaking | 214 Hz  |  0.81 | -1.8 dB |
| Peaking | 1789 Hz |  1.23 | -2.7 dB |
| Peaking | 2901 Hz |  4.91 | 2.0 dB  |
| Peaking | 5566 Hz |  4.13 | 5.5 dB  |
| Peaking | 226 Hz  |  1.7  | 0.8 dB  |
| Peaking | 466 Hz  |  0.55 | -1.4 dB |
| Peaking | 821 Hz  |  1.02 | 3.0 dB  |
| Peaking | 1102 Hz |  2.23 | -2.3 dB |
| Peaking | 7201 Hz | 10.17 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE425/Shure%20SE425.png)