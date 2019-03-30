# Creative Aurvana Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.5; 25 -8.2; 28 -9.2; 31 -9.9; 34 -10.6; 37 -11.2; 41 -11.8; 45 -12.4; 49 -12.8; 54 -13.2; 60 -13.7; 66 -14.0; 72 -14.3; 79 -14.7; 87 -15.2; 96 -15.8; 106 -16.5; 116 -16.8; 128 -16.5; 141 -15.9; 155 -15.9; 170 -16.1; 187 -15.8; 206 -15.1; 227 -14.2; 249 -13.4; 274 -12.4; 302 -11.3; 332 -10.1; 365 -8.7; 402 -7.2; 442 -5.8; 486 -4.4; 535 -3.3; 588 -2.9; 647 -2.9; 712 -3.2; 783 -3.1; 861 -3.2; 947 -3.1; 1042 -3.2; 1146 -3.0; 1261 -2.6; 1387 -2.0; 1526 -1.2; 1678 -0.6; 1846 -0.5; 2031 -0.5; 2234 -0.6; 2457 -1.2; 2703 -2.0; 2973 -2.7; 3270 -3.5; 3597 -4.6; 3957 -5.5; 4353 -6.9; 4788 -8.8; 5267 -9.5; 5793 -8.6; 6373 -6.8; 7010 -5.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative Aurvana Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.4  | -7.4 dB |
| Peaking | 265 Hz  | 0.49 | -6.0 dB |
| Peaking | 536 Hz  | 0.71 | 8.0 dB  |
| Peaking | 1990 Hz | 1.38 | 6.0 dB  |
| Peaking | 14 Hz   | 1    | 2.8 dB  |
| Peaking | 36 Hz   | 1.79 | -1.0 dB |
| Peaking | 3153 Hz | 2.56 | 1.4 dB  |
| Peaking | 5216 Hz | 2.77 | -4.0 dB |
| Peaking | 7010 Hz | 6.2  | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.8 dB |
| Peaking | 125 Hz   | 1.41 | -8.9 dB |
| Peaking | 250 Hz   | 1.41 | -6.8 dB |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Creative%20Aurvana%20Gold/Creative%20Aurvana%20Gold.png)