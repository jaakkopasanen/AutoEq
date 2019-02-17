# PSB M4U 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.0; 25 -8.3; 28 -8.5; 31 -8.7; 34 -8.8; 37 -8.9; 41 -9.0; 45 -8.9; 49 -8.9; 54 -8.9; 60 -8.9; 66 -8.9; 72 -8.9; 79 -8.9; 87 -8.9; 96 -8.9; 106 -8.7; 116 -8.6; 128 -8.4; 141 -8.3; 155 -8.1; 170 -7.8; 187 -7.6; 206 -7.3; 227 -6.9; 249 -6.7; 274 -6.4; 302 -6.2; 332 -5.9; 365 -5.7; 402 -5.6; 442 -5.2; 486 -5.3; 535 -5.3; 588 -5.0; 647 -5.0; 712 -5.3; 783 -5.3; 861 -5.7; 947 -6.2; 1042 -6.6; 1146 -7.2; 1261 -7.2; 1387 -7.5; 1526 -8.2; 1678 -8.4; 1846 -8.3; 2031 -8.1; 2234 -8.0; 2457 -7.4; 2703 -6.7; 2973 -5.8; 3270 -5.2; 3597 -5.0; 3957 -4.4; 4353 -5.1; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.31 | -2.6 dB |
| Peaking | 689 Hz  | 0.53 | 3.2 dB  |
| Peaking | 2487 Hz | 0.36 | -4.3 dB |
| Peaking | 3284 Hz | 1.53 | 3.9 dB  |
| Peaking | 5705 Hz | 2.16 | 8.5 dB  |
| Peaking | 6679 Hz | 7.21 | 2.2 dB  |
| Peaking | 7174 Hz | 2.05 | -1.7 dB |
| Peaking | 9035 Hz | 0.72 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%204/PSB%20M4U%204.png)