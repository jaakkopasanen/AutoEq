# Grado GR8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.7; 25 -4.8; 28 -5.1; 31 -5.3; 34 -5.5; 37 -5.7; 41 -5.9; 45 -5.9; 49 -5.9; 54 -6.0; 60 -6.4; 66 -6.8; 72 -7.2; 79 -7.6; 87 -7.9; 96 -8.4; 106 -8.8; 116 -9.0; 128 -9.4; 141 -9.8; 155 -10.1; 170 -10.2; 187 -10.3; 206 -10.4; 227 -10.4; 249 -10.4; 274 -10.3; 302 -10.2; 332 -10.1; 365 -9.9; 402 -9.8; 442 -9.5; 486 -9.3; 535 -9.0; 588 -8.5; 647 -8.2; 712 -7.6; 783 -7.0; 861 -6.5; 947 -6.1; 1042 -6.1; 1146 -6.5; 1261 -6.7; 1387 -6.7; 1526 -6.2; 1678 -5.3; 1846 -4.2; 2031 -3.4; 2234 -4.6; 2457 -3.9; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -1.3; 3957 -7.0; 4353 -6.9; 4788 -3.9; 5267 -3.0; 5793 -5.0; 6373 -9.0; 7010 -5.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.16 | 2.0 dB  |
| Peaking | 214 Hz   | 0.39 | -4.4 dB |
| Peaking | 925 Hz   | 2    | 1.4 dB  |
| Peaking | 2991 Hz  | 2.17 | 6.5 dB  |
| Peaking | 22050 Hz | 2.32 | 0.9 dB  |
| Peaking | 1942 Hz  | 7.92 | 2.1 dB  |
| Peaking | 3533 Hz  | 7.61 | 3.9 dB  |
| Peaking | 4083 Hz  | 3.35 | -5.4 dB |
| Peaking | 5137 Hz  | 2.95 | 4.4 dB  |
| Peaking | 6375 Hz  | 8.59 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Grado%20GR8/Grado%20GR8.png)