# JVC HA-FXZ200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.4; 25 -11.7; 28 -12.2; 31 -12.6; 34 -13.0; 37 -13.3; 41 -13.6; 45 -13.8; 49 -14.0; 54 -14.1; 60 -14.1; 66 -14.1; 72 -14.1; 79 -14.0; 87 -13.8; 96 -13.6; 106 -13.3; 116 -13.0; 128 -12.5; 141 -12.1; 155 -11.6; 170 -11.2; 187 -10.9; 206 -11.1; 227 -10.7; 249 -10.2; 274 -9.4; 302 -8.6; 332 -7.9; 365 -7.2; 402 -6.4; 442 -5.7; 486 -5.0; 535 -4.4; 588 -3.8; 647 -3.2; 712 -2.6; 783 -2.2; 861 -1.8; 947 -1.5; 1042 -1.4; 1146 -1.1; 1261 -0.9; 1387 -0.8; 1526 -0.5; 1678 -0.6; 1846 -1.4; 2031 -3.0; 2234 -5.0; 2457 -7.1; 2703 -9.0; 2973 -10.1; 3270 -10.2; 3597 -9.7; 3957 -9.2; 4353 -9.3; 4788 -9.6; 5267 -9.1; 5793 -6.9; 6373 -2.8; 7010 -3.2; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FXZ200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FXZ200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 38 Hz   | 0.4  | -4.0 dB  |
| Peaking | 160 Hz  | 0.2  | -6.3 dB  |
| Peaking | 1367 Hz | 0.28 | 8.3 dB   |
| Peaking | 3039 Hz | 1.47 | -10.5 dB |
| Peaking | 4798 Hz | 3.16 | -5.2 dB  |
| Peaking | 161 Hz  | 5.89 | 0.5 dB   |
| Peaking | 1704 Hz | 5.64 | 1.1 dB   |
| Peaking | 5795 Hz | 0.12 | -0.2 dB  |
| Peaking | 6667 Hz | 6.88 | 4.8 dB   |
| Peaking | 7663 Hz | 1.27 | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -7.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.1 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-FXZ200/JVC%20HA-FXZ200.png)