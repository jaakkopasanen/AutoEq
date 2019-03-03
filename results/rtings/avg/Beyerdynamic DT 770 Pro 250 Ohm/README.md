# Beyerdynamic DT 770 Pro 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.8; 25 -7.0; 28 -7.4; 31 -7.6; 34 -7.7; 37 -7.7; 41 -7.5; 45 -7.2; 49 -6.8; 54 -6.4; 60 -6.0; 66 -6.0; 72 -6.0; 79 -6.0; 87 -6.2; 96 -6.4; 106 -6.6; 116 -6.5; 128 -6.3; 141 -5.7; 155 -4.7; 170 -3.6; 187 -2.7; 206 -2.2; 227 -2.6; 249 -3.2; 274 -4.0; 302 -4.6; 332 -5.0; 365 -5.3; 402 -5.7; 442 -6.1; 486 -6.2; 535 -6.1; 588 -6.0; 647 -5.9; 712 -5.8; 783 -5.8; 861 -5.6; 947 -5.4; 1042 -5.2; 1146 -5.2; 1261 -5.7; 1387 -6.2; 1526 -6.5; 1678 -7.0; 1846 -7.4; 2031 -8.1; 2234 -8.2; 2457 -7.5; 2703 -6.1; 2973 -4.3; 3270 -1.3; 3597 -0.5; 3957 -6.1; 4353 -9.2; 4788 -7.1; 5267 -5.2; 5793 -6.4; 6373 -10.7; 7010 -9.4; 7711 -10.6; 8482 -14.3; 9330 -13.9; 10263 -8.3; 11289 -6.2; 12418 -9.3; 13660 -13.0; 15026 -12.0; 16529 -11.4; 18182 -14.9; 20000 -17.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 Pro 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 Pro 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 215 Hz   |  2.13 | 4.1 dB   |
| Peaking | 2155 Hz  |  3.59 | -2.4 dB  |
| Peaking | 3413 Hz  |  6.44 | 7.2 dB   |
| Peaking | 8673 Hz  |  3.5  | -7.6 dB  |
| Peaking | 19801 Hz |  0.35 | -10.9 dB |
| Peaking | 34 Hz    |  1.59 | -1.7 dB  |
| Peaking | 6453 Hz  | 10.76 | -3.3 dB  |
| Peaking | 11195 Hz |  4.71 | 4.2 dB   |
| Peaking | 13611 Hz |  4.52 | -3.4 dB  |
| Peaking | 20095 Hz |  4.14 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | 3.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.1 dB |
| Peaking | 16000 Hz | 1.41 | -8.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beyerdynamic%20DT%20770%20Pro%20250%20Ohm/Beyerdynamic%20DT%20770%20Pro%20250%20Ohm.png)