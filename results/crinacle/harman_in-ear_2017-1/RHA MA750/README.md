# RHA MA750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.5; 25 -6.7; 28 -7.1; 31 -7.2; 34 -7.3; 37 -7.4; 41 -7.5; 45 -7.6; 49 -7.8; 54 -7.9; 60 -8.0; 66 -8.2; 72 -8.3; 79 -8.6; 87 -8.8; 96 -9.2; 106 -9.4; 116 -9.7; 128 -9.9; 141 -10.1; 155 -10.3; 170 -10.4; 187 -10.5; 206 -10.5; 227 -10.5; 249 -10.5; 274 -10.4; 302 -10.3; 332 -10.0; 365 -9.7; 402 -9.6; 442 -9.4; 486 -9.1; 535 -8.7; 588 -8.3; 647 -7.9; 712 -7.3; 783 -6.7; 861 -6.2; 947 -5.8; 1042 -5.7; 1146 -5.7; 1261 -5.6; 1387 -5.2; 1526 -4.4; 1678 -3.4; 1846 -2.4; 2031 -1.4; 2234 -0.6; 2457 -0.5; 2703 -0.7; 2973 -2.1; 3270 -3.8; 3597 -4.9; 3957 -5.5; 4353 -6.3; 4788 -7.9; 5267 -8.6; 5793 -5.1; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -18.6; 15026 -30.9; 16529 -34.7; 18182 -33.6; 20000 -29.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA MA750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA MA750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 357 Hz   |  0.3  | -6.0 dB  |
| Peaking | 4844 Hz  |  2.1  | -11.9 dB |
| Peaking | 5447 Hz  |  0.27 | 29.5 dB  |
| Peaking | 12095 Hz |  1.79 | 15.6 dB  |
| Peaking | 16101 Hz |  0.21 | -43.9 dB |
| Peaking | 1366 Hz  |  2.73 | -1.5 dB  |
| Peaking | 2388 Hz  |  1.96 | 2.4 dB   |
| Peaking | 3455 Hz  |  3.95 | -2.6 dB  |
| Peaking | 6497 Hz  | 10.64 | 2.8 dB   |
| Peaking | 7578 Hz  |  7.42 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 10.7 dB  |
| Peaking | 16000 Hz | 1.41 | -36.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/RHA%20MA750/RHA%20MA750.png)