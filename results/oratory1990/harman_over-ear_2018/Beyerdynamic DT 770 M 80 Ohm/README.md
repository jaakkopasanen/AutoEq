# Beyerdynamic DT 770 M 80 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -1.9; 96 -7.6; 106 -13.0; 116 -14.4; 128 -13.4; 141 -12.2; 155 -12.0; 170 -11.3; 187 -10.8; 206 -10.3; 227 -10.0; 249 -9.6; 274 -9.1; 302 -8.6; 332 -8.1; 365 -7.6; 402 -7.2; 442 -6.9; 486 -6.5; 535 -6.1; 588 -5.8; 647 -5.5; 712 -5.4; 783 -5.3; 861 -5.3; 947 -5.3; 1042 -5.4; 1146 -5.8; 1261 -6.1; 1387 -6.1; 1526 -6.3; 1678 -6.7; 1846 -7.2; 2031 -7.4; 2234 -6.8; 2457 -6.0; 2703 -5.6; 2973 -4.5; 3270 -1.5; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -1.9; 5267 -1.6; 5793 -0.8; 6373 -5.3; 7010 -7.3; 7711 -8.2; 8482 -6.8; 9330 -6.5; 10263 -6.5; 11289 -7.3; 12418 -11.2; 13660 -10.3; 15026 -6.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 M 80 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 M 80 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 79 Hz    | 0.48 | 21.1 dB  |
| Peaking | 117 Hz   | 0.8  | -24.9 dB |
| Peaking | 3808 Hz  | 2.68 | 6.5 dB   |
| Peaking | 5539 Hz  | 4.89 | 4.8 dB   |
| Peaking | 12900 Hz | 3.42 | -5.5 dB  |
| Peaking | 21 Hz    | 2.23 | 2.1 dB   |
| Peaking | 239 Hz   | 1.76 | -1.5 dB  |
| Peaking | 766 Hz   | 0.97 | 1.6 dB   |
| Peaking | 1991 Hz  | 3.04 | -1.7 dB  |
| Peaking | 7415 Hz  | 5.79 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 8.5 dB  |
| Peaking | 125 Hz   | 1.41 | -8.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20770%20M%2080%20Ohm/Beyerdynamic%20DT%20770%20M%2080%20Ohm.png)