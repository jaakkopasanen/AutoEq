# Westone UM Pro 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -5.9; 25 -6.0; 28 -6.2; 31 -6.3; 34 -6.5; 37 -6.6; 41 -6.7; 45 -6.9; 49 -7.1; 54 -7.3; 60 -7.5; 66 -7.8; 72 -8.2; 79 -8.5; 87 -9.0; 96 -9.5; 106 -9.9; 116 -10.3; 128 -10.6; 141 -10.9; 155 -11.3; 170 -11.5; 187 -11.7; 206 -11.8; 227 -11.8; 249 -11.9; 274 -11.9; 302 -11.8; 332 -11.6; 365 -11.4; 402 -11.2; 442 -11.1; 486 -10.8; 535 -10.6; 588 -10.3; 647 -10.0; 712 -9.6; 783 -9.3; 861 -9.0; 947 -8.9; 1042 -9.1; 1146 -9.4; 1261 -9.7; 1387 -9.5; 1526 -8.7; 1678 -7.5; 1846 -6.2; 2031 -4.8; 2234 -3.3; 2457 -1.9; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -16.6; 18182 -25.8; 20000 -23.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM Pro 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM Pro 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 146 Hz   | 0.84 | -2.3 dB  |
| Peaking | 352 Hz   | 0.47 | -4.6 dB  |
| Peaking | 1460 Hz  | 1.26 | -5.5 dB  |
| Peaking | 3363 Hz  | 0.5  | 7.6 dB   |
| Peaking | 18913 Hz | 1.16 | -22.8 dB |
| Peaking | 23 Hz    | 1.07 | 0.8 dB   |
| Peaking | 6318 Hz  | 3.3  | 3.2 dB   |
| Peaking | 7618 Hz  | 2.34 | -3.4 dB  |
| Peaking | 14346 Hz | 3.15 | 5.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -9.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20UM%20Pro%2010/Westone%20UM%20Pro%2010.png)