# FiiO F9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.5; 25 -4.6; 28 -4.9; 31 -5.1; 34 -5.3; 37 -5.5; 41 -5.8; 45 -6.0; 49 -6.2; 54 -6.5; 60 -6.7; 66 -7.0; 72 -7.3; 79 -7.6; 87 -7.9; 96 -8.2; 106 -8.5; 116 -8.7; 128 -8.8; 141 -8.9; 155 -8.8; 170 -8.8; 187 -8.6; 206 -8.4; 227 -8.1; 249 -7.8; 274 -7.5; 302 -7.1; 332 -6.7; 365 -6.3; 402 -5.9; 442 -5.5; 486 -5.1; 535 -4.7; 588 -4.3; 647 -3.8; 712 -3.4; 783 -3.2; 861 -3.2; 947 -3.4; 1042 -4.0; 1146 -5.0; 1261 -6.2; 1387 -7.2; 1526 -7.9; 1678 -8.3; 1846 -8.5; 2031 -8.4; 2234 -7.2; 2457 -5.0; 2703 -2.6; 2973 -0.9; 3270 -0.5; 3597 -1.3; 3957 -3.1; 4353 -5.1; 4788 -7.1; 5267 -6.0; 5793 -5.7; 6373 -9.6; 7010 -13.1; 7711 -10.2; 8482 -8.8; 9330 -10.9; 10263 -11.2; 11289 -8.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -9.6; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO F9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO F9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 148 Hz  | 0.98 | -2.7 dB |
| Peaking | 748 Hz  | 1.81 | 3.7 dB  |
| Peaking | 3286 Hz | 3.3  | 6.8 dB  |
| Peaking | 6984 Hz | 5.76 | -7.0 dB |
| Peaking | 9869 Hz | 3.59 | -5.2 dB |
| Peaking | 23 Hz   | 1.19 | 2.2 dB  |
| Peaking | 1042 Hz | 3.77 | 1.7 dB  |
| Peaking | 1920 Hz | 1.11 | -4.4 dB |
| Peaking | 2126 Hz | 0.48 | 1.3 dB  |
| Peaking | 2689 Hz | 4.49 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FiiO%20F9/FiiO%20F9.png)