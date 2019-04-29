# JH Audio 13v2 Min
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.3; 25 -3.3; 28 -3.3; 31 -3.4; 34 -3.6; 37 -3.9; 41 -4.3; 45 -4.6; 49 -4.9; 54 -5.1; 60 -5.4; 66 -5.7; 72 -5.9; 79 -6.4; 87 -6.9; 96 -7.3; 106 -7.7; 116 -8.0; 128 -8.3; 141 -8.5; 155 -8.8; 170 -8.9; 187 -8.9; 206 -8.9; 227 -8.9; 249 -8.8; 274 -8.7; 302 -8.5; 332 -8.4; 365 -8.1; 402 -7.9; 442 -7.7; 486 -7.4; 535 -7.0; 588 -6.6; 647 -6.3; 712 -5.8; 783 -5.4; 861 -5.2; 947 -5.1; 1042 -5.2; 1146 -5.2; 1261 -5.3; 1387 -5.6; 1526 -5.6; 1678 -5.3; 1846 -5.2; 2031 -5.5; 2234 -5.7; 2457 -5.9; 2703 -4.8; 2973 -2.1; 3270 -1.2; 3597 -1.4; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.0; 5793 -6.6; 6373 -7.8; 7010 -14.0; 7711 -17.7; 8482 -12.8; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.2; 16529 -13.6; 18182 -20.0; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JH Audio 13v2 Min GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JH Audio 13v2 Min ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 27 Hz    |  0.62 | 3.3 dB   |
| Peaking | 188 Hz   |  0.77 | -2.8 dB  |
| Peaking | 4307 Hz  |  1.13 | 7.0 dB   |
| Peaking | 7533 Hz  |  3.98 | -14.2 dB |
| Peaking | 18871 Hz |  1.22 | -16.0 dB |
| Peaking | 947 Hz   |  1.85 | 1.4 dB   |
| Peaking | 2542 Hz  |  3.97 | -2.1 dB  |
| Peaking | 3090 Hz  |  6.68 | 1.8 dB   |
| Peaking | 5857 Hz  | 11.64 | -2.2 dB  |
| Peaking | 13312 Hz |  1.71 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.0 dB |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/JH%20Audio%2013v2%20Min/JH%20Audio%2013v2%20Min.png)