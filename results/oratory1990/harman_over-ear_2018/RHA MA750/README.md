# RHA MA750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.2; 25 -9.5; 28 -9.7; 31 -9.8; 34 -9.8; 37 -9.7; 41 -9.7; 45 -9.7; 49 -9.7; 54 -9.8; 60 -9.9; 66 -10.0; 72 -9.9; 79 -10.1; 87 -9.9; 96 -9.7; 106 -10.0; 116 -9.8; 128 -10.1; 141 -9.8; 155 -9.8; 170 -9.9; 187 -9.9; 206 -9.9; 227 -9.8; 249 -9.6; 274 -9.4; 302 -9.1; 332 -8.7; 365 -8.4; 402 -8.1; 442 -7.8; 486 -7.4; 535 -7.0; 588 -6.5; 647 -6.0; 712 -5.6; 783 -5.2; 861 -4.8; 947 -4.6; 1042 -4.5; 1146 -4.5; 1261 -4.6; 1387 -4.3; 1526 -3.7; 1678 -2.8; 1846 -1.8; 2031 -1.0; 2234 -0.5; 2457 -0.6; 2703 -1.4; 2973 -2.7; 3270 -4.1; 3597 -4.7; 3957 -5.1; 4353 -5.9; 4788 -7.8; 5267 -8.8; 5793 -5.9; 6373 -2.8; 7010 -3.5; 7711 -6.4; 8482 -6.5; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -9.3; 15026 -13.4; 16529 -14.0; 18182 -16.5; 20000 -21.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RHA MA750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA MA750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 115 Hz   | 0.11 | -4.1 dB  |
| Peaking | 832 Hz   | 0.76 | 3.2 dB   |
| Peaking | 2272 Hz  | 1.75 | 5.9 dB   |
| Peaking | 11441 Hz | 1.06 | 4.5 dB   |
| Peaking | 20065 Hz | 0.23 | -13.7 dB |
| Peaking | 5191 Hz  | 4.72 | -4.4 dB  |
| Peaking | 6591 Hz  | 3.27 | 4.9 dB   |
| Peaking | 7881 Hz  | 4.34 | -2.3 dB  |
| Peaking | 14874 Hz | 6.06 | -2.1 dB  |
| Peaking | 17491 Hz | 2.14 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -10.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/RHA%20MA750/RHA%20MA750.png)