# Whizzer A15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.8; 25 -6.1; 28 -6.4; 31 -6.7; 34 -7.0; 37 -7.2; 41 -7.4; 45 -7.7; 49 -7.9; 54 -8.1; 60 -8.5; 66 -8.8; 72 -9.1; 79 -9.5; 87 -9.9; 96 -10.3; 106 -10.7; 116 -11.0; 128 -11.3; 141 -11.6; 155 -11.8; 170 -11.9; 187 -11.9; 206 -11.8; 227 -11.7; 249 -11.4; 274 -11.2; 302 -10.8; 332 -10.3; 365 -9.8; 402 -9.3; 442 -8.7; 486 -8.1; 535 -7.4; 588 -6.7; 647 -5.7; 712 -4.9; 783 -4.3; 861 -3.8; 947 -3.6; 1042 -3.7; 1146 -4.1; 1261 -4.5; 1387 -4.4; 1526 -3.8; 1678 -3.1; 1846 -2.2; 2031 -1.2; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.9; 3597 -1.6; 3957 -2.5; 4353 -3.8; 4788 -5.6; 5267 -7.8; 5793 -7.6; 6373 -5.4; 7010 -5.7; 7711 -9.1; 8482 -8.9; 9330 -6.6; 10263 -6.5; 11289 -7.4; 12418 -10.9; 13660 -18.7; 15026 -26.4; 16529 -28.3; 18182 -25.7; 20000 -19.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Whizzer A15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Whizzer A15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 105 Hz   | 0.84 | -1.5 dB  |
| Peaking | 216 Hz   | 0.56 | -4.9 dB  |
| Peaking | 819 Hz   | 1.86 | 2.9 dB   |
| Peaking | 2746 Hz  | 0.8  | 6.5 dB   |
| Peaking | 17226 Hz | 0.92 | -24.1 dB |
| Peaking | 17 Hz    | 2.12 | 1.3 dB   |
| Peaking | 5308 Hz  | 5.48 | -3.0 dB  |
| Peaking | 11185 Hz | 1.94 | 6.5 dB   |
| Peaking | 14841 Hz | 2.69 | -8.0 dB  |
| Peaking | 15196 Hz | 1.22 | -0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -27.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Whizzer%20A15/Whizzer%20A15.png)