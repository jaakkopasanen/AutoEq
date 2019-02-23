# iHarmonix iHX Pro ev-Series
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.6; 25 -7.6; 28 -7.6; 31 -7.6; 34 -7.5; 37 -7.5; 41 -7.6; 45 -7.6; 49 -7.7; 54 -7.7; 60 -7.9; 66 -8.0; 72 -8.1; 79 -8.3; 87 -8.3; 96 -8.4; 106 -8.4; 116 -8.3; 128 -8.3; 141 -8.3; 155 -8.1; 170 -8.0; 187 -7.7; 206 -7.3; 227 -6.9; 249 -6.5; 274 -6.4; 302 -6.0; 332 -5.5; 365 -5.0; 402 -4.5; 442 -4.2; 486 -3.9; 535 -3.8; 588 -3.3; 647 -3.1; 712 -2.9; 783 -2.9; 861 -3.1; 947 -3.5; 1042 -4.1; 1146 -4.6; 1261 -5.3; 1387 -6.2; 1526 -7.8; 1678 -9.7; 1846 -11.0; 2031 -12.2; 2234 -13.3; 2457 -14.2; 2703 -12.1; 2973 -8.0; 3270 -4.2; 3597 -2.3; 3957 -3.6; 4353 -7.1; 4788 -10.2; 5267 -8.2; 5793 -2.5; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iHarmonix iHX Pro ev-Series GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iHarmonix iHX Pro ev-Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 820 Hz  | 1.11 | 4.0 dB   |
| Peaking | 2441 Hz | 1.47 | -10.8 dB |
| Peaking | 3518 Hz | 2.23 | 8.8 dB   |
| Peaking | 4886 Hz | 3.96 | -6.7 dB  |
| Peaking | 6184 Hz | 4.26 | 7.3 dB   |
| Peaking | 18 Hz   | 0.46 | -1.4 dB  |
| Peaking | 117 Hz  | 0.58 | -2.4 dB  |
| Peaking | 429 Hz  | 1.92 | 1.2 dB   |
| Peaking | 1354 Hz | 4.5  | 0.9 dB   |
| Peaking | 1702 Hz | 5.52 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/iHarmonix%20iHX%20Pro%20ev-Series/iHarmonix%20iHX%20Pro%20ev-Series.png)