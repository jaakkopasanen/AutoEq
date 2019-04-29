# Unique Melody Miracle V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -6.9; 25 -7.0; 28 -7.1; 31 -7.2; 34 -7.3; 37 -7.3; 41 -7.3; 45 -7.4; 49 -7.4; 54 -7.5; 60 -7.6; 66 -7.7; 72 -8.0; 79 -8.2; 87 -8.4; 96 -8.7; 106 -8.9; 116 -9.1; 128 -9.3; 141 -9.4; 155 -9.5; 170 -9.5; 187 -9.5; 206 -9.4; 227 -9.3; 249 -9.1; 274 -8.9; 302 -8.8; 332 -8.6; 365 -8.4; 402 -8.3; 442 -8.1; 486 -7.9; 535 -7.7; 588 -7.5; 647 -7.2; 712 -7.0; 783 -6.8; 861 -6.6; 947 -6.7; 1042 -7.1; 1146 -7.9; 1261 -8.7; 1387 -9.1; 1526 -8.9; 1678 -8.1; 1846 -6.7; 2031 -5.0; 2234 -3.5; 2457 -2.5; 2703 -1.7; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.3; 5267 -7.2; 5793 -6.8; 6373 -3.1; 7010 -8.0; 7711 -7.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.4; 18182 -8.1; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Miracle V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Miracle V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 167 Hz   |  0.51 | -3.0 dB |
| Peaking | 444 Hz   |  1.79 | -0.4 dB |
| Peaking | 1497 Hz  |  1.96 | -4.9 dB |
| Peaking | 3949 Hz  |  0.81 | 13.4 dB |
| Peaking | 5152 Hz  |  0.82 | -8.8 dB |
| Peaking | 1911 Hz  |  4.67 | -0.9 dB |
| Peaking | 2054 Hz  |  2.35 | 0.6 dB  |
| Peaking | 5522 Hz  |  9.87 | -3.6 dB |
| Peaking | 6217 Hz  | 12.69 | 5.3 dB  |
| Peaking | 19789 Hz |  0.78 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%20Miracle%20V2/Unique%20Melody%20Miracle%20V2.png)