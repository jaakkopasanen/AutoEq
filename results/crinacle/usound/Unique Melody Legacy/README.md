# Unique Melody Legacy
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.9; 25 -6.2; 28 -6.5; 31 -6.7; 34 -7.0; 37 -7.1; 41 -7.3; 45 -7.5; 49 -7.7; 54 -7.9; 60 -8.1; 66 -8.4; 72 -8.7; 79 -8.9; 87 -9.2; 96 -9.6; 106 -9.8; 116 -10.0; 128 -10.1; 141 -10.2; 155 -10.3; 170 -10.2; 187 -10.0; 206 -9.9; 227 -9.7; 249 -9.4; 274 -9.1; 302 -8.8; 332 -8.5; 365 -8.2; 402 -7.9; 442 -7.7; 486 -7.4; 535 -7.2; 588 -6.9; 647 -6.7; 712 -6.5; 783 -6.2; 861 -6.1; 947 -6.3; 1042 -6.7; 1146 -7.6; 1261 -8.5; 1387 -9.0; 1526 -9.0; 1678 -8.6; 1846 -7.8; 2031 -6.8; 2234 -5.7; 2457 -4.7; 2703 -4.0; 2973 -4.0; 3270 -4.6; 3597 -4.7; 3957 -1.4; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.4; 6373 -4.9; 7010 -6.7; 7711 -7.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Legacy GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Legacy ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 120 Hz  |  0.74 | -3.1 dB |
| Peaking | 234 Hz  |  1.08 | -1.7 dB |
| Peaking | 1513 Hz |  2.68 | -3.1 dB |
| Peaking | 2674 Hz |  3.4  | 2.2 dB  |
| Peaking | 4669 Hz |  2.52 | 6.8 dB  |
| Peaking | 18 Hz   |  1.63 | 1.0 dB  |
| Peaking | 854 Hz  |  1.9  | 2.2 dB  |
| Peaking | 939 Hz  |  1.18 | -1.3 dB |
| Peaking | 5440 Hz | 10.61 | 1.5 dB  |
| Peaking | 7440 Hz |  4.75 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%20Legacy/Unique%20Melody%20Legacy.png)