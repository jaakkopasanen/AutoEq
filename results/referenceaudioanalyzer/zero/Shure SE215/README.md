# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -9.9; 28 -10.0; 31 -10.1; 34 -10.1; 37 -10.1; 41 -10.1; 45 -10.1; 49 -10.1; 54 -10.1; 60 -10.1; 66 -10.1; 72 -10.1; 79 -10.1; 87 -9.8; 96 -9.7; 106 -9.6; 116 -9.4; 128 -9.2; 141 -9.0; 155 -8.7; 170 -8.5; 187 -8.2; 206 -7.8; 227 -7.4; 249 -7.0; 274 -6.6; 302 -6.2; 332 -5.8; 365 -5.3; 402 -4.9; 442 -4.4; 486 -3.9; 535 -3.5; 588 -3.1; 647 -2.7; 712 -2.4; 783 -2.2; 861 -2.0; 947 -2.0; 1042 -1.9; 1146 -2.0; 1261 -2.2; 1387 -2.8; 1526 -3.5; 1678 -4.3; 1846 -5.3; 2031 -6.9; 2234 -8.5; 2457 -9.4; 2703 -8.7; 2973 -6.8; 3270 -4.4; 3597 -2.9; 3957 -4.1; 4353 -7.7; 4788 -10.5; 5267 -10.5; 5793 -6.9; 6373 -0.5; 7010 -1.7; 7711 -3.9; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.39 | -4.4 dB |
| Peaking | 109 Hz  | 0.35 | -4.7 dB |
| Peaking | 2030 Hz | 0.29 | 4.3 dB  |
| Peaking | 2382 Hz | 1.74 | -9.3 dB |
| Peaking | 4983 Hz | 4.19 | -9.8 dB |
| Peaking | 3587 Hz | 4.93 | 3.6 dB  |
| Peaking | 3693 Hz | 2.14 | -1.7 dB |
| Peaking | 5728 Hz | 9.82 | -2.3 dB |
| Peaking | 6595 Hz | 6.13 | 5.3 dB  |
| Peaking | 8530 Hz | 1.18 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SE215/Shure%20SE215.png)