# Etymotic ER4P
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.5; 25 -1.7; 28 -1.9; 31 -2.1; 34 -2.3; 37 -2.6; 41 -2.9; 45 -3.1; 49 -3.3; 54 -3.6; 60 -4.0; 66 -4.4; 72 -4.7; 79 -5.1; 87 -5.6; 96 -6.1; 106 -6.6; 116 -7.0; 128 -7.4; 141 -7.8; 155 -8.1; 170 -8.4; 187 -8.6; 206 -8.7; 227 -8.8; 249 -9.0; 274 -9.0; 302 -9.0; 332 -8.9; 365 -8.7; 402 -8.7; 442 -8.7; 486 -8.6; 535 -8.4; 588 -8.3; 647 -8.1; 712 -7.9; 783 -7.6; 861 -7.5; 947 -7.6; 1042 -8.1; 1146 -9.0; 1261 -9.8; 1387 -10.3; 1526 -10.3; 1678 -9.9; 1846 -9.4; 2031 -8.8; 2234 -8.0; 2457 -7.4; 2703 -6.8; 2973 -6.1; 3270 -5.3; 3597 -4.8; 3957 -4.2; 4353 -3.6; 4788 -2.5; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.1; 15026 -22.1; 16529 -22.4; 18182 -13.1; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4P GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.22 | 5.1 dB   |
| Peaking | 233 Hz   | 0.48 | -2.9 dB  |
| Peaking | 1557 Hz  | 1.58 | -3.9 dB  |
| Peaking | 5617 Hz  | 1.6  | 6.4 dB   |
| Peaking | 16090 Hz | 2.12 | -19.8 dB |
| Peaking | 920 Hz   | 4.36 | 0.6 dB   |
| Peaking | 1246 Hz  | 5.96 | -0.5 dB  |
| Peaking | 7790 Hz  | 5.44 | -1.9 dB  |
| Peaking | 13164 Hz | 2.4  | 5.7 dB   |
| Peaking | 14739 Hz | 4.15 | -6.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB   |
| Peaking | 62 Hz    | 1.41 | 1.8 dB   |
| Peaking | 125 Hz   | 1.41 | -0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 16000 Hz | 1.41 | -16.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Etymotic%20ER4P/Etymotic%20ER4P.png)