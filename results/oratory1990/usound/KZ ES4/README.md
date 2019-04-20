# KZ ES4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.9; 25 -13.0; 28 -13.1; 31 -13.1; 34 -13.0; 37 -13.0; 41 -12.9; 45 -12.8; 49 -12.8; 54 -12.8; 60 -12.9; 66 -13.0; 72 -12.9; 79 -13.1; 87 -12.8; 96 -12.4; 106 -12.4; 116 -12.1; 128 -12.0; 141 -11.6; 155 -11.2; 170 -10.9; 187 -10.5; 206 -10.2; 227 -9.7; 249 -9.3; 274 -8.8; 302 -8.3; 332 -7.8; 365 -7.3; 402 -6.9; 442 -6.4; 486 -6.0; 535 -5.6; 588 -5.2; 647 -4.8; 712 -4.4; 783 -4.0; 861 -3.8; 947 -3.7; 1042 -4.2; 1146 -5.1; 1261 -6.1; 1387 -7.0; 1526 -7.6; 1678 -8.2; 1846 -9.0; 2031 -10.2; 2234 -11.2; 2457 -11.1; 2703 -9.8; 2973 -8.7; 3270 -8.7; 3597 -9.7; 3957 -8.7; 4353 -2.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.9; 13660 -7.4; 15026 -6.5; 16529 -6.5; 18182 -10.5; 20000 -14.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ES4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ES4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.19 | -6.7 dB |
| Peaking | 880 Hz   | 0.8  | 4.7 dB  |
| Peaking | 2231 Hz  | 4.95 | -1.8 dB |
| Peaking | 3996 Hz  | 0.48 | -9.9 dB |
| Peaking | 5270 Hz  | 1.24 | 15.8 dB |
| Peaking | 3033 Hz  | 6.19 | 1.5 dB  |
| Peaking | 3771 Hz  | 9.72 | -2.8 dB |
| Peaking | 6535 Hz  | 7.97 | 1.9 dB  |
| Peaking | 7582 Hz  | 4.26 | -1.2 dB |
| Peaking | 10857 Hz | 3.94 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ES4/KZ%20ES4.png)