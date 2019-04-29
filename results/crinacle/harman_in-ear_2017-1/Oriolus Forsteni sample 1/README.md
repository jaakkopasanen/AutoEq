# Oriolus Forsteni sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -10.9; 25 -10.9; 28 -10.8; 31 -10.8; 34 -10.7; 37 -10.7; 41 -10.6; 45 -10.5; 49 -10.4; 54 -10.3; 60 -10.3; 66 -10.3; 72 -10.3; 79 -10.3; 87 -10.4; 96 -10.5; 106 -10.5; 116 -10.5; 128 -10.4; 141 -10.4; 155 -10.3; 170 -10.1; 187 -10.0; 206 -9.8; 227 -9.5; 249 -9.3; 274 -9.1; 302 -8.8; 332 -8.4; 365 -8.1; 402 -7.9; 442 -7.6; 486 -7.4; 535 -7.1; 588 -6.9; 647 -6.6; 712 -6.4; 783 -6.1; 861 -6.0; 947 -6.2; 1042 -6.6; 1146 -7.3; 1261 -8.0; 1387 -8.2; 1526 -7.6; 1678 -6.2; 1846 -4.7; 2031 -3.4; 2234 -2.5; 2457 -2.1; 2703 -1.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -2.4; 5793 -4.8; 6373 -10.5; 7010 -14.7; 7711 -13.2; 8482 -10.6; 9330 -8.2; 10263 -6.5; 11289 -6.5; 12418 -6.7; 13660 -13.8; 15026 -22.9; 16529 -29.8; 18182 -29.9; 20000 -17.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Forsteni sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Forsteni sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.82 | -2.7 dB  |
| Peaking | 98 Hz    | 0.23 | -3.7 dB  |
| Peaking | 7242 Hz  | 2.67 | -17.4 dB |
| Peaking | 7997 Hz  | 0.39 | 14.7 dB  |
| Peaking | 17244 Hz | 0.66 | -31.2 dB |
| Peaking | 1414 Hz  | 1.49 | -6.6 dB  |
| Peaking | 1633 Hz  | 0.53 | 3.1 dB   |
| Peaking | 8810 Hz  | 3.87 | -2.7 dB  |
| Peaking | 12565 Hz | 2.97 | 5.1 dB   |
| Peaking | 15294 Hz | 2.81 | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -24.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Oriolus%20Forsteni%20sample%201/Oriolus%20Forsteni%20sample%201.png)