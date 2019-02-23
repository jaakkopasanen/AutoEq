# PSB M4U 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -9.1; 25 -9.3; 28 -9.6; 31 -9.8; 34 -9.9; 37 -10.0; 41 -10.0; 45 -10.0; 49 -10.0; 54 -10.0; 60 -10.0; 66 -10.0; 72 -10.0; 79 -10.0; 87 -10.0; 96 -10.0; 106 -9.8; 116 -9.6; 128 -9.5; 141 -9.3; 155 -9.1; 170 -8.9; 187 -8.6; 206 -8.4; 227 -8.0; 249 -7.8; 274 -7.5; 302 -7.2; 332 -7.0; 365 -6.8; 402 -6.6; 442 -6.3; 486 -6.4; 535 -6.3; 588 -6.1; 647 -6.1; 712 -6.4; 783 -6.3; 861 -6.8; 947 -7.2; 1042 -7.7; 1146 -8.2; 1261 -8.2; 1387 -8.6; 1526 -9.2; 1678 -9.4; 1846 -9.4; 2031 -9.1; 2234 -9.0; 2457 -8.5; 2703 -7.8; 2973 -6.9; 3270 -6.3; 3597 -6.1; 3957 -5.5; 4353 -6.2; 4788 -4.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -7.0; 9330 -7.1; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.46 | -3.4 dB |
| Peaking | 131 Hz  | 0.98 | -1.9 dB |
| Peaking | 1822 Hz | 1.36 | -3.3 dB |
| Peaking | 5869 Hz | 2.47 | 7.2 dB  |
| Peaking | 8436 Hz | 1.95 | -1.8 dB |
| Peaking | 633 Hz  | 1.54 | 0.8 dB  |
| Peaking | 1119 Hz | 3.8  | -0.7 dB |
| Peaking | 4526 Hz | 7.72 | -1.6 dB |
| Peaking | 5134 Hz | 9.36 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%204/PSB%20M4U%204.png)