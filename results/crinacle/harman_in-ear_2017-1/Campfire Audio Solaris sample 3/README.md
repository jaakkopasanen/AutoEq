# Campfire Audio Solaris sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.0; 25 -8.2; 28 -8.3; 31 -8.4; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.7; 49 -8.8; 54 -8.9; 60 -9.1; 66 -9.3; 72 -9.5; 79 -9.7; 87 -10.0; 96 -10.3; 106 -10.5; 116 -10.8; 128 -10.9; 141 -11.0; 155 -11.1; 170 -11.0; 187 -11.0; 206 -11.0; 227 -10.8; 249 -10.7; 274 -10.5; 302 -10.2; 332 -9.9; 365 -9.6; 402 -9.4; 442 -9.2; 486 -8.9; 535 -8.7; 588 -8.5; 647 -8.4; 712 -8.2; 783 -8.0; 861 -7.7; 947 -7.4; 1042 -7.1; 1146 -6.9; 1261 -6.7; 1387 -6.1; 1526 -5.4; 1678 -5.0; 1846 -5.1; 2031 -5.8; 2234 -6.2; 2457 -4.8; 2703 -2.3; 2973 -1.0; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.3; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.6; 11289 -6.5; 12418 -7.8; 13660 -14.9; 15026 -25.0; 16529 -31.7; 18182 -29.9; 20000 -17.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Solaris sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Solaris sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.11 | -1.1 dB  |
| Peaking | 206 Hz   | 0.33 | -3.8 dB  |
| Peaking | 5043 Hz  | 0.71 | 11.7 dB  |
| Peaking | 12001 Hz | 1.31 | 14.1 dB  |
| Peaking | 16725 Hz | 0.46 | -30.0 dB |
| Peaking | 2275 Hz  | 4.56 | -2.7 dB  |
| Peaking | 2883 Hz  | 5.34 | 1.5 dB   |
| Peaking | 3493 Hz  | 0.87 | 0.8 dB   |
| Peaking | 4594 Hz  | 3.93 | -1.4 dB  |
| Peaking | 18456 Hz | 5.14 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 16000 Hz | 1.41 | -28.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Campfire%20Audio%20Solaris%20sample%203/Campfire%20Audio%20Solaris%20sample%203.png)