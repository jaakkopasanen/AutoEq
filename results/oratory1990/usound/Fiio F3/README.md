# Fiio F3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.4; 25 -8.7; 28 -8.9; 31 -9.1; 34 -9.3; 37 -9.4; 41 -9.5; 45 -9.6; 49 -9.8; 54 -10.1; 60 -10.4; 66 -10.7; 72 -10.9; 79 -11.2; 87 -11.2; 96 -11.0; 106 -11.3; 116 -11.1; 128 -11.3; 141 -11.0; 155 -10.9; 170 -10.7; 187 -10.6; 206 -10.4; 227 -10.1; 249 -9.7; 274 -9.3; 302 -8.9; 332 -8.5; 365 -8.1; 402 -7.7; 442 -7.3; 486 -6.9; 535 -6.6; 588 -6.2; 647 -5.9; 712 -5.5; 783 -5.2; 861 -5.0; 947 -5.1; 1042 -5.4; 1146 -5.9; 1261 -6.7; 1387 -7.1; 1526 -7.0; 1678 -6.4; 1846 -5.5; 2031 -4.5; 2234 -3.4; 2457 -2.3; 2703 -1.6; 2973 -1.2; 3270 -1.3; 3597 -1.5; 3957 -1.3; 4353 -0.8; 4788 -0.5; 5267 -1.1; 5793 -3.3; 6373 -6.9; 7010 -9.1; 7711 -11.6; 8482 -10.9; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -7.7; 16529 -6.5; 18182 -6.8; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio F3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio F3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 74 Hz    | 0.48 | -4.2 dB |
| Peaking | 192 Hz   | 1.08 | -2.3 dB |
| Peaking | 2894 Hz  | 1.81 | 4.5 dB  |
| Peaking | 4858 Hz  | 1.92 | 5.9 dB  |
| Peaking | 7696 Hz  | 3.11 | -6.8 dB |
| Peaking | 28 Hz    | 1.63 | -0.5 dB |
| Peaking | 861 Hz   | 1.77 | 1.7 dB  |
| Peaking | 1446 Hz  | 3.23 | -1.7 dB |
| Peaking | 9719 Hz  | 5.48 | 1.4 dB  |
| Peaking | 19860 Hz | 0.13 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Fiio%20F3/Fiio%20F3.png)