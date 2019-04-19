# Kaldas Research Conquest RR1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.2; 34 -1.8; 37 -2.4; 41 -3.1; 45 -3.7; 49 -4.2; 54 -4.8; 60 -5.5; 66 -6.1; 72 -6.7; 79 -7.4; 87 -7.9; 96 -8.4; 106 -8.8; 116 -9.0; 128 -9.0; 141 -8.9; 155 -8.6; 170 -8.5; 187 -8.5; 206 -8.7; 227 -8.8; 249 -8.7; 274 -8.4; 302 -8.4; 332 -8.5; 365 -8.4; 402 -8.4; 442 -8.4; 486 -8.0; 535 -7.2; 588 -6.5; 647 -6.4; 712 -6.6; 783 -7.1; 861 -7.6; 947 -8.3; 1042 -9.2; 1146 -10.2; 1261 -11.4; 1387 -12.3; 1526 -11.4; 1678 -8.8; 1846 -5.7; 2031 -2.9; 2234 -1.9; 2457 -1.0; 2703 -1.6; 2973 -3.7; 3270 -3.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -4.1; 5267 -7.6; 5793 -6.1; 6373 -6.4; 7010 -9.2; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -10.2; 12418 -10.7; 13660 -7.1; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kaldas Research Conquest RR1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kaldas Research Conquest RR1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.67 | 7.4 dB   |
| Peaking | 845 Hz   | 0.04 | -3.2 dB  |
| Peaking | 1429 Hz  | 1.61 | -14.9 dB |
| Peaking | 1833 Hz  | 0.6  | 13.0 dB  |
| Peaking | 4082 Hz  | 4.39 | 5.1 dB   |
| Peaking | 621 Hz   | 4.68 | 1.3 dB   |
| Peaking | 2498 Hz  | 8.84 | 1.6 dB   |
| Peaking | 10085 Hz | 2.09 | 7.5 dB   |
| Peaking | 11610 Hz | 1.17 | -9.8 dB  |
| Peaking | 14170 Hz | 1.24 | 5.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Kaldas%20Research%20Conquest%20RR1/Kaldas%20Research%20Conquest%20RR1.png)