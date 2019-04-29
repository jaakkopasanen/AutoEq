# Final Audio E2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.3; 25 -1.9; 28 -2.8; 31 -3.6; 34 -4.2; 37 -4.7; 41 -5.3; 45 -5.9; 49 -6.4; 54 -6.9; 60 -7.5; 66 -8.1; 72 -8.6; 79 -9.1; 87 -9.6; 96 -10.2; 106 -10.6; 116 -11.0; 128 -11.2; 141 -11.5; 155 -11.6; 170 -11.6; 187 -11.6; 206 -11.4; 227 -11.1; 249 -10.9; 274 -10.5; 302 -10.2; 332 -9.8; 365 -9.3; 402 -8.9; 442 -8.5; 486 -8.0; 535 -7.5; 588 -7.0; 647 -6.4; 712 -5.7; 783 -5.1; 861 -4.5; 947 -4.2; 1042 -4.2; 1146 -4.6; 1261 -5.4; 1387 -6.0; 1526 -6.0; 1678 -5.6; 1846 -5.0; 2031 -4.7; 2234 -4.7; 2457 -4.8; 2703 -5.1; 2973 -4.6; 3270 -3.6; 3597 -2.6; 3957 -2.0; 4353 -1.4; 4788 -1.8; 5267 -3.1; 5793 -5.5; 6373 -7.2; 7010 -5.5; 7711 -6.5; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -7.9; 16529 -8.2; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio E2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio E2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.57 | 8.4 dB  |
| Peaking | 162 Hz   | 0.5  | -5.2 dB |
| Peaking | 918 Hz   | 1.59 | 3.1 dB  |
| Peaking | 2155 Hz  | 2.46 | 1.5 dB  |
| Peaking | 4246 Hz  | 2.14 | 5.6 dB  |
| Peaking | 1440 Hz  | 8.58 | -0.5 dB |
| Peaking | 5239 Hz  | 5.58 | 1.5 dB  |
| Peaking | 6376 Hz  | 3.53 | -2.2 dB |
| Peaking | 7023 Hz  | 9.24 | 1.8 dB  |
| Peaking | 15840 Hz | 3.56 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Final%20Audio%20E2000/Final%20Audio%20E2000.png)