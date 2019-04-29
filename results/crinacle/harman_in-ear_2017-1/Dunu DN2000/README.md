# Dunu DN2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -8.6; 25 -8.4; 28 -8.2; 31 -8.0; 34 -7.8; 37 -7.7; 41 -7.6; 45 -7.5; 49 -7.4; 54 -7.4; 60 -7.5; 66 -7.6; 72 -7.8; 79 -8.0; 87 -8.3; 96 -8.6; 106 -9.0; 116 -9.3; 128 -9.6; 141 -9.9; 155 -10.1; 170 -10.3; 187 -10.5; 206 -10.5; 227 -10.6; 249 -10.8; 274 -10.8; 302 -10.8; 332 -10.7; 365 -10.6; 402 -10.4; 442 -10.4; 486 -10.2; 535 -10.0; 588 -9.8; 647 -9.6; 712 -9.2; 783 -8.1; 861 -7.5; 947 -7.4; 1042 -7.3; 1146 -7.3; 1261 -7.2; 1387 -6.5; 1526 -5.4; 1678 -4.1; 1846 -2.5; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -2.9; 4353 -5.0; 4788 -4.0; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.1; 15026 -17.7; 16529 -17.0; 18182 -13.7; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.52 | -2.0 dB  |
| Peaking | 312 Hz   | 0.35 | -4.4 dB  |
| Peaking | 2449 Hz  | 1.39 | 5.3 dB   |
| Peaking | 8549 Hz  | 0.28 | 4.1 dB   |
| Peaking | 16046 Hz | 0.91 | -14.5 dB |
| Peaking | 851 Hz   | 6.86 | 0.9 dB   |
| Peaking | 4485 Hz  | 5.28 | -4.3 dB  |
| Peaking | 6161 Hz  | 1.75 | 5.4 dB   |
| Peaking | 7687 Hz  | 2.34 | -5.6 dB  |
| Peaking | 12468 Hz | 5.86 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | -12.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Dunu%20DN2000/Dunu%20DN2000.png)