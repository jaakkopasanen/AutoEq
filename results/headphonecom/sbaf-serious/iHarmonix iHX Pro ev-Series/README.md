# iHarmonix iHX Pro ev-Series
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -8.9; 25 -8.9; 28 -9.0; 31 -8.9; 34 -8.9; 37 -8.9; 41 -8.9; 45 -9.0; 49 -9.0; 54 -9.1; 60 -9.2; 66 -9.4; 72 -9.5; 79 -9.6; 87 -9.7; 96 -9.7; 106 -9.7; 116 -9.7; 128 -9.6; 141 -9.6; 155 -9.5; 170 -9.3; 187 -9.0; 206 -8.7; 227 -8.2; 249 -7.8; 274 -7.8; 302 -7.4; 332 -6.9; 365 -6.4; 402 -5.9; 442 -5.5; 486 -5.3; 535 -5.1; 588 -4.7; 647 -4.5; 712 -4.3; 783 -4.3; 861 -4.5; 947 -4.9; 1042 -5.5; 1146 -6.0; 1261 -6.6; 1387 -7.5; 1526 -9.2; 1678 -11.0; 1846 -12.4; 2031 -13.5; 2234 -14.7; 2457 -15.5; 2703 -13.5; 2973 -9.3; 3270 -5.5; 3597 -3.7; 3957 -5.0; 4353 -8.4; 4788 -11.6; 5267 -9.6; 5793 -3.8; 6373 -0.5; 7010 -2.7; 7711 -4.9; 8482 -5.2; 9330 -5.7; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iHarmonix iHX Pro ev-Series GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iHarmonix iHX Pro ev-Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.31 | -3.7 dB  |
| Peaking | 151 Hz  | 0.9  | -3.0 dB  |
| Peaking | 2240 Hz | 2.27 | -10.8 dB |
| Peaking | 4956 Hz | 6.44 | -7.4 dB  |
| Peaking | 6382 Hz | 4.36 | 5.7 dB   |
| Peaking | 751 Hz  | 1.73 | 1.7 dB   |
| Peaking | 1638 Hz | 5.56 | -2.2 dB  |
| Peaking | 2718 Hz | 7.06 | -3.5 dB  |
| Peaking | 3638 Hz | 3.12 | 4.4 dB   |
| Peaking | 4470 Hz | 5.18 | -2.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/iHarmonix%20iHX%20Pro%20ev-Series/iHarmonix%20iHX%20Pro%20ev-Series.png)