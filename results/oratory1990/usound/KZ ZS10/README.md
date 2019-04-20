# KZ ZS10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -10.0; 25 -10.3; 28 -10.5; 31 -10.5; 34 -10.5; 37 -10.5; 41 -10.5; 45 -10.5; 49 -10.6; 54 -10.8; 60 -11.1; 66 -11.3; 72 -11.4; 79 -11.6; 87 -11.5; 96 -11.1; 106 -11.3; 116 -11.1; 128 -11.1; 141 -10.8; 155 -10.4; 170 -10.2; 187 -10.0; 206 -9.6; 227 -9.3; 249 -8.8; 274 -8.4; 302 -8.0; 332 -7.4; 365 -7.0; 402 -6.5; 442 -6.0; 486 -5.6; 535 -5.2; 588 -4.8; 647 -4.4; 712 -4.1; 783 -4.0; 861 -3.7; 947 -3.6; 1042 -4.2; 1146 -5.1; 1261 -6.1; 1387 -7.0; 1526 -7.7; 1678 -8.4; 1846 -9.2; 2031 -10.3; 2234 -10.8; 2457 -10.0; 2703 -9.0; 2973 -8.6; 3270 -8.3; 3597 -8.9; 3957 -6.8; 4353 -1.8; 4788 -0.5; 5267 -2.7; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.5; 8482 -7.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.1; 15026 -7.3; 16529 -6.5; 18182 -7.3; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.07 | -2.1 dB |
| Peaking | 95 Hz    | 0.38 | -4.9 dB |
| Peaking | 939 Hz   | 0.68 | 7.3 dB  |
| Peaking | 3059 Hz  | 0.33 | -9.5 dB |
| Peaking | 5193 Hz  | 1.08 | 13.5 dB |
| Peaking | 2885 Hz  | 5.75 | 1.1 dB  |
| Peaking | 3716 Hz  | 9.57 | -2.3 dB |
| Peaking | 6450 Hz  | 8.7  | 2.2 dB  |
| Peaking | 8007 Hz  | 5.49 | -1.9 dB |
| Peaking | 10886 Hz | 3    | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/KZ%20ZS10/KZ%20ZS10.png)