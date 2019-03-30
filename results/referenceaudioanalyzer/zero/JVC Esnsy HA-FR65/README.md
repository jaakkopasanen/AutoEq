# JVC Esnsy HA-FR65
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.5; 25 -7.0; 28 -7.6; 31 -8.1; 34 -8.4; 37 -8.6; 41 -8.8; 45 -9.0; 49 -9.1; 54 -9.2; 60 -9.3; 66 -9.3; 72 -9.3; 79 -9.3; 87 -9.3; 96 -9.2; 106 -9.0; 116 -8.9; 128 -8.8; 141 -8.6; 155 -8.3; 170 -8.1; 187 -7.8; 206 -7.3; 227 -7.0; 249 -7.0; 274 -7.0; 302 -6.9; 332 -6.6; 365 -6.2; 402 -5.7; 442 -5.2; 486 -4.8; 535 -4.3; 588 -3.7; 647 -3.2; 712 -2.7; 783 -2.3; 861 -2.0; 947 -1.7; 1042 -1.2; 1146 -0.9; 1261 -0.7; 1387 -0.5; 1526 -0.7; 1678 -1.0; 1846 -1.5; 2031 -2.3; 2234 -3.5; 2457 -5.4; 2703 -8.4; 2973 -11.6; 3270 -13.0; 3597 -12.1; 3957 -9.8; 4353 -8.3; 4788 -8.2; 5267 -9.6; 5793 -11.2; 6373 -10.7; 7010 -7.0; 7711 -5.2; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC Esnsy HA-FR65 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC Esnsy HA-FR65 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 81 Hz   | 0.32 | -3.8 dB  |
| Peaking | 1630 Hz | 0.52 | 6.2 dB   |
| Peaking | 3227 Hz | 2.02 | -11.1 dB |
| Peaking | 6086 Hz | 2.75 | -6.7 dB  |
| Peaking | 7392 Hz | 4    | 2.7 dB   |
| Peaking | 17 Hz   | 1.11 | 2.0 dB   |
| Peaking | 32 Hz   | 0.86 | -0.7 dB  |
| Peaking | 294 Hz  | 0.93 | 0.9 dB   |
| Peaking | 331 Hz  | 1.68 | -1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20Esnsy%20HA-FR65/JVC%20Esnsy%20HA-FR65.png)