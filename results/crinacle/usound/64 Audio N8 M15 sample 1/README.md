# 64 Audio N8 M15 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.0; 25 -9.0; 28 -8.9; 31 -8.8; 34 -8.6; 37 -8.5; 41 -8.4; 45 -8.2; 49 -8.0; 54 -7.8; 60 -7.6; 66 -7.5; 72 -7.5; 79 -7.4; 87 -7.3; 96 -7.2; 106 -7.1; 116 -7.0; 128 -6.8; 141 -6.7; 155 -6.5; 170 -6.3; 187 -6.0; 206 -5.7; 227 -5.4; 249 -5.1; 274 -4.8; 302 -4.6; 332 -4.3; 365 -4.1; 402 -3.9; 442 -3.8; 486 -3.6; 535 -3.5; 588 -3.4; 647 -3.2; 712 -3.0; 783 -2.7; 861 -2.4; 947 -2.3; 1042 -2.4; 1146 -3.0; 1261 -3.7; 1387 -4.2; 1526 -4.2; 1678 -3.8; 1846 -3.4; 2031 -3.1; 2234 -2.8; 2457 -2.2; 2703 -1.4; 2973 -0.8; 3270 -0.6; 3597 -1.1; 3957 -1.9; 4353 -2.4; 4788 -3.5; 5267 -3.7; 5793 -0.5; 6373 -0.5; 7010 -2.8; 7711 -3.4; 8482 -3.6; 9330 -4.3; 10263 -3.7; 11289 -3.7; 12418 -3.7; 13660 -3.7; 15026 -4.4; 16529 -10.7; 18182 -14.6; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.24 | -5.3 dB  |
| Peaking | 143 Hz   | 1.01 | -1.7 dB  |
| Peaking | 3367 Hz  | 1.17 | 2.6 dB   |
| Peaking | 14741 Hz | 1.09 | 4.6 dB   |
| Peaking | 17787 Hz | 0.9  | -12.9 dB |
| Peaking | 1008 Hz  | 1.5  | 2.4 dB   |
| Peaking | 1357 Hz  | 1.47 | -2.1 dB  |
| Peaking | 3059 Hz  | 4.04 | 0.8 dB   |
| Peaking | 5149 Hz  | 3.38 | -2.7 dB  |
| Peaking | 5987 Hz  | 4.54 | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -6.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20M15%20sample%201/64%20Audio%20N8%20M15%20sample%201.png)