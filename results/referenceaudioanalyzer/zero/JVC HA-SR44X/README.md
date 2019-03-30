# JVC HA-SR44X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.2; 34 -2.6; 37 -4.1; 41 -5.9; 45 -7.4; 49 -8.5; 54 -9.5; 60 -10.0; 66 -10.1; 72 -9.9; 79 -9.5; 87 -9.2; 96 -9.0; 106 -8.8; 116 -8.8; 128 -8.5; 141 -8.4; 155 -8.4; 170 -8.4; 187 -8.4; 206 -8.2; 227 -8.0; 249 -7.7; 274 -7.4; 302 -7.5; 332 -7.6; 365 -7.6; 402 -7.5; 442 -7.5; 486 -7.5; 535 -7.6; 588 -8.0; 647 -8.7; 712 -9.3; 783 -10.0; 861 -10.8; 947 -11.3; 1042 -11.4; 1146 -11.4; 1261 -11.6; 1387 -11.7; 1526 -11.4; 1678 -10.5; 1846 -9.0; 2031 -6.8; 2234 -4.3; 2457 -2.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -4.1; 5793 -8.0; 6373 -8.1; 7010 -7.4; 7711 -9.5; 8482 -10.7; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-SR44X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-SR44X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.66 | 12.8 dB  |
| Peaking | 49 Hz   | 0.59 | -10.0 dB |
| Peaking | 1471 Hz | 0.75 | -12.3 dB |
| Peaking | 3220 Hz | 0.49 | 13.1 dB  |
| Peaking | 7152 Hz | 1.08 | -8.6 dB  |
| Peaking | 782 Hz  | 1.13 | 1.3 dB   |
| Peaking | 847 Hz  | 2.41 | -2.2 dB  |
| Peaking | 3744 Hz | 3.23 | -1.8 dB  |
| Peaking | 5196 Hz | 2.11 | 3.7 dB   |
| Peaking | 5678 Hz | 5.41 | -5.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-SR44X/JVC%20HA-SR44X.png)