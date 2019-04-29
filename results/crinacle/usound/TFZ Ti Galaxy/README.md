# TFZ Ti Galaxy
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.1; 25 -11.0; 28 -10.9; 31 -10.9; 34 -10.8; 37 -10.7; 41 -10.6; 45 -10.4; 49 -10.3; 54 -10.1; 60 -10.0; 66 -9.9; 72 -9.9; 79 -9.8; 87 -9.8; 96 -9.7; 106 -9.7; 116 -9.6; 128 -9.4; 141 -9.4; 155 -9.2; 170 -8.9; 187 -8.6; 206 -8.3; 227 -8.0; 249 -7.7; 274 -7.3; 302 -7.0; 332 -6.7; 365 -6.4; 402 -6.1; 442 -5.9; 486 -5.7; 535 -5.5; 588 -5.3; 647 -5.4; 712 -5.2; 783 -4.9; 861 -4.9; 947 -5.2; 1042 -5.9; 1146 -6.9; 1261 -8.1; 1387 -9.0; 1526 -9.6; 1678 -9.9; 1846 -9.9; 2031 -9.5; 2234 -8.4; 2457 -6.9; 2703 -5.5; 2973 -4.8; 3270 -5.0; 3597 -6.1; 3957 -7.7; 4353 -6.7; 4788 -3.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -7.9; 8482 -7.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Ti Galaxy GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Ti Galaxy ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.35 | -4.5 dB |
| Peaking | 134 Hz  | 1.25 | -2.0 dB |
| Peaking | 1777 Hz | 2.43 | -4.1 dB |
| Peaking | 2937 Hz | 5.47 | 2.2 dB  |
| Peaking | 5710 Hz | 3.52 | 7.1 dB  |
| Peaking | 816 Hz  | 1.14 | 2.0 dB  |
| Peaking | 1333 Hz | 3.01 | -1.8 dB |
| Peaking | 4109 Hz | 6.51 | -3.2 dB |
| Peaking | 5401 Hz | 1.15 | 1.0 dB  |
| Peaking | 7990 Hz | 6.34 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/TFZ%20Ti%20Galaxy/TFZ%20Ti%20Galaxy.png)