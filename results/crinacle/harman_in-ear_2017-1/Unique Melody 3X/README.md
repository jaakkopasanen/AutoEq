# Unique Melody 3X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.2; 25 -1.7; 28 -2.3; 31 -2.8; 34 -3.2; 37 -3.5; 41 -3.9; 45 -4.3; 49 -4.7; 54 -5.1; 60 -5.5; 66 -5.9; 72 -6.4; 79 -6.8; 87 -7.3; 96 -7.9; 106 -8.3; 116 -8.8; 128 -9.2; 141 -9.6; 155 -9.8; 170 -10.1; 187 -10.3; 206 -10.5; 227 -10.7; 249 -10.7; 274 -10.8; 302 -10.8; 332 -10.7; 365 -10.6; 402 -10.6; 442 -10.5; 486 -10.4; 535 -10.4; 588 -10.3; 647 -10.1; 712 -10.0; 783 -9.8; 861 -9.7; 947 -9.8; 1042 -10.2; 1146 -10.7; 1261 -10.9; 1387 -10.3; 1526 -9.0; 1678 -7.4; 1846 -5.5; 2031 -3.3; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.3; 6373 -7.9; 7010 -10.2; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.4; 15026 -15.4; 16529 -13.5; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody 3X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody 3X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.26 | 6.4 dB   |
| Peaking | 301 Hz   | 0.31 | -4.5 dB  |
| Peaking | 1335 Hz  | 1.7  | -5.1 dB  |
| Peaking | 2981 Hz  | 0.84 | 7.9 dB   |
| Peaking | 15490 Hz | 2.48 | -10.6 dB |
| Peaking | 2287 Hz  | 6.58 | 1.6 dB   |
| Peaking | 3103 Hz  | 2.4  | -1.3 dB  |
| Peaking | 5674 Hz  | 2.43 | 5.4 dB   |
| Peaking | 6692 Hz  | 4.19 | -9.0 dB  |
| Peaking | 12948 Hz | 5.43 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | -4.9 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -7.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Unique%20Melody%203X/Unique%20Melody%203X.png)