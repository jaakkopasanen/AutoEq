# AKG K67 Tiesto
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.9; 25 -8.4; 28 -8.8; 31 -9.1; 34 -9.2; 37 -9.3; 41 -9.3; 45 -9.1; 49 -8.7; 54 -8.5; 60 -8.7; 66 -8.9; 72 -9.1; 79 -9.8; 87 -10.3; 96 -10.7; 106 -10.9; 116 -10.9; 128 -10.7; 141 -9.9; 155 -8.2; 170 -6.4; 187 -4.2; 206 -3.0; 227 -2.2; 249 -1.4; 274 -0.9; 302 -0.5; 332 -1.0; 365 -1.9; 402 -2.7; 442 -3.3; 486 -4.1; 535 -4.5; 588 -4.6; 647 -5.2; 712 -5.9; 783 -6.5; 861 -7.3; 947 -7.9; 1042 -8.3; 1146 -8.6; 1261 -8.6; 1387 -8.7; 1526 -9.1; 1678 -8.7; 1846 -7.5; 2031 -5.8; 2234 -4.9; 2457 -3.6; 2703 -2.5; 2973 -1.5; 3270 -0.9; 3597 -2.1; 3957 -1.9; 4353 -2.5; 4788 -2.8; 5267 -3.8; 5793 -6.3; 6373 -4.6; 7010 -4.4; 7711 -5.1; 8482 -7.1; 9330 -6.3; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -6.7; 18182 -6.3; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K67 Tiesto GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K67 Tiesto ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.92 | -3.5 dB |
| Peaking | 124 Hz  | 0.92 | -8.1 dB |
| Peaking | 253 Hz  | 0.81 | 7.2 dB  |
| Peaking | 1441 Hz | 0.74 | -5.1 dB |
| Peaking | 3075 Hz | 1.31 | 6.0 dB  |
| Peaking | 2910 Hz | 6.05 | -0.3 dB |
| Peaking | 5162 Hz | 4.77 | 2.4 dB  |
| Peaking | 5597 Hz | 6.38 | -4.0 dB |
| Peaking | 6816 Hz | 1.86 | 0.9 dB  |
| Peaking | 8671 Hz | 5.23 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | 5.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K67%20Tiesto/AKG%20K67%20Tiesto.png)