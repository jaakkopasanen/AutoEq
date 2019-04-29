# Final Audio E2000 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.2; 25 -1.9; 28 -2.7; 31 -3.4; 34 -4.0; 37 -4.5; 41 -5.2; 45 -5.7; 49 -6.2; 54 -6.8; 60 -7.3; 66 -7.9; 72 -8.4; 79 -8.9; 87 -9.4; 96 -9.9; 106 -10.3; 116 -10.7; 128 -11.0; 141 -11.2; 155 -11.3; 170 -11.3; 187 -11.2; 206 -11.1; 227 -10.8; 249 -10.5; 274 -10.0; 302 -9.8; 332 -9.5; 365 -9.1; 402 -8.6; 442 -8.2; 486 -7.6; 535 -7.1; 588 -6.6; 647 -6.0; 712 -5.3; 783 -4.7; 861 -4.3; 947 -4.0; 1042 -3.8; 1146 -3.9; 1261 -4.7; 1387 -5.2; 1526 -5.2; 1678 -4.7; 1846 -3.9; 2031 -3.3; 2234 -3.1; 2457 -3.2; 2703 -3.7; 2973 -3.4; 3270 -2.8; 3597 -2.1; 3957 -1.6; 4353 -0.9; 4788 -1.6; 5267 -3.5; 5793 -6.1; 6373 -6.6; 7010 -4.3; 7711 -5.9; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -7.8; 16529 -6.3; 18182 -6.2; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E2000 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E2000 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.59 | 7.4 dB  |
| Peaking | 162 Hz   | 0.47 | -5.4 dB |
| Peaking | 915 Hz   | 1.49 | 2.9 dB  |
| Peaking | 2297 Hz  | 1.8  | 2.6 dB  |
| Peaking | 4230 Hz  | 2.46 | 5.2 dB  |
| Peaking | 1459 Hz  | 8.8  | -0.6 dB |
| Peaking | 5050 Hz  | 5.25 | 1.5 dB  |
| Peaking | 6166 Hz  | 3.42 | -2.5 dB |
| Peaking | 6959 Hz  | 8.5  | 2.6 dB  |
| Peaking | 15142 Hz | 5.2  | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E2000%20sample%201/Final%20Audio%20E2000%20sample%201.png)