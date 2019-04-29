# JH Audio Layla Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.8; 25 -4.2; 28 -4.7; 31 -5.1; 34 -5.4; 37 -5.6; 41 -6.0; 45 -6.4; 49 -6.7; 54 -7.0; 60 -7.3; 66 -7.7; 72 -8.1; 79 -8.5; 87 -8.9; 96 -9.3; 106 -9.7; 116 -10.1; 128 -10.4; 141 -10.7; 155 -10.8; 170 -11.0; 187 -11.2; 206 -11.3; 227 -11.3; 249 -11.2; 274 -11.3; 302 -11.2; 332 -11.1; 365 -10.9; 402 -10.8; 442 -10.7; 486 -10.6; 535 -10.4; 588 -10.2; 647 -10.0; 712 -9.7; 783 -9.3; 861 -8.9; 947 -8.8; 1042 -9.3; 1146 -9.9; 1261 -9.9; 1387 -8.8; 1526 -7.2; 1678 -5.1; 1846 -2.9; 2031 -0.8; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -10.0; 9330 -10.1; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -10.2; 15026 -18.4; 16529 -24.7; 18182 -29.5; 20000 -28.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Layla Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Layla Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.52 | 4.1 dB   |
| Peaking | 363 Hz   | 0.27 | -6.0 dB  |
| Peaking | 1258 Hz  | 1.83 | -6.4 dB  |
| Peaking | 7388 Hz  | 0.14 | 12.8 dB  |
| Peaking | 18526 Hz | 0.33 | -31.7 dB |
| Peaking | 3495 Hz  | 3.39 | -0.8 dB  |
| Peaking | 6159 Hz  | 3.7  | 2.2 dB   |
| Peaking | 8678 Hz  | 2.74 | -7.0 dB  |
| Peaking | 12916 Hz | 1.37 | 7.6 dB   |
| Peaking | 15460 Hz | 1.51 | -6.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB   |
| Peaking | 62 Hz    | 1.41 | -0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -21.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JH%20Audio%20Layla%20Min/JH%20Audio%20Layla%20Min.png)