# 64 Audio N8 M15 sample 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.2; 25 -10.4; 28 -10.5; 31 -10.5; 34 -10.5; 37 -10.5; 41 -10.4; 45 -10.4; 49 -10.3; 54 -10.2; 60 -10.1; 66 -10.1; 72 -10.1; 79 -10.2; 87 -10.3; 96 -10.3; 106 -10.2; 116 -10.3; 128 -10.2; 141 -10.1; 155 -9.9; 170 -9.7; 187 -9.6; 206 -9.4; 227 -9.2; 249 -8.9; 274 -8.7; 302 -8.4; 332 -8.0; 365 -7.7; 402 -7.5; 442 -7.4; 486 -7.1; 535 -6.9; 588 -6.7; 647 -6.5; 712 -6.2; 783 -5.9; 861 -5.7; 947 -5.6; 1042 -5.8; 1146 -6.4; 1261 -6.9; 1387 -7.0; 1526 -6.7; 1678 -6.1; 1846 -5.4; 2031 -4.6; 2234 -3.5; 2457 -2.3; 2703 -1.3; 2973 -0.6; 3270 -0.5; 3597 -1.2; 3957 -2.3; 4353 -3.3; 4788 -4.8; 5267 -3.7; 5793 -0.8; 6373 -1.8; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -6.1; 10263 -6.1; 11289 -5.9; 12418 -5.9; 13660 -9.6; 15026 -15.9; 16529 -24.1; 18182 -30.9; 20000 -22.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 sample 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 sample 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 0.12 | -4.5 dB  |
| Peaking | 1507 Hz  | 1.36 | -5.0 dB  |
| Peaking | 5506 Hz  | 0.22 | 7.9 dB   |
| Peaking | 12831 Hz | 1.47 | 8.6 dB   |
| Peaking | 18090 Hz | 0.41 | -28.2 dB |
| Peaking | 2081 Hz  | 4.98 | -0.7 dB  |
| Peaking | 3088 Hz  | 3.23 | 1.5 dB   |
| Peaking | 4960 Hz  | 3.19 | -5.1 dB  |
| Peaking | 5839 Hz  | 2.66 | 4.5 dB   |
| Peaking | 7792 Hz  | 4.31 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 16000 Hz | 1.41 | -21.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15%20sample%204/64%20Audio%20N8%20M15%20sample%204.png)