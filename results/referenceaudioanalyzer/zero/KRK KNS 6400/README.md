# KRK KNS 6400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.9; 25 -2.4; 28 -2.9; 31 -2.9; 34 -2.8; 37 -2.4; 41 -1.7; 45 -1.0; 49 -0.5; 54 -0.6; 60 -1.7; 66 -2.5; 72 -2.7; 79 -3.6; 87 -4.9; 96 -5.8; 106 -6.6; 116 -7.1; 128 -6.9; 141 -6.5; 155 -5.9; 170 -5.0; 187 -4.2; 206 -4.1; 227 -5.2; 249 -6.3; 274 -6.9; 302 -7.2; 332 -7.5; 365 -7.5; 402 -7.0; 442 -6.3; 486 -6.3; 535 -7.0; 588 -7.7; 647 -7.6; 712 -6.5; 783 -5.6; 861 -5.2; 947 -4.8; 1042 -4.3; 1146 -4.2; 1261 -4.2; 1387 -4.0; 1526 -3.9; 1678 -4.5; 1846 -5.5; 2031 -6.4; 2234 -7.4; 2457 -8.5; 2703 -8.7; 2973 -7.2; 3270 -5.0; 3597 -3.7; 3957 -3.0; 4353 -2.4; 4788 -2.7; 5267 -4.7; 5793 -6.5; 6373 -6.4; 7010 -5.0; 7711 -5.5; 8482 -5.8; 9330 -6.0; 10263 -6.0; 11289 -7.1; 12418 -9.0; 13660 -9.7; 15026 -8.4; 16529 -6.0; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK KNS 6400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK KNS 6400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.26 | 4.2 dB  |
| Peaking | 52 Hz    | 2.06 | 5.2 dB  |
| Peaking | 2621 Hz  | 4.35 | -3.9 dB |
| Peaking | 4210 Hz  | 2.64 | 3.8 dB  |
| Peaking | 13552 Hz | 2.11 | -4.3 dB |
| Peaking | 121 Hz   | 3.29 | -2.0 dB |
| Peaking | 199 Hz   | 3.71 | 2.3 dB  |
| Peaking | 322 Hz   | 1.95 | -2.0 dB |
| Peaking | 616 Hz   | 4.31 | -2.2 dB |
| Peaking | 1254 Hz  | 1.81 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/KRK%20KNS%206400/KRK%20KNS%206400.png)