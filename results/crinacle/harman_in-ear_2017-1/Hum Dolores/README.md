# Hum Dolores
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.3; 25 -2.6; 28 -3.1; 31 -3.4; 34 -3.6; 37 -3.8; 41 -4.0; 45 -4.3; 49 -4.5; 54 -4.8; 60 -5.0; 66 -5.3; 72 -5.6; 79 -6.0; 87 -6.4; 96 -6.7; 106 -7.1; 116 -7.5; 128 -7.8; 141 -8.0; 155 -8.2; 170 -8.3; 187 -8.5; 206 -8.6; 227 -8.5; 249 -8.4; 274 -8.3; 302 -8.2; 332 -7.9; 365 -7.6; 402 -7.4; 442 -7.1; 486 -6.8; 535 -6.5; 588 -6.2; 647 -5.9; 712 -5.6; 783 -5.3; 861 -5.2; 947 -5.5; 1042 -6.1; 1146 -7.2; 1261 -8.3; 1387 -8.9; 1526 -8.7; 1678 -7.4; 1846 -6.0; 2031 -5.9; 2234 -6.2; 2457 -4.8; 2703 -2.5; 2973 -0.9; 3270 -0.5; 3597 -1.1; 3957 -2.8; 4353 -5.5; 4788 -8.6; 5267 -8.0; 5793 -3.8; 6373 -1.1; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -9.1; 16529 -14.9; 18182 -10.2; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hum Dolores GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hum Dolores ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 1.34 | 4.0 dB   |
| Peaking | 1431 Hz  | 3.28 | -3.4 dB  |
| Peaking | 3208 Hz  | 3.08 | 6.2 dB   |
| Peaking | 15466 Hz | 0.47 | 2.6 dB   |
| Peaking | 16718 Hz | 1.61 | -12.1 dB |
| Peaking | 218 Hz   | 0.82 | -2.7 dB  |
| Peaking | 818 Hz   | 2.63 | 1.4 dB   |
| Peaking | 4990 Hz  | 6.1  | -5.4 dB  |
| Peaking | 6409 Hz  | 3.3  | 5.7 dB   |
| Peaking | 7839 Hz  | 2.03 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hum%20Dolores/Hum%20Dolores.png)