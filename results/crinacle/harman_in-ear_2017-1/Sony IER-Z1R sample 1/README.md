# Sony IER-Z1R sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -9.1; 25 -9.4; 28 -9.6; 31 -9.8; 34 -10.0; 37 -10.1; 41 -10.2; 45 -10.4; 49 -10.5; 54 -10.5; 60 -10.6; 66 -10.7; 72 -10.8; 79 -11.0; 87 -11.1; 96 -11.2; 106 -11.2; 116 -11.2; 128 -11.1; 141 -11.0; 155 -10.8; 170 -10.5; 187 -10.2; 206 -9.8; 227 -9.4; 249 -9.0; 274 -8.6; 302 -8.3; 332 -7.9; 365 -7.7; 402 -7.5; 442 -7.4; 486 -7.3; 535 -7.2; 588 -7.2; 647 -7.0; 712 -6.9; 783 -6.9; 861 -6.7; 947 -6.8; 1042 -7.1; 1146 -7.6; 1261 -8.1; 1387 -8.2; 1526 -7.9; 1678 -7.3; 1846 -6.3; 2031 -5.0; 2234 -3.4; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -2.9; 3597 -4.6; 3957 -4.4; 4353 -4.3; 4788 -2.9; 5267 -2.0; 5793 -3.3; 6373 -4.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.0; 10263 -6.7; 11289 -7.7; 12418 -10.9; 13660 -17.2; 15026 -25.0; 16529 -29.9; 18182 -28.4; 20000 -17.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-Z1R sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-Z1R sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.68 | -2.2 dB  |
| Peaking | 114 Hz   | 0.48 | -4.4 dB  |
| Peaking | 2751 Hz  | 3.37 | 5.9 dB   |
| Peaking | 9595 Hz  | 0.46 | 13.0 dB  |
| Peaking | 16750 Hz | 0.5  | -30.3 dB |
| Peaking | 1406 Hz  | 2.71 | -2.4 dB  |
| Peaking | 5294 Hz  | 4.74 | 2.8 dB   |
| Peaking | 8703 Hz  | 2.69 | -2.4 dB  |
| Peaking | 11814 Hz | 2.15 | 2.7 dB   |
| Peaking | 14713 Hz | 3.66 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 16000 Hz | 1.41 | -28.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20IER-Z1R%20sample%201/Sony%20IER-Z1R%20sample%201.png)