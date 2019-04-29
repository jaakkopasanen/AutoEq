# Kumitate KL-REF Type-S Half Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.2; 25 -9.3; 28 -9.4; 31 -9.4; 34 -9.4; 37 -9.4; 41 -9.4; 45 -9.4; 49 -9.3; 54 -9.3; 60 -9.2; 66 -9.2; 72 -9.3; 79 -9.3; 87 -9.5; 96 -9.6; 106 -9.7; 116 -9.7; 128 -9.8; 141 -9.8; 155 -9.8; 170 -9.7; 187 -9.6; 206 -9.5; 227 -9.3; 249 -9.1; 274 -8.9; 302 -8.7; 332 -8.5; 365 -8.4; 402 -8.5; 442 -8.4; 486 -8.2; 535 -8.1; 588 -7.8; 647 -7.6; 712 -7.3; 783 -7.0; 861 -6.8; 947 -6.9; 1042 -7.2; 1146 -7.8; 1261 -8.4; 1387 -8.6; 1526 -8.3; 1678 -7.8; 1846 -7.0; 2031 -5.9; 2234 -4.5; 2457 -3.1; 2703 -1.8; 2973 -0.6; 3270 -0.5; 3597 -0.6; 3957 -1.9; 4353 -4.1; 4788 -5.9; 5267 -4.7; 5793 -2.2; 6373 -2.2; 7010 -5.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.3; 16529 -11.5; 18182 -14.1; 20000 -14.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-REF Type-S Half Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-REF Type-S Half Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 80 Hz    | 0.17 | -3.2 dB |
| Peaking | 1710 Hz  | 1.29 | -4.6 dB |
| Peaking | 2947 Hz  | 0.91 | 7.0 dB  |
| Peaking | 19034 Hz | 0.9  | -9.2 dB |
| Peaking | 22050 Hz | 1.61 | 2.6 dB  |
| Peaking | 3750 Hz  | 2.06 | 3.5 dB  |
| Peaking | 4973 Hz  | 1.31 | -5.9 dB |
| Peaking | 6006 Hz  | 3.56 | 7.2 dB  |
| Peaking | 14593 Hz | 1.42 | 2.3 dB  |
| Peaking | 16861 Hz | 2.19 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -4.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-REF%20Type-S%20Half%20Bass/Kumitate%20KL-REF%20Type-S%20Half%20Bass.png)