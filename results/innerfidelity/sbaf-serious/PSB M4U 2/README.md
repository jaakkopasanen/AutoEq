# PSB M4U 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -5.8; 25 -6.9; 28 -7.4; 31 -6.9; 34 -6.2; 37 -5.6; 41 -5.0; 45 -4.6; 49 -4.3; 54 -4.0; 60 -3.9; 66 -3.8; 72 -3.6; 79 -3.4; 87 -3.7; 96 -4.8; 106 -5.6; 116 -5.7; 128 -5.7; 141 -5.8; 155 -5.7; 170 -5.4; 187 -5.8; 206 -5.5; 227 -5.1; 249 -4.8; 274 -4.3; 302 -3.8; 332 -3.3; 365 -3.0; 402 -2.6; 442 -1.9; 486 -2.3; 535 -2.3; 588 -2.4; 647 -2.5; 712 -3.0; 783 -3.5; 861 -4.3; 947 -5.1; 1042 -6.1; 1146 -6.5; 1261 -7.3; 1387 -8.4; 1526 -9.4; 1678 -9.5; 1846 -8.8; 2031 -7.8; 2234 -7.2; 2457 -6.1; 2703 -5.2; 2973 -4.8; 3270 -5.4; 3597 -6.0; 3957 -5.8; 4353 -4.8; 4788 -4.1; 5267 -2.4; 5793 -0.5; 6373 -1.5; 7010 -3.3; 7711 -5.5; 8482 -6.2; 9330 -6.0; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 2.06 | 2.5 dB  |
| Peaking | 527 Hz  | 0.99 | 4.1 dB  |
| Peaking | 1615 Hz | 1.68 | -4.3 dB |
| Peaking | 2814 Hz | 4.74 | 1.6 dB  |
| Peaking | 5892 Hz | 3.39 | 5.6 dB  |
| Peaking | 16 Hz   | 0.67 | 5.0 dB  |
| Peaking | 27 Hz   | 1.98 | -4.8 dB |
| Peaking | 148 Hz  | 1.49 | -0.6 dB |
| Peaking | 789 Hz  | 6.88 | 0.4 dB  |
| Peaking | 8755 Hz | 5.56 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%202/PSB%20M4U%202.png)