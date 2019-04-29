# PEARS SH3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.3; 25 -1.7; 28 -2.3; 31 -2.7; 34 -3.1; 37 -3.4; 41 -3.8; 45 -4.1; 49 -4.4; 54 -4.7; 60 -5.1; 66 -5.5; 72 -6.0; 79 -6.4; 87 -6.9; 96 -7.4; 106 -7.9; 116 -8.2; 128 -8.6; 141 -9.0; 155 -9.3; 170 -9.5; 187 -9.7; 206 -9.7; 227 -9.8; 249 -9.8; 274 -9.8; 302 -9.7; 332 -9.4; 365 -9.2; 402 -9.0; 442 -8.8; 486 -8.5; 535 -8.2; 588 -7.8; 647 -7.5; 712 -7.0; 783 -6.5; 861 -6.1; 947 -5.9; 1042 -6.1; 1146 -6.6; 1261 -7.1; 1387 -7.4; 1526 -7.5; 1678 -7.6; 1846 -7.5; 2031 -6.0; 2234 -3.8; 2457 -1.9; 2703 -1.0; 2973 -1.1; 3270 -1.8; 3597 -2.8; 3957 -3.6; 4353 -3.9; 4788 -3.6; 5267 -2.5; 5793 -0.5; 6373 -0.7; 7010 -3.8; 7711 -5.9; 8482 -6.1; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -7.4; 13660 -15.6; 15026 -20.6; 16529 -12.1; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`PEARS SH3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PEARS SH3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.28 | 6.0 dB   |
| Peaking | 222 Hz   | 0.49 | -3.9 dB  |
| Peaking | 2901 Hz  | 2.64 | 5.6 dB   |
| Peaking | 5988 Hz  | 2.88 | 6.0 dB   |
| Peaking | 14944 Hz | 2.81 | -16.3 dB |
| Peaking | 898 Hz   | 3.41 | 1.2 dB   |
| Peaking | 1657 Hz  | 3.33 | -2.1 dB  |
| Peaking | 12037 Hz | 3.59 | 3.1 dB   |
| Peaking | 13779 Hz | 4.9  | -3.4 dB  |
| Peaking | 17865 Hz | 3.11 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB   |
| Peaking | 62 Hz    | 1.41 | 0.6 dB   |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -11.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/PEARS%20SH3/PEARS%20SH3.png)