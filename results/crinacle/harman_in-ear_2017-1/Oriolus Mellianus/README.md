# Oriolus Mellianus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -5.4; 25 -5.8; 28 -6.4; 31 -6.8; 34 -7.1; 37 -7.4; 41 -7.6; 45 -7.9; 49 -8.1; 54 -8.4; 60 -8.6; 66 -8.8; 72 -9.0; 79 -9.2; 87 -9.5; 96 -9.6; 106 -9.7; 116 -9.9; 128 -9.9; 141 -9.8; 155 -9.7; 170 -9.5; 187 -9.3; 206 -9.1; 227 -8.8; 249 -8.4; 274 -8.1; 302 -7.8; 332 -7.3; 365 -6.9; 402 -6.7; 442 -6.5; 486 -6.3; 535 -6.1; 588 -6.0; 647 -5.9; 712 -5.9; 783 -5.9; 861 -6.1; 947 -6.6; 1042 -7.5; 1146 -8.7; 1261 -9.9; 1387 -10.6; 1526 -10.7; 1678 -10.3; 1846 -9.2; 2031 -7.3; 2234 -5.1; 2457 -3.3; 2703 -2.3; 2973 -2.4; 3270 -3.8; 3597 -5.3; 3957 -3.3; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.7; 6373 -3.9; 7010 -7.2; 7711 -7.0; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.5; 13660 -16.7; 15026 -23.5; 16529 -27.3; 18182 -27.1; 20000 -19.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Mellianus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Mellianus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 127 Hz   | 0.57 | -3.5 dB  |
| Peaking | 1542 Hz  | 1.32 | -8.8 dB  |
| Peaking | 2595 Hz  | 5.22 | 2.4 dB   |
| Peaking | 9482 Hz  | 0.18 | 20.8 dB  |
| Peaking | 16778 Hz | 0.28 | -37.4 dB |
| Peaking | 20 Hz    | 2.24 | 2.1 dB   |
| Peaking | 3619 Hz  | 6.11 | -3.8 dB  |
| Peaking | 5581 Hz  | 1.56 | 4.4 dB   |
| Peaking | 7111 Hz  | 2.58 | -6.2 dB  |
| Peaking | 11833 Hz | 5.02 | 4.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB   |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 16000 Hz | 1.41 | -25.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Oriolus%20Mellianus/Oriolus%20Mellianus.png)