# Final Audio E4000 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.9; 25 -4.4; 28 -5.1; 31 -5.7; 34 -6.1; 37 -6.5; 41 -7.0; 45 -7.4; 49 -7.7; 54 -8.0; 60 -8.4; 66 -8.8; 72 -9.1; 79 -9.4; 87 -9.7; 96 -9.9; 106 -10.2; 116 -10.3; 128 -10.4; 141 -10.4; 155 -10.4; 170 -10.2; 187 -10.0; 206 -9.7; 227 -9.3; 249 -8.9; 274 -8.5; 302 -8.0; 332 -7.6; 365 -7.2; 402 -6.7; 442 -6.2; 486 -5.7; 535 -5.3; 588 -4.7; 647 -4.2; 712 -3.5; 783 -2.9; 861 -2.7; 947 -2.6; 1042 -2.3; 1146 -2.7; 1261 -3.6; 1387 -4.2; 1526 -4.3; 1678 -4.1; 1846 -3.8; 2031 -3.7; 2234 -3.9; 2457 -4.1; 2703 -4.2; 2973 -4.0; 3270 -3.3; 3597 -2.5; 3957 -1.6; 4353 -1.0; 4788 -0.5; 5267 -0.9; 5793 -1.7; 6373 -2.7; 7010 -3.3; 7711 -4.9; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E4000 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E4000 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.19 | 3.1 dB  |
| Peaking | 66 Hz   | 0.44 | -1.5 dB |
| Peaking | 155 Hz  | 0.5  | -4.5 dB |
| Peaking | 900 Hz  | 1.12 | 3.1 dB  |
| Peaking | 4773 Hz | 1.7  | 4.8 dB  |
| Peaking | 1415 Hz | 6.36 | -0.7 dB |
| Peaking | 2000 Hz | 4.44 | 0.6 dB  |
| Peaking | 6772 Hz | 2.68 | 1.3 dB  |
| Peaking | 7673 Hz | 1.65 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E4000%20sample%201/Final%20Audio%20E4000%20sample%201.png)