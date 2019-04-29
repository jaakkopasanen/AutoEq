# JVC HA-FW03
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.9; 31 -2.4; 34 -2.7; 37 -3.0; 41 -3.4; 45 -3.7; 49 -4.0; 54 -4.3; 60 -4.7; 66 -5.1; 72 -5.5; 79 -5.9; 87 -6.4; 96 -6.9; 106 -7.3; 116 -7.6; 128 -8.0; 141 -8.3; 155 -8.5; 170 -8.6; 187 -8.7; 206 -8.7; 227 -8.6; 249 -8.5; 274 -8.3; 302 -8.0; 332 -7.7; 365 -7.3; 402 -7.0; 442 -6.8; 486 -6.5; 535 -6.0; 588 -5.6; 647 -5.1; 712 -4.7; 783 -4.3; 861 -3.8; 947 -3.9; 1042 -4.2; 1146 -4.7; 1261 -5.2; 1387 -5.4; 1526 -5.4; 1678 -5.1; 1846 -4.8; 2031 -4.5; 2234 -4.3; 2457 -4.5; 2703 -5.0; 2973 -5.2; 3270 -4.7; 3597 -4.0; 3957 -3.6; 4353 -3.6; 4788 -3.9; 5267 -3.9; 5793 -2.9; 6373 -1.6; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -9.7; 15026 -21.5; 16529 -26.8; 18182 -25.1; 20000 -21.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FW03 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FW03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.44 | 5.8 dB   |
| Peaking | 185 Hz   | 0.74 | -3.7 dB  |
| Peaking | 7434 Hz  | 0.37 | 15.0 dB  |
| Peaking | 12958 Hz | 1.49 | 15.5 dB  |
| Peaking | 15809 Hz | 0.3  | -31.9 dB |
| Peaking | 866 Hz   | 2.16 | 2.1 dB   |
| Peaking | 2046 Hz  | 0.13 | -0.4 dB  |
| Peaking | 6607 Hz  | 5.16 | 3.3 dB   |
| Peaking | 7561 Hz  | 3.08 | -1.7 dB  |
| Peaking | 10488 Hz | 3.28 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB   |
| Peaking | 62 Hz    | 1.41 | 0.3 dB   |
| Peaking | 125 Hz   | 1.41 | -2.4 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 16000 Hz | 1.41 | -23.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/JVC%20HA-FW03/JVC%20HA-FW03.png)