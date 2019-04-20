# AKG K601 (Dekoni Fenestrated Sheepskin Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.4; 31 -3.0; 34 -3.5; 37 -3.9; 41 -4.4; 45 -4.9; 49 -5.3; 54 -5.7; 60 -6.1; 66 -6.5; 72 -6.9; 79 -7.3; 87 -7.8; 96 -8.2; 106 -8.5; 116 -8.9; 128 -9.2; 141 -9.6; 155 -9.9; 170 -10.1; 187 -10.2; 206 -10.3; 227 -10.4; 249 -10.2; 274 -10.0; 302 -9.5; 332 -8.9; 365 -8.3; 402 -7.9; 442 -7.3; 486 -6.6; 535 -5.9; 588 -5.2; 647 -4.4; 712 -3.8; 783 -3.7; 861 -4.4; 947 -5.6; 1042 -6.2; 1146 -6.5; 1261 -6.7; 1387 -6.6; 1526 -6.7; 1678 -7.2; 1846 -7.8; 2031 -8.8; 2234 -9.7; 2457 -9.8; 2703 -8.5; 2973 -4.8; 3270 -0.7; 3597 -0.7; 3957 -0.8; 4353 -2.0; 4788 -5.2; 5267 -7.1; 5793 -8.0; 6373 -6.2; 7010 -5.6; 7711 -7.5; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -7.8; 12418 -9.0; 13660 -6.7; 15026 -6.7; 16529 -10.2; 18182 -14.3; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 (Dekoni Fenestrated Sheepskin Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 (Dekoni Fenestrated Sheepskin Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.92 | 6.2 dB  |
| Peaking | 186 Hz   | 1.03 | -4.1 dB |
| Peaking | 2457 Hz  | 2.92 | -5.5 dB |
| Peaking | 3528 Hz  | 2.38 | 7.9 dB  |
| Peaking | 18862 Hz | 1.05 | -8.6 dB |
| Peaking | 305 Hz   | 2.75 | -1.2 dB |
| Peaking | 726 Hz   | 2.28 | 3.5 dB  |
| Peaking | 5576 Hz  | 8.04 | -2.6 dB |
| Peaking | 12104 Hz | 6.71 | -2.5 dB |
| Peaking | 14801 Hz | 2.94 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K601%20(Dekoni%20Fenestrated%20Sheepskin%20Earpads)/AKG%20K601%20(Dekoni%20Fenestrated%20Sheepskin%20Earpads).png)