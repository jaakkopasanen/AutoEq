# KZ ZST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.6; 25 -9.8; 28 -9.9; 31 -10.0; 34 -10.0; 37 -10.1; 41 -10.2; 45 -10.3; 49 -10.3; 54 -10.3; 60 -10.4; 66 -10.5; 72 -10.6; 79 -10.7; 87 -10.8; 96 -10.9; 106 -10.9; 116 -10.9; 128 -10.8; 141 -10.6; 155 -10.4; 170 -10.1; 187 -9.8; 206 -9.5; 227 -9.1; 249 -8.7; 274 -8.3; 302 -7.8; 332 -7.4; 365 -7.0; 402 -6.7; 442 -6.3; 486 -6.0; 535 -5.6; 588 -5.3; 647 -4.9; 712 -4.9; 783 -4.5; 861 -4.3; 947 -4.4; 1042 -4.9; 1146 -5.8; 1261 -6.8; 1387 -7.6; 1526 -8.2; 1678 -8.8; 1846 -9.5; 2031 -10.3; 2234 -10.3; 2457 -9.1; 2703 -7.6; 2973 -7.2; 3270 -7.9; 3597 -6.6; 3957 -1.4; 4353 -0.5; 4788 -1.6; 5267 -2.9; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -7.0; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.3; 13660 -10.1; 15026 -7.5; 16529 -6.5; 18182 -6.5; 20000 -12.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 42 Hz    |  0.43 | -3.7 dB |
| Peaking | 140 Hz   |  1.06 | -3.1 dB |
| Peaking | 2130 Hz  |  2.49 | -4.3 dB |
| Peaking | 4343 Hz  |  4.72 | 6.5 dB  |
| Peaking | 6011 Hz  |  4.21 | 6.2 dB  |
| Peaking | 871 Hz   |  1.24 | 2.7 dB  |
| Peaking | 1460 Hz  |  2.62 | -1.7 dB |
| Peaking | 3372 Hz  | 10.23 | -2.3 dB |
| Peaking | 13569 Hz |  3.54 | -3.7 dB |
| Peaking | 13940 Hz |  2.61 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20ZST/KZ%20ZST.png)