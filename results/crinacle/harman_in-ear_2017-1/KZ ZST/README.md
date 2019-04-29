# KZ ZST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.8; 25 -10.9; 28 -11.0; 31 -11.1; 34 -11.2; 37 -11.3; 41 -11.4; 45 -11.4; 49 -11.5; 54 -11.5; 60 -11.5; 66 -11.6; 72 -11.7; 79 -11.8; 87 -11.9; 96 -12.0; 106 -12.0; 116 -12.0; 128 -11.9; 141 -11.8; 155 -11.6; 170 -11.3; 187 -11.0; 206 -10.6; 227 -10.3; 249 -9.9; 274 -9.4; 302 -8.9; 332 -8.4; 365 -7.9; 402 -7.5; 442 -7.1; 486 -6.7; 535 -6.4; 588 -6.0; 647 -5.6; 712 -5.5; 783 -5.2; 861 -5.0; 947 -5.2; 1042 -5.7; 1146 -6.5; 1261 -7.2; 1387 -7.8; 1526 -8.2; 1678 -8.6; 1846 -9.3; 2031 -9.7; 2234 -9.1; 2457 -7.3; 2703 -5.5; 2973 -4.9; 3270 -5.7; 3597 -4.6; 3957 -0.7; 4353 -0.5; 4788 -0.9; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -10.9; 13660 -19.0; 15026 -23.8; 16529 -22.2; 18182 -21.3; 20000 -24.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.36 | -4.8 dB  |
| Peaking | 151 Hz   | 0.94 | -3.5 dB  |
| Peaking | 5154 Hz  | 0.86 | 13.3 dB  |
| Peaking | 11627 Hz | 0.77 | 20.8 dB  |
| Peaking | 14572 Hz | 0.31 | -30.2 dB |
| Peaking | 834 Hz   | 1.65 | 2.5 dB   |
| Peaking | 1977 Hz  | 3.06 | -2.7 dB  |
| Peaking | 4885 Hz  | 2.19 | 2.9 dB   |
| Peaking | 5094 Hz  | 6.17 | -5.3 dB  |
| Peaking | 14012 Hz | 6.51 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 16000 Hz | 1.41 | -23.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20ZST/KZ%20ZST.png)