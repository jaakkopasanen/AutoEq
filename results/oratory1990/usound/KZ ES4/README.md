# KZ ES4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -13.1; 25 -13.3; 28 -13.1; 31 -13.1; 34 -13.0; 37 -12.9; 41 -12.9; 45 -12.8; 49 -12.7; 54 -12.8; 60 -12.9; 66 -13.1; 72 -12.9; 79 -13.1; 87 -12.8; 96 -12.4; 106 -12.5; 116 -12.0; 128 -12.0; 141 -11.5; 155 -11.2; 170 -10.9; 187 -10.5; 206 -10.2; 227 -9.7; 249 -9.2; 274 -8.8; 302 -8.3; 332 -7.8; 365 -7.3; 402 -6.9; 442 -6.4; 486 -6.0; 535 -5.6; 588 -5.2; 647 -4.8; 712 -4.4; 783 -4.0; 861 -3.8; 947 -3.7; 1042 -4.2; 1146 -5.1; 1261 -6.1; 1387 -7.0; 1526 -7.6; 1678 -8.2; 1846 -9.0; 2031 -10.2; 2234 -11.2; 2457 -11.1; 2703 -9.8; 2973 -8.7; 3270 -8.7; 3597 -9.7; 3957 -8.7; 4353 -2.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.9; 13660 -7.4; 15026 -6.5; 16529 -6.5; 18182 -10.5; 20000 -14.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ES4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ES4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.19 | -6.7 dB  |
| Peaking | 877 Hz   | 0.8  | 4.7 dB   |
| Peaking | 2236 Hz  | 5.18 | -1.8 dB  |
| Peaking | 4036 Hz  | 0.48 | -10.8 dB |
| Peaking | 5289 Hz  | 1.19 | 16.7 dB  |
| Peaking | 3117 Hz  | 3.76 | 2.6 dB   |
| Peaking | 3855 Hz  | 2.95 | -3.3 dB  |
| Peaking | 4488 Hz  | 8.47 | 4.3 dB   |
| Peaking | 7843 Hz  | 8.72 | -1.1 dB  |
| Peaking | 11058 Hz | 4.35 | 0.6 dB   |

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
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ES4/KZ%20ES4.png)