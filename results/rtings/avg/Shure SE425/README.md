# Shure SE425
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.9; 106 -1.5; 116 -2.6; 128 -3.5; 141 -4.3; 155 -5.0; 170 -5.5; 187 -6.0; 206 -6.4; 227 -6.7; 249 -6.8; 274 -6.9; 302 -6.9; 332 -6.9; 365 -6.8; 402 -6.7; 442 -6.5; 486 -6.3; 535 -5.9; 588 -5.4; 647 -5.0; 712 -4.8; 783 -4.7; 861 -5.0; 947 -6.0; 1042 -6.8; 1146 -7.3; 1261 -7.6; 1387 -7.7; 1526 -7.6; 1678 -7.4; 1846 -7.2; 2031 -6.9; 2234 -6.3; 2457 -5.6; 2703 -4.7; 2973 -4.6; 3270 -5.2; 3597 -6.2; 3957 -6.4; 4353 -5.3; 4788 -2.8; 5267 -0.9; 5793 -0.9; 6373 -3.1; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.31 | 7.2 dB  |
| Peaking | 726 Hz   | 0.82 | 6.1 dB  |
| Peaking | 827 Hz   | 0.16 | -5.1 dB |
| Peaking | 2699 Hz  | 1.51 | 4.7 dB  |
| Peaking | 5500 Hz  | 2.84 | 7.8 dB  |
| Peaking | 17 Hz    | 1.15 | 1.7 dB  |
| Peaking | 44 Hz    | 1.04 | -1.0 dB |
| Peaking | 94 Hz    | 2.35 | 1.3 dB  |
| Peaking | 152 Hz   | 2.49 | -0.6 dB |
| Peaking | 11573 Hz | 2.13 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.5 dB  |
| Peaking | 125 Hz   | 1.41 | 2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE425/Shure%20SE425.png)