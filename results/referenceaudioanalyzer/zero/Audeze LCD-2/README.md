# Audeze LCD-2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.8; 25 -4.8; 28 -5.9; 31 -6.7; 34 -7.2; 37 -7.6; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.6; 60 -8.5; 66 -8.3; 72 -8.1; 79 -8.0; 87 -7.9; 96 -7.7; 106 -7.7; 116 -7.7; 128 -7.6; 141 -7.3; 155 -7.0; 170 -6.8; 187 -6.9; 206 -7.0; 227 -7.0; 249 -7.0; 274 -7.0; 302 -7.0; 332 -7.0; 365 -7.3; 402 -7.6; 442 -7.5; 486 -7.2; 535 -7.1; 588 -7.4; 647 -7.8; 712 -8.4; 783 -8.8; 861 -9.0; 947 -8.8; 1042 -8.3; 1146 -7.3; 1261 -6.4; 1387 -5.9; 1526 -5.2; 1678 -4.3; 1846 -3.5; 2031 -2.8; 2234 -2.4; 2457 -1.7; 2703 -0.8; 2973 -0.5; 3270 -1.2; 3597 -1.9; 3957 -1.7; 4353 -1.5; 4788 -2.6; 5267 -4.5; 5793 -6.3; 6373 -7.5; 7010 -8.2; 7711 -8.4; 8482 -8.6; 9330 -9.0; 10263 -10.0; 11289 -11.0; 12418 -10.8; 13660 -9.1; 15026 -8.2; 16529 -8.2; 18182 -7.0; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.7  | 5.3 dB  |
| Peaking | 371 Hz   | 0    | -1.7 dB |
| Peaking | 2696 Hz  | 1.28 | 6.9 dB  |
| Peaking | 4418 Hz  | 2.77 | 4.2 dB  |
| Peaking | 11558 Hz | 1    | -3.5 dB |
| Peaking | 56 Hz    | 1.5  | -1.0 dB |
| Peaking | 232 Hz   | 0.7  | 0.8 dB  |
| Peaking | 887 Hz   | 2.54 | -2.1 dB |
| Peaking | 1691 Hz  | 3.44 | 1.0 dB  |
| Peaking | 17559 Hz | 0.44 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audeze%20LCD-2/Audeze%20LCD-2.png)