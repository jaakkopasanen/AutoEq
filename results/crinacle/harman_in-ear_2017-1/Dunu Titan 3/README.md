# Dunu Titan 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.7; 37 -0.8; 41 -1.0; 45 -1.2; 49 -1.4; 54 -1.7; 60 -2.0; 66 -2.3; 72 -2.7; 79 -3.1; 87 -3.6; 96 -4.1; 106 -4.6; 116 -5.1; 128 -5.6; 141 -6.0; 155 -6.4; 170 -6.8; 187 -7.2; 206 -7.4; 227 -7.6; 249 -7.9; 274 -8.0; 302 -8.2; 332 -8.2; 365 -6.8; 402 -8.1; 442 -8.2; 486 -8.2; 535 -8.0; 588 -7.7; 647 -7.4; 712 -6.8; 783 -6.2; 861 -5.9; 947 -5.8; 1042 -6.0; 1146 -6.7; 1261 -7.4; 1387 -7.8; 1526 -7.8; 1678 -7.8; 1846 -7.7; 2031 -7.7; 2234 -7.9; 2457 -8.4; 2703 -8.3; 2973 -7.2; 3270 -5.7; 3597 -4.9; 3957 -5.2; 4353 -6.8; 4788 -10.4; 5267 -11.3; 5793 -5.2; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.5; 15026 -16.3; 16529 -14.8; 18182 -14.7; 20000 -14.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu Titan 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.23 | 6.2 dB   |
| Peaking | 211 Hz   | 0.43 | -2.6 dB  |
| Peaking | 5186 Hz  | 4.71 | -10.1 dB |
| Peaking | 6081 Hz  | 1.98 | 7.1 dB   |
| Peaking | 17835 Hz | 0.6  | -9.7 dB  |
| Peaking | 920 Hz   | 2.9  | 1.9 dB   |
| Peaking | 2759 Hz  | 0.7  | -2.3 dB  |
| Peaking | 3626 Hz  | 2.78 | 3.6 dB   |
| Peaking | 12523 Hz | 2.07 | 4.7 dB   |
| Peaking | 14456 Hz | 3.03 | -6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.6 dB   |
| Peaking | 125 Hz   | 1.41 | 0.5 dB   |
| Peaking | 250 Hz   | 1.41 | -1.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | -11.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dunu%20Titan%203/Dunu%20Titan%203.png)