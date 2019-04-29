# Oriolus Mellianus
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.2; 25 -4.7; 28 -5.3; 31 -5.7; 34 -6.0; 37 -6.2; 41 -6.5; 45 -6.8; 49 -7.0; 54 -7.2; 60 -7.4; 66 -7.6; 72 -7.8; 79 -8.0; 87 -8.3; 96 -8.5; 106 -8.5; 116 -8.7; 128 -8.7; 141 -8.7; 155 -8.5; 170 -8.3; 187 -8.2; 206 -7.9; 227 -7.6; 249 -7.3; 274 -7.0; 302 -6.7; 332 -6.4; 365 -6.1; 402 -5.9; 442 -5.7; 486 -5.5; 535 -5.4; 588 -5.3; 647 -5.3; 712 -5.2; 783 -5.2; 861 -5.4; 947 -5.8; 1042 -6.7; 1146 -8.0; 1261 -9.4; 1387 -10.4; 1526 -10.8; 1678 -10.5; 1846 -9.4; 2031 -7.9; 2234 -6.3; 2457 -5.0; 2703 -4.4; 2973 -4.7; 3270 -6.1; 3597 -7.3; 3957 -4.9; 4353 -1.4; 4788 -0.5; 5267 -0.5; 5793 -1.6; 6373 -5.4; 7010 -9.5; 7711 -10.0; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -7.8; 15026 -7.2; 16529 -8.4; 18182 -10.6; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oriolus Mellianus GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oriolus Mellianus ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 3.19 | 2.8 dB  |
| Peaking | 1538 Hz  | 3.13 | -5.1 dB |
| Peaking | 5215 Hz  | 2.09 | 7.3 dB  |
| Peaking | 7260 Hz  | 3.96 | -6.1 dB |
| Peaking | 18433 Hz | 1.15 | -4.3 dB |
| Peaking | 93 Hz    | 1.25 | -1.3 dB |
| Peaking | 157 Hz   | 1.07 | -1.7 dB |
| Peaking | 638 Hz   | 1.03 | 1.7 dB  |
| Peaking | 2449 Hz  | 0.93 | -1.6 dB |
| Peaking | 2652 Hz  | 3.55 | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Oriolus%20Mellianus/Oriolus%20Mellianus.png)