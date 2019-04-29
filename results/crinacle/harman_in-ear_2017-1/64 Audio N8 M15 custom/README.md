# 64 Audio N8 M15 custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.7; 25 -10.9; 28 -11.1; 31 -11.2; 34 -11.3; 37 -11.3; 41 -11.4; 45 -11.4; 49 -11.4; 54 -11.5; 60 -11.5; 66 -11.6; 72 -11.7; 79 -11.9; 87 -12.1; 96 -12.1; 106 -12.1; 116 -12.2; 128 -12.2; 141 -12.2; 155 -12.0; 170 -12.0; 187 -11.9; 206 -11.6; 227 -11.4; 249 -11.2; 274 -10.9; 302 -10.6; 332 -10.2; 365 -9.8; 402 -9.5; 442 -9.2; 486 -8.9; 535 -8.5; 588 -8.1; 647 -7.7; 712 -7.1; 783 -6.6; 861 -6.2; 947 -6.0; 1042 -6.2; 1146 -6.8; 1261 -7.5; 1387 -7.9; 1526 -7.9; 1678 -7.6; 1846 -7.2; 2031 -6.5; 2234 -5.3; 2457 -3.8; 2703 -2.4; 2973 -1.2; 3270 -0.5; 3597 -0.6; 3957 -1.3; 4353 -1.9; 4788 -2.7; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -14.4; 15026 -23.1; 16529 -28.0; 18182 -27.8; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.58 | -3.3 dB  |
| Peaking | 143 Hz   | 0.35 | -5.4 dB  |
| Peaking | 5380 Hz  | 0.71 | 9.9 dB   |
| Peaking | 12017 Hz | 1.58 | 12.3 dB  |
| Peaking | 16887 Hz | 0.45 | -25.4 dB |
| Peaking | 946 Hz   | 1.55 | 2.6 dB   |
| Peaking | 1667 Hz  | 0.83 | -3.7 dB  |
| Peaking | 3193 Hz  | 1.35 | 5.0 dB   |
| Peaking | 5045 Hz  | 1.44 | -4.6 dB  |
| Peaking | 5892 Hz  | 3.31 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 16000 Hz | 1.41 | -25.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15%20custom/64%20Audio%20N8%20M15%20custom.png)