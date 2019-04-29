# Final Audio Heaven 7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.6; 41 -2.2; 45 -2.8; 49 -3.2; 54 -3.7; 60 -4.3; 66 -4.8; 72 -5.4; 79 -6.0; 87 -6.5; 96 -7.2; 106 -7.7; 116 -8.2; 128 -8.6; 141 -9.1; 155 -9.6; 170 -10.0; 187 -10.1; 206 -10.3; 227 -10.4; 249 -10.4; 274 -10.4; 302 -10.2; 332 -10.0; 365 -9.7; 402 -9.5; 442 -9.3; 486 -9.0; 535 -8.6; 588 -8.1; 647 -7.7; 712 -7.1; 783 -6.5; 861 -6.1; 947 -5.8; 1042 -5.9; 1146 -6.3; 1261 -6.5; 1387 -6.3; 1526 -5.6; 1678 -4.8; 1846 -4.1; 2031 -3.4; 2234 -2.9; 2457 -3.2; 2703 -4.8; 2973 -7.6; 3270 -7.7; 3597 -4.4; 3957 -1.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.0; 6373 -5.6; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -8.5; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.7; 18182 -10.4; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven 7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven 7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.57 | 6.3 dB  |
| Peaking | 225 Hz   | 0.61 | -4.4 dB |
| Peaking | 2100 Hz  | 2.98 | 3.7 dB  |
| Peaking | 4825 Hz  | 2.62 | 7.0 dB  |
| Peaking | 19951 Hz | 0.98 | -7.4 dB |
| Peaking | 915 Hz   | 4.13 | 1.3 dB  |
| Peaking | 3164 Hz  | 4.81 | -6.7 dB |
| Peaking | 3319 Hz  | 2.06 | 3.2 dB  |
| Peaking | 9589 Hz  | 7.4  | -3.1 dB |
| Peaking | 18366 Hz | 3.18 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20Heaven%207/Final%20Audio%20Heaven%207.png)