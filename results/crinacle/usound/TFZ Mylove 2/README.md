# TFZ Mylove 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.3; 25 -8.3; 28 -8.2; 31 -8.0; 34 -7.8; 37 -7.6; 41 -7.4; 45 -7.2; 49 -6.9; 54 -6.7; 60 -6.5; 66 -6.3; 72 -6.2; 79 -6.1; 87 -6.0; 96 -5.8; 106 -5.7; 116 -5.6; 128 -5.4; 141 -5.3; 155 -5.0; 170 -4.8; 187 -4.5; 206 -4.1; 227 -3.8; 249 -3.5; 274 -3.2; 302 -2.8; 332 -2.5; 365 -2.2; 402 -2.0; 442 -1.7; 486 -1.5; 535 -1.3; 588 -1.1; 647 -0.9; 712 -0.8; 783 -0.6; 861 -0.5; 947 -0.7; 1042 -1.3; 1146 -2.2; 1261 -3.1; 1387 -4.1; 1526 -4.7; 1678 -5.0; 1846 -5.4; 2031 -6.0; 2234 -6.2; 2457 -5.5; 2703 -4.0; 2973 -2.6; 3270 -1.8; 3597 -1.7; 3957 -2.7; 4353 -4.7; 4788 -6.4; 5267 -4.8; 5793 -2.1; 6373 -1.6; 7010 -5.9; 7711 -6.5; 8482 -3.3; 9330 -3.3; 10263 -3.3; 11289 -3.3; 12418 -3.3; 13660 -3.3; 15026 -3.3; 16529 -3.3; 18182 -3.3; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Mylove 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Mylove 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.41 | -4.9 dB |
| Peaking | 129 Hz  | 0.65 | -1.7 dB |
| Peaking | 1081 Hz | 0.42 | 3.9 dB  |
| Peaking | 1818 Hz | 1.19 | -5.9 dB |
| Peaking | 7432 Hz | 8.3  | -4.5 dB |
| Peaking | 1813 Hz | 4.7  | 1.5 dB  |
| Peaking | 2326 Hz | 1.7  | -1.9 dB |
| Peaking | 3394 Hz | 1.98 | 2.9 dB  |
| Peaking | 4793 Hz | 3.66 | -4.3 dB |
| Peaking | 6076 Hz | 6.16 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%20Mylove%202/TFZ%20Mylove%202.png)