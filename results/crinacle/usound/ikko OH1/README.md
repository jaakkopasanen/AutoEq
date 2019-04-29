# ikko OH1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -2.8; 25 -2.9; 28 -3.1; 31 -3.3; 34 -3.4; 37 -3.6; 41 -3.8; 45 -3.9; 49 -4.1; 54 -4.2; 60 -4.4; 66 -4.5; 72 -4.6; 79 -4.8; 87 -5.0; 96 -5.1; 106 -5.3; 116 -5.4; 128 -5.4; 141 -5.4; 155 -5.3; 170 -5.1; 187 -4.8; 206 -4.6; 227 -4.2; 249 -4.0; 274 -3.6; 302 -3.2; 332 -2.9; 365 -2.5; 402 -2.3; 442 -2.2; 486 -2.1; 535 -1.8; 588 -1.5; 647 -1.2; 712 -0.9; 783 -0.7; 861 -0.5; 947 -0.6; 1042 -1.1; 1146 -1.9; 1261 -2.9; 1387 -3.5; 1526 -3.8; 1678 -3.9; 1846 -4.1; 2031 -4.4; 2234 -4.9; 2457 -5.2; 2703 -4.9; 2973 -4.1; 3270 -3.3; 3597 -3.1; 3957 -4.0; 4353 -4.9; 4788 -4.8; 5267 -4.4; 5793 -2.0; 6373 -1.0; 7010 -4.0; 7711 -3.6; 8482 -3.0; 9330 -3.0; 10263 -3.0; 11289 -3.0; 12418 -3.0; 13660 -3.0; 15026 -3.0; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`ikko OH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ikko OH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 90 Hz   | 0.74 | -1.5 dB |
| Peaking | 161 Hz  | 1    | -1.6 dB |
| Peaking | 1105 Hz | 0.69 | 4.3 dB  |
| Peaking | 1336 Hz | 2.18 | -2.4 dB |
| Peaking | 2127 Hz | 0.89 | -3.5 dB |
| Peaking | 16 Hz   | 1.42 | 0.6 dB  |
| Peaking | 3501 Hz | 4.34 | 1.7 dB  |
| Peaking | 5067 Hz | 1.94 | -2.9 dB |
| Peaking | 6213 Hz | 2.79 | 4.3 dB  |
| Peaking | 7151 Hz | 6.97 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/ikko%20OH1/ikko%20OH1.png)