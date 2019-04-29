# KZ ZS6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.2; 25 -8.5; 28 -8.8; 31 -9.0; 34 -9.2; 37 -9.3; 41 -9.5; 45 -9.7; 49 -9.8; 54 -9.9; 60 -10.0; 66 -10.2; 72 -10.4; 79 -10.5; 87 -10.7; 96 -10.9; 106 -11.0; 116 -11.2; 128 -11.2; 141 -11.2; 155 -11.1; 170 -11.0; 187 -10.7; 206 -10.5; 227 -10.2; 249 -9.8; 274 -9.4; 302 -9.0; 332 -8.6; 365 -8.1; 402 -7.7; 442 -7.3; 486 -6.8; 535 -6.4; 588 -6.0; 647 -5.5; 712 -5.1; 783 -4.7; 861 -4.4; 947 -4.3; 1042 -4.6; 1146 -5.3; 1261 -6.0; 1387 -6.4; 1526 -6.2; 1678 -5.7; 1846 -5.2; 2031 -5.7; 2234 -6.9; 2457 -7.9; 2703 -8.0; 2973 -7.6; 3270 -7.7; 3597 -7.5; 3957 -2.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.1; 7711 -11.0; 8482 -11.9; 9330 -8.8; 10263 -8.9; 11289 -11.3; 12418 -13.7; 13660 -16.1; 15026 -16.0; 16529 -11.7; 18182 -9.0; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 65 Hz    | 0.48 | -3.4 dB  |
| Peaking | 175 Hz   | 1.03 | -3.2 dB  |
| Peaking | 5633 Hz  | 1.77 | 8.1 dB   |
| Peaking | 8080 Hz  | 5.47 | -7.2 dB  |
| Peaking | 14314 Hz | 1.09 | -10.4 dB |
| Peaking | 873 Hz   | 1.93 | 2.6 dB   |
| Peaking | 1861 Hz  | 5.69 | 1.6 dB   |
| Peaking | 3429 Hz  | 1.6  | -3.9 dB  |
| Peaking | 4257 Hz  | 4.64 | 5.7 dB   |
| Peaking | 16788 Hz | 5.41 | 0.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -11.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/KZ%20ZS6/KZ%20ZS6.png)