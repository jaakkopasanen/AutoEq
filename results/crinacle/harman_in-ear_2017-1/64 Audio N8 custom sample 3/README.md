# 64 Audio N8 custom sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.1; 25 -4.6; 28 -5.1; 31 -5.6; 34 -5.9; 37 -6.2; 41 -6.6; 45 -7.0; 49 -7.2; 54 -7.5; 60 -7.8; 66 -8.1; 72 -8.4; 79 -8.8; 87 -9.3; 96 -9.5; 106 -9.7; 116 -10.1; 128 -10.3; 141 -10.5; 155 -10.5; 170 -10.6; 187 -10.8; 206 -10.7; 227 -10.8; 249 -10.6; 274 -10.6; 302 -10.4; 332 -10.1; 365 -9.9; 402 -9.7; 442 -9.5; 486 -9.3; 535 -8.9; 588 -8.6; 647 -8.2; 712 -7.8; 783 -7.3; 861 -7.0; 947 -6.9; 1042 -7.1; 1146 -7.6; 1261 -8.3; 1387 -8.7; 1526 -8.8; 1678 -8.6; 1846 -8.1; 2031 -7.3; 2234 -5.9; 2457 -4.3; 2703 -2.7; 2973 -1.4; 3270 -0.6; 3597 -0.7; 3957 -1.4; 4353 -2.1; 4788 -3.1; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -7.3; 10263 -6.9; 11289 -6.5; 12418 -6.9; 13660 -14.8; 15026 -22.0; 16529 -25.6; 18182 -26.6; 20000 -18.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 custom sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 custom sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.23 | 3.8 dB   |
| Peaking | 180 Hz   | 0.23 | -4.2 dB  |
| Peaking | 5448 Hz  | 0.74 | 10.0 dB  |
| Peaking | 12031 Hz | 1.83 | 11.4 dB  |
| Peaking | 17151 Hz | 0.37 | -22.3 dB |
| Peaking | 938 Hz   | 1.07 | 4.1 dB   |
| Peaking | 1630 Hz  | 0.61 | -5.0 dB  |
| Peaking | 3014 Hz  | 1.56 | 5.1 dB   |
| Peaking | 4734 Hz  | 4.63 | -2.8 dB  |
| Peaking | 6063 Hz  | 4.76 | 1.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB   |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 16000 Hz | 1.41 | -23.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20custom%20sample%203/64%20Audio%20N8%20custom%20sample%203.png)