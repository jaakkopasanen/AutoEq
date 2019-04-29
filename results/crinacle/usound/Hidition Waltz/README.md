# Hidition Waltz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.7; 25 -3.1; 28 -3.6; 31 -4.0; 34 -4.2; 37 -4.4; 41 -4.7; 45 -5.0; 49 -5.2; 54 -5.4; 60 -5.7; 66 -5.9; 72 -6.1; 79 -6.3; 87 -6.6; 96 -6.7; 106 -6.9; 116 -7.0; 128 -7.0; 141 -7.0; 155 -6.8; 170 -6.7; 187 -6.5; 206 -6.3; 227 -6.0; 249 -5.6; 274 -5.2; 302 -4.9; 332 -4.6; 365 -4.2; 402 -4.0; 442 -3.7; 486 -3.5; 535 -3.3; 588 -3.1; 647 -2.9; 712 -2.7; 783 -2.5; 861 -2.5; 947 -2.6; 1042 -3.2; 1146 -4.2; 1261 -5.3; 1387 -6.0; 1526 -6.3; 1678 -6.3; 1846 -6.2; 2031 -6.1; 2234 -5.6; 2457 -4.5; 2703 -2.8; 2973 -1.2; 3270 -0.5; 3597 -1.0; 3957 -2.1; 4353 -3.7; 4788 -3.8; 5267 -2.5; 5793 -2.9; 6373 -2.0; 7010 -3.7; 7711 -6.4; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hidition Waltz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hidition Waltz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.47 | 2.3 dB  |
| Peaking | 127 Hz  | 0.59 | -3.0 dB |
| Peaking | 952 Hz  | 0.74 | 3.9 dB  |
| Peaking | 1610 Hz | 0.88 | -5.2 dB |
| Peaking | 3248 Hz | 1.96 | 4.8 dB  |
| Peaking | 4503 Hz | 8.23 | -1.5 dB |
| Peaking | 6690 Hz | 2.62 | 2.9 dB  |
| Peaking | 7552 Hz | 5.24 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Hidition%20Waltz/Hidition%20Waltz.png)