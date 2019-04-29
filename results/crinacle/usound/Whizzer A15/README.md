# Whizzer A15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.7; 25 -4.0; 28 -4.3; 31 -4.6; 34 -4.8; 37 -5.1; 41 -5.3; 45 -5.6; 49 -5.8; 54 -6.0; 60 -6.4; 66 -6.7; 72 -7.0; 79 -7.4; 87 -7.8; 96 -8.2; 106 -8.6; 116 -8.9; 128 -9.2; 141 -9.5; 155 -9.6; 170 -9.8; 187 -9.8; 206 -9.7; 227 -9.5; 249 -9.3; 274 -9.1; 302 -8.8; 332 -8.4; 365 -8.0; 402 -7.5; 442 -6.9; 486 -6.4; 535 -5.8; 588 -5.0; 647 -4.1; 712 -3.2; 783 -2.6; 861 -2.1; 947 -1.8; 1042 -1.9; 1146 -2.4; 1261 -3.0; 1387 -3.2; 1526 -2.9; 1678 -2.2; 1846 -1.4; 2031 -0.8; 2234 -0.5; 2457 -0.6; 2703 -0.9; 2973 -1.6; 3270 -2.2; 3597 -2.6; 3957 -3.2; 4353 -4.0; 4788 -5.5; 5267 -7.7; 5793 -7.7; 6373 -6.0; 7010 -7.1; 7711 -11.1; 8482 -9.6; 9330 -5.6; 10263 -5.5; 11289 -5.6; 12418 -7.4; 13660 -8.8; 15026 -9.1; 16529 -8.5; 18182 -8.2; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Whizzer A15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Whizzer A15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 196 Hz   | 0.59 | -4.5 dB |
| Peaking | 882 Hz   | 1.44 | 3.9 dB  |
| Peaking | 2408 Hz  | 1.34 | 5.1 dB  |
| Peaking | 7877 Hz  | 5.25 | -6.1 dB |
| Peaking | 16433 Hz | 0.77 | -3.6 dB |
| Peaking | 21 Hz    | 1.12 | 2.3 dB  |
| Peaking | 3920 Hz  | 3.74 | 1.0 dB  |
| Peaking | 5435 Hz  | 5.61 | -3.2 dB |
| Peaking | 10594 Hz | 2.37 | 1.6 dB  |
| Peaking | 13769 Hz | 3.16 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Whizzer%20A15/Whizzer%20A15.png)