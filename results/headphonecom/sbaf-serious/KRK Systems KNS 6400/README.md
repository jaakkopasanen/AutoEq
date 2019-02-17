# KRK Systems KNS 6400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -1.7; 25 -2.0; 28 -2.3; 31 -2.6; 34 -2.7; 37 -2.8; 41 -3.0; 45 -2.7; 49 -1.7; 54 -1.1; 60 -0.6; 66 -0.5; 72 -0.6; 79 -2.5; 87 -4.5; 96 -5.7; 106 -6.5; 116 -7.2; 128 -8.0; 141 -8.7; 155 -8.2; 170 -8.5; 187 -10.2; 206 -11.0; 227 -10.9; 249 -9.8; 274 -10.3; 302 -10.4; 332 -10.5; 365 -10.0; 402 -9.0; 442 -8.0; 486 -7.5; 535 -7.7; 588 -8.5; 647 -8.4; 712 -6.6; 783 -6.5; 861 -7.1; 947 -6.6; 1042 -6.5; 1146 -7.1; 1261 -7.4; 1387 -7.2; 1526 -7.6; 1678 -7.8; 1846 -9.3; 2031 -10.2; 2234 -10.0; 2457 -10.4; 2703 -9.9; 2973 -7.5; 3270 -7.6; 3597 -4.5; 3957 -5.4; 4353 -6.0; 4788 -4.1; 5267 -3.3; 5793 -5.4; 6373 -8.3; 7010 -7.5; 7711 -6.2; 8482 -6.6; 9330 -9.3; 10263 -7.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.9; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK Systems KNS 6400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 6400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.64 | 5.0 dB  |
| Peaking | 68 Hz   | 1.42 | 7.2 dB  |
| Peaking | 94 Hz   | 1.16 | -2.2 dB |
| Peaking | 248 Hz  | 0.89 | -4.4 dB |
| Peaking | 2234 Hz | 2.69 | -4.3 dB |
| Peaking | 2703 Hz | 6.23 | -2.0 dB |
| Peaking | 5380 Hz | 5.89 | 2.4 dB  |
| Peaking | 5605 Hz | 0.93 | 2.3 dB  |
| Peaking | 6459 Hz | 4.46 | -4.5 dB |
| Peaking | 9523 Hz | 5.39 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.5 dB  |
| Peaking | 62 Hz    | 1.41 | 6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KRK%20Systems%20KNS%206400/KRK%20Systems%20KNS%206400.png)