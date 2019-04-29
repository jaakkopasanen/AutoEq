# Kumitate KL-Corona
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.2; 25 -1.8; 28 -2.4; 31 -3.1; 34 -3.6; 37 -4.0; 41 -4.5; 45 -4.9; 49 -5.3; 54 -5.7; 60 -6.1; 66 -6.5; 72 -7.0; 79 -7.3; 87 -7.7; 96 -8.1; 106 -8.4; 116 -8.6; 128 -8.8; 141 -9.0; 155 -9.0; 170 -9.0; 187 -9.0; 206 -8.9; 227 -8.7; 249 -8.5; 274 -8.3; 302 -8.0; 332 -7.7; 365 -7.3; 402 -7.0; 442 -6.8; 486 -6.5; 535 -6.1; 588 -5.8; 647 -5.4; 712 -5.0; 783 -4.6; 861 -4.3; 947 -4.3; 1042 -4.6; 1146 -5.1; 1261 -5.7; 1387 -5.9; 1526 -5.7; 1678 -5.5; 1846 -5.3; 2031 -5.2; 2234 -4.7; 2457 -4.0; 2703 -3.2; 2973 -2.3; 3270 -1.6; 3597 -1.2; 3957 -0.8; 4353 -0.5; 4788 -0.6; 5267 -1.3; 5793 -2.7; 6373 -5.0; 7010 -5.1; 7711 -5.3; 8482 -5.3; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.9; 16529 -12.2; 18182 -13.8; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Corona GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Corona ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.67 | 5.7 dB  |
| Peaking | 157 Hz   | 0.49 | -3.9 dB |
| Peaking | 840 Hz   | 2.76 | 1.6 dB  |
| Peaking | 4172 Hz  | 1.53 | 5.3 dB  |
| Peaking | 18273 Hz | 1.18 | -9.6 dB |
| Peaking | 1590 Hz  | 2.38 | -0.7 dB |
| Peaking | 3013 Hz  | 4.53 | 1.0 dB  |
| Peaking | 5377 Hz  | 3.7  | 3.0 dB  |
| Peaking | 5873 Hz  | 1.7  | -2.1 dB |
| Peaking | 14028 Hz | 2.99 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Corona/Kumitate%20KL-Corona.png)