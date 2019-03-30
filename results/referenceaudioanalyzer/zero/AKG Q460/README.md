# AKG Q460
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.8; 25 -5.1; 28 -5.4; 31 -5.6; 34 -5.8; 37 -6.0; 41 -6.1; 45 -6.3; 49 -6.4; 54 -6.5; 60 -6.5; 66 -6.5; 72 -6.7; 79 -6.9; 87 -7.1; 96 -7.3; 106 -7.5; 116 -7.8; 128 -7.8; 141 -7.8; 155 -7.8; 170 -7.8; 187 -7.8; 206 -7.8; 227 -7.6; 249 -7.4; 274 -7.0; 302 -6.6; 332 -6.2; 365 -5.8; 402 -5.3; 442 -4.7; 486 -4.1; 535 -3.3; 588 -2.7; 647 -2.3; 712 -2.8; 783 -4.3; 861 -6.0; 947 -7.0; 1042 -7.7; 1146 -8.1; 1261 -8.1; 1387 -7.8; 1526 -7.0; 1678 -5.6; 1846 -3.9; 2031 -2.4; 2234 -1.4; 2457 -0.5; 2703 -0.5; 2973 -2.1; 3270 -4.5; 3597 -6.3; 3957 -6.7; 4353 -5.5; 4788 -4.9; 5267 -6.1; 5793 -7.5; 6373 -7.6; 7010 -5.7; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q460 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q460 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 160 Hz  | 0.51 | -2.7 dB |
| Peaking | 647 Hz  | 1.45 | 5.2 dB  |
| Peaking | 1172 Hz | 1.01 | -5.0 dB |
| Peaking | 2576 Hz | 1.39 | 9.8 dB  |
| Peaking | 3361 Hz | 1.05 | -4.9 dB |
| Peaking | 19 Hz   | 2.16 | 1.1 dB  |
| Peaking | 3854 Hz | 5.44 | -1.3 dB |
| Peaking | 4747 Hz | 3.17 | 2.2 dB  |
| Peaking | 6175 Hz | 2.98 | -3.0 dB |
| Peaking | 7308 Hz | 3.76 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.5 dB |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20Q460/AKG%20Q460.png)