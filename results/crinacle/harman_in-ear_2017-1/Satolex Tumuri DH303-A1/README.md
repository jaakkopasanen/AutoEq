# Satolex Tumuri DH303-A1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.2; 25 -1.7; 28 -2.3; 31 -2.9; 34 -3.3; 37 -3.7; 41 -4.2; 45 -4.6; 49 -5.0; 54 -5.4; 60 -5.8; 66 -6.3; 72 -6.7; 79 -7.1; 87 -7.6; 96 -8.1; 106 -8.5; 116 -8.8; 128 -9.1; 141 -9.3; 155 -9.5; 170 -9.6; 187 -9.6; 206 -9.5; 227 -9.3; 249 -9.1; 274 -8.8; 302 -8.3; 332 -7.8; 365 -7.3; 402 -6.8; 442 -6.3; 486 -5.8; 535 -5.2; 588 -4.5; 647 -3.9; 712 -3.2; 783 -2.4; 861 -1.9; 947 -1.5; 1042 -1.4; 1146 -2.4; 1261 -3.5; 1387 -3.6; 1526 -3.3; 1678 -2.9; 1846 -2.5; 2031 -2.2; 2234 -2.0; 2457 -2.4; 2703 -3.3; 2973 -3.6; 3270 -2.7; 3597 -1.5; 3957 -0.6; 4353 -0.5; 4788 -1.3; 5267 -3.3; 5793 -7.1; 6373 -7.1; 7010 -3.2; 7711 -4.6; 8482 -4.9; 9330 -6.1; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -10.1; 15026 -22.4; 16529 -26.1; 18182 -21.6; 20000 -18.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Satolex Tumuri DH303-A1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Satolex Tumuri DH303-A1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.92 | 4.7 dB   |
| Peaking | 174 Hz   | 0.61 | -5.1 dB  |
| Peaking | 5022 Hz  | 0.25 | 9.7 dB   |
| Peaking | 12789 Hz | 0.92 | 19.6 dB  |
| Peaking | 15572 Hz | 0.42 | -35.5 dB |
| Peaking | 982 Hz   | 2.01 | 3.2 dB   |
| Peaking | 1314 Hz  | 1.59 | -2.7 dB  |
| Peaking | 2993 Hz  | 3    | -2.9 dB  |
| Peaking | 4286 Hz  | 1.41 | 3.1 dB   |
| Peaking | 5978 Hz  | 6.02 | -5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB   |
| Peaking | 62 Hz    | 1.41 | -1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 16000 Hz | 1.41 | -22.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Satolex%20Tumuri%20DH303-A1/Satolex%20Tumuri%20DH303-A1.png)