# Ikko OH-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.5; 25 -7.5; 28 -7.6; 31 -7.6; 34 -7.7; 37 -7.7; 41 -7.6; 45 -7.6; 49 -7.6; 54 -7.6; 60 -7.5; 66 -7.4; 72 -7.4; 79 -7.4; 87 -7.4; 96 -7.4; 106 -7.2; 116 -7.1; 128 -6.9; 141 -6.8; 155 -6.7; 170 -6.5; 187 -6.2; 206 -5.9; 227 -5.4; 249 -5.0; 274 -4.5; 302 -3.9; 332 -3.3; 365 -2.7; 402 -2.3; 442 -2.0; 486 -1.7; 535 -1.3; 588 -1.0; 647 -0.7; 712 -0.5; 783 -0.5; 861 -0.6; 947 -0.9; 1042 -1.3; 1146 -1.9; 1261 -2.4; 1387 -2.8; 1526 -3.1; 1678 -3.3; 1846 -3.5; 2031 -3.8; 2234 -4.4; 2457 -4.6; 2703 -4.2; 2973 -3.4; 3270 -2.7; 3597 -2.5; 3957 -3.3; 4353 -4.5; 4788 -4.9; 5267 -4.3; 5793 -2.3; 6373 -1.9; 7010 -4.3; 7711 -4.3; 8482 -3.3; 9330 -3.3; 10263 -3.3; 11289 -3.3; 12418 -3.3; 13660 -3.3; 15026 -3.3; 16529 -3.3; 18182 -3.3; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ikko OH-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ikko OH-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 50 Hz   |  0.15 | -4.4 dB |
| Peaking | 610 Hz  |  0.69 | 3.7 dB  |
| Peaking | 2243 Hz |  2.45 | -1.6 dB |
| Peaking | 4831 Hz |  5.13 | -2.0 dB |
| Peaking | 6079 Hz |  8.6  | 2.0 dB  |
| Peaking | 960 Hz  |  2.17 | 1.4 dB  |
| Peaking | 1073 Hz |  1.29 | -1.1 dB |
| Peaking | 3467 Hz |  6.36 | 1.2 dB  |
| Peaking | 7334 Hz | 10.32 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Ikko%20OH-1/Ikko%20OH-1.png)