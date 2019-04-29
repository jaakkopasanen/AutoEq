# Advanced GT3 Superbass Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.2; 25 -11.4; 28 -11.5; 31 -11.6; 34 -11.6; 37 -11.6; 41 -11.5; 45 -11.4; 49 -11.3; 54 -11.2; 60 -11.2; 66 -11.2; 72 -11.2; 79 -11.3; 87 -11.4; 96 -11.7; 106 -11.8; 116 -12.0; 128 -12.1; 141 -12.3; 155 -12.4; 170 -12.5; 187 -12.6; 206 -12.5; 227 -12.5; 249 -12.5; 274 -12.5; 302 -12.3; 332 -12.1; 365 -11.8; 402 -11.7; 442 -11.5; 486 -11.1; 535 -11.1; 588 -10.7; 647 -10.2; 712 -9.6; 783 -9.1; 861 -8.7; 947 -8.3; 1042 -8.2; 1146 -8.1; 1261 -8.0; 1387 -7.4; 1526 -6.5; 1678 -5.3; 1846 -3.9; 2031 -2.4; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -2.0; 4353 -2.5; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.8; 15026 -26.2; 16529 -30.9; 18182 -31.1; 20000 -27.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3 Superbass Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3 Superbass Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.55 | -4.2 dB  |
| Peaking | 375 Hz   | 0.2  | -6.6 dB  |
| Peaking | 5255 Hz  | 0.31 | 18.0 dB  |
| Peaking | 12175 Hz | 1.76 | 13.7 dB  |
| Peaking | 16684 Hz | 0.25 | -32.3 dB |
| Peaking | 1404 Hz  | 2.61 | -2.0 dB  |
| Peaking | 2363 Hz  | 2.3  | 2.2 dB   |
| Peaking | 4277 Hz  | 3.63 | -3.1 dB  |
| Peaking | 6484 Hz  | 1.67 | 2.8 dB   |
| Peaking | 7617 Hz  | 4.01 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB  |
| Peaking | 500 Hz   | 1.41 | -3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 16000 Hz | 1.41 | -30.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20GT3%20Superbass%20Bass/Advanced%20GT3%20Superbass%20Bass.png)