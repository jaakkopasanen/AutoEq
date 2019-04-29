# TFZ 5S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.6; 25 -10.7; 28 -10.8; 31 -10.8; 34 -10.9; 37 -10.9; 41 -11.0; 45 -11.0; 49 -11.1; 54 -11.1; 60 -11.2; 66 -11.3; 72 -11.4; 79 -11.5; 87 -11.7; 96 -11.8; 106 -11.9; 116 -11.9; 128 -11.9; 141 -11.8; 155 -11.7; 170 -11.4; 187 -11.1; 206 -10.7; 227 -10.3; 249 -9.9; 274 -9.4; 302 -8.9; 332 -8.4; 365 -7.9; 402 -7.3; 442 -6.8; 486 -6.2; 535 -5.7; 588 -5.3; 647 -4.9; 712 -5.0; 783 -5.1; 861 -5.4; 947 -6.0; 1042 -6.8; 1146 -7.8; 1261 -8.9; 1387 -9.9; 1526 -10.7; 1678 -11.1; 1846 -11.0; 2031 -9.9; 2234 -7.9; 2457 -5.6; 2703 -3.9; 2973 -3.0; 3270 -3.0; 3597 -4.3; 3957 -6.4; 4353 -5.5; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.5; 18182 -6.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ 5S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ 5S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.41 | -4.3 dB |
| Peaking | 120 Hz  | 1.08 | -3.6 dB |
| Peaking | 215 Hz  | 1.83 | -2.4 dB |
| Peaking | 1672 Hz | 3.08 | -5.5 dB |
| Peaking | 5532 Hz | 2.11 | 6.5 dB  |
| Peaking | 691 Hz  | 2.21 | 2.3 dB  |
| Peaking | 2263 Hz | 1.42 | -3.9 dB |
| Peaking | 2864 Hz | 1.52 | 6.0 dB  |
| Peaking | 4078 Hz | 5.46 | -4.2 dB |
| Peaking | 8215 Hz | 3.31 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%205S/TFZ%205S.png)