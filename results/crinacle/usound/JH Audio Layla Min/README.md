# JH Audio Layla Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.6; 25 -3.0; 28 -3.5; 31 -3.9; 34 -4.2; 37 -4.5; 41 -4.8; 45 -5.2; 49 -5.5; 54 -5.8; 60 -6.2; 66 -6.6; 72 -6.9; 79 -7.3; 87 -7.7; 96 -8.2; 106 -8.6; 116 -8.9; 128 -9.3; 141 -9.5; 155 -9.7; 170 -9.9; 187 -10.0; 206 -10.2; 227 -10.2; 249 -10.1; 274 -10.2; 302 -10.2; 332 -10.1; 365 -10.1; 402 -10.0; 442 -9.9; 486 -9.8; 535 -9.7; 588 -9.6; 647 -9.4; 712 -9.1; 783 -8.6; 861 -8.2; 947 -8.0; 1042 -8.5; 1146 -9.2; 1261 -9.4; 1387 -8.7; 1526 -7.2; 1678 -5.2; 1846 -3.1; 2031 -1.3; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.6; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.5; 6373 -1.7; 7010 -5.9; 7711 -9.8; 8482 -11.7; 9330 -9.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -13.0; 20000 -17.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio Layla Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio Layla Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.29 | 4.9 dB  |
| Peaking | 368 Hz   | 0.25 | -4.4 dB |
| Peaking | 1321 Hz  | 2.21 | -5.2 dB |
| Peaking | 3028 Hz  | 0.42 | 7.9 dB  |
| Peaking | 8399 Hz  | 3.11 | -9.0 dB |
| Peaking | 2166 Hz  | 3.56 | 1.9 dB  |
| Peaking | 3054 Hz  | 0.87 | -1.1 dB |
| Peaking | 5691 Hz  | 2.89 | 1.8 dB  |
| Peaking | 18990 Hz | 1.68 | -6.5 dB |
| Peaking | 19807 Hz | 1.58 | -7.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%20Layla%20Min/JH%20Audio%20Layla%20Min.png)