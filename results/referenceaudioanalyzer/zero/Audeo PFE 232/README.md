# Audeo PFE 232
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.2; 25 -11.3; 28 -11.3; 31 -11.4; 34 -11.4; 37 -11.3; 41 -11.3; 45 -11.3; 49 -11.3; 54 -11.3; 60 -11.3; 66 -11.4; 72 -11.3; 79 -11.1; 87 -11.0; 96 -10.9; 106 -10.7; 116 -10.4; 128 -10.4; 141 -10.2; 155 -10.0; 170 -9.7; 187 -9.3; 206 -8.9; 227 -8.5; 249 -8.1; 274 -7.7; 302 -7.2; 332 -6.7; 365 -6.2; 402 -5.6; 442 -5.1; 486 -4.4; 535 -3.9; 588 -3.4; 647 -2.9; 712 -2.4; 783 -1.9; 861 -1.6; 947 -1.2; 1042 -1.0; 1146 -0.8; 1261 -0.6; 1387 -0.6; 1526 -0.6; 1678 -0.5; 1846 -0.9; 2031 -1.4; 2234 -1.6; 2457 -1.1; 2703 -1.0; 2973 -1.9; 3270 -3.8; 3597 -4.9; 3957 -4.6; 4353 -3.4; 4788 -2.5; 5267 -1.7; 5793 -1.9; 6373 -3.1; 7010 -2.5; 7711 -3.8; 8482 -4.1; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeo PFE 232 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 232 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 43 Hz   |  0.13 | -7.3 dB |
| Peaking | 1182 Hz |  0.51 | 4.0 dB  |
| Peaking | 2884 Hz |  2.64 | 2.4 dB  |
| Peaking | 3525 Hz |  2.52 | -3.4 dB |
| Peaking | 5366 Hz |  2.89 | 2.3 dB  |
| Peaking | 1670 Hz | 10.15 | 0.4 dB  |
| Peaking | 6394 Hz |  7.61 | -0.3 dB |
| Peaking | 7025 Hz |  8.7  | 1.2 dB  |
| Peaking | 8329 Hz |  2.17 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audeo%20PFE%20232/Audeo%20PFE%20232.png)