# Final Audio E4000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.7; 25 -5.2; 28 -5.9; 31 -6.5; 34 -7.0; 37 -7.4; 41 -7.8; 45 -8.1; 49 -8.4; 54 -8.7; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.0; 87 -10.3; 96 -10.5; 106 -10.8; 116 -10.9; 128 -10.9; 141 -11.0; 155 -10.9; 170 -10.7; 187 -10.5; 206 -10.2; 227 -9.8; 249 -9.4; 274 -9.0; 302 -8.6; 332 -8.2; 365 -7.7; 402 -7.2; 442 -6.8; 486 -6.3; 535 -5.9; 588 -5.4; 647 -4.9; 712 -4.3; 783 -3.8; 861 -3.5; 947 -3.3; 1042 -3.1; 1146 -3.6; 1261 -4.6; 1387 -5.1; 1526 -5.1; 1678 -4.7; 1846 -4.4; 2031 -4.2; 2234 -4.2; 2457 -4.4; 2703 -4.5; 2973 -4.2; 3270 -3.6; 3597 -2.8; 3957 -1.9; 4353 -1.2; 4788 -0.6; 5267 -0.5; 5793 -0.7; 6373 -1.4; 7010 -3.0; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.6; 16529 -5.6; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E4000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E4000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.24 | 2.8 dB  |
| Peaking | 58 Hz   | 0.45 | -1.8 dB |
| Peaking | 154 Hz  | 0.51 | -4.6 dB |
| Peaking | 887 Hz  | 1.32 | 2.7 dB  |
| Peaking | 5011 Hz | 1.58 | 5.4 dB  |
| Peaking | 14 Hz   | 0.86 | 0.4 dB  |
| Peaking | 1468 Hz | 3.17 | -1.5 dB |
| Peaking | 1634 Hz | 1.36 | 1.0 dB  |
| Peaking | 6586 Hz | 3.72 | 2.9 dB  |
| Peaking | 7364 Hz | 1.7  | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E4000/Final%20Audio%20E4000.png)