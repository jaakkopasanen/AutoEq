# Final Audio Heaven 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.7; 25 -7.1; 28 -7.6; 31 -7.9; 34 -8.2; 37 -8.5; 41 -8.8; 45 -9.1; 49 -9.4; 54 -9.7; 60 -10.0; 66 -10.4; 72 -10.7; 79 -11.1; 87 -11.5; 96 -11.9; 106 -12.2; 116 -12.6; 128 -12.9; 141 -13.1; 155 -13.2; 170 -13.2; 187 -13.3; 206 -13.3; 227 -13.1; 249 -12.9; 274 -12.7; 302 -12.4; 332 -11.9; 365 -11.4; 402 -11.0; 442 -10.6; 486 -10.1; 535 -9.5; 588 -9.0; 647 -8.4; 712 -7.7; 783 -7.0; 861 -6.4; 947 -6.0; 1042 -6.0; 1146 -6.2; 1261 -6.4; 1387 -6.0; 1526 -5.3; 1678 -4.3; 1846 -3.4; 2031 -2.4; 2234 -1.7; 2457 -1.6; 2703 -2.6; 2973 -4.2; 3270 -4.5; 3597 -1.9; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -15.6; 16529 -19.2; 18182 -15.4; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 131 Hz   | 0.49 | -5.7 dB  |
| Peaking | 307 Hz   | 0.88 | -3.0 dB  |
| Peaking | 2178 Hz  | 2.19 | 4.1 dB   |
| Peaking | 5027 Hz  | 1.28 | 6.7 dB   |
| Peaking | 17049 Hz | 1.24 | -13.4 dB |
| Peaking | 17 Hz    | 2.06 | 1.3 dB   |
| Peaking | 838 Hz   | 1.06 | -1.1 dB  |
| Peaking | 893 Hz   | 2.18 | 2.1 dB   |
| Peaking | 7884 Hz  | 6.42 | -1.9 dB  |
| Peaking | 13122 Hz | 4.16 | 3.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -12.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20Heaven%208/Final%20Audio%20Heaven%208.png)