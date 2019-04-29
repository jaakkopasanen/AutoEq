# Final Audio Heaven S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.8; 25 -7.0; 28 -7.1; 31 -7.3; 34 -7.4; 37 -7.6; 41 -7.8; 45 -8.0; 49 -8.1; 54 -8.2; 60 -8.5; 66 -8.9; 72 -9.3; 79 -9.7; 87 -10.0; 96 -10.3; 106 -10.6; 116 -11.0; 128 -11.2; 141 -11.4; 155 -11.6; 170 -11.7; 187 -11.8; 206 -11.8; 227 -11.7; 249 -11.5; 274 -11.3; 302 -10.9; 332 -10.5; 365 -10.1; 402 -9.7; 442 -9.3; 486 -8.8; 535 -8.3; 588 -7.8; 647 -7.1; 712 -6.5; 783 -5.9; 861 -5.3; 947 -5.0; 1042 -5.1; 1146 -5.4; 1261 -5.5; 1387 -5.3; 1526 -4.7; 1678 -3.9; 1846 -3.3; 2031 -2.7; 2234 -2.3; 2457 -2.7; 2703 -4.5; 2973 -5.7; 3270 -4.2; 3597 -1.4; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -4.8; 6373 -11.2; 7010 -10.7; 7711 -7.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.0; 15026 -18.5; 16529 -16.1; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Heaven S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Heaven S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 180 Hz   | 0.5  | -5.5 dB  |
| Peaking | 1901 Hz  | 0.98 | 3.3 dB   |
| Peaking | 4389 Hz  | 3.08 | 6.5 dB   |
| Peaking | 15638 Hz | 2.66 | -14.3 dB |
| Peaking | 22050 Hz | 1.25 | -7.7 dB  |
| Peaking | 891 Hz   | 2.79 | 1.5 dB   |
| Peaking | 1374 Hz  | 3.96 | -1.2 dB  |
| Peaking | 5397 Hz  | 5.92 | 4.6 dB   |
| Peaking | 6553 Hz  | 4.37 | -6.9 dB  |
| Peaking | 12510 Hz | 3.57 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -10.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20Heaven%20S/Final%20Audio%20Heaven%20S.png)