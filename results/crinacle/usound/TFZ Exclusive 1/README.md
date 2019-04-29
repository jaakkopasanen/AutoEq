# TFZ Exclusive 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.2; 25 -8.4; 28 -8.6; 31 -8.7; 34 -8.8; 37 -8.8; 41 -8.9; 45 -8.9; 49 -8.9; 54 -8.9; 60 -8.9; 66 -8.9; 72 -8.9; 79 -8.9; 87 -9.0; 96 -9.0; 106 -9.0; 116 -8.9; 128 -8.8; 141 -8.6; 155 -8.4; 170 -8.1; 187 -7.8; 206 -7.5; 227 -7.0; 249 -6.6; 274 -6.1; 302 -5.7; 332 -5.2; 365 -4.8; 402 -4.4; 442 -4.0; 486 -3.7; 535 -3.3; 588 -3.0; 647 -2.7; 712 -2.4; 783 -2.0; 861 -2.2; 947 -2.3; 1042 -1.6; 1146 -3.3; 1261 -4.1; 1387 -4.1; 1526 -4.7; 1678 -5.0; 1846 -5.2; 2031 -5.6; 2234 -6.2; 2457 -6.8; 2703 -6.6; 2973 -5.7; 3270 -4.8; 3597 -4.3; 3957 -4.7; 4353 -6.1; 4788 -7.8; 5267 -6.5; 5793 -2.9; 6373 -0.5; 7010 -2.6; 7711 -4.9; 8482 -7.4; 9330 -5.4; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Exclusive 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Exclusive 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.36 | -3.5 dB |
| Peaking | 142 Hz   | 0.78 | -2.4 dB |
| Peaking | 821 Hz   | 0.83 | 4.2 dB  |
| Peaking | 2822 Hz  | 0.27 | -1.5 dB |
| Peaking | 6440 Hz  | 5.43 | 6.4 dB  |
| Peaking | 2569 Hz  | 3.01 | -1.6 dB |
| Peaking | 3743 Hz  | 1.91 | 2.5 dB  |
| Peaking | 4462 Hz  | 4.49 | -1.2 dB |
| Peaking | 4901 Hz  | 6.66 | -2.7 dB |
| Peaking | 11958 Hz | 3.25 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%20Exclusive%201/TFZ%20Exclusive%201.png)