# JVC HA-RX500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.7; 41 -1.6; 45 -2.9; 49 -4.0; 54 -5.1; 60 -6.1; 66 -7.1; 72 -8.2; 79 -9.1; 87 -9.5; 96 -10.0; 106 -10.5; 116 -11.0; 128 -11.0; 141 -11.0; 155 -10.9; 170 -11.0; 187 -11.0; 206 -10.8; 227 -10.7; 249 -10.6; 274 -10.3; 302 -9.9; 332 -9.5; 365 -9.2; 402 -9.1; 442 -9.0; 486 -9.1; 535 -9.1; 588 -8.7; 647 -7.9; 712 -7.6; 783 -8.1; 861 -8.7; 947 -9.3; 1042 -9.8; 1146 -10.3; 1261 -10.4; 1387 -10.3; 1526 -9.7; 1678 -8.2; 1846 -6.1; 2031 -3.8; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.8; 5267 -2.1; 5793 -2.5; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.3; 10263 -7.7; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-RX500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-RX500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.55 | 9.0 dB  |
| Peaking | 85 Hz   | 0.48 | -5.8 dB |
| Peaking | 251 Hz  | 0.48 | -2.2 dB |
| Peaking | 1404 Hz | 1.32 | -7.1 dB |
| Peaking | 2887 Hz | 0.73 | 8.1 dB  |
| Peaking | 991 Hz  | 6.42 | -0.5 dB |
| Peaking | 2333 Hz | 6.68 | 1.1 dB  |
| Peaking | 3093 Hz | 3.6  | -1.1 dB |
| Peaking | 6534 Hz | 1.35 | 2.8 dB  |
| Peaking | 8494 Hz | 1.3  | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | -4.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-RX500/JVC%20HA-RX500.png)