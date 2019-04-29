# Final Audio E3000 sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.8; 25 -3.5; 28 -4.3; 31 -5.1; 34 -5.7; 37 -6.3; 41 -6.8; 45 -7.3; 49 -7.8; 54 -8.3; 60 -8.9; 66 -9.4; 72 -9.9; 79 -10.3; 87 -10.8; 96 -11.2; 106 -11.6; 116 -11.8; 128 -11.9; 141 -12.1; 155 -12.1; 170 -12.0; 187 -11.9; 206 -11.6; 227 -11.2; 249 -10.8; 274 -10.2; 302 -10.2; 332 -9.7; 365 -9.2; 402 -8.7; 442 -8.2; 486 -7.6; 535 -7.1; 588 -6.5; 647 -5.9; 712 -5.2; 783 -4.4; 861 -4.1; 947 -3.8; 1042 -3.7; 1146 -4.4; 1261 -5.1; 1387 -5.2; 1526 -5.0; 1678 -4.3; 1846 -3.7; 2031 -3.5; 2234 -3.5; 2457 -3.6; 2703 -3.7; 2973 -3.5; 3270 -2.9; 3597 -2.4; 3957 -1.9; 4353 -1.2; 4788 -0.8; 5267 -0.5; 5793 -0.7; 6373 -1.6; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.6; 16529 -6.7; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E3000 sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E3000 sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.17 | 4.8 dB  |
| Peaking | 100 Hz   | 0.67 | -2.0 dB |
| Peaking | 212 Hz   | 0.39 | -5.6 dB |
| Peaking | 870 Hz   | 0.39 | 3.0 dB  |
| Peaking | 5032 Hz  | 1.55 | 5.4 dB  |
| Peaking | 978 Hz   | 2.6  | 1.6 dB  |
| Peaking | 1369 Hz  | 1.6  | -2.4 dB |
| Peaking | 1927 Hz  | 1.18 | 1.3 dB  |
| Peaking | 8391 Hz  | 3.88 | -1.5 dB |
| Peaking | 15458 Hz | 2.41 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E3000%20sample%203/Final%20Audio%20E3000%20sample%203.png)