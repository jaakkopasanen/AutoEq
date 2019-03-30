# KZ ED12
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.7; 23 -9.0; 25 -9.3; 28 -9.7; 31 -10.0; 34 -10.2; 37 -10.3; 41 -10.4; 45 -10.5; 49 -10.6; 54 -10.7; 60 -10.8; 66 -10.8; 72 -10.8; 79 -10.7; 87 -10.6; 96 -10.4; 106 -10.4; 116 -10.4; 128 -10.1; 141 -10.1; 155 -9.8; 170 -9.8; 187 -9.5; 206 -9.3; 227 -9.0; 249 -8.7; 274 -8.4; 302 -8.0; 332 -7.7; 365 -7.3; 402 -7.0; 442 -6.6; 486 -6.3; 535 -6.0; 588 -5.7; 647 -5.4; 712 -5.2; 783 -5.0; 861 -4.9; 947 -4.9; 1042 -5.0; 1146 -5.3; 1261 -5.8; 1387 -6.4; 1526 -7.4; 1678 -8.7; 1846 -10.6; 2031 -13.1; 2234 -15.1; 2457 -15.9; 2703 -15.3; 2973 -14.4; 3270 -14.4; 3597 -14.5; 3957 -12.9; 4353 -9.6; 4788 -5.7; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ED12 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ED12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 39 Hz    | 0.55 | -3.0 dB  |
| Peaking | 133 Hz   | 0.47 | -3.0 dB  |
| Peaking | 1264 Hz  | 0.67 | 7.1 dB   |
| Peaking | 2699 Hz  | 0.65 | -13.6 dB |
| Peaking | 5726 Hz  | 2.06 | 12.1 dB  |
| Peaking | 1740 Hz  | 4.41 | 0.9 dB   |
| Peaking | 2371 Hz  | 2.59 | -2.0 dB  |
| Peaking | 2892 Hz  | 2.28 | 2.4 dB   |
| Peaking | 3686 Hz  | 5.03 | -2.3 dB  |
| Peaking | 12110 Hz | 1.59 | 0.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.6 dB |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/KZ%20ED12/KZ%20ED12.png)