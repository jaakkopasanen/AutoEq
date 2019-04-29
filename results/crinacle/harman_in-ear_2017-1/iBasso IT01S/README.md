# iBasso IT01S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.0; 25 -5.2; 28 -5.5; 31 -5.7; 34 -5.9; 37 -6.1; 41 -6.3; 45 -6.4; 49 -6.6; 54 -6.9; 60 -7.2; 66 -7.5; 72 -7.7; 79 -8.1; 87 -8.4; 96 -8.8; 106 -9.2; 116 -9.4; 128 -9.7; 141 -9.9; 155 -9.9; 170 -9.9; 187 -9.9; 206 -9.8; 227 -9.6; 249 -9.3; 274 -9.0; 302 -8.6; 332 -8.1; 365 -7.6; 402 -7.2; 442 -6.8; 486 -6.3; 535 -5.8; 588 -5.4; 647 -4.8; 712 -4.1; 783 -3.5; 861 -3.0; 947 -2.9; 1042 -3.1; 1146 -3.6; 1261 -3.9; 1387 -4.1; 1526 -4.0; 1678 -3.9; 1846 -3.9; 2031 -4.0; 2234 -4.1; 2457 -4.0; 2703 -3.3; 2973 -1.9; 3270 -0.8; 3597 -0.5; 3957 -1.3; 4353 -3.6; 4788 -7.6; 5267 -8.3; 5793 -3.9; 6373 -0.8; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -8.3; 13660 -12.4; 15026 -19.0; 16529 -24.3; 18182 -22.4; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT01S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT01S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 176 Hz   | 0.49 | -4.8 dB  |
| Peaking | 927 Hz   | 0.92 | 2.9 dB   |
| Peaking | 3432 Hz  | 3.07 | 5.3 dB   |
| Peaking | 11147 Hz | 0.59 | 11.8 dB  |
| Peaking | 16672 Hz | 0.5  | -24.6 dB |
| Peaking | 19 Hz    | 1.4  | 1.0 dB   |
| Peaking | 4149 Hz  | 5.91 | 2.0 dB   |
| Peaking | 5095 Hz  | 4.61 | -5.8 dB  |
| Peaking | 6448 Hz  | 3.85 | 5.5 dB   |
| Peaking | 8018 Hz  | 2.37 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB   |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 16000 Hz | 1.41 | -21.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/iBasso%20IT01S/iBasso%20IT01S.png)