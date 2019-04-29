# FitEar MH334SR custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.7; 25 -5.2; 28 -5.8; 31 -6.3; 34 -6.6; 37 -6.9; 41 -7.2; 45 -7.6; 49 -7.9; 54 -8.3; 60 -8.6; 66 -8.9; 72 -9.3; 79 -9.7; 87 -10.1; 96 -10.6; 106 -11.0; 116 -11.3; 128 -11.6; 141 -11.9; 155 -12.0; 170 -12.1; 187 -12.2; 206 -12.3; 227 -12.2; 249 -12.0; 274 -11.8; 302 -11.6; 332 -11.2; 365 -10.8; 402 -10.4; 442 -10.0; 486 -9.6; 535 -9.1; 588 -8.5; 647 -8.0; 712 -7.4; 783 -6.8; 861 -6.2; 947 -6.0; 1042 -6.1; 1146 -6.5; 1261 -6.9; 1387 -6.9; 1526 -6.6; 1678 -6.0; 1846 -5.1; 2031 -3.7; 2234 -2.5; 2457 -1.8; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.0; 5793 -2.8; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -10.8; 10263 -7.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -11.1; 16529 -9.9; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar MH334SR custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar MH334SR custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 19 Hz    |  1.3  | 3.1 dB  |
| Peaking | 191 Hz   |  0.45 | -5.9 dB |
| Peaking | 3908 Hz  |  0.77 | 6.7 dB  |
| Peaking | 9343 Hz  |  4.49 | -6.0 dB |
| Peaking | 15702 Hz |  2.71 | -5.6 dB |
| Peaking | 936 Hz   |  1.4  | 3.2 dB  |
| Peaking | 1577 Hz  |  0.63 | -4.0 dB |
| Peaking | 2439 Hz  |  1.2  | 3.7 dB  |
| Peaking | 3650 Hz  |  3.76 | -0.9 dB |
| Peaking | 6445 Hz  | 14    | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20MH334SR%20custom/FitEar%20MH334SR%20custom.png)