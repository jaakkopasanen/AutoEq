# AKG K702
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.9; 54 -1.5; 60 -1.9; 66 -2.1; 72 -2.5; 79 -2.9; 87 -3.4; 96 -3.8; 106 -4.1; 116 -4.3; 128 -4.4; 141 -4.6; 155 -4.7; 170 -4.8; 187 -5.0; 206 -5.1; 227 -5.1; 249 -5.1; 274 -5.1; 302 -5.1; 332 -5.0; 365 -4.8; 402 -4.6; 442 -4.3; 486 -4.1; 535 -4.1; 588 -4.0; 647 -3.8; 712 -3.8; 783 -3.8; 861 -3.9; 947 -4.3; 1042 -4.6; 1146 -4.8; 1261 -4.8; 1387 -5.0; 1526 -5.2; 1678 -5.8; 1846 -7.0; 2031 -8.2; 2234 -9.0; 2457 -8.9; 2703 -7.8; 2973 -6.3; 3270 -5.1; 3597 -5.1; 3957 -6.2; 4353 -7.4; 4788 -8.1; 5267 -8.9; 5793 -10.3; 6373 -13.8; 7010 -16.9; 7711 -17.2; 8482 -14.8; 9330 -12.2; 10263 -10.7; 11289 -9.3; 12418 -7.9; 13660 -7.5; 15026 -7.3; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.43 | 6.3 dB   |
| Peaking | 288 Hz   | 1.68 | -0.4 dB  |
| Peaking | 1706 Hz  | 0.19 | 3.0 dB   |
| Peaking | 2212 Hz  | 2.21 | -5.2 dB  |
| Peaking | 7518 Hz  | 1.63 | -12.9 dB |
| Peaking | 1148 Hz  | 3.96 | -0.7 dB  |
| Peaking | 2636 Hz  | 7.82 | -0.9 dB  |
| Peaking | 3417 Hz  | 5.23 | 1.4 dB   |
| Peaking | 10728 Hz | 5.35 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.4 dB   |
| Peaking | 125 Hz   | 1.41 | 1.2 dB   |
| Peaking | 250 Hz   | 1.41 | 0.6 dB   |
| Peaking | 500 Hz   | 1.41 | 1.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -10.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K702/AKG%20K702.png)