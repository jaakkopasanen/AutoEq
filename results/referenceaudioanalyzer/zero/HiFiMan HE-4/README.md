# HiFiMan HE-4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.7; 25 -7.2; 28 -7.8; 31 -8.0; 34 -8.0; 37 -8.0; 41 -7.9; 45 -7.7; 49 -7.6; 54 -7.4; 60 -7.3; 66 -7.2; 72 -6.9; 79 -6.7; 87 -6.6; 96 -6.4; 106 -6.4; 116 -6.3; 128 -6.4; 141 -6.6; 155 -6.7; 170 -6.8; 187 -7.0; 206 -7.1; 227 -6.9; 249 -6.4; 274 -5.5; 302 -4.8; 332 -4.7; 365 -4.7; 402 -5.1; 442 -5.4; 486 -5.1; 535 -4.0; 588 -2.8; 647 -2.1; 712 -2.0; 783 -2.3; 861 -2.5; 947 -2.4; 1042 -2.2; 1146 -1.9; 1261 -1.5; 1387 -0.8; 1526 -0.5; 1678 -0.7; 1846 -1.0; 2031 -1.7; 2234 -2.5; 2457 -2.9; 2703 -3.4; 2973 -4.3; 3270 -5.6; 3597 -7.2; 3957 -9.5; 4353 -11.5; 4788 -12.2; 5267 -12.7; 5793 -13.9; 6373 -14.0; 7010 -11.7; 7711 -8.6; 8482 -5.8; 9330 -5.7; 10263 -8.7; 11289 -11.4; 12418 -10.3; 13660 -6.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan HE-4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan HE-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.12 | -1.8 dB |
| Peaking | 671 Hz   | 2.9  | 2.5 dB  |
| Peaking | 1665 Hz  | 0.79 | 5.2 dB  |
| Peaking | 5453 Hz  | 1.49 | -9.5 dB |
| Peaking | 11730 Hz | 4.22 | -6.1 dB |
| Peaking | 215 Hz   | 3.64 | -1.1 dB |
| Peaking | 312 Hz   | 4.51 | 1.2 dB  |
| Peaking | 6740 Hz  | 5.33 | -2.6 dB |
| Peaking | 8916 Hz  | 2.61 | 3.2 dB  |
| Peaking | 10579 Hz | 5.1  | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.8 dB |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20HE-4/HiFiMan%20HE-4.png)