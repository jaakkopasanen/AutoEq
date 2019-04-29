# Unique Melody 3DD-Ti
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -6.8; 25 -6.6; 28 -6.3; 31 -6.0; 34 -5.7; 37 -5.5; 41 -5.3; 45 -5.1; 49 -4.9; 54 -4.7; 60 -4.6; 66 -4.5; 72 -4.5; 79 -4.6; 87 -4.6; 96 -4.8; 106 -4.9; 116 -5.1; 128 -5.2; 141 -5.3; 155 -5.3; 170 -5.3; 187 -5.3; 206 -5.3; 227 -5.2; 249 -5.1; 274 -5.0; 302 -4.9; 332 -4.7; 365 -4.5; 402 -4.3; 442 -4.1; 486 -3.9; 535 -3.7; 588 -3.5; 647 -3.6; 712 -3.9; 783 -4.6; 861 -5.2; 947 -6.3; 1042 -7.8; 1146 -9.6; 1261 -11.1; 1387 -11.4; 1526 -10.2; 1678 -8.1; 1846 -5.8; 2031 -3.9; 2234 -2.7; 2457 -2.6; 2703 -4.1; 2973 -9.3; 3270 -13.6; 3597 -7.3; 3957 -2.2; 4353 -0.5; 4788 -0.6; 5267 -2.1; 5793 -7.8; 6373 -9.5; 7010 -4.1; 7711 -5.1; 8482 -5.4; 9330 -5.9; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody 3DD-Ti GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody 3DD-Ti ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 1381 Hz | 2.78 | -7.5 dB  |
| Peaking | 2521 Hz | 1.77 | 5.1 dB   |
| Peaking | 3231 Hz | 4.04 | -14.2 dB |
| Peaking | 4419 Hz | 1.71 | 7.0 dB   |
| Peaking | 6095 Hz | 6.38 | -7.9 dB  |
| Peaking | 20 Hz   | 1.23 | -1.6 dB  |
| Peaking | 67 Hz   | 1.31 | 1.0 dB   |
| Peaking | 600 Hz  | 1.26 | 2.2 dB   |
| Peaking | 1109 Hz | 4.28 | -1.7 dB  |
| Peaking | 9306 Hz | 5.72 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%203DD-Ti/Unique%20Melody%203DD-Ti.png)