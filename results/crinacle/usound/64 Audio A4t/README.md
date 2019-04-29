# 64 Audio A4t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.0; 25 -6.3; 28 -6.6; 31 -6.9; 34 -7.0; 37 -7.1; 41 -7.3; 45 -7.4; 49 -7.4; 54 -7.4; 60 -7.4; 66 -7.5; 72 -7.6; 79 -7.6; 87 -7.6; 96 -7.7; 106 -7.7; 116 -7.6; 128 -7.4; 141 -7.3; 155 -7.1; 170 -6.8; 187 -6.4; 206 -6.0; 227 -5.6; 249 -5.3; 274 -4.9; 302 -4.5; 332 -4.2; 365 -3.9; 402 -3.7; 442 -3.6; 486 -3.6; 535 -3.6; 588 -3.7; 647 -3.8; 712 -3.8; 783 -3.7; 861 -3.7; 947 -3.9; 1042 -4.5; 1146 -5.4; 1261 -6.4; 1387 -7.2; 1526 -7.6; 1678 -7.7; 1846 -7.7; 2031 -7.9; 2234 -7.5; 2457 -5.5; 2703 -3.5; 2973 -1.8; 3270 -0.5; 3597 -1.2; 3957 -2.1; 4353 -2.6; 4788 -3.3; 5267 -2.9; 5793 -1.2; 6373 -1.5; 7010 -3.8; 7711 -4.4; 8482 -4.5; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -6.7; 15026 -10.5; 16529 -11.2; 18182 -11.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A4t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A4t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 70 Hz    | 0.53 | -3.4 dB |
| Peaking | 1941 Hz  | 1.78 | -4.6 dB |
| Peaking | 3293 Hz  | 2.13 | 4.8 dB  |
| Peaking | 6057 Hz  | 4.25 | 3.6 dB  |
| Peaking | 17238 Hz | 1.08 | -7.9 dB |
| Peaking | 170 Hz   | 1.56 | -1.1 dB |
| Peaking | 553 Hz   | 0.54 | 1.4 dB  |
| Peaking | 1369 Hz  | 3.66 | -1.8 dB |
| Peaking | 13083 Hz | 2.12 | 2.9 dB  |
| Peaking | 14541 Hz | 3.24 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -7.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20A4t/64%20Audio%20A4t.png)