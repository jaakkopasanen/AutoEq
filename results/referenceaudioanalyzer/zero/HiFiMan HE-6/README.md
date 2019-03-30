# HiFiMan HE-6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -3.1; 25 -3.8; 28 -4.6; 31 -5.2; 34 -5.4; 37 -5.6; 41 -5.6; 45 -5.5; 49 -5.4; 54 -5.4; 60 -5.4; 66 -5.4; 72 -5.3; 79 -5.1; 87 -5.1; 96 -5.1; 106 -4.8; 116 -4.7; 128 -4.7; 141 -4.6; 155 -4.4; 170 -4.4; 187 -4.4; 206 -4.4; 227 -4.1; 249 -4.1; 274 -4.1; 302 -4.1; 332 -4.1; 365 -4.3; 402 -4.4; 442 -4.3; 486 -4.1; 535 -4.1; 588 -4.1; 647 -4.1; 712 -4.1; 783 -4.1; 861 -4.4; 947 -4.4; 1042 -4.4; 1146 -4.4; 1261 -4.2; 1387 -3.4; 1526 -2.5; 1678 -1.6; 1846 -0.8; 2031 -0.5; 2234 -0.6; 2457 -0.8; 2703 -1.1; 2973 -1.6; 3270 -2.1; 3597 -3.7; 3957 -6.6; 4353 -9.7; 4788 -11.1; 5267 -11.0; 5793 -10.8; 6373 -11.2; 7010 -11.8; 7711 -11.9; 8482 -11.3; 9330 -10.7; 10263 -10.4; 11289 -10.0; 12418 -8.6; 13660 -6.7; 15026 -5.5; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan HE-6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan HE-6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 3.09 | 2.9 dB  |
| Peaking | 288 Hz   | 0.82 | 0.9 dB  |
| Peaking | 2636 Hz  | 0.92 | 6.1 dB  |
| Peaking | 4694 Hz  | 2.67 | -5.1 dB |
| Peaking | 7887 Hz  | 0.8  | -7.2 dB |
| Peaking | 1195 Hz  | 3.56 | -0.9 dB |
| Peaking | 1829 Hz  | 5.33 | 1.0 dB  |
| Peaking | 11843 Hz | 2.73 | -1.8 dB |
| Peaking | 14711 Hz | 0.83 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | -8.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/HiFiMan%20HE-6/HiFiMan%20HE-6.png)