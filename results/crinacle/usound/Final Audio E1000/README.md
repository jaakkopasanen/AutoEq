# Final Audio E1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.9; 41 -1.4; 45 -1.8; 49 -2.2; 54 -2.8; 60 -3.4; 66 -3.9; 72 -4.5; 79 -5.0; 87 -5.6; 96 -6.2; 106 -6.8; 116 -7.3; 128 -7.8; 141 -8.3; 155 -8.6; 170 -8.9; 187 -9.1; 206 -9.3; 227 -9.4; 249 -9.5; 274 -9.5; 302 -9.5; 332 -9.4; 365 -9.4; 402 -9.2; 442 -9.1; 486 -8.8; 535 -8.5; 588 -8.1; 647 -7.5; 712 -7.0; 783 -6.3; 861 -5.7; 947 -5.3; 1042 -5.3; 1146 -5.7; 1261 -6.4; 1387 -7.0; 1526 -6.9; 1678 -6.4; 1846 -5.8; 2031 -5.5; 2234 -5.3; 2457 -5.4; 2703 -5.4; 2973 -5.0; 3270 -4.4; 3597 -3.8; 3957 -3.3; 4353 -3.2; 4788 -3.9; 5267 -5.7; 5793 -7.4; 6373 -5.6; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.39 | 6.4 dB  |
| Peaking | 233 Hz  | 0.38 | -3.6 dB |
| Peaking | 935 Hz  | 2.11 | 2.4 dB  |
| Peaking | 3946 Hz | 1.67 | 3.3 dB  |
| Peaking | 1145 Hz | 4.79 | 0.6 dB  |
| Peaking | 1403 Hz | 2.78 | -0.9 dB |
| Peaking | 2054 Hz | 3.36 | 0.9 dB  |
| Peaking | 5816 Hz | 6.83 | -2.3 dB |
| Peaking | 6806 Hz | 9.78 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E1000/Final%20Audio%20E1000.png)