# KZ ES4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.1; 23 -15.6; 25 -15.8; 28 -15.7; 31 -15.6; 34 -15.6; 37 -15.5; 41 -15.5; 45 -15.3; 49 -15.3; 54 -15.4; 60 -15.4; 66 -15.6; 72 -15.4; 79 -15.7; 87 -15.4; 96 -15.0; 106 -15.0; 116 -14.6; 128 -14.6; 141 -14.1; 155 -13.7; 170 -13.4; 187 -13.1; 206 -12.7; 227 -12.3; 249 -11.8; 274 -11.3; 302 -10.8; 332 -10.4; 365 -9.9; 402 -9.4; 442 -9.0; 486 -8.5; 535 -8.1; 588 -7.7; 647 -7.3; 712 -7.0; 783 -6.5; 861 -6.3; 947 -6.3; 1042 -6.8; 1146 -7.6; 1261 -8.6; 1387 -9.5; 1526 -10.2; 1678 -10.8; 1846 -11.6; 2031 -12.7; 2234 -13.8; 2457 -13.7; 2703 -12.4; 2973 -11.2; 3270 -11.2; 3597 -12.3; 3957 -11.2; 4353 -5.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.7; 8482 -8.0; 9330 -6.5; 10263 -6.5; 11289 -7.3; 12418 -9.4; 13660 -10.0; 15026 -7.2; 16529 -7.2; 18182 -13.0; 20000 -16.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ES4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ES4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 48 Hz    | 0.19 | -9.4 dB  |
| Peaking | 2288 Hz  | 1.65 | -7.6 dB  |
| Peaking | 3790 Hz  | 3.63 | -7.6 dB  |
| Peaking | 5115 Hz  | 2.03 | 9.2 dB   |
| Peaking | 19882 Hz | 0.7  | -10.6 dB |
| Peaking | 851 Hz   | 2.84 | 1.8 dB   |
| Peaking | 6485 Hz  | 7.54 | 2.4 dB   |
| Peaking | 8190 Hz  | 6.02 | -2.7 dB  |
| Peaking | 13119 Hz | 3.33 | -3.4 dB  |
| Peaking | 15902 Hz | 2.77 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.2 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ES4/KZ%20ES4.png)