# Nakamichi NEP-S800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.9; 25 -7.4; 28 -8.1; 31 -8.6; 34 -9.0; 37 -9.3; 41 -9.6; 45 -9.8; 49 -10.0; 54 -10.1; 60 -10.3; 66 -10.5; 72 -10.5; 79 -10.5; 87 -10.5; 96 -10.5; 106 -10.5; 116 -10.5; 128 -10.4; 141 -10.2; 155 -10.0; 170 -9.6; 187 -9.0; 206 -9.1; 227 -10.9; 249 -12.0; 274 -11.8; 302 -11.2; 332 -10.9; 365 -10.6; 402 -10.3; 442 -10.0; 486 -9.7; 535 -9.3; 588 -9.0; 647 -8.6; 712 -8.1; 783 -7.7; 861 -7.2; 947 -6.6; 1042 -6.0; 1146 -5.4; 1261 -4.6; 1387 -3.7; 1526 -2.9; 1678 -2.1; 1846 -1.2; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -2.8; 5793 -7.8; 6373 -13.0; 7010 -13.4; 7711 -9.4; 8482 -6.5; 9330 -7.4; 10263 -8.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nakamichi NEP-S800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nakamichi NEP-S800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 65 Hz    | 0.65 | -3.6 dB  |
| Peaking | 381 Hz   | 0.47 | -4.5 dB  |
| Peaking | 3865 Hz  | 0.37 | 7.9 dB   |
| Peaking | 6633 Hz  | 3.13 | -13.4 dB |
| Peaking | 10319 Hz | 1.2  | -3.5 dB  |
| Peaking | 195 Hz   | 5.23 | 1.8 dB   |
| Peaking | 253 Hz   | 5.1  | -1.8 dB  |
| Peaking | 2000 Hz  | 2.37 | 1.6 dB   |
| Peaking | 3034 Hz  | 0.58 | -1.0 dB  |
| Peaking | 4813 Hz  | 4.43 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Nakamichi%20NEP-S800/Nakamichi%20NEP-S800.png)