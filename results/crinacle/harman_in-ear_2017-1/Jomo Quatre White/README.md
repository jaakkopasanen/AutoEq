# Jomo Quatre White
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.2; 25 -11.2; 28 -11.2; 31 -11.2; 34 -11.2; 37 -11.2; 41 -11.2; 45 -11.1; 49 -11.1; 54 -11.1; 60 -11.1; 66 -11.2; 72 -11.3; 79 -11.4; 87 -11.5; 96 -11.7; 106 -11.9; 116 -11.9; 128 -12.0; 141 -12.1; 155 -12.2; 170 -12.2; 187 -12.1; 206 -12.0; 227 -11.8; 249 -11.6; 274 -11.4; 302 -11.1; 332 -10.6; 365 -10.2; 402 -9.9; 442 -9.5; 486 -9.1; 535 -8.6; 588 -8.0; 647 -7.5; 712 -6.9; 783 -6.2; 861 -5.6; 947 -5.4; 1042 -5.5; 1146 -5.9; 1261 -6.2; 1387 -6.2; 1526 -5.8; 1678 -5.4; 1846 -5.0; 2031 -4.3; 2234 -3.4; 2457 -1.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -3.3; 4788 -6.5; 5267 -5.5; 5793 -1.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.2; 15026 -13.8; 16529 -18.3; 18182 -21.1; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Quatre White GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Quatre White ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.14 | -4.5 dB  |
| Peaking | 227 Hz   | 0.69 | -3.5 dB  |
| Peaking | 3085 Hz  | 1.44 | 6.7 dB   |
| Peaking | 6312 Hz  | 5.36 | 5.7 dB   |
| Peaking | 18114 Hz | 1.13 | -16.3 dB |
| Peaking | 906 Hz   | 3.89 | 1.6 dB   |
| Peaking | 3989 Hz  | 7.42 | 2.0 dB   |
| Peaking | 4861 Hz  | 7.55 | -3.3 dB  |
| Peaking | 12975 Hz | 2    | 3.9 dB   |
| Peaking | 15518 Hz | 1.77 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -12.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Quatre%20White/Jomo%20Quatre%20White.png)