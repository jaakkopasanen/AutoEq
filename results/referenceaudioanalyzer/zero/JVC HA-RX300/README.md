# JVC HA-RX300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.6; 45 -2.7; 49 -3.9; 54 -5.6; 60 -7.8; 66 -9.6; 72 -10.9; 79 -11.8; 87 -12.5; 96 -13.0; 106 -13.3; 116 -13.0; 128 -12.6; 141 -12.1; 155 -11.6; 170 -11.3; 187 -10.9; 206 -10.6; 227 -10.3; 249 -10.0; 274 -9.6; 302 -9.2; 332 -8.8; 365 -8.7; 402 -8.7; 442 -8.4; 486 -7.9; 535 -7.7; 588 -8.5; 647 -9.3; 712 -9.2; 783 -9.1; 861 -9.8; 947 -10.9; 1042 -12.0; 1146 -12.9; 1261 -13.4; 1387 -13.3; 1526 -12.1; 1678 -10.2; 1846 -7.9; 2031 -5.9; 2234 -4.2; 2457 -3.0; 2703 -2.2; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-RX300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-RX300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.5  | 10.4 dB |
| Peaking | 82 Hz   | 0.7  | -9.7 dB |
| Peaking | 141 Hz  | 0.45 | -2.6 dB |
| Peaking | 1308 Hz | 1.38 | -8.6 dB |
| Peaking | 3661 Hz | 0.8  | 7.5 dB  |
| Peaking | 2312 Hz | 4.51 | 0.9 dB  |
| Peaking | 3883 Hz | 4.34 | -0.6 dB |
| Peaking | 5501 Hz | 2.7  | 2.2 dB  |
| Peaking | 6418 Hz | 3.8  | 4.2 dB  |
| Peaking | 7094 Hz | 1.28 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 9.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-RX300/JVC%20HA-RX300.png)