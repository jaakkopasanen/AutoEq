# Sennheiser HD 201
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.8; 87 -1.2; 96 -1.4; 106 -1.7; 116 -2.0; 128 -2.2; 141 -2.4; 155 -2.4; 170 -2.4; 187 -2.4; 206 -2.4; 227 -2.2; 249 -2.0; 274 -1.9; 302 -3.4; 332 -4.1; 365 -4.6; 402 -5.3; 442 -5.9; 486 -6.3; 535 -6.4; 588 -6.1; 647 -5.7; 712 -5.7; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -6.4; 1387 -6.7; 1526 -7.9; 1678 -4.6; 1846 -7.1; 2031 -7.8; 2234 -7.3; 2457 -5.8; 2703 -4.8; 2973 -5.2; 3270 -6.5; 3597 -6.7; 3957 -4.4; 4353 -0.5; 4788 -0.5; 5267 -4.7; 5793 -1.8; 6373 -3.5; 7010 -5.6; 7711 -7.6; 8482 -8.6; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 201 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 39 Hz    |  0.24 | 6.2 dB  |
| Peaking | 253 Hz   |  2.3  | 2.8 dB  |
| Peaking | 4793 Hz  |  2.53 | 5.9 dB  |
| Peaking | 8564 Hz  |  4.76 | -2.9 dB |
| Peaking | 21660 Hz |  1.58 | 0.4 dB  |
| Peaking | 493 Hz   |  5.14 | -0.8 dB |
| Peaking | 2106 Hz  |  5.63 | -1.9 dB |
| Peaking | 2740 Hz  |  4.64 | 1.6 dB  |
| Peaking | 3505 Hz  |  6.85 | -2.4 dB |
| Peaking | 6095 Hz  | 10.54 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.8 dB  |
| Peaking | 125 Hz   | 1.41 | 2.9 dB  |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)