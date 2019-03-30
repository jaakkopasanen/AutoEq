# Fostex T7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.7; 25 -2.7; 28 -4.0; 31 -5.1; 34 -6.0; 37 -6.8; 41 -7.5; 45 -8.0; 49 -8.4; 54 -8.8; 60 -9.1; 66 -9.4; 72 -9.5; 79 -9.4; 87 -9.2; 96 -9.1; 106 -8.9; 116 -8.8; 128 -8.6; 141 -8.3; 155 -8.0; 170 -7.8; 187 -7.4; 206 -7.1; 227 -6.8; 249 -6.2; 274 -5.5; 302 -4.6; 332 -3.8; 365 -3.4; 402 -3.3; 442 -3.5; 486 -4.1; 535 -5.4; 588 -6.8; 647 -7.6; 712 -7.9; 783 -7.7; 861 -7.4; 947 -7.1; 1042 -6.8; 1146 -6.5; 1261 -6.1; 1387 -5.7; 1526 -5.4; 1678 -5.2; 1846 -4.9; 2031 -4.7; 2234 -5.1; 2457 -5.5; 2703 -6.0; 2973 -6.7; 3270 -7.4; 3597 -7.6; 3957 -8.8; 4353 -10.6; 4788 -10.3; 5267 -6.6; 5793 -0.5; 6373 -0.8; 7010 -3.7; 7711 -6.0; 8482 -6.6; 9330 -6.6; 10263 -6.8; 11289 -7.7; 12418 -8.4; 13660 -8.6; 15026 -7.7; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.01 | 7.9 dB  |
| Peaking | 63 Hz    | 0.44 | -3.8 dB |
| Peaking | 371 Hz   | 2.3  | 3.8 dB  |
| Peaking | 4626 Hz  | 3.09 | -6.1 dB |
| Peaking | 6014 Hz  | 4.12 | 8.1 dB  |
| Peaking | 483 Hz   | 4.28 | 1.8 dB  |
| Peaking | 714 Hz   | 1.74 | -2.1 dB |
| Peaking | 1924 Hz  | 2.09 | 1.8 dB  |
| Peaking | 13396 Hz | 1.45 | -2.7 dB |
| Peaking | 16446 Hz | 2.04 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fostex%20T7/Fostex%20T7.png)