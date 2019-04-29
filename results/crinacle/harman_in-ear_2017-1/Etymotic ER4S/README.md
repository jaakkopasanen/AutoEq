# Etymotic ER4S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.8; 37 -1.0; 41 -1.3; 45 -1.5; 49 -1.7; 54 -2.0; 60 -2.4; 66 -2.8; 72 -3.2; 79 -3.6; 87 -4.1; 96 -4.6; 106 -5.1; 116 -5.4; 128 -5.8; 141 -6.3; 155 -6.6; 170 -6.9; 187 -7.1; 206 -7.3; 227 -7.4; 249 -7.5; 274 -7.6; 302 -7.6; 332 -7.5; 365 -7.4; 402 -7.4; 442 -7.4; 486 -7.3; 535 -7.2; 588 -7.1; 647 -7.0; 712 -6.8; 783 -6.7; 861 -6.6; 947 -6.9; 1042 -7.4; 1146 -8.4; 1261 -9.4; 1387 -10.0; 1526 -10.1; 1678 -10.0; 1846 -9.8; 2031 -9.5; 2234 -9.1; 2457 -8.8; 2703 -8.2; 2973 -7.3; 3270 -6.2; 3597 -5.4; 3957 -4.8; 4353 -4.2; 4788 -3.4; 5267 -2.2; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.3; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -14.6; 15026 -28.3; 16529 -27.9; 18182 -17.4; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.34 | 6.1 dB   |
| Peaking | 212 Hz   | 0.75 | -1.6 dB  |
| Peaking | 1980 Hz  | 0.95 | -5.5 dB  |
| Peaking | 9885 Hz  | 0.32 | 10.2 dB  |
| Peaking | 15819 Hz | 1.13 | -32.8 dB |
| Peaking | 869 Hz   | 4.45 | 1.0 dB   |
| Peaking | 6110 Hz  | 2.6  | 5.7 dB   |
| Peaking | 7744 Hz  | 1.07 | -4.6 dB  |
| Peaking | 12762 Hz | 2.51 | 7.4 dB   |
| Peaking | 14609 Hz | 4.32 | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.0 dB   |
| Peaking | 125 Hz   | 1.41 | 0.2 dB   |
| Peaking | 250 Hz   | 1.41 | -1.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 16000 Hz | 1.41 | -23.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Etymotic%20ER4S/Etymotic%20ER4S.png)