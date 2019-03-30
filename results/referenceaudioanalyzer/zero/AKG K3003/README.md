# AKG K3003
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.4; 25 -3.7; 28 -4.2; 31 -4.5; 34 -4.8; 37 -5.0; 41 -5.2; 45 -5.4; 49 -5.5; 54 -5.6; 60 -5.8; 66 -5.9; 72 -5.8; 79 -5.8; 87 -5.8; 96 -5.8; 106 -5.8; 116 -5.7; 128 -5.5; 141 -5.5; 155 -5.4; 170 -5.2; 187 -5.1; 206 -4.9; 227 -4.7; 249 -4.5; 274 -4.3; 302 -4.1; 332 -3.9; 365 -3.7; 402 -3.5; 442 -3.2; 486 -3.0; 535 -2.8; 588 -2.6; 647 -2.5; 712 -2.3; 783 -2.1; 861 -1.8; 947 -1.6; 1042 -1.3; 1146 -1.0; 1261 -1.0; 1387 -1.0; 1526 -1.0; 1678 -1.0; 1846 -1.5; 2031 -2.6; 2234 -4.0; 2457 -5.4; 2703 -6.7; 2973 -7.0; 3270 -6.1; 3597 -3.9; 3957 -1.8; 4353 -1.8; 4788 -3.9; 5267 -5.7; 5793 -5.4; 6373 -2.3; 7010 -0.5; 7711 -2.7; 8482 -3.0; 9330 -3.0; 10263 -3.0; 11289 -5.4; 12418 -5.4; 13660 -3.0; 15026 -3.0; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 91 Hz    |  0.37 | -2.9 dB |
| Peaking | 2840 Hz  |  1.65 | -9.8 dB |
| Peaking | 2933 Hz  |  0.45 | 5.7 dB  |
| Peaking | 5420 Hz  |  4.3  | -5.8 dB |
| Peaking | 11670 Hz |  2.91 | -3.7 dB |
| Peaking | 19 Hz    |  2.2  | 1.1 dB  |
| Peaking | 6839 Hz  | 10.47 | 3.3 dB  |
| Peaking | 7919 Hz  |  2.06 | -1.2 dB |
| Peaking | 10300 Hz |  5.01 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K3003/AKG%20K3003.png)