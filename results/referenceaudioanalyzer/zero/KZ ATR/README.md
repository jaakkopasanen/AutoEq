# KZ ATR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.1; 25 -2.8; 28 -3.6; 31 -4.4; 34 -5.0; 37 -5.5; 41 -6.1; 45 -6.7; 49 -7.1; 54 -7.6; 60 -8.0; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.2; 96 -9.5; 106 -9.6; 116 -9.7; 128 -9.9; 141 -9.9; 155 -9.9; 170 -9.9; 187 -9.9; 206 -9.9; 227 -9.7; 249 -9.6; 274 -9.3; 302 -9.1; 332 -8.9; 365 -8.5; 402 -8.2; 442 -7.9; 486 -7.5; 535 -7.1; 588 -6.6; 647 -6.1; 712 -5.6; 783 -5.1; 861 -4.6; 947 -4.1; 1042 -3.8; 1146 -3.7; 1261 -3.9; 1387 -4.1; 1526 -4.4; 1678 -4.8; 1846 -5.5; 2031 -6.3; 2234 -7.3; 2457 -8.3; 2703 -8.9; 2973 -8.9; 3270 -8.9; 3597 -9.2; 3957 -9.9; 4353 -10.2; 4788 -9.1; 5267 -5.8; 5793 -0.9; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KZ ATR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KZ ATR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.83 | 5.7 dB  |
| Peaking | 152 Hz   | 0.31 | -4.2 dB |
| Peaking | 1127 Hz  | 0.97 | 3.5 dB  |
| Peaking | 4376 Hz  | 0.91 | -6.0 dB |
| Peaking | 6093 Hz  | 2.92 | 10.2 dB |
| Peaking | 1761 Hz  | 3.88 | 0.6 dB  |
| Peaking | 2621 Hz  | 2.53 | -1.2 dB |
| Peaking | 3425 Hz  | 2.73 | 1.2 dB  |
| Peaking | 4546 Hz  | 5.82 | -0.9 dB |
| Peaking | 11220 Hz | 1.67 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB |
| Peaking | 8000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/KZ%20ATR/KZ%20ATR.png)