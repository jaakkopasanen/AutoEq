# Acoustune HS1004
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.2; 28 -7.7; 31 -8.0; 34 -8.3; 37 -8.5; 41 -8.8; 45 -9.0; 49 -9.2; 54 -9.4; 60 -9.7; 66 -9.9; 72 -10.2; 79 -10.4; 87 -10.7; 96 -10.9; 106 -11.1; 116 -11.2; 128 -11.3; 141 -11.3; 155 -11.3; 170 -11.1; 187 -10.9; 206 -10.7; 227 -10.3; 249 -10.0; 274 -9.7; 302 -9.2; 332 -8.7; 365 -8.2; 402 -7.8; 442 -7.5; 486 -7.1; 535 -6.7; 588 -6.4; 647 -6.0; 712 -5.7; 783 -5.3; 861 -5.2; 947 -5.3; 1042 -5.7; 1146 -6.4; 1261 -7.1; 1387 -7.5; 1526 -7.6; 1678 -7.3; 1846 -6.8; 2031 -5.8; 2234 -4.2; 2457 -2.1; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -3.7; 5267 -5.0; 5793 -7.1; 6373 -8.1; 7010 -5.7; 7711 -6.2; 8482 -9.4; 9330 -9.9; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -17.2; 15026 -25.9; 16529 -26.2; 18182 -24.7; 20000 -25.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Acoustune HS1004 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Acoustune HS1004 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 100 Hz   | 0.47 | -3.8 dB  |
| Peaking | 198 Hz   | 0.85 | -1.9 dB  |
| Peaking | 8795 Hz  | 1.92 | -12.6 dB |
| Peaking | 9750 Hz  | 0.44 | 26.7 dB  |
| Peaking | 16302 Hz | 0.37 | -34.1 dB |
| Peaking | 1737 Hz  | 1.19 | -9.5 dB  |
| Peaking | 2383 Hz  | 0.57 | 7.3 dB   |
| Peaking | 5888 Hz  | 3    | -5.9 dB  |
| Peaking | 12351 Hz | 9.38 | 4.5 dB   |
| Peaking | 19955 Hz | 1.54 | -6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -25.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Acoustune%20HS1004/Acoustune%20HS1004.png)