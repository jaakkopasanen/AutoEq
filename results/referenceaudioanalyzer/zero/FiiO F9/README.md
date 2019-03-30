# FiiO F9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.6; 25 -3.9; 28 -4.1; 31 -4.3; 34 -4.4; 37 -4.5; 41 -4.6; 45 -4.6; 49 -4.6; 54 -4.6; 60 -4.6; 66 -4.6; 72 -4.6; 79 -4.6; 87 -4.6; 96 -4.5; 106 -4.3; 116 -4.0; 128 -3.9; 141 -3.9; 155 -4.0; 170 -3.8; 187 -3.6; 206 -3.6; 227 -3.2; 249 -3.0; 274 -2.8; 302 -2.6; 332 -2.4; 365 -2.2; 402 -2.0; 442 -1.8; 486 -1.5; 535 -1.3; 588 -1.1; 647 -1.0; 712 -0.7; 783 -0.7; 861 -0.7; 947 -0.7; 1042 -1.0; 1146 -1.4; 1261 -2.0; 1387 -2.8; 1526 -4.0; 1678 -5.4; 1846 -6.8; 2031 -7.8; 2234 -7.8; 2457 -6.9; 2703 -5.2; 2973 -3.0; 3270 -1.5; 3597 -1.1; 3957 -1.8; 4353 -2.9; 4788 -3.9; 5267 -3.5; 5793 -1.6; 6373 -0.5; 7010 -2.7; 7711 -5.6; 8482 -5.8; 9330 -3.2; 10263 -3.0; 11289 -3.0; 12418 -3.0; 13660 -3.0; 15026 -3.0; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FiiO F9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FiiO F9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 916 Hz  | 0.86 | 3.1 dB  |
| Peaking | 2141 Hz | 1.57 | -6.2 dB |
| Peaking | 3364 Hz | 3.19 | 3.7 dB  |
| Peaking | 6348 Hz | 6.13 | 3.4 dB  |
| Peaking | 8033 Hz | 5.06 | -3.7 dB |
| Peaking | 40 Hz   | 0.88 | -1.2 dB |
| Peaking | 95 Hz   | 0.82 | -1.2 dB |
| Peaking | 9894 Hz | 4.22 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/FiiO%20F9/FiiO%20F9.png)