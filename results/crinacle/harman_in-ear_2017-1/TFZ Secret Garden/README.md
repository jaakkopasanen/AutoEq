# TFZ Secret Garden
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.1; 25 -4.3; 28 -4.6; 31 -4.7; 34 -4.9; 37 -5.0; 41 -5.1; 45 -5.2; 49 -5.3; 54 -5.4; 60 -5.6; 66 -5.7; 72 -5.8; 79 -6.0; 87 -6.1; 96 -6.3; 106 -6.5; 116 -6.5; 128 -6.6; 141 -6.6; 155 -6.4; 170 -6.3; 187 -6.1; 206 -5.9; 227 -5.6; 249 -5.3; 274 -5.0; 302 -4.6; 332 -4.1; 365 -3.7; 402 -3.4; 442 -3.1; 486 -2.8; 535 -2.5; 588 -2.3; 647 -2.0; 712 -1.7; 783 -1.6; 861 -1.5; 947 -1.7; 1042 -2.4; 1146 -3.5; 1261 -4.7; 1387 -5.8; 1526 -6.1; 1678 -6.1; 1846 -6.5; 2031 -7.1; 2234 -7.3; 2457 -6.5; 2703 -4.4; 2973 -2.1; 3270 -0.7; 3597 -0.5; 3957 -1.5; 4353 -4.0; 4788 -7.8; 5267 -8.0; 5793 -4.0; 6373 -2.3; 7010 -5.3; 7711 -4.2; 8482 -4.0; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -5.4; 15026 -9.6; 16529 -10.3; 18182 -8.5; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Secret Garden GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Secret Garden ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 793 Hz   | 0.34 | 12.3 dB  |
| Peaking | 2136 Hz  | 0.21 | -32.8 dB |
| Peaking | 3710 Hz  | 0.29 | 29.1 dB  |
| Peaking | 4928 Hz  | 3.09 | -9.7 dB  |
| Peaking | 18378 Hz | 0.49 | -6.3 dB  |
| Peaking | 1365 Hz  | 3.98 | -2.6 dB  |
| Peaking | 1386 Hz  | 2.08 | 1.6 dB   |
| Peaking | 7224 Hz  | 9.88 | -2.5 dB  |
| Peaking | 12911 Hz | 2.35 | 2.3 dB   |
| Peaking | 15341 Hz | 3.15 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%20Secret%20Garden/TFZ%20Secret%20Garden.png)