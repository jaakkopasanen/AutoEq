# HiFiMan HE-400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.6; 25 -4.5; 28 -5.6; 31 -6.5; 34 -7.1; 37 -7.6; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.5; 60 -8.4; 66 -8.4; 72 -8.4; 79 -8.4; 87 -8.2; 96 -8.1; 106 -8.1; 116 -8.0; 128 -7.8; 141 -7.8; 155 -7.5; 170 -7.5; 187 -7.5; 206 -7.5; 227 -8.0; 249 -8.6; 274 -8.7; 302 -7.8; 332 -7.2; 365 -7.4; 402 -8.0; 442 -8.5; 486 -8.1; 535 -6.8; 588 -6.1; 647 -6.7; 712 -8.2; 783 -9.7; 861 -10.8; 947 -11.8; 1042 -12.3; 1146 -11.6; 1261 -9.7; 1387 -7.2; 1526 -4.8; 1678 -3.4; 1846 -2.1; 2031 -0.6; 2234 -0.5; 2457 -1.4; 2703 -2.8; 2973 -2.8; 3270 -1.6; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -3.0; 5267 -5.0; 5793 -7.8; 6373 -10.4; 7010 -10.7; 7711 -8.7; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -8.6; 12418 -9.3; 13660 -6.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan HE-400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan HE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 4.05 | 4.2 dB  |
| Peaking | 1057 Hz  | 1.64 | -7.2 dB |
| Peaking | 2000 Hz  | 1.56 | 6.5 dB  |
| Peaking | 4015 Hz  | 1.93 | 5.9 dB  |
| Peaking | 6645 Hz  | 2.98 | -5.8 dB |
| Peaking | 17 Hz    | 1.83 | 3.9 dB  |
| Peaking | 61 Hz    | 0.71 | -2.1 dB |
| Peaking | 319 Hz   | 0.79 | -1.2 dB |
| Peaking | 606 Hz   | 4.73 | 2.4 dB  |
| Peaking | 12105 Hz | 5.04 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.9 dB |
| Peaking | 2000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20HE-400/HiFiMan%20HE-400.png)