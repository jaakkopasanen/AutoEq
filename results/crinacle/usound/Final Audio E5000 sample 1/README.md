# Final Audio E5000 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -9.0; 25 -9.5; 28 -10.0; 31 -10.4; 34 -10.7; 37 -10.9; 41 -11.2; 45 -11.4; 49 -11.5; 54 -11.6; 60 -11.7; 66 -11.9; 72 -12.0; 79 -12.1; 87 -12.2; 96 -12.3; 106 -12.3; 116 -12.3; 128 -12.2; 141 -12.1; 155 -12.0; 170 -11.7; 187 -11.5; 206 -11.1; 227 -10.8; 249 -10.4; 274 -10.0; 302 -9.6; 332 -9.2; 365 -8.8; 402 -8.5; 442 -8.1; 486 -7.7; 535 -7.4; 588 -7.0; 647 -6.6; 712 -6.2; 783 -5.7; 861 -5.3; 947 -5.2; 1042 -5.4; 1146 -6.1; 1261 -6.8; 1387 -7.1; 1526 -7.0; 1678 -6.6; 1846 -6.0; 2031 -5.6; 2234 -5.5; 2457 -5.3; 2703 -5.3; 2973 -5.4; 3270 -4.9; 3597 -3.8; 3957 -2.6; 4353 -1.4; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E5000 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E5000 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.58 | -3.3 dB |
| Peaking | 142 Hz  | 0.49 | -4.9 dB |
| Peaking | 860 Hz  | 2.5  | 1.8 dB  |
| Peaking | 5114 Hz | 1.73 | 6.7 dB  |
| Peaking | 1466 Hz | 2.54 | -1.9 dB |
| Peaking | 1659 Hz | 1.02 | 1.1 dB  |
| Peaking | 6441 Hz | 4.79 | 3.5 dB  |
| Peaking | 7328 Hz | 1.98 | -1.7 dB |
| Peaking | 7625 Hz | 1.11 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E5000%20sample%201/Final%20Audio%20E5000%20sample%201.png)