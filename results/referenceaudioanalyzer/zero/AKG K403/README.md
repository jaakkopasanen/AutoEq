# AKG K403
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.4; 87 -2.2; 96 -2.9; 106 -3.4; 116 -3.9; 128 -4.2; 141 -4.3; 155 -4.5; 170 -4.6; 187 -4.6; 206 -4.5; 227 -4.2; 249 -4.2; 274 -4.1; 302 -3.9; 332 -3.7; 365 -3.6; 402 -3.6; 442 -3.5; 486 -3.3; 535 -3.3; 588 -3.3; 647 -3.3; 712 -3.3; 783 -3.3; 861 -3.2; 947 -3.4; 1042 -3.6; 1146 -3.7; 1261 -4.0; 1387 -4.3; 1526 -4.8; 1678 -5.4; 1846 -6.1; 2031 -7.2; 2234 -8.6; 2457 -11.1; 2703 -15.0; 2973 -17.5; 3270 -16.9; 3597 -14.3; 3957 -12.9; 4353 -11.1; 4788 -7.5; 5267 -7.8; 5793 -10.3; 6373 -10.4; 7010 -9.4; 7711 -9.2; 8482 -9.3; 9330 -10.2; 10263 -12.0; 11289 -13.6; 12418 -13.2; 13660 -10.2; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K403 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K403 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.44 | 6.6 dB   |
| Peaking | 953 Hz   | 0.35 | 3.8 dB   |
| Peaking | 3088 Hz  | 1.88 | -13.0 dB |
| Peaking | 11411 Hz | 1.54 | -7.2 dB  |
| Peaking | 22050 Hz | 2.09 | -5.1 dB  |
| Peaking | 71 Hz    | 1.92 | 2.8 dB   |
| Peaking | 72 Hz    | 0.93 | -1.7 dB  |
| Peaking | 5008 Hz  | 8.28 | 3.2 dB   |
| Peaking | 6108 Hz  | 3.93 | -2.5 dB  |
| Peaking | 15478 Hz | 3.37 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -6.9 dB |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K403/AKG%20K403.png)