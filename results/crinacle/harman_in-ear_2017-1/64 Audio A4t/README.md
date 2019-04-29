# 64 Audio A4t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -9.1; 25 -9.4; 28 -9.7; 31 -10.0; 34 -10.1; 37 -10.2; 41 -10.4; 45 -10.5; 49 -10.5; 54 -10.5; 60 -10.5; 66 -10.6; 72 -10.7; 79 -10.7; 87 -10.7; 96 -10.8; 106 -10.8; 116 -10.7; 128 -10.5; 141 -10.4; 155 -10.2; 170 -9.9; 187 -9.5; 206 -9.1; 227 -8.7; 249 -8.4; 274 -8.0; 302 -7.5; 332 -7.1; 365 -6.7; 402 -6.5; 442 -6.4; 486 -6.3; 535 -6.3; 588 -6.3; 647 -6.4; 712 -6.4; 783 -6.4; 861 -6.4; 947 -6.7; 1042 -7.3; 1146 -8.1; 1261 -8.8; 1387 -9.3; 1526 -9.5; 1678 -9.5; 1846 -9.5; 2031 -9.3; 2234 -8.3; 2457 -5.8; 2703 -3.4; 2973 -1.5; 3270 -0.5; 3597 -1.1; 3957 -2.4; 4353 -3.4; 4788 -4.4; 5267 -4.0; 5793 -2.1; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -17.4; 15026 -28.8; 16529 -32.0; 18182 -29.5; 20000 -18.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A4t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A4t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 74 Hz    | 0.31 | -4.4 dB  |
| Peaking | 1689 Hz  | 0.9  | -10.9 dB |
| Peaking | 4501 Hz  | 0.28 | 15.9 dB  |
| Peaking | 12135 Hz | 1.54 | 15.1 dB  |
| Peaking | 15922 Hz | 0.39 | -34.7 dB |
| Peaking | 2197 Hz  | 6.17 | -2.0 dB  |
| Peaking | 3184 Hz  | 2.92 | 2.8 dB   |
| Peaking | 4828 Hz  | 2.36 | -3.3 dB  |
| Peaking | 6153 Hz  | 4.11 | 3.3 dB   |
| Peaking | 14506 Hz | 9.35 | -2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 16000 Hz | 1.41 | -30.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20A4t/64%20Audio%20A4t.png)