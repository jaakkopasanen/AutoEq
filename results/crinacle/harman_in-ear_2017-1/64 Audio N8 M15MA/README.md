# 64 Audio N8 M15MA
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.0; 25 -9.2; 28 -9.4; 31 -9.6; 34 -9.7; 37 -9.8; 41 -10.0; 45 -10.1; 49 -10.3; 54 -10.5; 60 -10.8; 66 -11.0; 72 -11.3; 79 -11.6; 87 -11.9; 96 -12.2; 106 -12.5; 116 -12.7; 128 -12.8; 141 -12.9; 155 -12.9; 170 -12.8; 187 -12.7; 206 -12.5; 227 -12.2; 249 -11.9; 274 -11.6; 302 -11.2; 332 -10.7; 365 -10.3; 402 -9.8; 442 -9.4; 486 -8.9; 535 -8.4; 588 -7.9; 647 -7.4; 712 -6.8; 783 -6.3; 861 -5.8; 947 -5.7; 1042 -5.9; 1146 -6.5; 1261 -7.2; 1387 -7.6; 1526 -7.6; 1678 -7.3; 1846 -6.9; 2031 -6.1; 2234 -5.0; 2457 -3.5; 2703 -2.1; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -1.4; 4353 -2.3; 4788 -3.2; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.5; 15026 -26.4; 16529 -33.8; 18182 -32.7; 20000 -16.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 M15MA GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 M15MA ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.24 | -2.6 dB  |
| Peaking | 182 Hz   | 0.5  | -4.8 dB  |
| Peaking | 5600 Hz  | 0.6  | 12.4 dB  |
| Peaking | 12325 Hz | 1.61 | 15.5 dB  |
| Peaking | 16767 Hz | 0.49 | -33.3 dB |
| Peaking | 929 Hz   | 1.59 | 2.8 dB   |
| Peaking | 1854 Hz  | 0.74 | -5.1 dB  |
| Peaking | 2972 Hz  | 0.96 | 5.4 dB   |
| Peaking | 4623 Hz  | 4.06 | -3.8 dB  |
| Peaking | 15040 Hz | 7.19 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 16000 Hz | 1.41 | -30.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20M15MA/64%20Audio%20N8%20M15MA.png)