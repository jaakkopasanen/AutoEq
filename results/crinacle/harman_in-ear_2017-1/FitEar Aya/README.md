# FitEar Aya
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.5; 28 -7.7; 31 -7.9; 34 -8.1; 37 -8.2; 41 -8.4; 45 -8.6; 49 -8.7; 54 -8.9; 60 -9.1; 66 -9.4; 72 -9.8; 79 -10.1; 87 -10.5; 96 -10.9; 106 -11.2; 116 -11.5; 128 -11.8; 141 -12.1; 155 -12.2; 170 -12.3; 187 -12.4; 206 -12.3; 227 -12.2; 249 -12.1; 274 -11.9; 302 -11.6; 332 -11.2; 365 -10.7; 402 -10.3; 442 -9.9; 486 -9.5; 535 -9.0; 588 -8.5; 647 -8.0; 712 -7.4; 783 -6.8; 861 -6.3; 947 -6.1; 1042 -6.2; 1146 -6.6; 1261 -6.7; 1387 -6.5; 1526 -6.0; 1678 -5.2; 1846 -4.3; 2031 -3.3; 2234 -2.4; 2457 -1.9; 2703 -1.3; 2973 -1.3; 3270 -2.7; 3597 -3.9; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -3.0; 6373 -5.2; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.2; 15026 -17.5; 16529 -10.2; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Aya GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Aya ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 126 Hz   | 0.48 | -4.1 dB  |
| Peaking | 275 Hz   | 0.76 | -3.1 dB  |
| Peaking | 2565 Hz  | 1.76 | 4.8 dB   |
| Peaking | 4699 Hz  | 2.33 | 5.8 dB   |
| Peaking | 15116 Hz | 3.38 | -12.4 dB |
| Peaking | 33 Hz    | 1.85 | -0.4 dB  |
| Peaking | 907 Hz   | 3.59 | 1.0 dB   |
| Peaking | 1326 Hz  | 4.59 | -0.7 dB  |
| Peaking | 12740 Hz | 6.72 | 2.1 dB   |
| Peaking | 17549 Hz | 6.4  | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -7.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20Aya/FitEar%20Aya.png)