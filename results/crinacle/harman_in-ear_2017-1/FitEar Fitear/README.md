# FitEar Fitear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.2; 25 -9.3; 28 -9.3; 31 -9.4; 34 -9.5; 37 -9.6; 41 -9.8; 45 -9.9; 49 -10.0; 54 -10.2; 60 -10.4; 66 -10.7; 72 -11.0; 79 -11.3; 87 -11.7; 96 -12.1; 106 -12.3; 116 -12.7; 128 -12.9; 141 -13.1; 155 -13.3; 170 -13.4; 187 -13.4; 206 -13.4; 227 -13.3; 249 -13.1; 274 -13.0; 302 -12.7; 332 -12.2; 365 -11.8; 402 -11.5; 442 -11.1; 486 -10.6; 535 -10.1; 588 -9.5; 647 -8.9; 712 -8.3; 783 -7.7; 861 -7.1; 947 -6.7; 1042 -6.7; 1146 -6.9; 1261 -7.0; 1387 -6.7; 1526 -6.0; 1678 -5.0; 1846 -4.0; 2031 -2.9; 2234 -1.9; 2457 -1.2; 2703 -1.1; 2973 -1.3; 3270 -1.4; 3597 -0.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.2; 16529 -20.6; 18182 -12.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Fitear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Fitear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.12 | -2.3 dB  |
| Peaking | 219 Hz   | 0.45 | -5.7 dB  |
| Peaking | 2688 Hz  | 1.23 | 4.9 dB   |
| Peaking | 5176 Hz  | 1.57 | 5.6 dB   |
| Peaking | 16795 Hz | 2.52 | -16.0 dB |
| Peaking | 1378 Hz  | 6.41 | -1.0 dB  |
| Peaking | 6507 Hz  | 5.76 | 2.5 dB   |
| Peaking | 7625 Hz  | 2.74 | -2.0 dB  |
| Peaking | 13946 Hz | 4.71 | 3.1 dB   |
| Peaking | 22046 Hz | 2.03 | -0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.8 dB  |
| Peaking | 500 Hz   | 1.41 | -2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -10.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20Fitear/FitEar%20Fitear.png)