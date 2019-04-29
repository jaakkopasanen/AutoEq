# KZ ZS5v1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.4; 25 -8.8; 28 -9.2; 31 -9.6; 34 -9.8; 37 -10.1; 41 -10.3; 45 -10.4; 49 -10.5; 54 -10.6; 60 -10.8; 66 -11.0; 72 -11.2; 79 -11.4; 87 -11.6; 96 -11.8; 106 -11.9; 116 -12.0; 128 -12.0; 141 -12.0; 155 -12.0; 170 -11.8; 187 -11.6; 206 -11.3; 227 -11.0; 249 -10.6; 274 -10.3; 302 -9.8; 332 -9.3; 365 -8.8; 402 -8.4; 442 -8.0; 486 -7.6; 535 -7.2; 588 -6.8; 647 -6.4; 712 -6.1; 783 -5.7; 861 -5.5; 947 -5.6; 1042 -6.1; 1146 -6.9; 1261 -7.4; 1387 -7.2; 1526 -7.8; 1678 -8.5; 1846 -9.4; 2031 -10.1; 2234 -9.8; 2457 -8.8; 2703 -7.8; 2973 -6.7; 3270 -4.0; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -6.5; 10263 -7.2; 11289 -9.8; 12418 -13.6; 13660 -18.1; 15026 -18.7; 16529 -17.1; 18182 -19.2; 20000 -24.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS5v1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS5v1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 70 Hz    | 0.37 | -3.9 dB  |
| Peaking | 191 Hz   | 0.69 | -3.1 dB  |
| Peaking | 2293 Hz  | 0.98 | -12.3 dB |
| Peaking | 4386 Hz  | 0.4  | 14.1 dB  |
| Peaking | 19916 Hz | 0.1  | -15.5 dB |
| Peaking | 816 Hz   | 4.95 | 0.9 dB   |
| Peaking | 7890 Hz  | 3.97 | -3.1 dB  |
| Peaking | 10675 Hz | 1.2  | 3.3 dB   |
| Peaking | 13842 Hz | 1.87 | -5.0 dB  |
| Peaking | 16872 Hz | 2.17 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -19.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20ZS5v1/KZ%20ZS5v1.png)