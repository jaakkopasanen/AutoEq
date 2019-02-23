# KZ ZS6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -10.1; 25 -10.4; 28 -10.4; 31 -10.6; 34 -10.7; 37 -10.8; 41 -10.9; 45 -10.9; 49 -11.0; 54 -11.3; 60 -11.4; 66 -11.8; 72 -11.7; 79 -12.0; 87 -11.8; 96 -11.6; 106 -11.8; 116 -11.5; 128 -11.7; 141 -11.2; 155 -11.1; 170 -10.9; 187 -10.7; 206 -10.4; 227 -10.1; 249 -9.8; 274 -9.4; 302 -8.9; 332 -8.5; 365 -8.1; 402 -7.6; 442 -7.3; 486 -6.8; 535 -6.3; 588 -5.9; 647 -5.5; 712 -5.0; 783 -4.7; 861 -4.3; 947 -4.3; 1042 -4.6; 1146 -5.3; 1261 -5.9; 1387 -6.4; 1526 -6.2; 1678 -5.6; 1846 -5.2; 2031 -5.6; 2234 -6.8; 2457 -7.9; 2703 -7.9; 2973 -7.5; 3270 -7.7; 3597 -7.5; 3957 -2.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -10.9; 8482 -11.9; 9330 -8.9; 10263 -8.9; 11289 -11.3; 12418 -13.7; 13660 -16.1; 15026 -15.9; 16529 -11.8; 18182 -9.0; 20000 -12.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 56 Hz    | 0.41 | -4.9 dB  |
| Peaking | 173 Hz   | 1.02 | -2.6 dB  |
| Peaking | 5632 Hz  | 1.75 | 8.1 dB   |
| Peaking | 8066 Hz  | 5.44 | -7.2 dB  |
| Peaking | 14321 Hz | 1.1  | -10.3 dB |
| Peaking | 871 Hz   | 1.86 | 2.6 dB   |
| Peaking | 1873 Hz  | 5.75 | 1.7 dB   |
| Peaking | 3429 Hz  | 1.62 | -3.8 dB  |
| Peaking | 4235 Hz  | 4.7  | 5.6 dB   |
| Peaking | 19829 Hz | 2.53 | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -11.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ZS6/KZ%20ZS6.png)