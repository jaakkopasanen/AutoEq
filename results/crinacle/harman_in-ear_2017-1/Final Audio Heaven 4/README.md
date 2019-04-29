# Final Audio Heaven 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.2; 25 -6.3; 28 -6.5; 31 -6.7; 34 -6.8; 37 -6.9; 41 -7.0; 45 -7.2; 49 -7.3; 54 -7.6; 60 -7.9; 66 -8.2; 72 -8.5; 79 -8.9; 87 -9.3; 96 -9.8; 106 -10.1; 116 -10.5; 128 -10.8; 141 -11.1; 155 -11.3; 170 -11.5; 187 -11.6; 206 -11.5; 227 -11.5; 249 -11.4; 274 -11.3; 302 -11.0; 332 -10.7; 365 -10.3; 402 -10.0; 442 -9.7; 486 -9.2; 535 -8.8; 588 -8.3; 647 -7.7; 712 -7.1; 783 -6.5; 861 -6.0; 947 -5.7; 1042 -5.8; 1146 -6.2; 1261 -6.4; 1387 -6.2; 1526 -5.6; 1678 -4.8; 1846 -4.0; 2031 -3.3; 2234 -2.6; 2457 -2.5; 2703 -2.9; 2973 -3.4; 3270 -3.0; 3597 -1.9; 3957 -0.9; 4353 -0.5; 4788 -1.0; 5267 -2.3; 5793 -4.1; 6373 -4.8; 7010 -5.8; 7711 -6.1; 8482 -6.3; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -8.4; 15026 -18.0; 16529 -15.2; 18182 -6.6; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 154 Hz   | 0.67 | -4.4 dB  |
| Peaking | 334 Hz   | 1.03 | -2.6 dB  |
| Peaking | 2263 Hz  | 1.83 | 3.2 dB   |
| Peaking | 4373 Hz  | 1.85 | 5.8 dB   |
| Peaking | 15519 Hz | 2.88 | -13.9 dB |
| Peaking | 15 Hz    | 1.09 | 1.0 dB   |
| Peaking | 900 Hz   | 2.3  | 2.4 dB   |
| Peaking | 925 Hz   | 1.15 | -1.3 dB  |
| Peaking | 13177 Hz | 3.32 | 3.2 dB   |
| Peaking | 14418 Hz | 5.85 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -9.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20Heaven%204/Final%20Audio%20Heaven%204.png)