# TFZ King Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.6; 25 -11.5; 28 -11.4; 31 -11.3; 34 -11.1; 37 -11.0; 41 -10.8; 45 -10.6; 49 -10.4; 54 -10.2; 60 -10.0; 66 -9.8; 72 -9.7; 79 -9.6; 87 -9.6; 96 -9.5; 106 -9.4; 116 -9.3; 128 -9.2; 141 -9.0; 155 -8.9; 170 -8.6; 187 -8.4; 206 -8.1; 227 -7.8; 249 -7.5; 274 -7.2; 302 -6.9; 332 -6.5; 365 -6.2; 402 -6.0; 442 -5.8; 486 -5.6; 535 -5.4; 588 -5.3; 647 -5.2; 712 -4.7; 783 -4.7; 861 -4.8; 947 -5.1; 1042 -5.9; 1146 -6.9; 1261 -7.8; 1387 -8.5; 1526 -9.0; 1678 -9.4; 1846 -9.7; 2031 -9.5; 2234 -8.4; 2457 -6.5; 2703 -4.6; 2973 -3.1; 3270 -1.4; 3597 -0.5; 3957 -1.7; 4353 -4.3; 4788 -5.6; 5267 -3.3; 5793 -1.0; 6373 -0.8; 7010 -3.8; 7711 -7.9; 8482 -8.3; 9330 -7.2; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -13.0; 16529 -20.8; 18182 -22.8; 20000 -20.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ King Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ King Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.34 | -5.2 dB  |
| Peaking | 134 Hz   | 1.28 | -1.8 dB  |
| Peaking | 4778 Hz  | 0.73 | 9.6 dB   |
| Peaking | 13674 Hz | 0.55 | 25.7 dB  |
| Peaking | 16616 Hz | 0.23 | -32.3 dB |
| Peaking | 822 Hz   | 1.19 | 2.9 dB   |
| Peaking | 1858 Hz  | 1.2  | -3.9 dB  |
| Peaking | 3468 Hz  | 1.85 | 5.5 dB   |
| Peaking | 4650 Hz  | 2.9  | -5.7 dB  |
| Peaking | 6135 Hz  | 5.3  | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -14.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%20King%20Pro/TFZ%20King%20Pro.png)