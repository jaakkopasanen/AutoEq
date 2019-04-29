# Sony IER-M9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.1; 25 -8.4; 28 -8.7; 31 -9.0; 34 -9.2; 37 -9.4; 41 -9.6; 45 -9.8; 49 -9.9; 54 -10.1; 60 -10.3; 66 -10.5; 72 -10.7; 79 -10.9; 87 -11.1; 96 -11.3; 106 -11.5; 116 -11.5; 128 -11.6; 141 -11.6; 155 -11.5; 170 -11.4; 187 -11.3; 206 -11.1; 227 -10.9; 249 -10.7; 274 -10.4; 302 -10.1; 332 -9.7; 365 -9.3; 402 -9.0; 442 -8.7; 486 -8.4; 535 -8.0; 588 -7.7; 647 -7.3; 712 -6.9; 783 -6.4; 861 -6.1; 947 -6.1; 1042 -6.4; 1146 -6.9; 1261 -7.3; 1387 -7.3; 1526 -6.8; 1678 -6.3; 1846 -5.5; 2031 -4.6; 2234 -3.2; 2457 -1.5; 2703 -0.5; 2973 -0.5; 3270 -3.4; 3597 -5.2; 3957 -4.0; 4353 -3.7; 4788 -3.9; 5267 -2.3; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.7; 13660 -18.6; 15026 -28.4; 16529 -32.9; 18182 -28.4; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 58 Hz    | 0.41 | -2.5 dB  |
| Peaking | 182 Hz   | 0.5  | -3.9 dB  |
| Peaking | 2702 Hz  | 3.72 | 5.2 dB   |
| Peaking | 9288 Hz  | 0.44 | 14.1 dB  |
| Peaking | 16404 Hz | 0.65 | -34.6 dB |
| Peaking | 1399 Hz  | 4.68 | -1.4 dB  |
| Peaking | 6118 Hz  | 2.89 | 6.3 dB   |
| Peaking | 7604 Hz  | 1.27 | -4.7 dB  |
| Peaking | 11903 Hz | 2.42 | 5.4 dB   |
| Peaking | 14661 Hz | 3.61 | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.9 dB   |
| Peaking | 16000 Hz | 1.41 | -30.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20IER-M9/Sony%20IER-M9.png)