# Acoustune HS1004 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.6; 25 -7.0; 28 -7.6; 31 -8.0; 34 -8.4; 37 -8.7; 41 -9.1; 45 -9.4; 49 -9.7; 54 -10.0; 60 -10.3; 66 -10.6; 72 -10.9; 79 -11.2; 87 -11.5; 96 -11.7; 106 -12.0; 116 -12.1; 128 -12.2; 141 -12.2; 155 -12.1; 170 -12.0; 187 -11.8; 206 -11.5; 227 -11.2; 249 -10.8; 274 -10.4; 302 -10.0; 332 -9.4; 365 -8.9; 402 -8.5; 442 -8.0; 486 -7.6; 535 -7.1; 588 -6.7; 647 -6.3; 712 -5.9; 783 -5.5; 861 -5.2; 947 -5.4; 1042 -5.9; 1146 -6.8; 1261 -7.5; 1387 -7.8; 1526 -7.7; 1678 -7.2; 1846 -6.3; 2031 -4.9; 2234 -3.0; 2457 -0.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -2.8; 5267 -3.5; 5793 -4.6; 6373 -5.8; 7010 -5.0; 7711 -6.2; 8482 -8.8; 9330 -9.2; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -17.2; 15026 -25.9; 16529 -26.5; 18182 -25.3; 20000 -26.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1004 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1004 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 57 Hz    | 0.92 | -1.4 dB  |
| Peaking | 150 Hz   | 0.52 | -5.5 dB  |
| Peaking | 8574 Hz  | 2.11 | -11.1 dB |
| Peaking | 9317 Hz  | 0.42 | 23.7 dB  |
| Peaking | 16468 Hz | 0.38 | -32.7 dB |
| Peaking | 1618 Hz  | 1.26 | -9.4 dB  |
| Peaking | 2120 Hz  | 0.55 | 6.5 dB   |
| Peaking | 5884 Hz  | 2.24 | -3.8 dB  |
| Peaking | 12357 Hz | 8.46 | 4.9 dB   |
| Peaking | 20025 Hz | 1.68 | -6.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 16000 Hz | 1.41 | -25.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Acoustune%20HS1004%20sample%202/Acoustune%20HS1004%20sample%202.png)