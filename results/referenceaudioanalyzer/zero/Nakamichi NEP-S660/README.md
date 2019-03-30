# Nakamichi NEP-S660
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.9; 54 -1.4; 60 -2.0; 66 -2.4; 72 -2.7; 79 -3.1; 87 -3.4; 96 -3.7; 106 -4.0; 116 -4.2; 128 -4.4; 141 -4.6; 155 -4.9; 170 -5.0; 187 -5.2; 206 -5.3; 227 -5.6; 249 -5.9; 274 -5.9; 302 -5.9; 332 -6.3; 365 -6.7; 402 -7.2; 442 -7.7; 486 -8.0; 535 -8.4; 588 -8.7; 647 -8.8; 712 -8.8; 783 -8.4; 861 -7.7; 947 -6.6; 1042 -5.3; 1146 -3.8; 1261 -2.2; 1387 -0.6; 1526 -0.5; 1678 -0.5; 1846 -1.2; 2031 -2.6; 2234 -4.6; 2457 -8.4; 2703 -13.1; 2973 -15.9; 3270 -16.0; 3597 -13.6; 3957 -10.5; 4353 -8.5; 4788 -8.3; 5267 -10.7; 5793 -13.3; 6373 -12.9; 7010 -8.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nakamichi NEP-S660 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nakamichi NEP-S660 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.29 | 6.1 dB   |
| Peaking | 777 Hz  | 0.97 | -6.0 dB  |
| Peaking | 1666 Hz | 0.73 | 10.2 dB  |
| Peaking | 3043 Hz | 2.05 | -15.2 dB |
| Peaking | 5991 Hz | 4.88 | -7.5 dB  |
| Peaking | 295 Hz  | 4.13 | 0.5 dB   |
| Peaking | 3564 Hz | 8.57 | -1.2 dB  |
| Peaking | 4424 Hz | 7.31 | 1.2 dB   |
| Peaking | 6624 Hz | 8.68 | -2.5 dB  |
| Peaking | 7291 Hz | 5.24 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -8.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Nakamichi%20NEP-S660/Nakamichi%20NEP-S660.png)