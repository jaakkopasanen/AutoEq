# TFZ Ti Galaxy
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -12.2; 25 -12.2; 28 -12.1; 31 -12.1; 34 -12.0; 37 -11.9; 41 -11.8; 45 -11.6; 49 -11.4; 54 -11.3; 60 -11.2; 66 -11.1; 72 -11.1; 79 -11.0; 87 -11.0; 96 -10.9; 106 -10.9; 116 -10.8; 128 -10.6; 141 -10.6; 155 -10.4; 170 -10.1; 187 -9.8; 206 -9.5; 227 -9.2; 249 -8.9; 274 -8.5; 302 -8.1; 332 -7.7; 365 -7.3; 402 -7.0; 442 -6.8; 486 -6.5; 535 -6.3; 588 -6.0; 647 -6.1; 712 -5.9; 783 -5.6; 861 -5.7; 947 -6.0; 1042 -6.7; 1146 -7.7; 1261 -8.6; 1387 -9.2; 1526 -9.5; 1678 -9.7; 1846 -9.7; 2031 -8.9; 2234 -7.3; 2457 -5.2; 2703 -3.5; 2973 -2.5; 3270 -2.8; 3597 -4.2; 3957 -6.1; 4353 -5.5; 4788 -2.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -19.7; 16529 -26.2; 18182 -22.0; 20000 -13.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Ti Galaxy GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Ti Galaxy ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.17 | -5.7 dB  |
| Peaking | 155 Hz   | 0.93 | -2.2 dB  |
| Peaking | 5740 Hz  | 1.34 | 8.9 dB   |
| Peaking | 13110 Hz | 1.06 | 16.6 dB  |
| Peaking | 16213 Hz | 0.64 | -27.9 dB |
| Peaking | 852 Hz   | 1.2  | 2.5 dB   |
| Peaking | 1817 Hz  | 0.89 | -5.5 dB  |
| Peaking | 2689 Hz  | 2.79 | 1.6 dB   |
| Peaking | 3044 Hz  | 1.41 | 5.4 dB   |
| Peaking | 4101 Hz  | 4.65 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 16000 Hz | 1.41 | -19.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%20Ti%20Galaxy/TFZ%20Ti%20Galaxy.png)