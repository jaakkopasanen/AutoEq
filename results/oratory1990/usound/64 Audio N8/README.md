# 64 Audio N8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -5.4; 25 -5.9; 28 -5.9; 31 -6.0; 34 -6.1; 37 -6.2; 41 -6.3; 45 -6.5; 49 -6.6; 54 -6.9; 60 -7.1; 66 -7.6; 72 -7.5; 79 -7.8; 87 -7.9; 96 -7.4; 106 -7.9; 116 -7.7; 128 -7.9; 141 -7.9; 155 -7.8; 170 -7.9; 187 -8.0; 206 -8.0; 227 -8.0; 249 -8.0; 274 -8.0; 302 -7.9; 332 -7.9; 365 -7.7; 402 -7.6; 442 -7.5; 486 -7.3; 535 -7.1; 588 -6.8; 647 -6.5; 712 -6.1; 783 -5.6; 861 -5.2; 947 -5.1; 1042 -5.3; 1146 -6.0; 1261 -7.0; 1387 -7.8; 1526 -8.1; 1678 -8.0; 1846 -7.8; 2031 -7.5; 2234 -7.0; 2457 -6.2; 2703 -5.1; 2973 -4.2; 3270 -3.6; 3597 -3.4; 3957 -3.8; 4353 -4.3; 4788 -4.9; 5267 -4.4; 5793 -0.9; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -7.1; 15026 -9.4; 16529 -6.3; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 167 Hz   |  0.42 | -2.3 dB |
| Peaking | 1744 Hz  |  2.28 | -2.5 dB |
| Peaking | 3436 Hz  |  2.59 | 2.6 dB  |
| Peaking | 6185 Hz  |  4.56 | 6.0 dB  |
| Peaking | 14907 Hz |  3.57 | -4.0 dB |
| Peaking | 20 Hz    |  2.69 | 2.5 dB  |
| Peaking | 457 Hz   |  1.52 | -0.6 dB |
| Peaking | 946 Hz   |  2.07 | 1.6 dB  |
| Peaking | 1356 Hz  |  4.46 | -1.2 dB |
| Peaking | 5072 Hz  | 12.74 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/64%20Audio%20N8/64%20Audio%20N8.png)