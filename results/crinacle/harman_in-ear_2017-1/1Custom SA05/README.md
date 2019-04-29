# 1Custom SA05
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.4; 25 -6.8; 28 -7.3; 31 -7.6; 34 -7.8; 37 -8.0; 41 -8.3; 45 -8.6; 49 -8.8; 54 -9.0; 60 -9.3; 66 -9.6; 72 -9.8; 79 -10.1; 87 -10.6; 96 -10.9; 106 -11.3; 116 -11.6; 128 -11.8; 141 -12.0; 155 -12.0; 170 -12.1; 187 -12.1; 206 -12.1; 227 -12.0; 249 -11.7; 274 -11.5; 302 -11.2; 332 -10.7; 365 -10.2; 402 -9.7; 442 -9.3; 486 -8.7; 535 -8.1; 588 -7.5; 647 -6.9; 712 -6.2; 783 -5.6; 861 -5.0; 947 -4.7; 1042 -4.8; 1146 -5.1; 1261 -5.3; 1387 -5.2; 1526 -4.6; 1678 -4.1; 1846 -3.4; 2031 -2.0; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -3.9; 4353 -5.2; 4788 -3.7; 5267 -4.8; 5793 -6.7; 6373 -4.9; 7010 -4.2; 7711 -6.5; 8482 -8.5; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.2; 15026 -26.4; 16529 -33.5; 18182 -31.1; 20000 -22.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1Custom SA05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1Custom SA05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 112 Hz   | 0.48 | -2.4 dB  |
| Peaking | 247 Hz   | 0.45 | -4.2 dB  |
| Peaking | 827 Hz   | 4.74 | 0.7 dB   |
| Peaking | 9886 Hz  | 0.18 | 21.8 dB  |
| Peaking | 16996 Hz | 0.37 | -45.5 dB |
| Peaking | 2890 Hz  | 1.23 | 8.2 dB   |
| Peaking | 3442 Hz  | 0.56 | -5.6 dB  |
| Peaking | 8597 Hz  | 5.7  | -3.2 dB  |
| Peaking | 13073 Hz | 1.94 | 9.7 dB   |
| Peaking | 15128 Hz | 2.69 | -9.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 16000 Hz | 1.41 | -29.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/1Custom%20SA05/1Custom%20SA05.png)