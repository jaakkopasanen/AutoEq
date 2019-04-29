# qdc 3SH
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.5; 25 -8.6; 28 -8.7; 31 -8.8; 34 -8.9; 37 -9.0; 41 -9.2; 45 -9.3; 49 -9.3; 54 -9.4; 60 -9.7; 66 -10.0; 72 -10.4; 79 -10.7; 87 -11.0; 96 -11.4; 106 -11.8; 116 -12.1; 128 -12.3; 141 -12.6; 155 -12.8; 170 -12.9; 187 -12.9; 206 -12.9; 227 -12.8; 249 -12.7; 274 -12.4; 302 -12.1; 332 -11.7; 365 -11.3; 402 -11.0; 442 -10.6; 486 -10.1; 535 -9.7; 588 -9.1; 647 -8.6; 712 -8.1; 783 -7.6; 861 -7.2; 947 -7.1; 1042 -7.3; 1146 -8.0; 1261 -8.6; 1387 -8.7; 1526 -8.2; 1678 -7.4; 1846 -6.1; 2031 -3.6; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.2; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -8.6; 11289 -6.6; 12418 -7.3; 13660 -16.7; 15026 -25.6; 16529 -24.3; 18182 -18.5; 20000 -19.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc 3SH GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc 3SH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.1  | -1.4 dB  |
| Peaking | 251 Hz   | 0.34 | -6.0 dB  |
| Peaking | 1464 Hz  | 1.67 | -7.1 dB  |
| Peaking | 9008 Hz  | 0.16 | 16.7 dB  |
| Peaking | 15843 Hz | 0.46 | -34.1 dB |
| Peaking | 2357 Hz  | 5.73 | 1.9 dB   |
| Peaking | 5690 Hz  | 3.2  | 2.4 dB   |
| Peaking | 10773 Hz | 0.69 | -3.8 dB  |
| Peaking | 12032 Hz | 2.84 | 9.3 dB   |
| Peaking | 20008 Hz | 3.32 | -4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -5.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 16000 Hz | 1.41 | -22.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%203SH/qdc%203SH.png)