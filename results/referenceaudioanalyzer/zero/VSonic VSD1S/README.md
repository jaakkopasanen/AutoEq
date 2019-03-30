# VSonic VSD1S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.5; 25 -4.9; 28 -5.4; 31 -5.8; 34 -6.2; 37 -6.5; 41 -6.8; 45 -7.0; 49 -7.2; 54 -7.4; 60 -7.5; 66 -7.7; 72 -7.7; 79 -7.7; 87 -7.7; 96 -7.7; 106 -7.7; 116 -7.7; 128 -7.7; 141 -7.4; 155 -7.3; 170 -7.1; 187 -6.9; 206 -6.6; 227 -6.3; 249 -6.0; 274 -5.8; 302 -5.6; 332 -5.3; 365 -4.9; 402 -4.6; 442 -4.2; 486 -3.7; 535 -3.3; 588 -2.8; 647 -2.4; 712 -1.9; 783 -1.6; 861 -1.2; 947 -0.9; 1042 -0.7; 1146 -0.8; 1261 -0.9; 1387 -0.9; 1526 -1.1; 1678 -1.5; 1846 -2.2; 2031 -3.2; 2234 -4.2; 2457 -4.9; 2703 -5.2; 2973 -4.5; 3270 -2.9; 3597 -1.1; 3957 -0.6; 4353 -1.9; 4788 -3.5; 5267 -4.8; 5793 -4.9; 6373 -3.0; 7010 -0.5; 7711 -2.5; 8482 -2.8; 9330 -2.8; 10263 -2.8; 11289 -2.8; 12418 -2.8; 13660 -2.8; 15026 -2.8; 16529 -2.8; 18182 -2.8; 20000 -2.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD1S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD1S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 97 Hz   | 0.29 | -5.0 dB |
| Peaking | 1128 Hz | 0.73 | 2.7 dB  |
| Peaking | 2743 Hz | 1.66 | -6.2 dB |
| Peaking | 3857 Hz | 0.96 | 5.1 dB  |
| Peaking | 5264 Hz | 2.96 | -5.3 dB |
| Peaking | 15 Hz   | 1.68 | 0.8 dB  |
| Peaking | 6939 Hz | 9.15 | 3.0 dB  |
| Peaking | 7707 Hz | 1.45 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/VSonic%20VSD1S/VSonic%20VSD1S.png)