# Roland RH-A30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.7; 25 -2.4; 28 -3.2; 31 -3.8; 34 -4.3; 37 -4.7; 41 -5.0; 45 -5.4; 49 -5.6; 54 -5.8; 60 -5.8; 66 -5.8; 72 -5.9; 79 -6.2; 87 -6.4; 96 -6.4; 106 -6.6; 116 -6.7; 128 -6.8; 141 -6.6; 155 -6.4; 170 -6.3; 187 -6.0; 206 -5.7; 227 -5.5; 249 -5.9; 274 -6.1; 302 -6.1; 332 -5.9; 365 -5.7; 402 -5.5; 442 -5.5; 486 -5.5; 535 -5.4; 588 -5.5; 647 -5.4; 712 -5.5; 783 -5.8; 861 -5.8; 947 -6.0; 1042 -5.8; 1146 -5.8; 1261 -6.1; 1387 -6.8; 1526 -7.5; 1678 -8.0; 1846 -7.9; 2031 -7.1; 2234 -6.3; 2457 -5.8; 2703 -5.7; 2973 -5.8; 3270 -5.4; 3597 -4.6; 3957 -5.5; 4353 -7.5; 4788 -7.4; 5267 -4.9; 5793 -1.5; 6373 -0.5; 7010 -3.4; 7711 -5.9; 8482 -9.5; 9330 -11.8; 10263 -11.9; 11289 -10.2; 12418 -8.1; 13660 -6.8; 15026 -6.5; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Roland RH-A30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Roland RH-A30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.71 | 5.0 dB  |
| Peaking | 1748 Hz | 3.11 | -2.6 dB |
| Peaking | 4819 Hz | 2.89 | -7.2 dB |
| Peaking | 6009 Hz | 1.37 | 9.8 dB  |
| Peaking | 9495 Hz | 1.55 | -8.8 dB |
| Peaking | 30 Hz   | 1.9  | 0.4 dB  |
| Peaking | 119 Hz  | 1.73 | -1.0 dB |
| Peaking | 546 Hz  | 1.01 | 0.6 dB  |
| Peaking | 1491 Hz | 5.64 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Roland%20RH-A30/Roland%20RH-A30.png)