# KZ ZS5v1 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.2; 25 -8.5; 28 -9.0; 31 -9.3; 34 -9.6; 37 -9.7; 41 -9.9; 45 -10.1; 49 -10.2; 54 -10.3; 60 -10.4; 66 -10.6; 72 -10.7; 79 -10.8; 87 -11.0; 96 -11.1; 106 -11.2; 116 -11.2; 128 -11.2; 141 -11.1; 155 -11.0; 170 -10.7; 187 -10.5; 206 -10.2; 227 -9.8; 249 -9.5; 274 -9.2; 302 -8.8; 332 -8.3; 365 -7.9; 402 -7.5; 442 -7.2; 486 -6.9; 535 -6.6; 588 -6.4; 647 -6.3; 712 -6.1; 783 -5.9; 861 -6.0; 947 -6.4; 1042 -7.1; 1146 -8.3; 1261 -8.7; 1387 -8.1; 1526 -9.2; 1678 -10.4; 1846 -11.8; 2031 -12.8; 2234 -11.7; 2457 -10.2; 2703 -9.6; 2973 -8.1; 3270 -2.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -8.3; 10263 -10.1; 11289 -12.5; 12418 -14.5; 13660 -16.1; 15026 -14.7; 16529 -13.7; 18182 -18.1; 20000 -25.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ZS5v1 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ZS5v1 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 62 Hz    |  0.46 | -3.7 dB  |
| Peaking | 167 Hz   |  0.91 | -2.8 dB  |
| Peaking | 2201 Hz  |  1.44 | -9.7 dB  |
| Peaking | 4653 Hz  |  0.74 | 10.4 dB  |
| Peaking | 20360 Hz |  0.11 | -13.1 dB |
| Peaking | 741 Hz   |  1.39 | 1.8 dB   |
| Peaking | 993 Hz   |  0.36 | -0.7 dB  |
| Peaking | 3470 Hz  | 10.63 | 2.8 dB   |
| Peaking | 13196 Hz |  2.79 | -2.4 dB  |
| Peaking | 16368 Hz |  2.55 | 4.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -8.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -15.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/KZ%20ZS5v1%20sample%202/KZ%20ZS5v1%20sample%202.png)