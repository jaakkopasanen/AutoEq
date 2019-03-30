# OPPO PM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.1; 31 -2.5; 34 -2.7; 37 -2.8; 41 -2.9; 45 -3.1; 49 -3.5; 54 -4.1; 60 -4.6; 66 -4.8; 72 -4.9; 79 -5.1; 87 -5.3; 96 -5.4; 106 -5.4; 116 -5.4; 128 -5.4; 141 -5.6; 155 -5.8; 170 -5.5; 187 -5.4; 206 -5.4; 227 -5.6; 249 -6.0; 274 -6.4; 302 -6.4; 332 -6.1; 365 -5.4; 402 -4.2; 442 -3.2; 486 -3.0; 535 -3.7; 588 -4.6; 647 -5.4; 712 -5.9; 783 -6.1; 861 -6.0; 947 -5.4; 1042 -4.5; 1146 -3.9; 1261 -3.8; 1387 -3.4; 1526 -2.5; 1678 -1.8; 1846 -1.5; 2031 -1.5; 2234 -1.5; 2457 -1.7; 2703 -2.4; 2973 -2.8; 3270 -3.1; 3597 -3.2; 3957 -3.3; 4353 -3.7; 4788 -3.8; 5267 -3.9; 5793 -4.3; 6373 -4.6; 7010 -3.2; 7711 -3.5; 8482 -3.8; 9330 -3.8; 10263 -3.8; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`OPPO PM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `OPPO PM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.73 | 4.3 dB  |
| Peaking | 116 Hz  | 0.72 | -1.9 dB |
| Peaking | 291 Hz  | 3.1  | -2.3 dB |
| Peaking | 813 Hz  | 2.72 | -2.7 dB |
| Peaking | 2040 Hz | 1.62 | 2.6 dB  |
| Peaking | 354 Hz  | 5.24 | -0.9 dB |
| Peaking | 468 Hz  | 3.51 | 1.7 dB  |
| Peaking | 644 Hz  | 5.05 | -0.8 dB |
| Peaking | 6102 Hz | 7.25 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/OPPO%20PM1/OPPO%20PM1.png)