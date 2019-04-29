# FiiO F9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.7; 25 -5.8; 28 -6.1; 31 -6.3; 34 -6.5; 37 -6.7; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.6; 60 -7.9; 66 -8.2; 72 -8.5; 79 -8.8; 87 -9.1; 96 -9.4; 106 -9.7; 116 -9.8; 128 -10.0; 141 -10.1; 155 -10.0; 170 -10.0; 187 -9.8; 206 -9.6; 227 -9.3; 249 -9.0; 274 -8.7; 302 -8.2; 332 -7.7; 365 -7.2; 402 -6.8; 442 -6.4; 486 -5.9; 535 -5.5; 588 -5.0; 647 -4.5; 712 -4.1; 783 -3.9; 861 -3.9; 947 -4.2; 1042 -4.8; 1146 -5.7; 1261 -6.7; 1387 -7.4; 1526 -7.8; 1678 -8.2; 1846 -8.4; 2031 -7.9; 2234 -6.1; 2457 -3.3; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.5; 4353 -4.0; 4788 -6.3; 5267 -5.2; 5793 -4.7; 6373 -8.1; 7010 -10.8; 7711 -7.3; 8482 -7.1; 9330 -11.9; 10263 -13.5; 11289 -9.6; 12418 -6.9; 13660 -8.8; 15026 -14.5; 16529 -22.0; 18182 -26.1; 20000 -21.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO F9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO F9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 146 Hz   |  0.66 | -3.7 dB  |
| Peaking | 733 Hz   |  1.98 | 3.1 dB   |
| Peaking | 3327 Hz  |  2.35 | 7.3 dB   |
| Peaking | 10030 Hz |  6.86 | -5.4 dB  |
| Peaking | 18537 Hz |  0.9  | -21.9 dB |
| Peaking | 21 Hz    |  1.64 | 1.2 dB   |
| Peaking | 1844 Hz  |  2.55 | -3.1 dB  |
| Peaking | 2656 Hz  |  6.31 | 3.1 dB   |
| Peaking | 6850 Hz  | 11.49 | -4.4 dB  |
| Peaking | 12916 Hz |  4.09 | 5.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB   |
| Peaking | 62 Hz    | 1.41 | -1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 16000 Hz | 1.41 | -16.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FiiO%20F9/FiiO%20F9.png)