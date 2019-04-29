# HUM Pristine Reference
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.0; 25 -4.2; 28 -4.6; 31 -4.9; 34 -5.2; 37 -5.4; 41 -5.7; 45 -5.9; 49 -6.1; 54 -6.3; 60 -6.6; 66 -6.9; 72 -7.3; 79 -7.7; 87 -8.0; 96 -8.5; 106 -8.9; 116 -9.2; 128 -9.5; 141 -9.8; 155 -10.0; 170 -10.0; 187 -10.1; 206 -10.1; 227 -9.9; 249 -9.8; 274 -9.6; 302 -9.3; 332 -8.9; 365 -8.4; 402 -8.1; 442 -7.7; 486 -7.2; 535 -6.8; 588 -6.3; 647 -5.8; 712 -5.3; 783 -4.8; 861 -4.4; 947 -4.4; 1042 -4.8; 1146 -5.6; 1261 -6.5; 1387 -7.2; 1526 -7.8; 1678 -8.4; 1846 -9.2; 2031 -9.0; 2234 -7.6; 2457 -5.5; 2703 -3.2; 2973 -1.7; 3270 -1.6; 3597 -3.0; 3957 -4.8; 4353 -4.7; 4788 -5.6; 5267 -6.9; 5793 -3.5; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.6; 16529 -9.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HUM Pristine Reference GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HUM Pristine Reference ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 19 Hz    |  0.99 | 2.4 dB  |
| Peaking | 179 Hz   |  0.72 | -4.5 dB |
| Peaking | 1936 Hz  |  3.02 | -4.2 dB |
| Peaking | 3080 Hz  |  2.96 | 5.2 dB  |
| Peaking | 6359 Hz  |  6.93 | 6.1 dB  |
| Peaking | 372 Hz   |  1.71 | -0.8 dB |
| Peaking | 909 Hz   |  1.5  | 2.3 dB  |
| Peaking | 1393 Hz  |  2.66 | -1.4 dB |
| Peaking | 5276 Hz  | 10.91 | -2.2 dB |
| Peaking | 16353 Hz |  3.74 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -2.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/HUM%20Pristine%20Reference/HUM%20Pristine%20Reference.png)