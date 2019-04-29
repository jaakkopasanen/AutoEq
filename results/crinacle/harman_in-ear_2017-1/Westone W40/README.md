# Westone W40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.5; 25 -3.9; 28 -4.5; 31 -5.2; 34 -5.7; 37 -6.3; 41 -6.8; 45 -7.2; 49 -7.5; 54 -8.0; 60 -8.5; 66 -9.0; 72 -9.5; 79 -10.0; 87 -10.5; 96 -11.1; 106 -11.6; 116 -12.0; 128 -12.4; 141 -12.8; 155 -13.1; 170 -13.3; 187 -13.4; 206 -13.5; 227 -13.5; 249 -13.4; 274 -13.3; 302 -13.1; 332 -12.8; 365 -12.4; 402 -12.1; 442 -11.7; 486 -11.2; 535 -10.6; 588 -10.0; 647 -9.3; 712 -8.5; 783 -7.7; 861 -7.1; 947 -6.7; 1042 -6.8; 1146 -7.2; 1261 -7.5; 1387 -7.2; 1526 -6.3; 1678 -4.9; 1846 -3.4; 2031 -1.6; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -8.6; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -15.7; 15026 -24.0; 16529 -24.4; 18182 -22.4; 20000 -20.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.54 | 5.1 dB   |
| Peaking | 202 Hz   | 0.65 | -2.7 dB  |
| Peaking | 366 Hz   | 0.18 | -5.0 dB  |
| Peaking | 7882 Hz  | 0.18 | 14.1 dB  |
| Peaking | 16537 Hz | 0.41 | -28.6 dB |
| Peaking | 1419 Hz  | 1.98 | -5.8 dB  |
| Peaking | 1467 Hz  | 0.88 | 3.3 dB   |
| Peaking | 8428 Hz  | 3.71 | -5.0 dB  |
| Peaking | 12490 Hz | 2.16 | 6.4 dB   |
| Peaking | 14593 Hz | 3.22 | -6.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -6.3 dB  |
| Peaking | 500 Hz   | 1.41 | -3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 16000 Hz | 1.41 | -22.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Westone%20W40/Westone%20W40.png)