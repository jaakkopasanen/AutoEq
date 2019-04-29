# Final Audio Heaven 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -3.9; 25 -4.0; 28 -4.2; 31 -4.4; 34 -4.5; 37 -4.6; 41 -4.7; 45 -4.9; 49 -5.0; 54 -5.2; 60 -5.5; 66 -5.9; 72 -6.2; 79 -6.6; 87 -7.0; 96 -7.5; 106 -7.8; 116 -8.2; 128 -8.5; 141 -8.8; 155 -9.0; 170 -9.2; 187 -9.3; 206 -9.2; 227 -9.2; 249 -9.1; 274 -9.0; 302 -8.8; 332 -8.6; 365 -8.3; 402 -8.0; 442 -7.7; 486 -7.3; 535 -6.9; 588 -6.5; 647 -5.9; 712 -5.3; 783 -4.7; 861 -4.1; 947 -3.8; 1042 -3.9; 1146 -4.3; 1261 -4.8; 1387 -4.9; 1526 -4.5; 1678 -3.8; 1846 -3.0; 2031 -2.6; 2234 -2.6; 2457 -3.1; 2703 -3.9; 2973 -4.5; 3270 -4.1; 3597 -2.7; 3957 -1.3; 4353 -0.5; 4788 -0.7; 5267 -2.0; 5793 -4.0; 6373 -5.2; 7010 -7.0; 7711 -5.6; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.21 | 1.7 dB  |
| Peaking | 191 Hz  | 0.42 | -4.5 dB |
| Peaking | 908 Hz  | 2.01 | 2.2 dB  |
| Peaking | 2091 Hz | 2.58 | 2.7 dB  |
| Peaking | 4449 Hz | 3.05 | 5.2 dB  |
| Peaking | 1352 Hz | 5.23 | -0.2 dB |
| Peaking | 5244 Hz | 5.89 | 0.9 dB  |
| Peaking | 7105 Hz | 5.9  | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20Heaven%204/Final%20Audio%20Heaven%204.png)