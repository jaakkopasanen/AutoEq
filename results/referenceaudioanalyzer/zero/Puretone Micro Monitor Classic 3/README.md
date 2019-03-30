# Puretone Micro Monitor Classic 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -13.5; 25 -13.5; 28 -13.5; 31 -13.5; 34 -13.5; 37 -13.5; 41 -13.5; 45 -13.5; 49 -13.5; 54 -13.5; 60 -13.5; 66 -13.6; 72 -13.8; 79 -13.8; 87 -13.8; 96 -13.8; 106 -13.8; 116 -13.8; 128 -13.8; 141 -13.8; 155 -13.8; 170 -13.6; 187 -13.5; 206 -13.5; 227 -13.5; 249 -13.5; 274 -13.5; 302 -13.5; 332 -13.3; 365 -13.2; 402 -13.2; 442 -13.2; 486 -13.1; 535 -13.1; 588 -12.9; 647 -12.8; 712 -12.9; 783 -13.1; 861 -13.2; 947 -13.2; 1042 -13.2; 1146 -13.2; 1261 -13.2; 1387 -13.2; 1526 -13.5; 1678 -14.5; 1846 -16.0; 2031 -16.4; 2234 -14.1; 2457 -11.4; 2703 -10.0; 2973 -9.3; 3270 -6.3; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Puretone Micro Monitor Classic 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Puretone Micro Monitor Classic 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.17 | -6.4 dB |
| Peaking | 180 Hz  | 0.33 | -5.5 dB |
| Peaking | 987 Hz  | 0.46 | -4.3 dB |
| Peaking | 2051 Hz | 1.67 | -7.7 dB |
| Peaking | 4495 Hz | 1.32 | 8.8 dB  |
| Peaking | 3108 Hz | 5.03 | -4.7 dB |
| Peaking | 3581 Hz | 2.19 | 4.4 dB  |
| Peaking | 4398 Hz | 3.07 | -2.9 dB |
| Peaking | 6341 Hz | 3.29 | 4.2 dB  |
| Peaking | 7410 Hz | 1.64 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.0 dB  |
| Peaking | 62 Hz    | 1.41 | -5.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -10.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Puretone%20Micro%20Monitor%20Classic%203/Puretone%20Micro%20Monitor%20Classic%203.png)