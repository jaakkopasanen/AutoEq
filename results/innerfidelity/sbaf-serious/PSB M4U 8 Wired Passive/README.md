# PSB M4U 8 Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -7.9; 25 -7.9; 28 -7.8; 31 -7.7; 34 -7.6; 37 -7.5; 41 -7.3; 45 -7.0; 49 -6.9; 54 -6.9; 60 -7.3; 66 -7.3; 72 -7.2; 79 -6.9; 87 -6.7; 96 -6.7; 106 -7.8; 116 -8.3; 128 -8.9; 141 -9.4; 155 -8.7; 170 -7.7; 187 -8.6; 206 -7.8; 227 -7.0; 249 -6.2; 274 -5.4; 302 -5.3; 332 -4.5; 365 -3.6; 402 -2.9; 442 -2.0; 486 -1.9; 535 -1.3; 588 -0.7; 647 -0.5; 712 -0.8; 783 -1.2; 861 -2.0; 947 -2.3; 1042 -2.5; 1146 -3.0; 1261 -3.4; 1387 -3.6; 1526 -3.8; 1678 -3.8; 1846 -3.3; 2031 -2.6; 2234 -2.9; 2457 -2.8; 2703 -2.9; 2973 -3.1; 3270 -3.8; 3597 -4.5; 3957 -5.1; 4353 -4.6; 4788 -3.3; 5267 -2.9; 5793 -2.1; 6373 -2.1; 7010 -2.5; 7711 -2.2; 8482 -2.3; 9330 -2.4; 10263 -2.4; 11289 -2.4; 12418 -2.4; 13660 -2.4; 15026 -2.4; 16529 -2.4; 18182 -2.4; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 8 Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 8 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 1.06 | -5.2 dB |
| Peaking | 32 Hz   | 0.49 | -4.2 dB |
| Peaking | 158 Hz  | 0.81 | -5.9 dB |
| Peaking | 597 Hz  | 2.1  | 2.7 dB  |
| Peaking | 3906 Hz | 2.65 | -2.7 dB |
| Peaking | 91 Hz   | 1.79 | -1.0 dB |
| Peaking | 91 Hz   | 3.92 | 1.7 dB  |
| Peaking | 754 Hz  | 5.85 | 0.7 dB  |
| Peaking | 1479 Hz | 2.43 | -1.5 dB |
| Peaking | 6134 Hz | 4.64 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%208%20Wired%20Passive/PSB%20M4U%208%20Wired%20Passive.png)