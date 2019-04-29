# Clear Tune CT-6E sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.8; 25 -1.9; 28 -2.1; 31 -2.3; 34 -2.5; 37 -2.6; 41 -2.8; 45 -3.1; 49 -3.3; 54 -3.5; 60 -3.7; 66 -4.1; 72 -4.5; 79 -4.9; 87 -5.3; 96 -5.7; 106 -6.1; 116 -6.5; 128 -6.8; 141 -7.4; 155 -7.6; 170 -7.8; 187 -7.9; 206 -8.0; 227 -8.1; 249 -8.1; 274 -8.1; 302 -8.0; 332 -8.0; 365 -7.8; 402 -7.7; 442 -7.6; 486 -7.5; 535 -7.3; 588 -7.1; 647 -6.9; 712 -6.6; 783 -6.3; 861 -6.1; 947 -6.1; 1042 -6.6; 1146 -7.5; 1261 -8.5; 1387 -9.4; 1526 -10.0; 1678 -10.8; 1846 -11.3; 2031 -10.5; 2234 -9.0; 2457 -7.2; 2703 -6.0; 2973 -6.1; 3270 -6.5; 3597 -6.5; 3957 -6.8; 4353 -6.0; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-6E sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-6E sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.6  | 4.6 dB  |
| Peaking | 56 Hz   | 0.89 | 1.8 dB  |
| Peaking | 222 Hz  | 0.76 | -2.0 dB |
| Peaking | 1776 Hz | 2.38 | -5.1 dB |
| Peaking | 5645 Hz | 2.86 | 7.0 dB  |
| Peaking | 907 Hz  | 1.82 | 2.9 dB  |
| Peaking | 1024 Hz | 0.94 | -1.9 dB |
| Peaking | 3992 Hz | 1    | 1.7 dB  |
| Peaking | 4005 Hz | 3.74 | -3.2 dB |
| Peaking | 8239 Hz | 2.8  | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Clear%20Tune%20CT-6E%20sample%202/Clear%20Tune%20CT-6E%20sample%202.png)