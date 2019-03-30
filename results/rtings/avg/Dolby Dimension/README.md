# Dolby Dimension
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.9; 25 -2.5; 28 -3.2; 31 -3.7; 34 -4.2; 37 -4.5; 41 -5.1; 45 -5.6; 49 -6.0; 54 -6.3; 60 -6.7; 66 -7.0; 72 -7.3; 79 -7.5; 87 -7.7; 96 -8.0; 106 -8.6; 116 -9.1; 128 -9.2; 141 -8.9; 155 -8.7; 170 -8.9; 187 -9.2; 206 -9.2; 227 -8.8; 249 -8.9; 274 -8.9; 302 -8.9; 332 -9.1; 365 -9.0; 402 -9.1; 442 -9.0; 486 -8.9; 535 -9.2; 588 -9.2; 647 -8.7; 712 -8.5; 783 -7.9; 861 -6.9; 947 -5.9; 1042 -5.5; 1146 -6.0; 1261 -5.8; 1387 -5.5; 1526 -5.9; 1678 -6.4; 1846 -6.9; 2031 -7.1; 2234 -6.5; 2457 -5.6; 2703 -5.4; 2973 -6.1; 3270 -7.3; 3597 -7.4; 3957 -6.6; 4353 -3.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -7.3; 10263 -6.5; 11289 -6.8; 12418 -9.2; 13660 -9.6; 15026 -8.6; 16529 -9.9; 18182 -10.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dolby Dimension GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dolby Dimension ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.48 | 6.6 dB  |
| Peaking | 375 Hz   | 0.15 | -3.0 dB |
| Peaking | 1191 Hz  | 1.19 | 3.4 dB  |
| Peaking | 5545 Hz  | 2.22 | 7.6 dB  |
| Peaking | 16486 Hz | 0.55 | -3.4 dB |
| Peaking | 2711 Hz  | 3.7  | 2.2 dB  |
| Peaking | 3667 Hz  | 2.1  | -2.2 dB |
| Peaking | 4635 Hz  | 7.75 | 3.1 dB  |
| Peaking | 8570 Hz  | 4.99 | -1.1 dB |
| Peaking | 10585 Hz | 6.11 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -4.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Dolby%20Dimension/Dolby%20Dimension.png)