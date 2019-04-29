# iBasso IT01 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.2; 25 -11.2; 28 -11.1; 31 -11.0; 34 -10.9; 37 -10.8; 41 -10.7; 45 -10.7; 49 -10.5; 54 -10.4; 60 -10.4; 66 -10.4; 72 -10.5; 79 -10.5; 87 -10.6; 96 -10.7; 106 -10.9; 116 -10.9; 128 -10.9; 141 -11.0; 155 -11.0; 170 -10.9; 187 -10.8; 206 -10.6; 227 -10.5; 249 -10.4; 274 -10.1; 302 -9.8; 332 -9.3; 365 -8.9; 402 -8.6; 442 -8.2; 486 -7.8; 535 -7.3; 588 -6.8; 647 -6.3; 712 -5.7; 783 -5.0; 861 -4.4; 947 -3.8; 1042 -3.6; 1146 -4.0; 1261 -4.2; 1387 -4.2; 1526 -3.8; 1678 -3.4; 1846 -3.1; 2031 -2.7; 2234 -2.2; 2457 -1.9; 2703 -1.5; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -1.3; 4353 -3.2; 4788 -6.3; 5267 -8.2; 5793 -5.8; 6373 -3.8; 7010 -5.6; 7711 -6.3; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -7.4; 13660 -12.7; 15026 -21.0; 16529 -26.3; 18182 -23.6; 20000 -15.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT01 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT01 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.66 | -3.7 dB  |
| Peaking | 29 Hz    | 0.55 | -3.2 dB  |
| Peaking | 181 Hz   | 0.36 | -4.9 dB  |
| Peaking | 5059 Hz  | 0.15 | 4.4 dB   |
| Peaking | 17155 Hz | 0.85 | -24.3 dB |
| Peaking | 1503 Hz  | 3.39 | -1.1 dB  |
| Peaking | 3551 Hz  | 2.17 | 2.6 dB   |
| Peaking | 5144 Hz  | 4.14 | -5.8 dB  |
| Peaking | 12077 Hz | 2.56 | 4.7 dB   |
| Peaking | 15356 Hz | 3.53 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 16000 Hz | 1.41 | -22.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/iBasso%20IT01%20sample%201/iBasso%20IT01%20sample%201.png)