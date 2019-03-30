# Shure SE315
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -9.9; 25 -9.8; 28 -9.7; 31 -9.6; 34 -9.5; 37 -9.5; 41 -9.5; 45 -9.4; 49 -9.3; 54 -9.2; 60 -9.2; 66 -9.2; 72 -9.2; 79 -9.2; 87 -9.2; 96 -9.1; 106 -8.9; 116 -8.9; 128 -8.9; 141 -8.9; 155 -9.0; 170 -9.2; 187 -9.2; 206 -9.2; 227 -9.2; 249 -9.2; 274 -9.2; 302 -9.2; 332 -9.2; 365 -9.1; 402 -9.2; 442 -9.2; 486 -9.4; 535 -9.5; 588 -9.5; 647 -9.7; 712 -9.8; 783 -10.1; 861 -10.4; 947 -10.8; 1042 -11.4; 1146 -12.0; 1261 -12.7; 1387 -13.3; 1526 -13.4; 1678 -13.3; 1846 -12.2; 2031 -10.2; 2234 -7.9; 2457 -5.6; 2703 -3.7; 2973 -2.2; 3270 -1.2; 3597 -1.3; 3957 -2.7; 4353 -4.4; 4788 -4.3; 5267 -1.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE315 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE315 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.24 | -3.3 dB |
| Peaking | 818 Hz   | 0.1  | -2.6 dB |
| Peaking | 1595 Hz  | 1.25 | -6.2 dB |
| Peaking | 3129 Hz  | 1.47 | 8.6 dB  |
| Peaking | 5969 Hz  | 3.12 | 6.9 dB  |
| Peaking | 2440 Hz  | 7.7  | 0.3 dB  |
| Peaking | 7827 Hz  | 6.92 | -0.8 dB |
| Peaking | 11455 Hz | 0.71 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | -5.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Shure%20SE315/Shure%20SE315.png)