# KZ ES4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.1; 25 -11.2; 28 -11.4; 31 -11.4; 34 -11.4; 37 -11.4; 41 -11.5; 45 -11.5; 49 -11.4; 54 -11.4; 60 -11.4; 66 -11.4; 72 -11.5; 79 -11.6; 87 -11.6; 96 -11.6; 106 -11.6; 116 -11.6; 128 -11.5; 141 -11.4; 155 -11.2; 170 -10.9; 187 -10.5; 206 -10.1; 227 -9.7; 249 -9.3; 274 -8.7; 302 -8.3; 332 -7.9; 365 -7.4; 402 -6.9; 442 -6.5; 486 -6.0; 535 -5.6; 588 -5.2; 647 -4.8; 712 -4.4; 783 -4.1; 861 -3.8; 947 -3.7; 1042 -4.2; 1146 -5.1; 1261 -6.1; 1387 -7.0; 1526 -7.6; 1678 -8.2; 1846 -9.0; 2031 -10.2; 2234 -11.2; 2457 -11.1; 2703 -9.9; 2973 -8.7; 3270 -8.6; 3597 -9.8; 3957 -8.9; 4353 -2.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -7.9; 15026 -6.5; 16529 -6.5; 18182 -9.1; 20000 -15.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ES4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ES4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 64 Hz   | 0.2  | -5.3 dB  |
| Peaking | 870 Hz  | 0.72 | 4.9 dB   |
| Peaking | 2232 Hz | 5.1  | -1.8 dB  |
| Peaking | 4079 Hz | 0.47 | -11.2 dB |
| Peaking | 5275 Hz | 1.16 | 17.1 dB  |
| Peaking | 3092 Hz | 5.31 | 1.9 dB   |
| Peaking | 3809 Hz | 5.34 | -2.2 dB  |
| Peaking | 4301 Hz | 2.78 | -1.3 dB  |
| Peaking | 4457 Hz | 8.47 | 4.2 dB   |
| Peaking | 7755 Hz | 9.88 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20ES4/KZ%20ES4.png)