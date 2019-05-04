# KZ AS-10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.0; 25 -8.1; 28 -8.2; 31 -8.3; 34 -8.4; 37 -8.5; 41 -8.6; 45 -8.7; 49 -8.8; 54 -8.9; 60 -9.1; 66 -9.3; 72 -9.4; 79 -9.6; 87 -9.8; 96 -9.9; 106 -10.0; 116 -10.0; 128 -10.0; 141 -9.8; 155 -9.5; 170 -9.2; 187 -8.8; 206 -8.5; 227 -8.1; 249 -7.7; 274 -7.2; 302 -6.6; 332 -6.0; 365 -5.4; 402 -4.8; 442 -4.3; 486 -3.7; 535 -3.0; 588 -2.4; 647 -1.7; 712 -1.1; 783 -0.7; 861 -0.5; 947 -0.8; 1042 -1.6; 1146 -2.5; 1261 -3.4; 1387 -4.1; 1526 -4.8; 1678 -5.6; 1846 -6.7; 2031 -8.1; 2234 -9.3; 2457 -9.5; 2703 -8.0; 2973 -5.8; 3270 -5.0; 3597 -5.9; 3957 -7.3; 4353 -4.2; 4788 -6.1; 5267 -10.6; 5793 -7.9; 6373 -3.9; 7010 -3.3; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.7; 12418 -6.8; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ AS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ AS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.33 | -2.1 dB |
| Peaking | 132 Hz   | 0.56 | -3.9 dB |
| Peaking | 836 Hz   | 0.87 | 6.7 dB  |
| Peaking | 1473 Hz  | 0.47 | -1.8 dB |
| Peaking | 2293 Hz  | 3.6  | -4.2 dB |
| Peaking | 3229 Hz  | 6.06 | 2.5 dB  |
| Peaking | 4569 Hz  | 6.1  | 6.3 dB  |
| Peaking | 5319 Hz  | 2.23 | -8.0 dB |
| Peaking | 6468 Hz  | 3.08 | 6.2 dB  |
| Peaking | 12328 Hz | 7.68 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/KZ%20AS-10/KZ%20AS-10.png)