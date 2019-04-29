# FitEar EST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.5; 31 -1.7; 34 -2.0; 37 -2.1; 41 -2.4; 45 -2.6; 49 -2.9; 54 -3.2; 60 -3.5; 66 -3.8; 72 -4.1; 79 -4.5; 87 -4.9; 96 -5.3; 106 -5.7; 116 -6.0; 128 -6.3; 141 -6.6; 155 -6.8; 170 -7.0; 187 -7.0; 206 -7.1; 227 -7.1; 249 -7.0; 274 -6.9; 302 -6.7; 332 -6.5; 365 -6.4; 402 -6.1; 442 -5.9; 486 -5.7; 535 -5.3; 588 -5.0; 647 -4.6; 712 -4.1; 783 -3.6; 861 -3.2; 947 -3.0; 1042 -3.2; 1146 -3.7; 1261 -4.2; 1387 -4.4; 1526 -4.0; 1678 -3.3; 1846 -2.5; 2031 -1.8; 2234 -1.3; 2457 -1.0; 2703 -1.0; 2973 -1.1; 3270 -1.4; 3597 -1.7; 3957 -2.2; 4353 -3.2; 4788 -4.6; 5267 -5.3; 5793 -4.0; 6373 -3.9; 7010 -5.0; 7711 -5.0; 8482 -4.3; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -4.3; 16529 -4.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar EST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar EST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.26 | 3.8 dB  |
| Peaking | 199 Hz  | 0.5  | -3.0 dB |
| Peaking | 876 Hz  | 2.6  | 1.7 dB  |
| Peaking | 2676 Hz | 1.57 | 3.8 dB  |
| Peaking | 1464 Hz | 2.87 | -1.5 dB |
| Peaking | 1732 Hz | 1.24 | 1.0 dB  |
| Peaking | 2681 Hz | 3.38 | -0.9 dB |
| Peaking | 3861 Hz | 3.01 | 1.0 dB  |
| Peaking | 5020 Hz | 4.44 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20EST/FitEar%20EST.png)