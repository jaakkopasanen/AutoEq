# Advanced GT3ef
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.7; 25 -7.8; 28 -7.8; 31 -7.8; 34 -7.8; 37 -7.8; 41 -7.7; 45 -7.7; 49 -7.7; 54 -7.6; 60 -7.6; 66 -7.7; 72 -8.0; 79 -8.1; 87 -8.2; 96 -8.5; 106 -8.6; 116 -8.8; 128 -9.0; 141 -9.1; 155 -9.2; 170 -9.3; 187 -9.3; 206 -9.2; 227 -9.1; 249 -8.9; 274 -8.7; 302 -8.4; 332 -8.0; 365 -7.5; 402 -7.2; 442 -6.8; 486 -6.3; 535 -5.8; 588 -5.2; 647 -4.7; 712 -4.0; 783 -3.4; 861 -2.9; 947 -2.7; 1042 -2.7; 1146 -3.1; 1261 -3.3; 1387 -3.1; 1526 -2.5; 1678 -1.9; 1846 -1.4; 2031 -1.0; 2234 -0.5; 2457 -0.7; 2703 -1.6; 2973 -3.2; 3270 -5.1; 3597 -6.2; 3957 -5.8; 4353 -5.6; 4788 -7.1; 5267 -9.6; 5793 -11.2; 6373 -8.6; 7010 -5.9; 7711 -7.9; 8482 -11.3; 9330 -10.0; 10263 -6.2; 11289 -6.1; 12418 -8.9; 13660 -20.7; 15026 -30.5; 16529 -32.9; 18182 -33.4; 20000 -37.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT3ef GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT3ef ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 243 Hz   | 0.4  | -7.6 dB  |
| Peaking | 2254 Hz  | 2.48 | 4.1 dB   |
| Peaking | 3636 Hz  | 0.09 | 19.3 dB  |
| Peaking | 17667 Hz | 0.83 | -20.5 dB |
| Peaking | 17829 Hz | 0.02 | -19.2 dB |
| Peaking | 27 Hz    | 1.37 | -1.5 dB  |
| Peaking | 5607 Hz  | 5.45 | -5.0 dB  |
| Peaking | 11723 Hz | 2.59 | 10.5 dB  |
| Peaking | 14867 Hz | 2.75 | -9.7 dB  |
| Peaking | 19942 Hz | 3.23 | -8.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 6.1 dB   |
| Peaking | 16000 Hz | 1.41 | -36.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20GT3ef/Advanced%20GT3ef.png)