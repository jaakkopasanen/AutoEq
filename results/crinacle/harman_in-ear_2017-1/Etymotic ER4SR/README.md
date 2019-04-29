# Etymotic ER4SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -0.9; 34 -1.2; 37 -1.4; 41 -1.7; 45 -2.0; 49 -2.2; 54 -2.5; 60 -2.9; 66 -3.2; 72 -3.6; 79 -4.1; 87 -4.5; 96 -5.1; 106 -5.5; 116 -5.9; 128 -6.4; 141 -6.7; 155 -7.1; 170 -7.4; 187 -7.5; 206 -7.7; 227 -7.8; 249 -7.9; 274 -8.0; 302 -8.0; 332 -7.9; 365 -7.8; 402 -7.7; 442 -7.7; 486 -7.7; 535 -7.7; 588 -7.5; 647 -7.4; 712 -7.2; 783 -7.0; 861 -6.9; 947 -7.1; 1042 -7.7; 1146 -8.7; 1261 -9.7; 1387 -10.3; 1526 -10.2; 1678 -10.0; 1846 -9.7; 2031 -9.2; 2234 -8.6; 2457 -8.0; 2703 -7.3; 2973 -6.5; 3270 -5.8; 3597 -5.2; 3957 -4.7; 4353 -4.2; 4788 -3.2; 5267 -1.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.3; 15026 -27.1; 16529 -25.3; 18182 -9.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 1.01 | 6.1 dB   |
| Peaking | 58 Hz    | 1.68 | 2.7 dB   |
| Peaking | 1596 Hz  | 1.13 | -3.9 dB  |
| Peaking | 5749 Hz  | 1.51 | 6.3 dB   |
| Peaking | 15789 Hz | 2.69 | -25.3 dB |
| Peaking | 285 Hz   | 0.88 | -1.6 dB  |
| Peaking | 907 Hz   | 3.69 | 1.2 dB   |
| Peaking | 7803 Hz  | 4.93 | -2.0 dB  |
| Peaking | 13034 Hz | 2.37 | 7.9 dB   |
| Peaking | 14525 Hz | 3.27 | -9.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB   |
| Peaking | 62 Hz    | 1.41 | 2.7 dB   |
| Peaking | 125 Hz   | 1.41 | -0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 16000 Hz | 1.41 | -19.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Etymotic%20ER4SR/Etymotic%20ER4SR.png)