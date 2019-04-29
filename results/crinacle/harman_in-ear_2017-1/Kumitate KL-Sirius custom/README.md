# Kumitate KL-Sirius custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.7; 25 -2.2; 28 -2.8; 31 -3.3; 34 -3.7; 37 -4.0; 41 -4.4; 45 -4.7; 49 -4.9; 54 -5.1; 60 -5.4; 66 -5.7; 72 -6.1; 79 -6.4; 87 -6.7; 96 -7.1; 106 -7.5; 116 -7.8; 128 -8.0; 141 -8.4; 155 -8.6; 170 -8.8; 187 -8.9; 206 -9.0; 227 -9.0; 249 -9.0; 274 -9.1; 302 -9.0; 332 -8.8; 365 -8.7; 402 -8.6; 442 -8.5; 486 -8.4; 535 -8.3; 588 -8.2; 647 -8.1; 712 -7.9; 783 -7.8; 861 -7.9; 947 -8.2; 1042 -8.9; 1146 -9.9; 1261 -10.7; 1387 -10.8; 1526 -10.1; 1678 -8.9; 1846 -7.4; 2031 -5.8; 2234 -4.3; 2457 -3.3; 2703 -2.8; 2973 -2.8; 3270 -2.8; 3597 -2.6; 3957 -2.5; 4353 -2.9; 4788 -2.2; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -7.7; 10263 -10.5; 11289 -7.3; 12418 -6.5; 13660 -7.3; 15026 -14.6; 16529 -17.2; 18182 -16.6; 20000 -18.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Sirius custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Sirius custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.35 | 6.3 dB   |
| Peaking | 237 Hz   | 0.49 | -2.7 dB  |
| Peaking | 1389 Hz  | 1.82 | -5.2 dB  |
| Peaking | 2909 Hz  | 1.26 | 4.5 dB   |
| Peaking | 5644 Hz  | 3.19 | 5.9 dB   |
| Peaking | 878 Hz   | 3.45 | 0.2 dB   |
| Peaking | 4127 Hz  | 4.25 | 0.9 dB   |
| Peaking | 6532 Hz  | 7.82 | 2.5 dB   |
| Peaking | 18673 Hz | 0.57 | -12.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB   |
| Peaking | 62 Hz    | 1.41 | 0.5 dB   |
| Peaking | 125 Hz   | 1.41 | -1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 16000 Hz | 1.41 | -12.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Sirius%20custom/Kumitate%20KL-Sirius%20custom.png)