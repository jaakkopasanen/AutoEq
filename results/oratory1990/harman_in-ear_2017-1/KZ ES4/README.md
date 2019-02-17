# KZ ES4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.4; 23 -16.0; 25 -16.2; 28 -16.0; 31 -15.9; 34 -15.9; 37 -15.8; 41 -15.8; 45 -15.7; 49 -15.6; 54 -15.7; 60 -15.8; 66 -16.0; 72 -15.8; 79 -16.0; 87 -15.7; 96 -15.3; 106 -15.4; 116 -14.9; 128 -14.9; 141 -14.4; 155 -14.1; 170 -13.8; 187 -13.4; 206 -13.0; 227 -12.6; 249 -12.1; 274 -11.7; 302 -11.1; 332 -10.5; 365 -9.9; 402 -9.4; 442 -9.0; 486 -8.5; 535 -8.0; 588 -7.6; 647 -7.2; 712 -6.8; 783 -6.4; 861 -6.2; 947 -6.2; 1042 -6.8; 1146 -7.5; 1261 -8.3; 1387 -8.9; 1526 -9.3; 1678 -9.8; 1846 -10.6; 2031 -11.4; 2234 -11.8; 2457 -11.1; 2703 -9.5; 2973 -8.1; 3270 -8.2; 3597 -9.5; 3957 -8.8; 4353 -3.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.7; 11289 -7.8; 12418 -11.2; 13660 -18.1; 15026 -22.7; 16529 -25.1; 18182 -28.7; 20000 -27.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ES4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ES4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.13 | -9.5 dB  |
| Peaking | 2246 Hz  | 0.67 | -18.4 dB |
| Peaking | 3769 Hz  | 4.36 | -8.1 dB  |
| Peaking | 4696 Hz  | 0.26 | 21.7 dB  |
| Peaking | 18054 Hz | 0.24 | -27.2 dB |
| Peaking | 1330 Hz  | 6.02 | -0.9 dB  |
| Peaking | 6361 Hz  | 1.92 | 2.1 dB   |
| Peaking | 7629 Hz  | 2.44 | -4.6 dB  |
| Peaking | 11698 Hz | 1.59 | 4.4 dB   |
| Peaking | 14150 Hz | 2.53 | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.6 dB  |
| Peaking | 62 Hz    | 1.41 | -6.9 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 16000 Hz | 1.41 | -27.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ES4/KZ%20ES4.png)