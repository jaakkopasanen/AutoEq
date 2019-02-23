# PSB M4U 2 passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -4.9; 25 -4.9; 28 -4.9; 31 -4.8; 34 -4.7; 37 -4.6; 41 -4.4; 45 -4.2; 49 -4.0; 54 -3.7; 60 -3.3; 66 -2.7; 72 -2.3; 79 -2.0; 87 -3.4; 96 -5.9; 106 -7.1; 116 -6.7; 128 -6.3; 141 -6.3; 155 -5.6; 170 -5.4; 187 -6.0; 206 -5.3; 227 -4.6; 249 -4.0; 274 -2.9; 302 -2.5; 332 -2.1; 365 -2.2; 402 -1.5; 442 -1.1; 486 -1.6; 535 -1.8; 588 -2.1; 647 -2.3; 712 -3.1; 783 -3.5; 861 -4.3; 947 -4.6; 1042 -4.6; 1146 -4.6; 1261 -4.7; 1387 -5.1; 1526 -5.2; 1678 -5.1; 1846 -4.4; 2031 -3.8; 2234 -3.5; 2457 -3.0; 2703 -2.6; 2973 -2.7; 3270 -3.7; 3597 -4.8; 3957 -5.2; 4353 -4.5; 4788 -4.1; 5267 -2.8; 5793 -0.5; 6373 -1.4; 7010 -1.9; 7711 -3.5; 8482 -4.4; 9330 -4.1; 10263 -3.8; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 2 passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 2 passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 80 Hz   | 1.33 | 6.1 dB  |
| Peaking | 102 Hz  | 2.67 | -3.9 dB |
| Peaking | 221 Hz  | 0.19 | -4.5 dB |
| Peaking | 417 Hz  | 0.77 | 6.7 dB  |
| Peaking | 6031 Hz | 4.42 | 3.4 dB  |
| Peaking | 11 Hz   | 1.98 | -0.7 dB |
| Peaking | 1580 Hz | 2.94 | -1.1 dB |
| Peaking | 2936 Hz | 1.48 | 2.5 dB  |
| Peaking | 3774 Hz | 2.53 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%202%20passive/PSB%20M4U%202%20passive.png)