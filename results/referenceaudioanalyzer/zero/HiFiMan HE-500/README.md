# HiFiMan HE-500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -2.4; 25 -4.0; 28 -6.1; 31 -7.9; 34 -9.4; 37 -10.6; 41 -11.7; 45 -12.2; 49 -12.4; 54 -12.2; 60 -11.7; 66 -11.2; 72 -10.7; 79 -10.1; 87 -9.6; 96 -9.3; 106 -9.0; 116 -8.8; 128 -8.8; 141 -8.6; 155 -8.5; 170 -8.5; 187 -8.2; 206 -8.2; 227 -8.2; 249 -8.0; 274 -7.9; 302 -7.9; 332 -8.0; 365 -8.2; 402 -8.2; 442 -8.2; 486 -8.1; 535 -8.1; 588 -8.2; 647 -8.1; 712 -7.7; 783 -7.5; 861 -7.8; 947 -7.9; 1042 -8.0; 1146 -8.1; 1261 -8.1; 1387 -7.7; 1526 -6.7; 1678 -5.4; 1846 -4.3; 2031 -3.7; 2234 -3.6; 2457 -3.8; 2703 -4.1; 2973 -4.7; 3270 -5.4; 3597 -5.7; 3957 -5.4; 4353 -5.3; 4788 -5.0; 5267 -3.6; 5793 -3.6; 6373 -7.7; 7010 -11.2; 7711 -13.0; 8482 -13.2; 9330 -13.1; 10263 -13.4; 11289 -13.2; 12418 -11.1; 13660 -8.1; 15026 -7.5; 16529 -7.5; 18182 -7.5; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan HE-500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan HE-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-8.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.87 | 11.1 dB |
| Peaking | 43 Hz    | 0.73 | -7.6 dB |
| Peaking | 2370 Hz  | 1.79 | 4.4 dB  |
| Peaking | 5513 Hz  | 2.09 | 7.7 dB  |
| Peaking | 8427 Hz  | 0.97 | -7.9 dB |
| Peaking | 904 Hz   | 0.53 | -0.8 dB |
| Peaking | 1859 Hz  | 5.32 | 1.6 dB  |
| Peaking | 9057 Hz  | 4.82 | 1.5 dB  |
| Peaking | 11477 Hz | 1.88 | -3.1 dB |
| Peaking | 13983 Hz | 1.39 | 2.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20HE-500/HiFiMan%20HE-500.png)