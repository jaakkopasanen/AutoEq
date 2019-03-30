# JVC HA-RX700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -3.1; 25 -3.9; 28 -4.8; 31 -5.5; 34 -6.0; 37 -6.4; 41 -6.6; 45 -6.7; 49 -6.7; 54 -6.7; 60 -6.7; 66 -6.9; 72 -7.0; 79 -7.0; 87 -7.0; 96 -7.0; 106 -7.0; 116 -7.3; 128 -7.1; 141 -7.0; 155 -6.9; 170 -6.6; 187 -6.4; 206 -6.4; 227 -6.6; 249 -6.9; 274 -7.2; 302 -7.4; 332 -7.4; 365 -7.2; 402 -6.9; 442 -6.5; 486 -5.6; 535 -3.9; 588 -3.0; 647 -4.3; 712 -5.4; 783 -6.0; 861 -6.3; 947 -6.9; 1042 -7.6; 1146 -8.0; 1261 -7.6; 1387 -6.5; 1526 -4.9; 1678 -3.4; 1846 -2.3; 2031 -1.9; 2234 -2.0; 2457 -1.7; 2703 -0.9; 2973 -1.2; 3270 -1.9; 3597 -1.2; 3957 -0.5; 4353 -3.7; 4788 -5.4; 5267 -5.2; 5793 -5.5; 6373 -6.5; 7010 -7.3; 7711 -8.9; 8482 -9.8; 9330 -9.1; 10263 -7.9; 11289 -7.8; 12418 -7.9; 13660 -5.7; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-RX700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-RX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.4  | 4.0 dB  |
| Peaking | 417 Hz  | 0.1  | -1.9 dB |
| Peaking | 583 Hz  | 3.89 | 4.4 dB  |
| Peaking | 2891 Hz | 0.99 | 6.4 dB  |
| Peaking | 8765 Hz | 1.37 | -4.4 dB |
| Peaking | 13 Hz   | 0.39 | -0.7 dB |
| Peaking | 194 Hz  | 3.06 | 1.1 dB  |
| Peaking | 1207 Hz | 3.34 | -2.5 dB |
| Peaking | 1832 Hz | 3.06 | 1.9 dB  |
| Peaking | 2607 Hz | 2.88 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-RX700/JVC%20HA-RX700.png)