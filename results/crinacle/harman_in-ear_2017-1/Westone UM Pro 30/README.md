# Westone UM Pro 30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.7; 25 -8.8; 28 -9.0; 31 -9.2; 34 -9.3; 37 -9.5; 41 -9.6; 45 -9.7; 49 -9.8; 54 -10.0; 60 -10.3; 66 -10.6; 72 -10.9; 79 -11.2; 87 -11.5; 96 -12.0; 106 -12.4; 116 -12.7; 128 -12.9; 141 -13.2; 155 -13.4; 170 -13.5; 187 -13.5; 206 -13.5; 227 -13.4; 249 -13.2; 274 -13.1; 302 -12.8; 332 -12.4; 365 -11.9; 402 -11.6; 442 -11.2; 486 -10.7; 535 -10.2; 588 -9.7; 647 -9.2; 712 -8.6; 783 -8.0; 861 -7.6; 947 -7.5; 1042 -7.7; 1146 -8.3; 1261 -8.9; 1387 -9.0; 1526 -8.6; 1678 -7.9; 1846 -6.9; 2031 -5.0; 2234 -2.2; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.2; 9330 -8.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -10.8; 16529 -11.2; 18182 -15.7; 20000 -18.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM Pro 30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM Pro 30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 43 Hz    |  0.31 | -2.3 dB  |
| Peaking | 130 Hz   |  0.8  | -2.4 dB  |
| Peaking | 281 Hz   |  0.56 | -5.3 dB  |
| Peaking | 1526 Hz  |  2    | -4.4 dB  |
| Peaking | 3358 Hz  |  0.8  | 7.4 dB   |
| Peaking | 872 Hz   |  4.76 | 0.4 dB   |
| Peaking | 2395 Hz  | 10    | 1.8 dB   |
| Peaking | 6010 Hz  |  3.81 | 3.3 dB   |
| Peaking | 8791 Hz  |  4.53 | -3.8 dB  |
| Peaking | 19445 Hz |  0.73 | -12.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20UM%20Pro%2030/Westone%20UM%20Pro%2030.png)