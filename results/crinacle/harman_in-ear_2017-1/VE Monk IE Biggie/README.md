# VE Monk IE Biggie
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.2; 25 -8.5; 28 -8.9; 31 -9.3; 34 -9.5; 37 -9.8; 41 -10.0; 45 -10.3; 49 -10.6; 54 -10.9; 60 -11.2; 66 -11.6; 72 -12.0; 79 -12.4; 87 -12.9; 96 -13.4; 106 -13.9; 116 -14.3; 128 -14.8; 141 -15.2; 155 -15.5; 170 -15.8; 187 -16.1; 206 -16.3; 227 -16.5; 249 -16.7; 274 -16.8; 302 -16.9; 332 -16.8; 365 -16.6; 402 -16.5; 442 -16.1; 486 -15.5; 535 -14.7; 588 -13.6; 647 -12.3; 712 -10.6; 783 -8.9; 861 -7.1; 947 -5.7; 1042 -4.7; 1146 -4.2; 1261 -4.0; 1387 -4.0; 1526 -4.3; 1678 -4.9; 1846 -5.2; 2031 -4.0; 2234 -1.4; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -2.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -15.2; 16529 -19.3; 18182 -10.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VE Monk IE Biggie GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VE Monk IE Biggie ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 141 Hz   | 0.21 | -3.7 dB  |
| Peaking | 512 Hz   | 0.25 | -8.8 dB  |
| Peaking | 1022 Hz  | 1.16 | 8.5 dB   |
| Peaking | 3225 Hz  | 0.6  | 8.5 dB   |
| Peaking | 16395 Hz | 2.17 | -14.7 dB |
| Peaking | 1906 Hz  | 5.74 | -1.8 dB  |
| Peaking | 2360 Hz  | 4.71 | 1.9 dB   |
| Peaking | 6051 Hz  | 2.64 | 6.5 dB   |
| Peaking | 6735 Hz  | 1.18 | -4.4 dB  |
| Peaking | 13359 Hz | 4.28 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | -8.6 dB  |
| Peaking | 500 Hz   | 1.41 | -8.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -10.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/VE%20Monk%20IE%20Biggie/VE%20Monk%20IE%20Biggie.png)