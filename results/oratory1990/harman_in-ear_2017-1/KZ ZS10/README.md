# KZ ZS10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -11.5; 25 -11.8; 28 -11.7; 31 -11.6; 34 -11.7; 37 -11.7; 41 -11.7; 45 -11.7; 49 -11.8; 54 -12.0; 60 -12.2; 66 -12.5; 72 -12.5; 79 -12.7; 87 -12.7; 96 -12.3; 106 -12.5; 116 -12.2; 128 -12.2; 141 -11.9; 155 -11.6; 170 -11.4; 187 -11.1; 206 -10.8; 227 -10.4; 249 -10.0; 274 -9.6; 302 -9.1; 332 -8.4; 365 -7.8; 402 -7.3; 442 -6.9; 486 -6.4; 535 -5.9; 588 -5.4; 647 -5.1; 712 -4.7; 783 -4.6; 861 -4.4; 947 -4.4; 1042 -5.0; 1146 -5.8; 1261 -6.6; 1387 -7.2; 1526 -7.7; 1678 -8.2; 1846 -9.0; 2031 -9.8; 2234 -9.6; 2457 -8.3; 2703 -6.9; 2973 -6.4; 3270 -6.0; 3597 -7.0; 3957 -5.2; 4353 -1.0; 4788 -0.5; 5267 -1.9; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.0; 13660 -17.0; 15026 -23.6; 16529 -23.3; 18182 -23.6; 20000 -25.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.23 | -4.8 dB  |
| Peaking | 200 Hz   | 0.41 | -3.1 dB  |
| Peaking | 2132 Hz  | 0.7  | -12.5 dB |
| Peaking | 7162 Hz  | 0.16 | 22.8 dB  |
| Peaking | 16690 Hz | 0.22 | -32.6 dB |
| Peaking | 3746 Hz  | 4.28 | -6.1 dB  |
| Peaking | 4215 Hz  | 1.8  | 3.9 dB   |
| Peaking | 7617 Hz  | 5.5  | -3.1 dB  |
| Peaking | 8820 Hz  | 5.27 | -1.6 dB  |
| Peaking | 12120 Hz | 5.6  | 5.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -23.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/KZ%20ZS10/KZ%20ZS10.png)