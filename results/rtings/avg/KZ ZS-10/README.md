# KZ ZS-10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.3; 31 -1.5; 34 -1.7; 37 -1.9; 41 -2.0; 45 -2.2; 49 -2.4; 54 -2.6; 60 -3.1; 66 -3.6; 72 -4.0; 79 -4.5; 87 -5.0; 96 -5.6; 106 -6.3; 116 -6.9; 128 -7.4; 141 -7.8; 155 -8.1; 170 -8.2; 187 -8.3; 206 -8.3; 227 -8.1; 249 -7.8; 274 -7.5; 302 -7.0; 332 -6.6; 365 -6.1; 402 -5.6; 442 -5.0; 486 -4.5; 535 -3.8; 588 -3.1; 647 -2.5; 712 -1.9; 783 -1.5; 861 -1.4; 947 -1.6; 1042 -2.8; 1146 -3.8; 1261 -4.5; 1387 -5.1; 1526 -5.8; 1678 -6.7; 1846 -7.8; 2031 -9.0; 2234 -9.4; 2457 -8.9; 2703 -8.1; 2973 -7.9; 3270 -8.9; 3597 -10.1; 3957 -10.4; 4353 -6.9; 4788 -2.3; 5267 -4.3; 5793 -8.8; 6373 -5.7; 7010 -3.3; 7711 -5.6; 8482 -5.8; 9330 -6.3; 10263 -8.0; 11289 -7.5; 12418 -7.1; 13660 -8.1; 15026 -7.7; 16529 -5.9; 18182 -5.8; 20000 -9.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.4  | 5.3 dB  |
| Peaking | 48 Hz    | 2.28 | 3.1 dB  |
| Peaking | 834 Hz   | 1.73 | 5.1 dB  |
| Peaking | 2217 Hz  | 2.37 | -3.9 dB |
| Peaking | 3708 Hz  | 5.61 | -4.9 dB |
| Peaking | 192 Hz   | 0.35 | 3.5 dB  |
| Peaking | 192 Hz   | 0.68 | -6.3 dB |
| Peaking | 4886 Hz  | 8.81 | 6.0 dB  |
| Peaking | 6901 Hz  | 7.62 | 4.8 dB  |
| Peaking | 10718 Hz | 0.31 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/KZ%20ZS-10/KZ%20ZS-10.png)