# Audeze LCD-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -5.0; 25 -5.9; 28 -7.1; 31 -8.1; 34 -8.6; 37 -8.7; 41 -8.4; 45 -8.3; 49 -8.4; 54 -8.5; 60 -8.5; 66 -8.5; 72 -8.5; 79 -8.5; 87 -8.5; 96 -8.5; 106 -8.2; 116 -8.2; 128 -8.2; 141 -8.2; 155 -8.2; 170 -8.2; 187 -8.2; 206 -8.2; 227 -8.2; 249 -8.2; 274 -8.0; 302 -7.5; 332 -7.2; 365 -7.4; 402 -7.6; 442 -7.3; 486 -6.9; 535 -6.9; 588 -7.0; 647 -7.3; 712 -7.5; 783 -7.6; 861 -7.1; 947 -6.1; 1042 -5.4; 1146 -5.5; 1261 -5.9; 1387 -6.4; 1526 -6.8; 1678 -6.6; 1846 -6.0; 2031 -5.1; 2234 -3.9; 2457 -1.8; 2703 -0.5; 2973 -2.2; 3270 -4.0; 3597 -4.7; 3957 -5.5; 4353 -7.8; 4788 -10.4; 5267 -10.4; 5793 -7.8; 6373 -6.0; 7010 -4.9; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.52 | 4.7 dB  |
| Peaking | 30 Hz   | 0.83 | -2.0 dB |
| Peaking | 114 Hz  | 0.21 | -2.1 dB |
| Peaking | 2716 Hz | 3.18 | 5.8 dB  |
| Peaking | 4981 Hz | 4.77 | -5.6 dB |
| Peaking | 14 Hz   | 0.95 | -0.4 dB |
| Peaking | 796 Hz  | 2.28 | -2.5 dB |
| Peaking | 1059 Hz | 1.04 | 2.5 dB  |
| Peaking | 1517 Hz | 2.1  | -2.3 dB |
| Peaking | 7100 Hz | 8.11 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audeze%20LCD-X/Audeze%20LCD-X.png)