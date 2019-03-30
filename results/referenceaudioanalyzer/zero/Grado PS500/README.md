# Grado PS500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.8; 49 -3.1; 54 -4.6; 60 -6.2; 66 -7.5; 72 -8.7; 79 -9.7; 87 -10.2; 96 -10.2; 106 -9.8; 116 -9.1; 128 -8.3; 141 -7.5; 155 -6.6; 170 -5.8; 187 -5.2; 206 -5.0; 227 -4.8; 249 -4.4; 274 -4.1; 302 -3.8; 332 -3.6; 365 -3.3; 402 -3.1; 442 -2.8; 486 -2.7; 535 -2.9; 588 -3.1; 647 -3.1; 712 -3.1; 783 -3.1; 861 -3.2; 947 -3.4; 1042 -3.6; 1146 -3.9; 1261 -4.3; 1387 -4.9; 1526 -5.4; 1678 -6.1; 1846 -7.9; 2031 -10.3; 2234 -11.9; 2457 -12.1; 2703 -11.3; 2973 -9.8; 3270 -7.5; 3597 -6.2; 3957 -9.3; 4353 -12.9; 4788 -13.4; 5267 -12.7; 5793 -11.9; 6373 -10.1; 7010 -7.1; 7711 -6.2; 8482 -6.5; 9330 -7.3; 10263 -9.7; 11289 -10.4; 12418 -9.1; 13660 -6.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.53 | 8.1 dB  |
| Peaking | 86 Hz    | 0.87 | -8.7 dB |
| Peaking | 588 Hz   | 0.21 | 3.8 dB  |
| Peaking | 2316 Hz  | 2.27 | -8.0 dB |
| Peaking | 5018 Hz  | 2.32 | -7.8 dB |
| Peaking | 2864 Hz  | 4.82 | -1.2 dB |
| Peaking | 3517 Hz  | 7.9  | 3.0 dB  |
| Peaking | 6150 Hz  | 5.21 | -2.0 dB |
| Peaking | 7488 Hz  | 2.5  | 2.4 dB  |
| Peaking | 11152 Hz | 2.72 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20PS500/Grado%20PS500.png)