# Etymotic ER4XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.6; 25 -2.8; 28 -3.1; 31 -3.3; 34 -3.5; 37 -3.6; 41 -3.8; 45 -4.0; 49 -4.2; 54 -4.4; 60 -4.7; 66 -5.0; 72 -5.3; 79 -5.6; 87 -6.0; 96 -6.4; 106 -6.7; 116 -7.1; 128 -7.4; 141 -7.6; 155 -7.9; 170 -8.0; 187 -8.1; 206 -8.2; 227 -8.2; 249 -8.2; 274 -8.1; 302 -8.0; 332 -7.8; 365 -7.6; 402 -7.5; 442 -7.4; 486 -7.3; 535 -7.2; 588 -7.0; 647 -6.8; 712 -6.6; 783 -6.3; 861 -6.2; 947 -6.3; 1042 -7.0; 1146 -8.0; 1261 -8.9; 1387 -9.4; 1526 -9.4; 1678 -9.1; 1846 -8.8; 2031 -8.3; 2234 -7.6; 2457 -7.0; 2703 -6.4; 2973 -5.6; 3270 -4.9; 3597 -4.4; 3957 -4.1; 4353 -4.0; 4788 -3.6; 5267 -2.4; 5793 -0.5; 6373 -0.8; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -7.5; 10263 -6.6; 11289 -6.3; 12418 -6.3; 13660 -12.5; 15026 -27.6; 16529 -28.9; 18182 -14.9; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.24 | 3.9 dB   |
| Peaking | 198 Hz   | 0.68 | -2.3 dB  |
| Peaking | 1740 Hz  | 1.24 | -4.2 dB  |
| Peaking | 8143 Hz  | 0.37 | 5.6 dB   |
| Peaking | 15939 Hz | 1.81 | -29.8 dB |
| Peaking | 880 Hz   | 4.52 | 1.1 dB   |
| Peaking | 6141 Hz  | 3.1  | 5.7 dB   |
| Peaking | 7764 Hz  | 1.07 | -4.1 dB  |
| Peaking | 12979 Hz | 2.27 | 8.2 dB   |
| Peaking | 14656 Hz | 3.31 | -8.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB   |
| Peaking | 62 Hz    | 1.41 | 1.2 dB   |
| Peaking | 125 Hz   | 1.41 | -1.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 16000 Hz | 1.41 | -22.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Etymotic%20ER4XR/Etymotic%20ER4XR.png)