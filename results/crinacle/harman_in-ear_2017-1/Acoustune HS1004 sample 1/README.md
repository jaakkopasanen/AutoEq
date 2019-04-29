# Acoustune HS1004 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.3; 25 -7.5; 28 -7.8; 31 -8.0; 34 -8.2; 37 -8.3; 41 -8.5; 45 -8.6; 49 -8.8; 54 -8.9; 60 -9.1; 66 -9.3; 72 -9.5; 79 -9.7; 87 -9.9; 96 -10.1; 106 -10.3; 116 -10.4; 128 -10.4; 141 -10.4; 155 -10.4; 170 -10.2; 187 -10.1; 206 -9.8; 227 -9.5; 249 -9.2; 274 -8.9; 302 -8.5; 332 -8.0; 365 -7.5; 402 -7.2; 442 -6.9; 486 -6.6; 535 -6.3; 588 -6.0; 647 -5.7; 712 -5.5; 783 -5.2; 861 -5.1; 947 -5.2; 1042 -5.5; 1146 -6.0; 1261 -6.7; 1387 -7.3; 1526 -7.4; 1678 -7.4; 1846 -7.3; 2031 -6.8; 2234 -5.4; 2457 -3.3; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -4.6; 5267 -6.5; 5793 -9.7; 6373 -10.4; 7010 -6.4; 7711 -6.3; 8482 -10.0; 9330 -10.5; 10263 -6.6; 11289 -6.5; 12418 -6.7; 13660 -17.1; 15026 -26.0; 16529 -25.9; 18182 -24.1; 20000 -25.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1004 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1004 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 120 Hz   | 0.49 | -4.0 dB  |
| Peaking | 6134 Hz  | 3.92 | -10.2 dB |
| Peaking | 8861 Hz  | 3.49 | -13.0 dB |
| Peaking | 9178 Hz  | 0.46 | 22.7 dB  |
| Peaking | 16292 Hz | 0.41 | -31.0 dB |
| Peaking | 790 Hz   | 0.84 | 2.5 dB   |
| Peaking | 1877 Hz  | 1.19 | -4.9 dB  |
| Peaking | 3049 Hz  | 1.26 | 6.0 dB   |
| Peaking | 10567 Hz | 0.02 | -1.3 dB  |
| Peaking | 12341 Hz | 5.4  | 5.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 16000 Hz | 1.41 | -24.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Acoustune%20HS1004%20sample%201/Acoustune%20HS1004%20sample%201.png)