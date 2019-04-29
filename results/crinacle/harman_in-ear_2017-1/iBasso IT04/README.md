# iBasso IT04
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.2; 25 -6.4; 28 -6.6; 31 -6.7; 34 -6.8; 37 -6.9; 41 -7.1; 45 -7.2; 49 -7.2; 54 -7.4; 60 -7.6; 66 -7.8; 72 -8.0; 79 -8.3; 87 -8.6; 96 -8.9; 106 -9.2; 116 -9.5; 128 -9.7; 141 -9.9; 155 -10.1; 170 -10.1; 187 -10.1; 206 -10.1; 227 -10.0; 249 -9.8; 274 -9.5; 302 -9.2; 332 -8.6; 365 -8.1; 402 -7.7; 442 -7.2; 486 -6.8; 535 -6.4; 588 -6.1; 647 -5.7; 712 -5.6; 783 -5.6; 861 -5.6; 947 -5.7; 1042 -6.1; 1146 -6.7; 1261 -7.2; 1387 -7.6; 1526 -7.7; 1678 -7.6; 1846 -7.0; 2031 -5.8; 2234 -5.1; 2457 -4.4; 2703 -2.7; 2973 -1.9; 3270 -2.4; 3597 -3.4; 3957 -2.3; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.5; 6373 -3.2; 7010 -5.7; 7711 -9.6; 8482 -9.8; 9330 -8.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -11.6; 15026 -19.0; 16529 -21.0; 18182 -17.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT04 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT04 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 169 Hz   | 0.72 | -3.9 dB  |
| Peaking | 2932 Hz  | 6.33 | 2.1 dB   |
| Peaking | 7332 Hz  | 0.66 | 10.6 dB  |
| Peaking | 8035 Hz  | 2.3  | -12.9 dB |
| Peaking | 16437 Hz | 1.1  | -17.3 dB |
| Peaking | 751 Hz   | 1.68 | 1.5 dB   |
| Peaking | 1553 Hz  | 2.1  | -2.4 dB  |
| Peaking | 4532 Hz  | 5.28 | 1.6 dB   |
| Peaking | 12793 Hz | 5.24 | 3.6 dB   |
| Peaking | 14672 Hz | 4.54 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB   |
| Peaking | 62 Hz    | 1.41 | -0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -15.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/iBasso%20IT04/iBasso%20IT04.png)