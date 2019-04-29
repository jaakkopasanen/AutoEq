# FitEar Private 333
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.1; 31 -1.3; 34 -1.4; 37 -1.6; 41 -1.8; 45 -1.9; 49 -2.1; 54 -2.3; 60 -2.6; 66 -2.9; 72 -3.3; 79 -3.7; 87 -4.0; 96 -4.5; 106 -4.9; 116 -5.3; 128 -5.6; 141 -5.9; 155 -6.1; 170 -6.3; 187 -6.4; 206 -6.4; 227 -6.4; 249 -6.3; 274 -6.2; 302 -6.0; 332 -5.8; 365 -5.6; 402 -5.4; 442 -5.1; 486 -4.8; 535 -4.5; 588 -4.1; 647 -3.7; 712 -3.2; 783 -2.7; 861 -2.3; 947 -2.2; 1042 -2.4; 1146 -2.9; 1261 -3.5; 1387 -3.9; 1526 -3.8; 1678 -3.5; 1846 -3.2; 2031 -3.3; 2234 -3.8; 2457 -4.0; 2703 -3.2; 2973 -2.2; 3270 -1.9; 3597 -2.1; 3957 -2.2; 4353 -3.1; 4788 -5.5; 5267 -7.6; 5793 -8.7; 6373 -10.2; 7010 -6.4; 7711 -4.2; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Private 333 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Private 333 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.39 | 4.0 dB  |
| Peaking | 48 Hz   | 2.28 | 2.1 dB  |
| Peaking | 939 Hz  | 2.45 | 2.5 dB  |
| Peaking | 3536 Hz | 1.62 | 3.1 dB  |
| Peaking | 5985 Hz | 3.21 | -6.2 dB |
| Peaking | 73 Hz   | 1.85 | 1.1 dB  |
| Peaking | 210 Hz  | 0.66 | -2.1 dB |
| Peaking | 676 Hz  | 1.92 | 0.8 dB  |
| Peaking | 6620 Hz | 9.97 | -2.6 dB |
| Peaking | 7384 Hz | 4.17 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20Private%20333/FitEar%20Private%20333.png)