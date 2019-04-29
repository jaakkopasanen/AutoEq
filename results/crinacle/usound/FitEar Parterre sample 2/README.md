# FitEar Parterre sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.8; 25 -8.0; 28 -8.1; 31 -8.2; 34 -8.4; 37 -8.5; 41 -8.6; 45 -8.8; 49 -8.9; 54 -9.1; 60 -9.3; 66 -9.6; 72 -9.9; 79 -10.2; 87 -10.6; 96 -10.9; 106 -11.2; 116 -11.5; 128 -11.6; 141 -11.9; 155 -12.0; 170 -12.0; 187 -11.9; 206 -11.8; 227 -11.7; 249 -11.4; 274 -11.1; 302 -10.8; 332 -10.4; 365 -10.0; 402 -9.6; 442 -9.2; 486 -8.7; 535 -8.2; 588 -7.6; 647 -7.0; 712 -6.3; 783 -5.5; 861 -4.8; 947 -4.3; 1042 -4.1; 1146 -4.3; 1261 -4.5; 1387 -4.4; 1526 -3.9; 1678 -3.2; 1846 -2.8; 2031 -2.7; 2234 -2.6; 2457 -2.0; 2703 -1.3; 2973 -0.8; 3270 -0.5; 3597 -0.6; 3957 -1.1; 4353 -2.0; 4788 -1.5; 5267 -1.1; 5793 -1.4; 6373 -2.2; 7010 -5.2; 7711 -9.5; 8482 -7.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Parterre sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Parterre sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 65 Hz   | 0.07 | -1.2 dB |
| Peaking | 195 Hz  | 0.39 | -4.8 dB |
| Peaking | 1102 Hz | 0.58 | 3.0 dB  |
| Peaking | 3279 Hz | 1.46 | 5.1 dB  |
| Peaking | 5522 Hz | 3.87 | 4.0 dB  |
| Peaking | 993 Hz  | 2.9  | 1.1 dB  |
| Peaking | 1321 Hz | 1.63 | -1.2 dB |
| Peaking | 1780 Hz | 2.82 | 1.1 dB  |
| Peaking | 6620 Hz | 5.43 | 2.4 dB  |
| Peaking | 7821 Hz | 5.3  | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20Parterre%20sample%202/FitEar%20Parterre%20sample%202.png)