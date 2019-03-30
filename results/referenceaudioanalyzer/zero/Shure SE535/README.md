# Shure SE535
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.0; 25 -8.3; 28 -8.5; 31 -8.7; 34 -8.8; 37 -8.9; 41 -9.0; 45 -9.1; 49 -9.2; 54 -9.2; 60 -9.2; 66 -9.2; 72 -9.2; 79 -9.2; 87 -9.2; 96 -9.2; 106 -9.2; 116 -9.2; 128 -9.2; 141 -8.9; 155 -8.9; 170 -8.9; 187 -8.9; 206 -8.9; 227 -8.9; 249 -8.6; 274 -8.6; 302 -8.6; 332 -8.6; 365 -8.6; 402 -8.5; 442 -8.3; 486 -8.2; 535 -8.0; 588 -7.9; 647 -7.7; 712 -7.6; 783 -7.3; 861 -7.2; 947 -6.9; 1042 -6.7; 1146 -6.4; 1261 -6.2; 1387 -6.0; 1526 -6.0; 1678 -6.0; 1846 -6.3; 2031 -6.6; 2234 -6.6; 2457 -6.2; 2703 -6.0; 2973 -6.3; 3270 -6.9; 3597 -6.7; 3957 -5.5; 4353 -3.5; 4788 -1.9; 5267 -1.2; 5793 -0.6; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE535 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.65 | -0.7 dB |
| Peaking | 92 Hz   | 0.27 | -3.0 dB |
| Peaking | 492 Hz  | 0.77 | -1.2 dB |
| Peaking | 3436 Hz | 3.83 | -1.9 dB |
| Peaking | 5613 Hz | 2.28 | 6.1 dB  |
| Peaking | 1493 Hz | 2.65 | 0.5 dB  |
| Peaking | 2070 Hz | 4.72 | -0.7 dB |
| Peaking | 4614 Hz | 5.22 | 1.6 dB  |
| Peaking | 6509 Hz | 5.03 | 4.1 dB  |
| Peaking | 6623 Hz | 1.65 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SE535/Shure%20SE535.png)