# 64 Audio A12t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.9; 25 -10.2; 28 -10.4; 31 -10.6; 34 -10.7; 37 -10.8; 41 -10.8; 45 -10.8; 49 -10.8; 54 -10.7; 60 -10.6; 66 -10.6; 72 -10.7; 79 -10.6; 87 -10.6; 96 -10.7; 106 -10.6; 116 -10.5; 128 -10.4; 141 -10.3; 155 -10.1; 170 -9.9; 187 -9.7; 206 -9.4; 227 -9.2; 249 -9.0; 274 -8.8; 302 -8.7; 332 -8.5; 365 -8.4; 402 -8.5; 442 -8.6; 486 -8.6; 535 -8.6; 588 -8.6; 647 -8.3; 712 -7.9; 783 -7.4; 861 -6.9; 947 -6.6; 1042 -6.7; 1146 -7.1; 1261 -7.5; 1387 -7.6; 1526 -7.4; 1678 -7.3; 1846 -7.3; 2031 -7.3; 2234 -6.7; 2457 -4.7; 2703 -2.2; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -1.6; 4353 -2.8; 4788 -4.8; 5267 -4.0; 5793 -1.5; 6373 -3.5; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -18.4; 15026 -30.0; 16529 -36.5; 18182 -36.6; 20000 -20.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A12t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A12t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.31 | -3.5 dB  |
| Peaking | 407 Hz   | 0.14 | -2.2 dB  |
| Peaking | 4841 Hz  | 0.46 | 15.4 dB  |
| Peaking | 11828 Hz | 1.2  | 18.6 dB  |
| Peaking | 16599 Hz | 0.33 | -38.6 dB |
| Peaking | 2148 Hz  | 1.89 | -4.9 dB  |
| Peaking | 2890 Hz  | 1.36 | 4.9 dB   |
| Peaking | 4986 Hz  | 3.27 | -5.7 dB  |
| Peaking | 5671 Hz  | 3.54 | 3.4 dB   |
| Peaking | 18136 Hz | 4.85 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 9.6 dB   |
| Peaking | 16000 Hz | 1.41 | -36.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20A12t/64%20Audio%20A12t.png)