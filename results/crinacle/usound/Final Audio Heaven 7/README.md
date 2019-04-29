# Final Audio Heaven 7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.1; 45 -1.6; 49 -2.1; 54 -2.6; 60 -3.1; 66 -3.7; 72 -4.3; 79 -4.9; 87 -5.3; 96 -6.0; 106 -6.6; 116 -7.0; 128 -7.5; 141 -8.0; 155 -8.4; 170 -8.8; 187 -9.0; 206 -9.1; 227 -9.2; 249 -9.3; 274 -9.2; 302 -9.1; 332 -9.1; 365 -8.8; 402 -8.7; 442 -8.5; 486 -8.2; 535 -7.9; 588 -7.5; 647 -7.1; 712 -6.5; 783 -5.9; 861 -5.4; 947 -5.0; 1042 -5.1; 1146 -5.6; 1261 -6.0; 1387 -6.1; 1526 -5.7; 1678 -5.0; 1846 -4.3; 2031 -3.9; 2234 -4.0; 2457 -4.9; 2703 -6.9; 2973 -9.9; 3270 -10.0; 3597 -6.3; 3957 -3.2; 4353 -1.2; 4788 -0.5; 5267 -0.6; 5793 -3.1; 6373 -7.1; 7010 -6.5; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven 7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven 7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.5  | 6.4 dB  |
| Peaking | 222 Hz  | 0.63 | -3.4 dB |
| Peaking | 2250 Hz | 0.95 | 2.9 dB  |
| Peaking | 3106 Hz | 3.97 | -7.2 dB |
| Peaking | 4736 Hz | 2.96 | 6.6 dB  |
| Peaking | 934 Hz  | 3.22 | 1.5 dB  |
| Peaking | 1402 Hz | 4.23 | -1.2 dB |
| Peaking | 5535 Hz | 8.36 | 1.9 dB  |
| Peaking | 6515 Hz | 7.54 | -2.7 dB |
| Peaking | 9421 Hz | 6.05 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20Heaven%207/Final%20Audio%20Heaven%207.png)