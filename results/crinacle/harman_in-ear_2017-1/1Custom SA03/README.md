# 1Custom SA03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.8; 25 -7.1; 28 -7.5; 31 -7.7; 34 -7.9; 37 -8.1; 41 -8.4; 45 -8.6; 49 -8.9; 54 -9.1; 60 -9.3; 66 -9.6; 72 -9.9; 79 -10.2; 87 -10.6; 96 -11.0; 106 -11.3; 116 -11.6; 128 -11.9; 141 -12.1; 155 -12.1; 170 -12.2; 187 -12.3; 206 -12.3; 227 -12.1; 249 -11.9; 274 -11.7; 302 -11.4; 332 -10.9; 365 -10.4; 402 -10.0; 442 -9.6; 486 -9.0; 535 -8.5; 588 -7.9; 647 -7.3; 712 -6.6; 783 -5.9; 861 -5.3; 947 -5.0; 1042 -5.0; 1146 -5.3; 1261 -5.5; 1387 -5.3; 1526 -4.7; 1678 -3.9; 1846 -3.0; 2031 -1.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.2; 4353 -3.2; 4788 -3.0; 5267 -3.1; 5793 -4.3; 6373 -6.8; 7010 -4.8; 7711 -6.2; 8482 -8.9; 9330 -13.2; 10263 -9.9; 11289 -6.5; 12418 -6.5; 13660 -12.5; 15026 -23.3; 16529 -28.5; 18182 -26.7; 20000 -20.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1Custom SA03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1Custom SA03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 132 Hz   | 0.51 | -4.8 dB  |
| Peaking | 290 Hz   | 0.98 | -2.6 dB  |
| Peaking | 2926 Hz  | 0.84 | 6.7 dB   |
| Peaking | 16296 Hz | 2.14 | -15.2 dB |
| Peaking | 18744 Hz | 0.85 | -17.7 dB |
| Peaking | 910 Hz   | 3.22 | 1.3 dB   |
| Peaking | 1395 Hz  | 3.63 | -1.1 dB  |
| Peaking | 9449 Hz  | 4.75 | -8.0 dB  |
| Peaking | 12691 Hz | 1.52 | 7.3 dB   |
| Peaking | 14654 Hz | 2.86 | -7.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -24.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/1Custom%20SA03/1Custom%20SA03.png)