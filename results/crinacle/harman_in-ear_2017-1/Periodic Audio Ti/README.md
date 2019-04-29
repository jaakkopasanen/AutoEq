# Periodic Audio Ti
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.2; 25 -7.6; 28 -8.2; 31 -8.6; 34 -8.9; 37 -9.2; 41 -9.5; 45 -9.8; 49 -10.1; 54 -10.3; 60 -10.5; 66 -10.8; 72 -11.1; 79 -11.4; 87 -11.6; 96 -11.9; 106 -12.1; 116 -12.2; 128 -12.2; 141 -12.2; 155 -12.2; 170 -11.9; 187 -11.6; 206 -11.3; 227 -10.9; 249 -10.4; 274 -9.8; 302 -9.3; 332 -8.7; 365 -8.1; 402 -7.5; 442 -6.8; 486 -6.1; 535 -5.4; 588 -4.6; 647 -3.8; 712 -3.0; 783 -2.2; 861 -1.6; 947 -1.2; 1042 -1.0; 1146 -0.9; 1261 -0.8; 1387 -0.5; 1526 -0.8; 1678 -1.7; 1846 -1.8; 2031 -1.1; 2234 -0.6; 2457 -0.7; 2703 -1.4; 2973 -2.8; 3270 -4.1; 3597 -4.8; 3957 -5.2; 4353 -6.3; 4788 -8.5; 5267 -9.1; 5793 -5.7; 6373 -1.9; 7010 -3.1; 7711 -5.3; 8482 -6.2; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -6.2; 13660 -17.9; 15026 -26.3; 16529 -27.5; 18182 -25.6; 20000 -18.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Ti GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Ti ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 424 Hz   | 0.11 | -9.1 dB  |
| Peaking | 4296 Hz  | 4.9  | 6.7 dB   |
| Peaking | 4497 Hz  | 1.42 | -18.4 dB |
| Peaking | 5494 Hz  | 0.15 | 27.2 dB  |
| Peaking | 16399 Hz | 0.36 | -38.7 dB |
| Peaking | 883 Hz   | 2.21 | 1.2 dB   |
| Peaking | 1780 Hz  | 5.17 | -1.8 dB  |
| Peaking | 8473 Hz  | 5.13 | -2.7 dB  |
| Peaking | 12299 Hz | 2.73 | 7.0 dB   |
| Peaking | 14305 Hz | 3.28 | -7.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 16000 Hz | 1.41 | -27.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Periodic%20Audio%20Ti/Periodic%20Audio%20Ti.png)