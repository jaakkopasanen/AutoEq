# Audeze LCD-i4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.6; 25 -1.8; 28 -2.1; 31 -2.4; 34 -2.6; 37 -2.8; 41 -3.1; 45 -3.3; 49 -3.5; 54 -3.8; 60 -4.2; 66 -4.6; 72 -5.0; 79 -5.5; 87 -6.0; 96 -6.4; 106 -7.0; 116 -7.3; 128 -7.7; 141 -8.2; 155 -8.6; 170 -8.9; 187 -9.2; 206 -9.4; 227 -9.6; 249 -9.7; 274 -9.9; 302 -10.0; 332 -9.9; 365 -10.0; 402 -10.1; 442 -10.3; 486 -10.3; 535 -10.5; 588 -10.9; 647 -11.3; 712 -11.8; 783 -12.0; 861 -11.3; 947 -10.5; 1042 -10.9; 1146 -11.4; 1261 -11.6; 1387 -11.7; 1526 -11.9; 1678 -12.3; 1846 -10.9; 2031 -8.2; 2234 -4.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.1; 10263 -9.6; 11289 -9.5; 12418 -10.4; 13660 -18.6; 15026 -29.3; 16529 -32.3; 18182 -27.2; 20000 -19.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-i4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-i4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.36 | 5.0 dB   |
| Peaking | 925 Hz   | 0.29 | -19.6 dB |
| Peaking | 1669 Hz  | 2.18 | -8.6 dB  |
| Peaking | 3437 Hz  | 0.14 | 23.4 dB  |
| Peaking | 16327 Hz | 0.5  | -37.2 dB |
| Peaking | 2075 Hz  | 4.83 | -2.0 dB  |
| Peaking | 2396 Hz  | 5.71 | 3.3 dB   |
| Peaking | 7740 Hz  | 5.97 | -2.4 dB  |
| Peaking | 12398 Hz | 3.97 | 5.2 dB   |
| Peaking | 14807 Hz | 4.64 | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB   |
| Peaking | 62 Hz    | 1.41 | 1.7 dB   |
| Peaking | 125 Hz   | 1.41 | -1.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | -2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 9.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 16000 Hz | 1.41 | -32.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audeze%20LCD-i4/Audeze%20LCD-i4.png)