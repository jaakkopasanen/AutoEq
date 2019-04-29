# Ocharaku Flat-4 Akakeyaki
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.4; 25 -5.6; 28 -5.8; 31 -6.1; 34 -6.2; 37 -6.4; 41 -6.6; 45 -6.8; 49 -6.8; 54 -6.8; 60 -7.0; 66 -7.2; 72 -7.4; 79 -7.7; 87 -8.1; 96 -8.5; 106 -8.8; 116 -8.9; 128 -9.0; 141 -9.2; 155 -9.4; 170 -9.4; 187 -9.4; 206 -9.3; 227 -9.2; 249 -9.0; 274 -8.9; 302 -8.6; 332 -8.2; 365 -8.0; 402 -7.8; 442 -7.6; 486 -7.4; 535 -7.2; 588 -7.1; 647 -6.9; 712 -6.7; 783 -6.6; 861 -6.5; 947 -6.5; 1042 -6.7; 1146 -6.9; 1261 -7.0; 1387 -6.3; 1526 -4.5; 1678 -2.3; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -1.2; 2703 -4.2; 2973 -5.9; 3270 -4.5; 3597 -2.2; 3957 -1.9; 4353 -3.3; 4788 -8.0; 5267 -7.9; 5793 -0.5; 6373 -1.7; 7010 -12.5; 7711 -17.7; 8482 -13.2; 9330 -7.0; 10263 -6.5; 11289 -6.5; 12418 -8.8; 13660 -16.3; 15026 -21.5; 16529 -24.3; 18182 -28.3; 20000 -30.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ocharaku Flat-4 Akakeyaki GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ocharaku Flat-4 Akakeyaki ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 179 Hz   | 0.64 | -3.0 dB  |
| Peaking | 1851 Hz  | 4.07 | 5.5 dB   |
| Peaking | 2307 Hz  | 4.7  | 5.1 dB   |
| Peaking | 3913 Hz  | 3.17 | 5.4 dB   |
| Peaking | 19014 Hz | 0.62 | -25.7 dB |
| Peaking | 5046 Hz  | 8.11 | -7.7 dB  |
| Peaking | 6075 Hz  | 3.57 | 11.4 dB  |
| Peaking | 7640 Hz  | 3.25 | -14.9 dB |
| Peaking | 11301 Hz | 1.17 | 10.2 dB  |
| Peaking | 14890 Hz | 1.26 | -8.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB   |
| Peaking | 62 Hz    | 1.41 | -0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -22.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ocharaku%20Flat-4%20Akakeyaki/Ocharaku%20Flat-4%20Akakeyaki.png)