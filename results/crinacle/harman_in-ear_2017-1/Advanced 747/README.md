# Advanced 747
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.5; 23 -12.6; 25 -12.8; 28 -12.9; 31 -13.1; 34 -13.2; 37 -13.2; 41 -13.4; 45 -13.5; 49 -13.6; 54 -13.7; 60 -13.8; 66 -14.0; 72 -14.2; 79 -14.5; 87 -14.7; 96 -14.9; 106 -15.1; 116 -15.3; 128 -15.3; 141 -15.3; 155 -15.2; 170 -15.0; 187 -14.8; 206 -14.4; 227 -14.1; 249 -13.6; 274 -13.1; 302 -12.4; 332 -11.7; 365 -10.9; 402 -10.2; 442 -9.5; 486 -8.7; 535 -7.9; 588 -7.0; 647 -6.1; 712 -5.0; 783 -4.0; 861 -3.0; 947 -2.3; 1042 -1.8; 1146 -1.4; 1261 -1.0; 1387 -1.0; 1526 -1.2; 1678 -1.9; 1846 -2.4; 2031 -2.0; 2234 -1.4; 2457 -1.1; 2703 -1.3; 2973 -1.7; 3270 -1.5; 3597 -0.8; 3957 -0.5; 4353 -0.6; 4788 -1.7; 5267 -3.7; 5793 -6.6; 6373 -5.0; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.4; 15026 -17.9; 16529 -21.6; 18182 -26.8; 20000 -23.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced 747 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced 747 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 42 Hz    | 0.19 | -6.2 dB  |
| Peaking | 192 Hz   | 0.58 | -6.4 dB  |
| Peaking | 430 Hz   | 0.97 | -4.0 dB  |
| Peaking | 2850 Hz  | 0.08 | 6.1 dB   |
| Peaking | 18431 Hz | 0.51 | -24.0 dB |
| Peaking | 1905 Hz  | 6.41 | -1.3 dB  |
| Peaking | 4283 Hz  | 3.36 | 1.8 dB   |
| Peaking | 5808 Hz  | 5.39 | -3.9 dB  |
| Peaking | 12641 Hz | 2.71 | 6.9 dB   |
| Peaking | 14375 Hz | 1.71 | -4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB  |
| Peaking | 125 Hz   | 1.41 | -7.4 dB  |
| Peaking | 250 Hz   | 1.41 | -6.2 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -19.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20747/Advanced%20747.png)