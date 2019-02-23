# PSB M4U 8 Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -7.9; 25 -7.9; 28 -7.8; 31 -7.7; 34 -7.6; 37 -7.5; 41 -7.3; 45 -7.0; 49 -6.9; 54 -6.9; 60 -7.3; 66 -7.3; 72 -7.2; 79 -6.9; 87 -6.7; 96 -6.7; 106 -7.8; 116 -8.3; 128 -8.9; 141 -9.4; 155 -8.7; 170 -7.7; 187 -8.6; 206 -7.8; 227 -7.0; 249 -6.2; 274 -5.4; 302 -5.3; 332 -4.5; 365 -3.6; 402 -2.9; 442 -2.0; 486 -1.9; 535 -1.3; 588 -0.7; 647 -0.5; 712 -0.8; 783 -1.2; 861 -2.0; 947 -2.3; 1042 -2.5; 1146 -3.0; 1261 -3.4; 1387 -3.6; 1526 -3.8; 1678 -3.8; 1846 -3.3; 2031 -2.6; 2234 -2.9; 2457 -2.8; 2703 -2.9; 2973 -3.1; 3270 -3.8; 3597 -4.5; 3957 -5.1; 4353 -4.6; 4788 -3.3; 5267 -2.9; 5793 -2.1; 6373 -2.1; 7010 -2.5; 7711 -3.6; 8482 -3.9; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -3.9; 18182 -3.9; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PSB M4U 8 Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 8 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.86 | -3.4 dB |
| Peaking | 33 Hz   | 0.56 | -2.7 dB |
| Peaking | 156 Hz  | 0.89 | -4.8 dB |
| Peaking | 614 Hz  | 1.11 | 3.8 dB  |
| Peaking | 6250 Hz | 3.74 | 2.2 dB  |
| Peaking | 90 Hz   | 1.8  | -1.0 dB |
| Peaking | 91 Hz   | 3.93 | 1.8 dB  |
| Peaking | 1588 Hz | 1.75 | -1.7 dB |
| Peaking | 2036 Hz | 1.12 | 1.8 dB  |
| Peaking | 3969 Hz | 4.7  | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%208%20Wired%20Passive/PSB%20M4U%208%20Wired%20Passive.png)