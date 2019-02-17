# KZ ZS-10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.0; 25 -1.2; 28 -1.5; 31 -1.7; 34 -1.9; 37 -2.0; 41 -2.2; 45 -2.4; 49 -2.6; 54 -2.8; 60 -3.3; 66 -3.8; 72 -4.2; 79 -4.7; 87 -5.2; 96 -5.8; 106 -6.4; 116 -7.1; 128 -7.6; 141 -8.0; 155 -8.2; 170 -8.4; 187 -8.5; 206 -8.5; 227 -8.3; 249 -8.0; 274 -7.7; 302 -7.2; 332 -6.8; 365 -6.3; 402 -5.8; 442 -5.2; 486 -4.6; 535 -4.0; 588 -3.3; 647 -2.7; 712 -2.1; 783 -1.7; 861 -1.5; 947 -1.8; 1042 -2.9; 1146 -3.9; 1261 -4.7; 1387 -5.3; 1526 -6.0; 1678 -6.8; 1846 -8.0; 2031 -9.1; 2234 -9.6; 2457 -9.1; 2703 -8.3; 2973 -8.1; 3270 -9.1; 3597 -10.3; 3957 -10.6; 4353 -7.1; 4788 -2.5; 5267 -4.5; 5793 -9.0; 6373 -5.8; 7010 -0.5; 7711 -2.2; 8482 -2.8; 9330 -6.3; 10263 -8.2; 11289 -7.7; 12418 -7.3; 13660 -8.3; 15026 -7.9; 16529 -5.1; 18182 -4.9; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 188 Hz   | 0.74 | -6.5 dB  |
| Peaking | 2118 Hz  | 1.96 | -6.3 dB  |
| Peaking | 3647 Hz  | 2.36 | -6.7 dB  |
| Peaking | 11802 Hz | 1.96 | -3.6 dB  |
| Peaking | 21222 Hz | 0.1  | -4.1 dB  |
| Peaking | 20 Hz    | 1    | 1.8 dB   |
| Peaking | 821 Hz   | 3.11 | 2.4 dB   |
| Peaking | 5986 Hz  | 5.52 | -12.4 dB |
| Peaking | 6342 Hz  | 1.26 | 11.7 dB  |
| Peaking | 7378 Hz  | 0.49 | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | -5.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -6.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/KZ%20ZS-10/KZ%20ZS-10.png)