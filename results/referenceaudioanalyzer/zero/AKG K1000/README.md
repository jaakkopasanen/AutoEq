# AKG K1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -2.2; 66 -3.3; 72 -4.1; 79 -4.6; 87 -4.9; 96 -4.9; 106 -4.9; 116 -4.6; 128 -4.5; 141 -4.2; 155 -3.9; 170 -3.8; 187 -3.6; 206 -3.6; 227 -3.3; 249 -3.2; 274 -3.2; 302 -3.2; 332 -3.2; 365 -3.2; 402 -3.2; 442 -3.2; 486 -3.2; 535 -3.5; 588 -3.4; 647 -3.2; 712 -3.4; 783 -3.6; 861 -3.7; 947 -4.1; 1042 -4.8; 1146 -5.4; 1261 -6.2; 1387 -7.3; 1526 -8.3; 1678 -8.6; 1846 -9.3; 2031 -10.8; 2234 -11.6; 2457 -11.0; 2703 -8.6; 2973 -6.1; 3270 -3.8; 3597 -4.5; 3957 -6.9; 4353 -8.7; 4788 -10.7; 5267 -12.3; 5793 -12.3; 6373 -11.7; 7010 -13.5; 7711 -15.2; 8482 -14.3; 9330 -11.8; 10263 -10.9; 11289 -12.1; 12418 -13.6; 13660 -13.8; 15026 -12.2; 16529 -8.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 55 Hz    | 0.01 | 3.2 dB  |
| Peaking | 2023 Hz  | 2.01 | -6.7 dB |
| Peaking | 7395 Hz  | 1.28 | -7.7 dB |
| Peaking | 13722 Hz | 1.53 | -7.0 dB |
| Peaking | 22050 Hz | 2.22 | -5.2 dB |
| Peaking | 51 Hz    | 0.45 | 5.1 dB  |
| Peaking | 88 Hz    | 0.88 | -5.7 dB |
| Peaking | 2491 Hz  | 4.21 | -2.7 dB |
| Peaking | 3374 Hz  | 4.31 | 4.0 dB  |
| Peaking | 5067 Hz  | 4.13 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.4 dB |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K1000/AKG%20K1000.png)