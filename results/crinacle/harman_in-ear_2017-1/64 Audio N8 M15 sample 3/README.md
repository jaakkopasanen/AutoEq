# 64 Audio N8 M15 sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -9.1; 25 -9.4; 28 -9.8; 31 -10.0; 34 -10.2; 37 -10.2; 41 -10.3; 45 -10.5; 49 -10.6; 54 -10.6; 60 -10.7; 66 -10.7; 72 -10.8; 79 -10.9; 87 -11.1; 96 -11.1; 106 -11.0; 116 -11.1; 128 -11.0; 141 -10.8; 155 -10.6; 170 -10.4; 187 -10.3; 206 -9.9; 227 -9.7; 249 -9.4; 274 -9.1; 302 -8.7; 332 -8.3; 365 -8.0; 402 -7.7; 442 -7.5; 486 -7.3; 535 -7.0; 588 -6.8; 647 -6.6; 712 -6.2; 783 -5.9; 861 -5.6; 947 -5.5; 1042 -5.7; 1146 -6.3; 1261 -6.8; 1387 -6.9; 1526 -6.5; 1678 -5.9; 1846 -5.2; 2031 -4.4; 2234 -3.3; 2457 -2.2; 2703 -1.2; 2973 -0.6; 3270 -0.5; 3597 -1.2; 3957 -2.4; 4353 -3.3; 4788 -4.7; 5267 -4.1; 5793 -1.1; 6373 -1.7; 7010 -3.6; 7711 -5.8; 8482 -6.1; 9330 -6.1; 10263 -6.2; 11289 -6.1; 12418 -6.1; 13660 -10.3; 15026 -17.5; 16529 -27.5; 18182 -34.3; 20000 -19.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.75 | -2.3 dB  |
| Peaking | 116 Hz   | 0.39 | -4.7 dB  |
| Peaking | 5442 Hz  | 0.49 | 7.7 dB   |
| Peaking | 12680 Hz | 1.31 | 11.6 dB  |
| Peaking | 17908 Hz | 0.52 | -31.3 dB |
| Peaking | 1508 Hz  | 2.49 | -2.2 dB  |
| Peaking | 3091 Hz  | 2.09 | 2.9 dB   |
| Peaking | 5114 Hz  | 2.2  | -4.6 dB  |
| Peaking | 5895 Hz  | 3.86 | 4.8 dB   |
| Peaking | 14796 Hz | 6.85 | 0.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 16000 Hz | 1.41 | -24.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15%20sample%203/64%20Audio%20N8%20M15%20sample%203.png)