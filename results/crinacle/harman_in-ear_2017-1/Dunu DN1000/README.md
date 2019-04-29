# Dunu DN1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.7; 25 -3.9; 28 -4.1; 31 -4.3; 34 -4.5; 37 -4.6; 41 -4.8; 45 -5.0; 49 -5.2; 54 -5.4; 60 -5.8; 66 -6.1; 72 -6.4; 79 -6.8; 87 -7.3; 96 -7.7; 106 -8.2; 116 -8.6; 128 -8.9; 141 -9.3; 155 -9.6; 170 -9.8; 187 -10.0; 206 -10.1; 227 -10.1; 249 -10.2; 274 -10.1; 302 -10.0; 332 -9.8; 365 -9.6; 402 -9.4; 442 -9.2; 486 -8.9; 535 -8.6; 588 -8.2; 647 -7.8; 712 -7.3; 783 -6.7; 861 -6.2; 947 -6.0; 1042 -6.0; 1146 -6.3; 1261 -6.4; 1387 -6.1; 1526 -5.5; 1678 -4.6; 1846 -3.8; 2031 -2.9; 2234 -2.0; 2457 -1.5; 2703 -1.5; 2973 -1.7; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -1.9; 4788 -4.5; 5267 -4.6; 5793 -3.7; 6373 -3.9; 7010 -5.3; 7711 -9.2; 8482 -10.1; 9330 -8.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -14.7; 16529 -17.1; 18182 -14.5; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.28 | 3.1 dB   |
| Peaking | 226 Hz   | 0.54 | -4.0 dB  |
| Peaking | 2354 Hz  | 1.61 | 3.8 dB   |
| Peaking | 3824 Hz  | 1.8  | 5.2 dB   |
| Peaking | 17517 Hz | 0.91 | -10.7 dB |
| Peaking | 903 Hz   | 4.99 | 1.0 dB   |
| Peaking | 6556 Hz  | 4.54 | 3.0 dB   |
| Peaking | 8157 Hz  | 3.15 | -4.8 dB  |
| Peaking | 13728 Hz | 1.18 | 5.0 dB   |
| Peaking | 15450 Hz | 2.74 | -7.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB   |
| Peaking | 62 Hz    | 1.41 | 0.7 dB   |
| Peaking | 125 Hz   | 1.41 | -2.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -10.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dunu%20DN1000/Dunu%20DN1000.png)