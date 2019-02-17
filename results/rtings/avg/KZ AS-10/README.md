# KZ AS-10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.3; 25 -3.4; 28 -3.5; 31 -3.6; 34 -3.7; 37 -3.8; 41 -3.9; 45 -4.0; 49 -4.1; 54 -4.3; 60 -4.8; 66 -5.2; 72 -5.6; 79 -5.9; 87 -6.4; 96 -6.9; 106 -7.4; 116 -7.9; 128 -8.3; 141 -8.6; 155 -8.6; 170 -8.6; 187 -8.5; 206 -8.5; 227 -8.3; 249 -7.9; 274 -7.4; 302 -6.8; 332 -6.3; 365 -5.7; 402 -5.1; 442 -4.5; 486 -3.8; 535 -3.1; 588 -2.5; 647 -1.8; 712 -1.1; 783 -0.7; 861 -0.5; 947 -0.8; 1042 -1.6; 1146 -2.5; 1261 -3.4; 1387 -4.1; 1526 -4.8; 1678 -5.6; 1846 -6.6; 2031 -7.7; 2234 -8.6; 2457 -8.8; 2703 -7.7; 2973 -5.9; 3270 -5.3; 3597 -6.3; 3957 -8.0; 4353 -4.6; 4788 -5.9; 5267 -10.5; 5793 -7.9; 6373 -5.0; 7010 -2.8; 7711 -1.0; 8482 -1.2; 9330 -3.2; 10263 -4.1; 11289 -4.5; 12418 -6.6; 13660 -4.3; 15026 -1.2; 16529 -1.2; 18182 -1.2; 20000 -1.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ AS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ AS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 155 Hz   | 0.53 | -7.7 dB |
| Peaking | 2389 Hz  | 1.43 | -7.3 dB |
| Peaking | 5380 Hz  | 3.81 | -8.2 dB |
| Peaking | 12416 Hz | 2.88 | -5.5 dB |
| Peaking | 22050 Hz | 2.19 | -2.6 dB |
| Peaking | 25 Hz    | 1.22 | -1.5 dB |
| Peaking | 824 Hz   | 2.81 | 2.5 dB  |
| Peaking | 2982 Hz  | 6.93 | 1.1 dB  |
| Peaking | 3922 Hz  | 9.47 | -3.6 dB |
| Peaking | 7783 Hz  | 6.64 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -6.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | -5.1 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/KZ%20AS-10/KZ%20AS-10.png)