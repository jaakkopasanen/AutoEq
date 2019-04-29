# Tin Audio T3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -1.8; 31 -2.3; 34 -2.8; 37 -3.2; 41 -3.6; 45 -3.9; 49 -4.3; 54 -4.7; 60 -5.1; 66 -5.6; 72 -6.0; 79 -6.4; 87 -6.9; 96 -7.4; 106 -7.8; 116 -8.2; 128 -8.6; 141 -8.9; 155 -9.2; 170 -9.3; 187 -9.4; 206 -9.4; 227 -9.4; 249 -9.3; 274 -9.2; 302 -9.0; 332 -8.9; 365 -8.6; 402 -8.4; 442 -8.1; 486 -7.8; 535 -7.3; 588 -6.9; 647 -6.5; 712 -5.9; 783 -5.3; 861 -4.9; 947 -4.6; 1042 -4.7; 1146 -5.2; 1261 -5.7; 1387 -6.0; 1526 -6.0; 1678 -5.9; 1846 -5.7; 2031 -5.8; 2234 -6.1; 2457 -6.0; 2703 -4.3; 2973 -2.0; 3270 -1.1; 3597 -1.0; 3957 -1.3; 4353 -2.2; 4788 -3.5; 5267 -4.7; 5793 -4.5; 6373 -4.2; 7010 -7.5; 7711 -11.7; 8482 -9.2; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -8.3; 13660 -7.5; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.5  | 6.3 dB  |
| Peaking | 194 Hz   | 0.73 | -3.5 dB |
| Peaking | 3646 Hz  | 1.86 | 5.9 dB  |
| Peaking | 6377 Hz  | 4.96 | 2.4 dB  |
| Peaking | 7757 Hz  | 4.92 | -6.7 dB |
| Peaking | 417 Hz   | 2.03 | -0.8 dB |
| Peaking | 924 Hz   | 2.14 | 2.1 dB  |
| Peaking | 2384 Hz  | 6.57 | -1.5 dB |
| Peaking | 9368 Hz  | 5.29 | 0.8 dB  |
| Peaking | 12814 Hz | 4.83 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Tin%20Audio%20T3/Tin%20Audio%20T3.png)