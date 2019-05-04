# KZ ZS-10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.6; 25 -4.9; 28 -5.2; 31 -5.4; 34 -5.6; 37 -5.8; 41 -6.0; 45 -6.1; 49 -6.3; 54 -6.4; 60 -6.6; 66 -6.9; 72 -7.1; 79 -7.3; 87 -7.6; 96 -7.8; 106 -8.0; 116 -8.1; 128 -8.2; 141 -8.1; 155 -8.0; 170 -7.9; 187 -7.7; 206 -7.5; 227 -7.1; 249 -6.8; 274 -6.4; 302 -6.0; 332 -5.5; 365 -5.1; 402 -4.6; 442 -4.0; 486 -3.5; 535 -2.8; 588 -2.2; 647 -1.6; 712 -1.0; 783 -0.6; 861 -0.5; 947 -0.8; 1042 -1.9; 1146 -3.0; 1261 -3.7; 1387 -4.3; 1526 -5.0; 1678 -5.9; 1846 -7.2; 2031 -8.5; 2234 -9.3; 2457 -8.8; 2703 -7.6; 2973 -7.0; 3270 -7.7; 3597 -8.9; 3957 -9.0; 4353 -5.5; 4788 -1.7; 5267 -3.8; 5793 -7.7; 6373 -3.6; 7010 -2.6; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -6.5; 11289 -7.4; 12418 -6.4; 13660 -6.6; 15026 -6.3; 16529 -5.1; 18182 -5.1; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS-10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS-10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 136 Hz   | 0.58 | -3.2 dB |
| Peaking | 792 Hz   | 1.09 | 5.0 dB  |
| Peaking | 2214 Hz  | 2.27 | -4.8 dB |
| Peaking | 3715 Hz  | 6.43 | -4.2 dB |
| Peaking | 11537 Hz | 3.31 | -2.4 dB |
| Peaking | 16 Hz    | 1.6  | 1.1 dB  |
| Peaking | 4950 Hz  | 6.55 | 5.6 dB  |
| Peaking | 5995 Hz  | 3.35 | -5.0 dB |
| Peaking | 6622 Hz  | 5.61 | 6.8 dB  |
| Peaking | 14326 Hz | 4.49 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/KZ%20ZS-10/KZ%20ZS-10.png)