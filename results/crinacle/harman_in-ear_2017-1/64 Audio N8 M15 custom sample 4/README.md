# 64 Audio N8 M15 custom sample 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.9; 25 -11.0; 28 -11.2; 31 -11.3; 34 -11.4; 37 -11.4; 41 -11.5; 45 -11.5; 49 -11.6; 54 -11.5; 60 -11.6; 66 -11.6; 72 -11.7; 79 -11.8; 87 -11.9; 96 -12.0; 106 -11.9; 116 -12.0; 128 -12.0; 141 -11.9; 155 -11.7; 170 -11.7; 187 -11.5; 206 -11.2; 227 -11.0; 249 -10.8; 274 -10.5; 302 -10.2; 332 -9.8; 365 -9.6; 402 -9.3; 442 -9.1; 486 -8.9; 535 -8.6; 588 -8.3; 647 -7.9; 712 -7.4; 783 -6.8; 861 -6.3; 947 -6.1; 1042 -6.2; 1146 -6.8; 1261 -7.4; 1387 -7.8; 1526 -7.8; 1678 -7.5; 1846 -7.1; 2031 -6.4; 2234 -5.3; 2457 -3.9; 2703 -2.5; 2973 -1.3; 3270 -0.6; 3597 -0.7; 3957 -1.2; 4353 -1.6; 4788 -2.0; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -14.1; 15026 -23.7; 16529 -30.3; 18182 -29.1; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15 custom sample 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15 custom sample 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.54 | -3.1 dB  |
| Peaking | 131 Hz   | 0.3  | -5.1 dB  |
| Peaking | 5307 Hz  | 0.72 | 9.9 dB   |
| Peaking | 12103 Hz | 1.54 | 12.5 dB  |
| Peaking | 16869 Hz | 0.53 | -27.9 dB |
| Peaking | 1717 Hz  | 2.28 | -2.5 dB  |
| Peaking | 3192 Hz  | 2.14 | 2.9 dB   |
| Peaking | 5125 Hz  | 1.81 | -2.9 dB  |
| Peaking | 6030 Hz  | 4.07 | 3.4 dB   |
| Peaking | 15274 Hz | 7.42 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 16000 Hz | 1.41 | -26.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15%20custom%20sample%204/64%20Audio%20N8%20M15%20custom%20sample%204.png)