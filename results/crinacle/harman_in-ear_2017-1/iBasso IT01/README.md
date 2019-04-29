# iBasso IT01
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.6; 25 -11.6; 28 -11.5; 31 -11.5; 34 -11.4; 37 -11.3; 41 -11.2; 45 -11.2; 49 -11.1; 54 -11.0; 60 -11.0; 66 -11.0; 72 -11.0; 79 -11.1; 87 -11.1; 96 -11.3; 106 -11.4; 116 -11.5; 128 -11.5; 141 -11.6; 155 -11.6; 170 -11.5; 187 -11.4; 206 -11.3; 227 -11.2; 249 -11.0; 274 -10.8; 302 -10.4; 332 -10.0; 365 -9.6; 402 -9.3; 442 -8.9; 486 -8.5; 535 -8.0; 588 -7.4; 647 -6.8; 712 -6.1; 783 -5.4; 861 -4.8; 947 -4.4; 1042 -4.3; 1146 -4.6; 1261 -4.9; 1387 -4.9; 1526 -4.5; 1678 -4.1; 1846 -3.6; 2031 -3.1; 2234 -2.5; 2457 -2.0; 2703 -1.5; 2973 -0.9; 3270 -0.5; 3597 -0.6; 3957 -1.6; 4353 -3.4; 4788 -5.9; 5267 -6.6; 5793 -4.2; 6373 -2.4; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.7; 13660 -11.7; 15026 -20.5; 16529 -26.6; 18182 -23.7; 20000 -11.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iBasso IT01 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iBasso IT01 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.43 | -2.7 dB  |
| Peaking | 35 Hz    | 0.3  | -3.2 dB  |
| Peaking | 212 Hz   | 0.48 | -4.4 dB  |
| Peaking | 5899 Hz  | 0.18 | 4.9 dB   |
| Peaking | 17053 Hz | 0.97 | -24.8 dB |
| Peaking | 3412 Hz  | 2.88 | 2.3 dB   |
| Peaking | 4678 Hz  | 5.04 | -1.3 dB  |
| Peaking | 5107 Hz  | 5.81 | -3.9 dB  |
| Peaking | 12482 Hz | 3.12 | 4.5 dB   |
| Peaking | 15390 Hz | 3.79 | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 16000 Hz | 1.41 | -21.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/iBasso%20IT01/iBasso%20IT01.png)