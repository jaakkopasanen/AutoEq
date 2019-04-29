# Hyla CE-5 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -8.8; 25 -8.9; 28 -8.9; 31 -8.9; 34 -8.9; 37 -8.8; 41 -8.8; 45 -8.7; 49 -8.7; 54 -8.6; 60 -8.5; 66 -8.5; 72 -8.5; 79 -8.5; 87 -8.5; 96 -8.5; 106 -8.5; 116 -8.4; 128 -8.2; 141 -8.1; 155 -7.9; 170 -7.6; 187 -7.3; 206 -6.9; 227 -6.4; 249 -6.0; 274 -5.8; 302 -5.3; 332 -4.8; 365 -4.4; 402 -4.1; 442 -3.8; 486 -3.6; 535 -3.4; 588 -3.2; 647 -3.0; 712 -2.9; 783 -2.8; 861 -2.8; 947 -3.2; 1042 -3.9; 1146 -5.0; 1261 -6.0; 1387 -6.7; 1526 -7.0; 1678 -7.1; 1846 -7.0; 2031 -6.6; 2234 -5.8; 2457 -4.6; 2703 -3.2; 2973 -2.1; 3270 -1.6; 3597 -1.9; 3957 -2.9; 4353 -4.2; 4788 -4.8; 5267 -3.4; 5793 -1.1; 6373 -0.5; 7010 -2.3; 7711 -4.3; 8482 -4.6; 9330 -5.4; 10263 -8.4; 11289 -4.9; 12418 -4.6; 13660 -14.0; 15026 -25.1; 16529 -20.3; 18182 -6.9; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hyla CE-5 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hyla CE-5 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 47 Hz    | 0.31 | -4.6 dB  |
| Peaking | 1768 Hz  | 2.65 | -3.1 dB  |
| Peaking | 3300 Hz  | 3.01 | 3.5 dB   |
| Peaking | 6301 Hz  | 3.36 | 4.9 dB   |
| Peaking | 15510 Hz | 2.54 | -23.5 dB |
| Peaking | 741 Hz   | 1.07 | 2.4 dB   |
| Peaking | 1311 Hz  | 3.4  | -1.9 dB  |
| Peaking | 4732 Hz  | 6.86 | -1.4 dB  |
| Peaking | 12579 Hz | 4.18 | 6.3 dB   |
| Peaking | 14455 Hz | 5.01 | -6.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 16000 Hz | 1.41 | -18.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hyla%20CE-5%20sample%201/Hyla%20CE-5%20sample%201.png)