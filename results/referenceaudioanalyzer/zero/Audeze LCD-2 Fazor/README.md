# Audeze LCD-2 Fazor
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -3.6; 25 -3.7; 28 -4.5; 31 -5.8; 34 -6.9; 37 -7.6; 41 -7.9; 45 -8.4; 49 -8.9; 54 -8.9; 60 -8.4; 66 -8.2; 72 -8.2; 79 -8.2; 87 -8.2; 96 -7.9; 106 -7.9; 116 -7.9; 128 -7.9; 141 -7.9; 155 -7.9; 170 -7.9; 187 -7.6; 206 -7.5; 227 -7.5; 249 -7.5; 274 -7.7; 302 -8.0; 332 -8.2; 365 -8.1; 402 -7.7; 442 -7.5; 486 -7.3; 535 -7.2; 588 -7.4; 647 -7.8; 712 -8.2; 783 -8.4; 861 -8.2; 947 -7.6; 1042 -6.5; 1146 -6.0; 1261 -6.7; 1387 -7.7; 1526 -7.6; 1678 -6.5; 1846 -4.9; 2031 -3.6; 2234 -2.4; 2457 -0.6; 2703 -0.5; 2973 -1.0; 3270 -4.8; 3597 -6.5; 3957 -6.1; 4353 -5.7; 4788 -6.7; 5267 -8.2; 5793 -9.4; 6373 -10.1; 7010 -9.0; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Fazor GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Fazor ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.27 | 4.3 dB  |
| Peaking | 44 Hz   | 0.89 | -2.8 dB |
| Peaking | 547 Hz  | 0.15 | -1.3 dB |
| Peaking | 2571 Hz | 2.31 | 7.5 dB  |
| Peaking | 6202 Hz | 3.65 | -3.9 dB |
| Peaking | 852 Hz  | 2.5  | -2.6 dB |
| Peaking | 1076 Hz | 1.35 | 2.5 dB  |
| Peaking | 1453 Hz | 3.78 | -2.4 dB |
| Peaking | 6989 Hz | 6.01 | -1.5 dB |
| Peaking | 7667 Hz | 3.89 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audeze%20LCD-2%20Fazor/Audeze%20LCD-2%20Fazor.png)