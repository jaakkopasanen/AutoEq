# AKG N200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.7; 25 -6.1; 28 -6.5; 31 -6.9; 34 -7.2; 37 -7.4; 41 -7.6; 45 -7.8; 49 -7.9; 54 -7.9; 60 -8.0; 66 -8.0; 72 -8.0; 79 -7.9; 87 -7.7; 96 -7.4; 106 -7.0; 116 -6.6; 128 -6.0; 141 -5.2; 155 -4.4; 170 -3.6; 187 -3.1; 206 -2.9; 227 -2.9; 249 -2.9; 274 -3.1; 302 -3.2; 332 -3.3; 365 -3.4; 402 -3.4; 442 -3.3; 486 -3.0; 535 -2.5; 588 -2.0; 647 -1.4; 712 -1.0; 783 -0.6; 861 -0.5; 947 -0.5; 1042 -1.4; 1146 -1.8; 1261 -2.3; 1387 -2.9; 1526 -3.2; 1678 -3.8; 1846 -4.6; 2031 -5.3; 2234 -5.4; 2457 -4.7; 2703 -4.0; 2973 -3.6; 3270 -3.5; 3597 -3.5; 3957 -3.8; 4353 -4.0; 4788 -4.5; 5267 -5.6; 5793 -7.3; 6373 -5.2; 7010 -1.8; 7711 -3.0; 8482 -3.3; 9330 -4.1; 10263 -8.2; 11289 -6.4; 12418 -4.6; 13660 -8.2; 15026 -9.8; 16529 -5.4; 18182 -4.3; 20000 -12.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG N200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 57 Hz    | 0.65 | -5.2 dB |
| Peaking | 854 Hz   | 1.34 | 3.0 dB  |
| Peaking | 2109 Hz  | 1.93 | -2.2 dB |
| Peaking | 14538 Hz | 1.31 | -5.6 dB |
| Peaking | 19836 Hz | 2.37 | -8.7 dB |
| Peaking | 206 Hz   | 3.18 | 1.5 dB  |
| Peaking | 5885 Hz  | 4.01 | -4.4 dB |
| Peaking | 7032 Hz  | 4.91 | 3.1 dB  |
| Peaking | 15003 Hz | 4.34 | -1.3 dB |
| Peaking | 17280 Hz | 2.49 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -5.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20N200/AKG%20N200.png)