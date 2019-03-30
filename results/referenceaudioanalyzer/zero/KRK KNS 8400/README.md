# KRK KNS 8400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.5; 25 -6.2; 28 -5.8; 31 -5.5; 34 -5.2; 37 -5.0; 41 -4.9; 45 -4.9; 49 -5.1; 54 -5.8; 60 -6.9; 66 -7.7; 72 -8.1; 79 -8.6; 87 -9.4; 96 -10.0; 106 -10.5; 116 -10.9; 128 -10.9; 141 -10.3; 155 -9.4; 170 -8.7; 187 -7.9; 206 -7.2; 227 -6.7; 249 -6.7; 274 -6.7; 302 -6.3; 332 -5.3; 365 -3.9; 402 -2.4; 442 -1.0; 486 -0.5; 535 -1.1; 588 -2.0; 647 -1.9; 712 -1.5; 783 -1.6; 861 -1.6; 947 -1.2; 1042 -1.2; 1146 -1.4; 1261 -1.8; 1387 -1.7; 1526 -1.4; 1678 -1.8; 1846 -2.7; 2031 -3.5; 2234 -4.2; 2457 -4.6; 2703 -4.5; 2973 -3.7; 3270 -2.9; 3597 -3.0; 3957 -3.5; 4353 -3.8; 4788 -3.8; 5267 -4.4; 5793 -5.4; 6373 -5.8; 7010 -5.7; 7711 -6.0; 8482 -7.2; 9330 -8.3; 10263 -8.5; 11289 -8.4; 12418 -8.8; 13660 -8.8; 15026 -7.4; 16529 -5.0; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK KNS 8400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK KNS 8400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 121 Hz   | 0.85 | -6.3 dB |
| Peaking | 477 Hz   | 3.13 | 3.9 dB  |
| Peaking | 1043 Hz  | 0.9  | 3.5 dB  |
| Peaking | 3892 Hz  | 2.35 | 1.5 dB  |
| Peaking | 11762 Hz | 0.9  | -4.5 dB |
| Peaking | 17 Hz    | 1.08 | -2.5 dB |
| Peaking | 44 Hz    | 2.53 | 1.5 dB  |
| Peaking | 291 Hz   | 6.32 | -1.2 dB |
| Peaking | 2293 Hz  | 1.39 | 1.7 dB  |
| Peaking | 2382 Hz  | 2.65 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/KRK%20KNS%208400/KRK%20KNS%208400.png)