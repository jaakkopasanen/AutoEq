# JVC HA-SZ2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -13.4; 25 -13.6; 28 -13.6; 31 -13.5; 34 -13.3; 37 -13.0; 41 -12.4; 45 -11.7; 49 -11.1; 54 -10.5; 60 -10.5; 66 -10.9; 72 -11.2; 79 -11.4; 87 -11.6; 96 -11.7; 106 -11.7; 116 -11.5; 128 -11.2; 141 -10.8; 155 -10.2; 170 -9.7; 187 -9.2; 206 -8.5; 227 -7.4; 249 -6.8; 274 -6.9; 302 -7.5; 332 -8.1; 365 -8.6; 402 -9.1; 442 -9.1; 486 -9.0; 535 -8.7; 588 -8.4; 647 -8.4; 712 -8.3; 783 -8.0; 861 -7.0; 947 -5.6; 1042 -4.0; 1146 -3.1; 1261 -2.9; 1387 -2.2; 1526 -0.6; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -3.3; 2457 -5.9; 2703 -6.8; 2973 -7.1; 3270 -6.7; 3597 -5.8; 3957 -4.7; 4353 -4.3; 4788 -5.4; 5267 -6.2; 5793 -5.9; 6373 -6.3; 7010 -7.0; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.7; 12418 -8.9; 13660 -10.5; 15026 -9.3; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-SZ2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-SZ2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.67 | -7.1 dB |
| Peaking | 110 Hz   | 1.12 | -4.4 dB |
| Peaking | 544 Hz   | 1.27 | -2.8 dB |
| Peaking | 1623 Hz  | 1.65 | 6.8 dB  |
| Peaking | 13889 Hz | 2.68 | -4.5 dB |
| Peaking | 255 Hz   | 6.07 | 1.4 dB  |
| Peaking | 2068 Hz  | 6.12 | 2.9 dB  |
| Peaking | 2156 Hz  | 3.03 | 0.2 dB  |
| Peaking | 2710 Hz  | 1.94 | -2.5 dB |
| Peaking | 4203 Hz  | 3.62 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JVC%20HA-SZ2000/JVC%20HA-SZ2000.png)