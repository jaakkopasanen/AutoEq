# Stax SR-404
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.3; 49 -3.0; 54 -5.3; 60 -8.0; 66 -10.4; 72 -11.9; 79 -12.4; 87 -12.0; 96 -10.9; 106 -9.7; 116 -8.7; 128 -7.9; 141 -7.1; 155 -6.6; 170 -6.2; 187 -5.9; 206 -5.6; 227 -5.4; 249 -5.2; 274 -5.0; 302 -4.8; 332 -5.1; 365 -5.2; 402 -5.1; 442 -4.8; 486 -4.9; 535 -4.9; 588 -4.8; 647 -4.9; 712 -5.1; 783 -5.3; 861 -5.6; 947 -6.0; 1042 -6.5; 1146 -7.0; 1261 -7.5; 1387 -8.2; 1526 -8.9; 1678 -9.3; 1846 -9.0; 2031 -8.6; 2234 -7.9; 2457 -6.5; 2703 -5.0; 2973 -4.0; 3270 -3.5; 3597 -3.5; 3957 -4.5; 4353 -5.7; 4788 -6.4; 5267 -6.6; 5793 -8.7; 6373 -11.5; 7010 -12.6; 7711 -10.6; 8482 -6.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-404 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-404 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 56 Hz   | 0.22 | 20.7 dB  |
| Peaking | 79 Hz   | 0.54 | -26.0 dB |
| Peaking | 1776 Hz | 1.62 | -3.8 dB  |
| Peaking | 3296 Hz | 1.88 | 4.0 dB   |
| Peaking | 6853 Hz | 3.62 | -7.0 dB  |
| Peaking | 25 Hz   | 1.02 | -1.0 dB  |
| Peaking | 44 Hz   | 2.45 | 1.7 dB   |
| Peaking | 63 Hz   | 4.63 | -1.1 dB  |
| Peaking | 665 Hz  | 2.52 | 0.6 dB   |
| Peaking | 8998 Hz | 6.87 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 9.9 dB  |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Stax%20SR-404/Stax%20SR-404.png)