# Final Audio Heaven 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.5; 25 -5.9; 28 -6.4; 31 -6.8; 34 -7.1; 37 -7.3; 41 -7.6; 45 -7.9; 49 -8.2; 54 -8.6; 60 -8.9; 66 -9.2; 72 -9.6; 79 -9.9; 87 -10.4; 96 -10.8; 106 -11.1; 116 -11.5; 128 -11.7; 141 -11.9; 155 -12.0; 170 -12.1; 187 -12.1; 206 -12.1; 227 -12.0; 249 -11.7; 274 -11.5; 302 -11.3; 332 -11.0; 365 -10.6; 402 -10.2; 442 -9.8; 486 -9.3; 535 -8.8; 588 -8.3; 647 -7.7; 712 -7.0; 783 -6.3; 861 -5.7; 947 -5.2; 1042 -5.2; 1146 -5.5; 1261 -5.9; 1387 -5.9; 1526 -5.3; 1678 -4.5; 1846 -3.6; 2031 -3.0; 2234 -2.8; 2457 -3.4; 2703 -4.7; 2973 -6.5; 3270 -6.8; 3597 -3.9; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -8.2; 8482 -7.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.94 | 1.8 dB  |
| Peaking | 143 Hz  | 0.59 | -5.1 dB |
| Peaking | 323 Hz  | 1.2  | -2.5 dB |
| Peaking | 2011 Hz | 2.17 | 3.4 dB  |
| Peaking | 5030 Hz | 2.01 | 7.0 dB  |
| Peaking | 955 Hz  | 3.59 | 1.7 dB  |
| Peaking | 3202 Hz | 6.26 | -3.0 dB |
| Peaking | 3977 Hz | 8.12 | 2.7 dB  |
| Peaking | 6480 Hz | 5.89 | 3.2 dB  |
| Peaking | 7832 Hz | 4.3  | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20Heaven%208/Final%20Audio%20Heaven%208.png)