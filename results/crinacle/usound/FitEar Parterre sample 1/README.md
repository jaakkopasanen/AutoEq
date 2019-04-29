# FitEar Parterre sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.4; 25 -11.3; 28 -11.2; 31 -11.2; 34 -11.3; 37 -11.4; 41 -11.5; 45 -11.5; 49 -11.6; 54 -11.8; 60 -12.0; 66 -12.2; 72 -12.4; 79 -12.7; 87 -12.9; 96 -13.2; 106 -13.4; 116 -13.6; 128 -13.8; 141 -13.9; 155 -14.0; 170 -13.9; 187 -13.8; 206 -13.5; 227 -13.3; 249 -12.9; 274 -12.6; 302 -12.1; 332 -11.7; 365 -11.2; 402 -10.6; 442 -10.0; 486 -9.4; 535 -8.7; 588 -7.9; 647 -7.1; 712 -6.2; 783 -5.3; 861 -4.4; 947 -3.7; 1042 -3.4; 1146 -3.5; 1261 -3.5; 1387 -3.2; 1526 -2.5; 1678 -1.6; 1846 -1.0; 2031 -0.7; 2234 -0.7; 2457 -0.8; 2703 -0.8; 2973 -0.8; 3270 -0.7; 3597 -0.8; 3957 -1.0; 4353 -1.5; 4788 -1.0; 5267 -0.5; 5793 -0.7; 6373 -2.3; 7010 -7.8; 7711 -9.6; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Parterre sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Parterre sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.31 | -4.4 dB |
| Peaking | 176 Hz   | 0.36 | -7.4 dB |
| Peaking | 2240 Hz  | 0.39 | 5.9 dB  |
| Peaking | 6157 Hz  | 2.08 | 5.9 dB  |
| Peaking | 7292 Hz  | 2.79 | -8.6 dB |
| Peaking | 923 Hz   | 3.44 | 1.0 dB  |
| Peaking | 1353 Hz  | 3.83 | -1.3 dB |
| Peaking | 4743 Hz  | 0.35 | 0.2 dB  |
| Peaking | 11761 Hz | 1.33 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20Parterre%20sample%201/FitEar%20Parterre%20sample%201.png)