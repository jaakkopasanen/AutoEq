# JVC HA-RX900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.9; 25 -7.4; 28 -8.1; 31 -8.5; 34 -8.8; 37 -8.9; 41 -9.0; 45 -9.1; 49 -9.2; 54 -9.3; 60 -9.5; 66 -9.7; 72 -9.9; 79 -10.1; 87 -10.3; 96 -10.5; 106 -10.6; 116 -10.9; 128 -10.9; 141 -10.7; 155 -10.4; 170 -10.0; 187 -9.7; 206 -9.6; 227 -9.3; 249 -9.1; 274 -8.8; 302 -8.6; 332 -8.1; 365 -7.5; 402 -6.9; 442 -6.2; 486 -5.4; 535 -4.6; 588 -3.7; 647 -3.2; 712 -4.3; 783 -6.2; 861 -7.2; 947 -7.5; 1042 -7.7; 1146 -7.8; 1261 -7.5; 1387 -7.0; 1526 -6.2; 1678 -5.1; 1846 -3.9; 2031 -2.8; 2234 -1.8; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -2.9; 3597 -8.8; 3957 -11.0; 4353 -9.8; 4788 -6.4; 5267 -5.8; 5793 -6.8; 6373 -7.3; 7010 -6.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-RX900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-RX900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 2.03 | -1.0 dB |
| Peaking | 119 Hz  | 0.46 | -4.2 dB |
| Peaking | 599 Hz  | 3.34 | 4.1 dB  |
| Peaking | 2783 Hz | 1.95 | 7.8 dB  |
| Peaking | 3867 Hz | 3.88 | -7.7 dB |
| Peaking | 12 Hz   | 1.8  | 1.7 dB  |
| Peaking | 769 Hz  | 1.08 | 1.9 dB  |
| Peaking | 1026 Hz | 1.23 | -3.1 dB |
| Peaking | 1967 Hz | 3.18 | 1.5 dB  |
| Peaking | 6425 Hz | 8.82 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-RX900/JVC%20HA-RX900.png)