# 64 Audio A6t M20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -9.0; 25 -9.4; 28 -9.8; 31 -10.0; 34 -10.2; 37 -10.4; 41 -10.5; 45 -10.6; 49 -10.7; 54 -10.7; 60 -10.7; 66 -10.8; 72 -10.8; 79 -10.8; 87 -10.9; 96 -10.9; 106 -10.9; 116 -10.9; 128 -10.8; 141 -10.7; 155 -10.5; 170 -10.3; 187 -10.1; 206 -9.9; 227 -9.6; 249 -9.4; 274 -9.2; 302 -9.0; 332 -8.9; 365 -8.8; 402 -8.6; 442 -8.6; 486 -8.5; 535 -8.3; 588 -8.1; 647 -7.7; 712 -7.1; 783 -6.5; 861 -5.9; 947 -5.4; 1042 -5.3; 1146 -5.5; 1261 -5.9; 1387 -6.1; 1526 -5.9; 1678 -5.5; 1846 -5.3; 2031 -5.3; 2234 -5.4; 2457 -5.1; 2703 -4.6; 2973 -3.9; 3270 -2.8; 3597 -2.2; 3957 -2.3; 4353 -3.0; 4788 -3.4; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.0; 16529 -12.6; 18182 -17.0; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A6t M20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A6t M20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.84 | -1.4 dB  |
| Peaking | 106 Hz   | 0.3  | -4.2 dB  |
| Peaking | 5250 Hz  | 0.75 | 5.9 dB   |
| Peaking | 14406 Hz | 1.05 | 9.4 dB   |
| Peaking | 17394 Hz | 0.38 | -12.8 dB |
| Peaking | 991 Hz   | 2.11 | 2.3 dB   |
| Peaking | 1950 Hz  | 0.37 | -2.2 dB  |
| Peaking | 2265 Hz  | 0.66 | 2.1 dB   |
| Peaking | 6206 Hz  | 5.2  | 2.9 dB   |
| Peaking | 7660 Hz  | 5.29 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20A6t%20M20/64%20Audio%20A6t%20M20.png)