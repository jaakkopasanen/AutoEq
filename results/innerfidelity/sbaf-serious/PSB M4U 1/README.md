# PSB M4U 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.3; 25 -4.3; 28 -4.1; 31 -4.0; 34 -3.8; 37 -3.6; 41 -3.3; 45 -3.0; 49 -2.7; 54 -2.3; 60 -1.9; 66 -1.5; 72 -1.1; 79 -1.0; 87 -2.2; 96 -5.0; 106 -6.1; 116 -5.4; 128 -5.6; 141 -6.2; 155 -5.5; 170 -5.0; 187 -6.0; 206 -5.4; 227 -4.9; 249 -4.4; 274 -3.7; 302 -2.4; 332 -2.6; 365 -2.9; 402 -1.4; 442 -0.5; 486 -1.6; 535 -1.4; 588 -0.6; 647 -0.6; 712 -1.6; 783 -2.0; 861 -3.2; 947 -3.4; 1042 -3.3; 1146 -3.5; 1261 -3.7; 1387 -4.2; 1526 -4.6; 1678 -4.9; 1846 -4.9; 2031 -4.7; 2234 -4.8; 2457 -4.6; 2703 -4.8; 2973 -5.2; 3270 -5.5; 3597 -6.6; 3957 -7.0; 4353 -7.2; 4788 -5.4; 5267 -3.8; 5793 -1.3; 6373 -1.3; 7010 -3.5; 7711 -7.0; 8482 -9.1; 9330 -8.2; 10263 -4.3; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 70 Hz   | 3.63 | 3.6 dB  |
| Peaking | 560 Hz  | 1.47 | 3.7 dB  |
| Peaking | 4316 Hz | 1.63 | -4.0 dB |
| Peaking | 6067 Hz | 2.31 | 5.6 dB  |
| Peaking | 8468 Hz | 3.39 | -6.2 dB |
| Peaking | 51 Hz   | 1.52 | 2.5 dB  |
| Peaking | 83 Hz   | 6.09 | 3.3 dB  |
| Peaking | 110 Hz  | 0.46 | -2.5 dB |
| Peaking | 333 Hz  | 1.59 | 1.6 dB  |
| Peaking | 1712 Hz | 5.24 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%201/PSB%20M4U%201.png)