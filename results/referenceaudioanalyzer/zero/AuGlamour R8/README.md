# AuGlamour R8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.0; 23 -17.0; 25 -17.0; 28 -16.9; 31 -16.8; 34 -16.7; 37 -16.6; 41 -16.5; 45 -16.3; 49 -16.1; 54 -15.9; 60 -15.6; 66 -15.3; 72 -15.0; 79 -14.6; 87 -14.3; 96 -13.9; 106 -13.5; 116 -13.1; 128 -12.6; 141 -12.1; 155 -11.7; 170 -11.3; 187 -10.8; 206 -10.1; 227 -9.5; 249 -8.8; 274 -8.2; 302 -7.5; 332 -6.9; 365 -6.2; 402 -5.7; 442 -5.1; 486 -4.6; 535 -4.1; 588 -3.7; 647 -3.3; 712 -3.1; 783 -2.8; 861 -2.7; 947 -3.0; 1042 -3.2; 1146 -3.6; 1261 -4.1; 1387 -5.2; 1526 -6.7; 1678 -8.7; 1846 -11.2; 2031 -13.3; 2234 -13.8; 2457 -12.5; 2703 -10.0; 2973 -7.7; 3270 -7.0; 3597 -8.6; 3957 -11.4; 4353 -12.5; 4788 -10.8; 5267 -5.6; 5793 -0.5; 6373 -0.8; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AuGlamour R8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AuGlamour R8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 14 Hz   | 0.38 | -7.1 dB  |
| Peaking | 69 Hz   | 0.28 | -7.2 dB  |
| Peaking | 1808 Hz | 0.27 | 7.3 dB   |
| Peaking | 2136 Hz | 1.45 | -14.7 dB |
| Peaking | 4323 Hz | 4.11 | -9.9 dB  |
| Peaking | 4962 Hz | 7.04 | -3.6 dB  |
| Peaking | 6025 Hz | 2.52 | 7.2 dB   |
| Peaking | 7585 Hz | 0.68 | -2.1 dB  |
| Peaking | 7622 Hz | 3.02 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AuGlamour%20R8/AuGlamour%20R8.png)