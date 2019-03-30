# JBL Synchros S700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.9; 23 -14.5; 25 -14.1; 28 -13.9; 31 -13.9; 34 -14.3; 37 -14.8; 41 -15.2; 45 -15.0; 49 -14.6; 54 -14.9; 60 -16.0; 66 -17.1; 72 -17.9; 79 -18.3; 87 -18.1; 96 -17.5; 106 -16.7; 116 -15.7; 128 -14.6; 141 -13.3; 155 -11.7; 170 -10.1; 187 -8.7; 206 -7.4; 227 -6.1; 249 -5.3; 274 -4.9; 302 -4.3; 332 -3.6; 365 -2.9; 402 -2.5; 442 -2.3; 486 -1.7; 535 -1.2; 588 -1.5; 647 -2.5; 712 -3.1; 783 -3.3; 861 -3.0; 947 -2.0; 1042 -0.6; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -2.2; 2031 -4.8; 2234 -7.9; 2457 -10.5; 2703 -12.1; 2973 -12.5; 3270 -12.0; 3597 -11.0; 3957 -9.5; 4353 -8.2; 4788 -8.3; 5267 -10.1; 5793 -12.2; 6373 -13.4; 7010 -12.2; 7711 -8.6; 8482 -6.5; 9330 -6.7; 10263 -7.7; 11289 -7.4; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Synchros S700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Synchros S700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.21 | -7.2 dB  |
| Peaking | 95 Hz    | 0.95 | -9.7 dB  |
| Peaking | 1802 Hz  | 0.35 | 26.1 dB  |
| Peaking | 2621 Hz  | 0.44 | -27.4 dB |
| Peaking | 3436 Hz  | 2.71 | -0.6 dB  |
| Peaking | 4574 Hz  | 2.5  | 3.7 dB   |
| Peaking | 6517 Hz  | 1.99 | -6.4 dB  |
| Peaking | 8297 Hz  | 3.02 | 4.1 dB   |
| Peaking | 13774 Hz | 1    | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -9.0 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JBL%20Synchros%20S700/JBL%20Synchros%20S700.png)