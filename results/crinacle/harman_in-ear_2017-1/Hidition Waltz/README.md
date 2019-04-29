# Hidition Waltz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.1; 25 -6.5; 28 -7.0; 31 -7.4; 34 -7.6; 37 -7.8; 41 -8.1; 45 -8.4; 49 -8.6; 54 -8.8; 60 -9.1; 66 -9.3; 72 -9.5; 79 -9.7; 87 -10.0; 96 -10.1; 106 -10.3; 116 -10.4; 128 -10.4; 141 -10.4; 155 -10.2; 170 -10.1; 187 -9.9; 206 -9.7; 227 -9.4; 249 -9.0; 274 -8.6; 302 -8.2; 332 -7.8; 365 -7.3; 402 -7.0; 442 -6.8; 486 -6.5; 535 -6.2; 588 -6.0; 647 -5.8; 712 -5.6; 783 -5.4; 861 -5.4; 947 -5.7; 1042 -6.3; 1146 -7.2; 1261 -8.0; 1387 -8.4; 1526 -8.5; 1678 -8.4; 1846 -8.3; 2031 -7.8; 2234 -6.7; 2457 -5.0; 2703 -2.9; 2973 -1.2; 3270 -0.5; 3597 -1.3; 3957 -2.7; 4353 -4.8; 4788 -5.2; 5267 -3.9; 5793 -4.1; 6373 -2.7; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -11.5; 15026 -21.4; 16529 -24.1; 18182 -17.7; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hidition Waltz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hidition Waltz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 94 Hz    | 0.66 | -3.4 dB  |
| Peaking | 191 Hz   | 1.25 | -2.0 dB  |
| Peaking | 3321 Hz  | 3.11 | 6.2 dB   |
| Peaking | 12004 Hz | 0.6  | 9.7 dB   |
| Peaking | 16048 Hz | 0.94 | -25.2 dB |
| Peaking | 17 Hz    | 2.16 | 1.4 dB   |
| Peaking | 815 Hz   | 1.57 | 1.6 dB   |
| Peaking | 1542 Hz  | 1.78 | -3.0 dB  |
| Peaking | 6543 Hz  | 3.19 | 3.5 dB   |
| Peaking | 8139 Hz  | 2.27 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -18.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hidition%20Waltz/Hidition%20Waltz.png)