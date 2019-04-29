# Etymotic ER4S custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.3; 60 -1.8; 66 -2.4; 72 -2.8; 79 -3.3; 87 -3.9; 96 -4.4; 106 -4.9; 116 -5.5; 128 -5.9; 141 -6.3; 155 -6.6; 170 -6.8; 187 -7.1; 206 -7.4; 227 -7.5; 249 -7.6; 274 -7.7; 302 -7.7; 332 -7.6; 365 -7.5; 402 -7.6; 442 -7.5; 486 -7.5; 535 -7.5; 588 -7.4; 647 -7.3; 712 -7.2; 783 -7.0; 861 -7.1; 947 -7.4; 1042 -8.1; 1146 -9.2; 1261 -10.3; 1387 -11.1; 1526 -11.5; 1678 -11.7; 1846 -11.8; 2031 -11.7; 2234 -11.1; 2457 -9.9; 2703 -8.1; 2973 -6.4; 3270 -5.3; 3597 -5.0; 3957 -5.3; 4353 -6.1; 4788 -6.0; 5267 -3.8; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.9; 11289 -7.3; 12418 -10.6; 13660 -23.0; 15026 -32.2; 16529 -26.4; 18182 -12.8; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4S custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4S custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.68 | 6.8 dB   |
| Peaking | 1726 Hz  | 1.32 | -5.9 dB  |
| Peaking | 6325 Hz  | 1.27 | 7.7 dB   |
| Peaking | 11686 Hz | 3.13 | 9.2 dB   |
| Peaking | 15155 Hz | 1.47 | -29.3 dB |
| Peaking | 270 Hz   | 1.06 | -1.5 dB  |
| Peaking | 2402 Hz  | 2.73 | -2.9 dB  |
| Peaking | 3023 Hz  | 1.28 | 2.7 dB   |
| Peaking | 4664 Hz  | 4.78 | -3.0 dB  |
| Peaking | 9297 Hz  | 9.91 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.6 dB   |
| Peaking | 125 Hz   | 1.41 | 0.1 dB   |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -26.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Etymotic%20ER4S%20custom/Etymotic%20ER4S%20custom.png)