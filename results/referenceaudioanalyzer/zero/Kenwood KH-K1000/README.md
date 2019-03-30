# Kenwood KH-K1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.0; 41 -2.0; 45 -2.9; 49 -3.6; 54 -4.3; 60 -5.0; 66 -5.5; 72 -6.2; 79 -7.0; 87 -7.8; 96 -8.3; 106 -8.6; 116 -8.9; 128 -9.0; 141 -8.8; 155 -8.6; 170 -8.3; 187 -7.7; 206 -7.0; 227 -6.1; 249 -5.4; 274 -4.9; 302 -4.4; 332 -4.2; 365 -4.1; 402 -4.1; 442 -4.6; 486 -5.2; 535 -5.6; 588 -5.5; 647 -4.9; 712 -4.7; 783 -5.3; 861 -5.7; 947 -5.5; 1042 -4.9; 1146 -4.0; 1261 -3.4; 1387 -3.4; 1526 -4.7; 1678 -6.4; 1846 -7.5; 2031 -8.0; 2234 -7.7; 2457 -7.3; 2703 -7.4; 2973 -8.1; 3270 -8.9; 3597 -9.9; 3957 -11.1; 4353 -12.3; 4788 -12.8; 5267 -12.3; 5793 -10.0; 6373 -5.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kenwood KH-K1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kenwood KH-K1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.58 | 6.8 dB  |
| Peaking | 136 Hz   | 0.57 | -4.7 dB |
| Peaking | 306 Hz   | 0.8  | 4.2 dB  |
| Peaking | 1281 Hz  | 3.7  | 3.5 dB  |
| Peaking | 4522 Hz  | 2.33 | -6.8 dB |
| Peaking | 1517 Hz  | 3.93 | 1.1 dB  |
| Peaking | 1925 Hz  | 2.89 | -1.7 dB |
| Peaking | 5517 Hz  | 5.86 | -2.4 dB |
| Peaking | 6735 Hz  | 5.38 | 4.5 dB  |
| Peaking | 20883 Hz | 1.31 | 0.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.8 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Kenwood%20KH-K1000/Kenwood%20KH-K1000.png)