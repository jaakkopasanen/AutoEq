# AKG N200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.8; 31 -2.2; 34 -2.4; 37 -2.7; 41 -2.9; 45 -3.0; 49 -3.1; 54 -3.3; 60 -3.6; 66 -3.9; 72 -4.1; 79 -4.2; 87 -4.3; 96 -4.4; 106 -4.5; 116 -4.5; 128 -4.4; 141 -4.0; 155 -3.6; 170 -3.2; 187 -2.9; 206 -2.9; 227 -3.0; 249 -3.1; 274 -3.3; 302 -3.4; 332 -3.5; 365 -3.5; 402 -3.6; 442 -3.4; 486 -3.1; 535 -2.6; 588 -2.1; 647 -1.5; 712 -1.0; 783 -0.7; 861 -0.5; 947 -0.5; 1042 -1.5; 1146 -1.7; 1261 -2.3; 1387 -2.8; 1526 -3.1; 1678 -3.7; 1846 -4.3; 2031 -5.0; 2234 -4.7; 2457 -4.0; 2703 -3.6; 2973 -3.7; 3270 -3.8; 3597 -3.9; 3957 -4.3; 4353 -4.5; 4788 -4.3; 5267 -5.3; 5793 -7.6; 6373 -6.4; 7010 -1.9; 7711 -2.9; 8482 -3.2; 9330 -5.1; 10263 -8.5; 11289 -5.3; 12418 -4.3; 13660 -8.8; 15026 -10.0; 16529 -5.7; 18182 -4.3; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 2.39 | 2.8 dB  |
| Peaking | 840 Hz   | 2.34 | 3.1 dB  |
| Peaking | 5812 Hz  | 5.16 | -4.6 dB |
| Peaking | 14658 Hz | 1.79 | -6.9 dB |
| Peaking | 19862 Hz | 2.23 | -8.1 dB |
| Peaking | 100 Hz   | 1.55 | -1.4 dB |
| Peaking | 2072 Hz  | 4.14 | -2.0 dB |
| Peaking | 4312 Hz  | 1.63 | -1.0 dB |
| Peaking | 9825 Hz  | 1.14 | 3.2 dB  |
| Peaking | 10089 Hz | 4.06 | -7.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20N200/AKG%20N200.png)