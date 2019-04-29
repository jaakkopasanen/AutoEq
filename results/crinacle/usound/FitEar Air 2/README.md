# FitEar Air 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.7; 23 -2.2; 25 -2.6; 28 -3.2; 31 -3.7; 34 -4.1; 37 -4.5; 41 -4.9; 45 -5.2; 49 -5.5; 54 -5.8; 60 -6.2; 66 -6.6; 72 -7.0; 79 -7.4; 87 -7.7; 96 -8.1; 106 -8.4; 116 -8.6; 128 -8.8; 141 -8.9; 155 -8.9; 170 -8.8; 187 -8.7; 206 -8.5; 227 -8.2; 249 -7.9; 274 -7.5; 302 -7.1; 332 -6.7; 365 -6.2; 402 -5.8; 442 -5.4; 486 -4.9; 535 -4.5; 588 -4.0; 647 -3.6; 712 -3.1; 783 -2.7; 861 -2.4; 947 -2.4; 1042 -2.9; 1146 -3.5; 1261 -4.4; 1387 -5.4; 1526 -6.2; 1678 -7.2; 1846 -8.4; 2031 -8.5; 2234 -6.9; 2457 -4.7; 2703 -2.9; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -1.6; 4788 -1.5; 5267 -2.2; 5793 -4.4; 6373 -8.7; 7010 -8.7; 7711 -5.1; 8482 -5.1; 9330 -5.2; 10263 -5.2; 11289 -8.4; 12418 -11.2; 13660 -12.7; 15026 -9.6; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Air 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Air 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.4  | 3.6 dB  |
| Peaking | 141 Hz   | 0.84 | -4.1 dB |
| Peaking | 1993 Hz  | 3.64 | -5.2 dB |
| Peaking | 3463 Hz  | 1.48 | 5.2 dB  |
| Peaking | 13441 Hz | 2.11 | -8.2 dB |
| Peaking | 844 Hz   | 1.97 | 3.1 dB  |
| Peaking | 5139 Hz  | 4.71 | 2.2 dB  |
| Peaking | 6618 Hz  | 5.53 | -5.9 dB |
| Peaking | 9339 Hz  | 2.7  | 1.3 dB  |
| Peaking | 16435 Hz | 4.74 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20Air%202/FitEar%20Air%202.png)