# JH Audio Angie Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.4; 25 -1.7; 28 -2.2; 31 -2.6; 34 -3.0; 37 -3.4; 41 -3.9; 45 -4.3; 49 -4.6; 54 -5.0; 60 -5.4; 66 -5.9; 72 -6.4; 79 -6.9; 87 -7.4; 96 -8.0; 106 -8.4; 116 -8.8; 128 -9.2; 141 -9.6; 155 -9.9; 170 -10.1; 187 -10.2; 206 -10.3; 227 -10.4; 249 -10.4; 274 -10.4; 302 -10.4; 332 -10.3; 365 -10.1; 402 -10.1; 442 -10.0; 486 -9.8; 535 -9.7; 588 -9.5; 647 -9.4; 712 -9.2; 783 -9.0; 861 -8.9; 947 -9.5; 1042 -10.6; 1146 -11.9; 1261 -12.6; 1387 -12.5; 1526 -11.5; 1678 -9.7; 1846 -7.3; 2031 -4.6; 2234 -2.2; 2457 -0.6; 2703 -0.5; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.7; 8482 -9.0; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.6; 15026 -15.6; 16529 -23.1; 18182 -29.4; 20000 -30.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Angie Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Angie Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.25 | 6.0 dB   |
| Peaking | 349 Hz   | 0.27 | -5.1 dB  |
| Peaking | 1387 Hz  | 1.46 | -11.2 dB |
| Peaking | 7526 Hz  | 0.13 | 12.9 dB  |
| Peaking | 18789 Hz | 0.34 | -32.8 dB |
| Peaking | 6183 Hz  | 4.45 | 1.9 dB   |
| Peaking | 8297 Hz  | 3.21 | -5.4 dB  |
| Peaking | 13433 Hz | 1.79 | 6.3 dB   |
| Peaking | 15274 Hz | 2.16 | -3.1 dB  |
| Peaking | 17007 Hz | 3.03 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB   |
| Peaking | 62 Hz    | 1.41 | 0.4 dB   |
| Peaking | 125 Hz   | 1.41 | -2.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -18.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%20Angie%20Min/JH%20Audio%20Angie%20Min.png)