# JVC HA-FX1X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -11.1; 25 -11.6; 28 -12.3; 31 -12.7; 34 -13.0; 37 -13.3; 41 -13.5; 45 -13.7; 49 -13.8; 54 -13.9; 60 -14.1; 66 -14.1; 72 -14.0; 79 -13.8; 87 -13.8; 96 -13.5; 106 -13.5; 116 -13.2; 128 -13.0; 141 -12.7; 155 -12.4; 170 -12.2; 187 -11.9; 206 -11.6; 227 -11.0; 249 -10.5; 274 -9.9; 302 -9.3; 332 -8.8; 365 -8.2; 402 -7.5; 442 -6.7; 486 -5.7; 535 -4.8; 588 -3.7; 647 -2.7; 712 -1.6; 783 -0.6; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -1.0; 2234 -2.7; 2457 -5.1; 2703 -8.4; 2973 -12.7; 3270 -16.4; 3597 -17.5; 3957 -15.5; 4353 -12.7; 4788 -11.9; 5267 -12.7; 5793 -12.8; 6373 -10.8; 7010 -5.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FX1X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FX1X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 50 Hz   | 0.4  | -6.7 dB  |
| Peaking | 274 Hz  | 0.42 | -5.4 dB  |
| Peaking | 1479 Hz | 0.29 | 9.8 dB   |
| Peaking | 3485 Hz | 1.8  | -18.3 dB |
| Peaking | 5633 Hz | 3.22 | -6.5 dB  |
| Peaking | 790 Hz  | 2.82 | 1.5 dB   |
| Peaking | 1270 Hz | 0.88 | -0.9 dB  |
| Peaking | 2018 Hz | 3.02 | 2.1 dB   |
| Peaking | 4716 Hz | 0.13 | -0.3 dB  |
| Peaking | 7148 Hz | 9.76 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB  |
| Peaking | 62 Hz    | 1.41 | -6.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -12.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 16000 Hz | 1.41 | 0.0 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-FX1X/JVC%20HA-FX1X.png)