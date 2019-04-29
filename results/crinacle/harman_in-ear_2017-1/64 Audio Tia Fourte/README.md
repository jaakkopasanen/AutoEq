# 64 Audio Tia Fourte
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.2; 25 -10.1; 28 -10.0; 31 -9.8; 34 -9.7; 37 -9.6; 41 -9.4; 45 -9.3; 49 -9.2; 54 -9.1; 60 -8.9; 66 -8.9; 72 -8.8; 79 -8.8; 87 -8.9; 96 -8.9; 106 -9.0; 116 -9.1; 128 -9.1; 141 -9.1; 155 -9.2; 170 -9.2; 187 -9.3; 206 -9.1; 227 -9.2; 249 -9.2; 274 -9.3; 302 -9.2; 332 -9.2; 365 -9.1; 402 -9.1; 442 -9.2; 486 -9.4; 535 -9.8; 588 -10.1; 647 -10.4; 712 -10.4; 783 -9.5; 861 -7.8; 947 -5.8; 1042 -4.2; 1146 -3.3; 1261 -3.1; 1387 -3.4; 1526 -3.7; 1678 -4.1; 1846 -4.7; 2031 -5.0; 2234 -5.0; 2457 -4.5; 2703 -3.6; 2973 -2.5; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -2.7; 5267 -5.1; 5793 -5.5; 6373 -4.8; 7010 -4.9; 7711 -7.4; 8482 -8.1; 9330 -6.7; 10263 -6.7; 11289 -8.0; 12418 -11.3; 13660 -19.4; 15026 -27.9; 16529 -32.4; 18182 -33.8; 20000 -30.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio Tia Fourte GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio Tia Fourte ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 60 Hz    | 0.04 | -2.8 dB  |
| Peaking | 717 Hz   | 1.33 | -4.2 dB  |
| Peaking | 1107 Hz  | 2.29 | 3.9 dB   |
| Peaking | 8187 Hz  | 0.21 | 21.2 dB  |
| Peaking | 17309 Hz | 0.24 | -40.5 dB |
| Peaking | 3942 Hz  | 3    | 3.3 dB   |
| Peaking | 5553 Hz  | 4.31 | -3.1 dB  |
| Peaking | 8114 Hz  | 3.93 | -3.9 dB  |
| Peaking | 11733 Hz | 1.5  | 5.3 dB   |
| Peaking | 14819 Hz | 2.56 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | -4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 16000 Hz | 1.41 | -34.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20Tia%20Fourte/64%20Audio%20Tia%20Fourte.png)