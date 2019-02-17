# KZ ZS6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.7; 23 -12.2; 25 -12.5; 28 -12.5; 31 -12.7; 34 -12.8; 37 -12.9; 41 -13.0; 45 -13.0; 49 -13.2; 54 -13.4; 60 -13.6; 66 -13.9; 72 -13.8; 79 -14.2; 87 -14.0; 96 -13.7; 106 -14.0; 116 -13.6; 128 -13.8; 141 -13.4; 155 -13.2; 170 -13.0; 187 -12.8; 206 -12.6; 227 -12.3; 249 -11.9; 274 -11.5; 302 -11.1; 332 -10.7; 365 -10.2; 402 -9.8; 442 -9.4; 486 -8.9; 535 -8.5; 588 -8.1; 647 -7.6; 712 -7.2; 783 -6.8; 861 -6.5; 947 -6.4; 1042 -6.7; 1146 -7.4; 1261 -8.1; 1387 -8.5; 1526 -8.3; 1678 -7.8; 1846 -7.3; 2031 -7.8; 2234 -8.9; 2457 -10.0; 2703 -10.1; 2973 -9.7; 3270 -9.8; 3597 -9.6; 3957 -4.8; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -5.3; 7711 -13.1; 8482 -14.0; 9330 -11.0; 10263 -11.0; 11289 -13.4; 12418 -15.8; 13660 -18.2; 15026 -18.0; 16529 -13.9; 18182 -11.1; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.54 | -3.5 dB  |
| Peaking | 113 Hz   | 0.33 | -6.9 dB  |
| Peaking | 5732 Hz  | 2.26 | 9.7 dB   |
| Peaking | 8028 Hz  | 6    | -7.2 dB  |
| Peaking | 14465 Hz | 0.67 | -11.4 dB |
| Peaking | 879 Hz   | 1.9  | 1.4 dB   |
| Peaking | 1360 Hz  | 3.71 | -1.5 dB  |
| Peaking | 3281 Hz  | 1.51 | -5.2 dB  |
| Peaking | 4337 Hz  | 4.42 | 7.1 dB   |
| Peaking | 17066 Hz | 4.44 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -5.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 16000 Hz | 1.41 | -14.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ZS6/KZ%20ZS6.png)