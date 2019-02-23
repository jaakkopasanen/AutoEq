# KRK Systems KNS 6400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.9; 31 -1.1; 34 -1.3; 37 -1.4; 41 -1.6; 45 -1.3; 49 -0.6; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.2; 87 -3.1; 96 -4.3; 106 -5.1; 116 -5.8; 128 -6.6; 141 -7.3; 155 -6.8; 170 -7.1; 187 -8.8; 206 -9.6; 227 -9.5; 249 -8.4; 274 -8.9; 302 -9.0; 332 -9.1; 365 -8.6; 402 -7.6; 442 -6.6; 486 -6.1; 535 -6.3; 588 -7.1; 647 -7.0; 712 -5.2; 783 -5.1; 861 -5.7; 947 -5.2; 1042 -5.1; 1146 -5.7; 1261 -6.0; 1387 -5.8; 1526 -6.2; 1678 -6.4; 1846 -7.9; 2031 -8.8; 2234 -8.6; 2457 -9.0; 2703 -8.5; 2973 -6.1; 3270 -6.2; 3597 -3.1; 3957 -4.0; 4353 -4.6; 4788 -2.7; 5267 -1.9; 5793 -4.0; 6373 -6.9; 7010 -6.1; 7711 -6.2; 8482 -6.5; 9330 -7.9; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK Systems KNS 6400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 6400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.65 | 5.5 dB  |
| Peaking | 70 Hz   | 0.99 | 6.1 dB  |
| Peaking | 106 Hz  | 1.37 | -2.4 dB |
| Peaking | 235 Hz  | 1.36 | -3.4 dB |
| Peaking | 5026 Hz | 3.38 | 4.7 dB  |
| Peaking | 342 Hz  | 5.92 | -1.5 dB |
| Peaking | 1062 Hz | 0.86 | 1.5 dB  |
| Peaking | 2265 Hz | 1.98 | -3.2 dB |
| Peaking | 3682 Hz | 7.7  | 3.7 dB  |
| Peaking | 9583 Hz | 7.46 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.1 dB  |
| Peaking | 62 Hz    | 1.41 | 6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KRK%20Systems%20KNS%206400/KRK%20Systems%20KNS%206400.png)