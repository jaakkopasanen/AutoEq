# InEar PhoPhile-8 Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.6; 25 -5.9; 28 -6.2; 31 -6.4; 34 -6.6; 37 -6.8; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.5; 60 -7.8; 66 -8.1; 72 -8.4; 79 -8.6; 87 -8.8; 96 -9.2; 106 -9.4; 116 -9.6; 128 -9.7; 141 -9.7; 155 -9.6; 170 -9.5; 187 -9.2; 206 -8.9; 227 -8.6; 249 -8.2; 274 -7.9; 302 -7.5; 332 -7.1; 365 -6.8; 402 -6.6; 442 -6.4; 486 -6.2; 535 -6.1; 588 -5.9; 647 -5.7; 712 -5.5; 783 -5.3; 861 -5.1; 947 -5.2; 1042 -5.6; 1146 -6.3; 1261 -6.9; 1387 -7.0; 1526 -6.6; 1678 -6.0; 1846 -5.2; 2031 -4.1; 2234 -2.8; 2457 -1.5; 2703 -0.6; 2973 -0.5; 3270 -1.0; 3597 -1.0; 3957 -0.8; 4353 -0.7; 4788 -1.4; 5267 -3.3; 5793 -4.8; 6373 -3.1; 7010 -3.1; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -7.6; 15026 -16.3; 16529 -22.4; 18182 -25.4; 20000 -22.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`InEar PhoPhile-8 Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar PhoPhile-8 Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 95 Hz    | 0.62 | -2.9 dB  |
| Peaking | 179 Hz   | 1    | -2.3 dB  |
| Peaking | 3693 Hz  | 0.72 | 9.3 dB   |
| Peaking | 12605 Hz | 0.42 | 25.5 dB  |
| Peaking | 17049 Hz | 0.19 | -34.6 dB |
| Peaking | 930 Hz   | 1.18 | 2.3 dB   |
| Peaking | 1341 Hz  | 1.8  | -2.0 dB  |
| Peaking | 2133 Hz  | 0.26 | -0.9 dB  |
| Peaking | 2582 Hz  | 2.96 | 2.3 dB   |
| Peaking | 6811 Hz  | 7.64 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -18.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/InEar%20PhoPhile-8%20Bass/InEar%20PhoPhile-8%20Bass.png)