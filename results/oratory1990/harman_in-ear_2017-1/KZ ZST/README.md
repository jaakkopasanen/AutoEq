# KZ ZST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.3; 25 -9.5; 28 -9.7; 31 -9.9; 34 -10.0; 37 -10.0; 41 -10.1; 45 -10.2; 49 -10.2; 54 -10.3; 60 -10.3; 66 -10.4; 72 -10.5; 79 -10.5; 87 -10.6; 96 -10.6; 106 -10.6; 116 -10.5; 128 -10.3; 141 -10.0; 155 -10.0; 170 -10.4; 187 -10.0; 206 -9.6; 227 -9.2; 249 -8.8; 274 -8.4; 302 -7.9; 332 -7.4; 365 -6.9; 402 -6.6; 442 -6.3; 486 -5.9; 535 -5.6; 588 -5.4; 647 -5.2; 712 -5.0; 783 -5.0; 861 -5.4; 947 -5.5; 1042 -6.1; 1146 -6.6; 1261 -7.1; 1387 -7.4; 1526 -7.9; 1678 -8.6; 1846 -9.3; 2031 -9.2; 2234 -7.7; 2457 -6.2; 2703 -4.4; 2973 -4.0; 3270 -4.7; 3597 -4.1; 3957 -0.8; 4353 -0.5; 4788 -0.7; 5267 -5.6; 5793 -5.3; 6373 -6.7; 7010 -7.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -12.0; 11289 -15.3; 12418 -16.3; 13660 -21.1; 15026 -25.1; 16529 -21.1; 18182 -13.6; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 57 Hz    | 0.32 | -3.8 dB  |
| Peaking | 185 Hz   | 1.02 | -1.7 dB  |
| Peaking | 1877 Hz  | 0.95 | -11.1 dB |
| Peaking | 2583 Hz  | 0.36 | 9.2 dB   |
| Peaking | 15048 Hz | 0.98 | -20.0 dB |
| Peaking | 3440 Hz  | 6.36 | -3.1 dB  |
| Peaking | 4381 Hz  | 2.26 | 5.4 dB   |
| Peaking | 5677 Hz  | 1.54 | -4.4 dB  |
| Peaking | 9419 Hz  | 2.4  | 4.4 dB   |
| Peaking | 10628 Hz | 4.17 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -23.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZST/KZ%20ZST.png)