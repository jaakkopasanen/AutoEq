# Dunu DN2002
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.6; 25 -9.7; 28 -9.8; 31 -9.9; 34 -10.0; 37 -10.1; 41 -10.3; 45 -10.4; 49 -10.5; 54 -10.6; 60 -10.8; 66 -11.0; 72 -11.2; 79 -11.4; 87 -11.7; 96 -11.9; 106 -12.1; 116 -12.3; 128 -12.4; 141 -12.4; 155 -12.5; 170 -12.4; 187 -12.3; 206 -12.2; 227 -12.0; 249 -11.8; 274 -11.6; 302 -11.3; 332 -11.0; 365 -10.7; 402 -10.4; 442 -10.2; 486 -9.9; 535 -9.6; 588 -9.2; 647 -8.9; 712 -8.4; 783 -7.9; 861 -7.4; 947 -7.0; 1042 -6.7; 1146 -6.8; 1261 -7.0; 1387 -6.7; 1526 -5.8; 1678 -4.7; 1846 -3.3; 2031 -1.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.2; 3597 -1.0; 3957 -0.5; 4353 -2.6; 4788 -4.8; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -14.2; 15026 -21.7; 16529 -19.0; 18182 -14.3; 20000 -17.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN2002 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2002 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 138 Hz   |  0.23 | -5.7 dB  |
| Peaking | 2917 Hz  |  0.94 | 8.3 dB   |
| Peaking | 6085 Hz  |  3.13 | 6.7 dB   |
| Peaking | 12674 Hz |  0.7  | 21.3 dB  |
| Peaking | 14772 Hz |  0.6  | -31.2 dB |
| Peaking | 20 Hz    |  2.31 | -1.2 dB  |
| Peaking | 2145 Hz  |  2.92 | 4.0 dB   |
| Peaking | 2164 Hz  |  1.36 | -2.7 dB  |
| Peaking | 4022 Hz  |  6.44 | 2.4 dB   |
| Peaking | 4747 Hz  | 10.29 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -16.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dunu%20DN2002/Dunu%20DN2002.png)