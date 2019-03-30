# Grado GR 10e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -7.7; 25 -7.8; 28 -7.9; 31 -7.9; 34 -7.9; 37 -8.0; 41 -8.1; 45 -8.2; 49 -8.2; 54 -8.2; 60 -8.2; 66 -8.2; 72 -8.2; 79 -8.2; 87 -8.2; 96 -8.0; 106 -7.9; 116 -7.8; 128 -7.5; 141 -7.7; 155 -8.3; 170 -8.9; 187 -9.2; 206 -9.1; 227 -8.9; 249 -8.7; 274 -8.5; 302 -8.5; 332 -8.3; 365 -8.2; 402 -8.0; 442 -7.9; 486 -7.8; 535 -7.5; 588 -7.4; 647 -7.2; 712 -6.8; 783 -6.3; 861 -5.4; 947 -4.1; 1042 -2.7; 1146 -1.9; 1261 -1.5; 1387 -1.6; 1526 -1.9; 1678 -2.6; 1846 -3.2; 2031 -4.1; 2234 -5.8; 2457 -7.3; 2703 -8.7; 2973 -9.5; 3270 -8.5; 3597 -5.4; 3957 -4.6; 4353 -7.4; 4788 -8.1; 5267 -5.6; 5793 -2.1; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR 10e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR 10e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.54 | -2.0 dB |
| Peaking | 690 Hz  | 0.17 | -3.3 dB |
| Peaking | 1356 Hz | 0.98 | 7.8 dB  |
| Peaking | 2841 Hz | 4.09 | -3.9 dB |
| Peaking | 6299 Hz | 4.87 | 6.6 dB  |
| Peaking | 136 Hz  | 3.89 | 0.9 dB  |
| Peaking | 184 Hz  | 2.7  | -0.9 dB |
| Peaking | 383 Hz  | 2.8  | 0.4 dB  |
| Peaking | 3839 Hz | 9.01 | 3.1 dB  |
| Peaking | 4691 Hz | 7.31 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20GR%2010e/Grado%20GR%2010e.png)