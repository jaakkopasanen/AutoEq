# KRK Systems KNS 6400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.7; 37 -0.7; 41 -0.6; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.4; 87 -3.1; 96 -4.1; 106 -4.5; 116 -5.5; 128 -6.2; 141 -6.6; 155 -6.6; 170 -7.2; 187 -7.8; 206 -7.7; 227 -7.7; 249 -7.3; 274 -7.0; 302 -7.7; 332 -7.7; 365 -7.7; 402 -7.4; 442 -6.9; 486 -7.2; 535 -7.6; 588 -7.8; 647 -6.7; 712 -5.6; 783 -5.8; 861 -5.8; 947 -5.6; 1042 -5.6; 1146 -6.0; 1261 -6.2; 1387 -6.3; 1526 -7.2; 1678 -7.9; 1846 -9.2; 2031 -9.3; 2234 -9.2; 2457 -9.7; 2703 -9.6; 2973 -7.7; 3270 -8.1; 3597 -6.2; 3957 -5.4; 4353 -4.0; 4788 -2.2; 5267 -1.0; 5793 -2.4; 6373 -3.9; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -7.9; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK Systems KNS 6400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 6400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 145 Hz  | 0.1  | 8.6 dB  |
| Peaking | 158 Hz  | 0.7  | -7.2 dB |
| Peaking | 456 Hz  | 0.58 | -6.9 dB |
| Peaking | 2234 Hz | 1.1  | -5.0 dB |
| Peaking | 5196 Hz | 2.55 | 6.1 dB  |
| Peaking | 74 Hz   | 3.99 | 2.2 dB  |
| Peaking | 81 Hz   | 2.31 | -1.3 dB |
| Peaking | 588 Hz  | 4.8  | -2.7 dB |
| Peaking | 589 Hz  | 2.38 | 1.6 dB  |
| Peaking | 9593 Hz | 5.47 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KRK%20Systems%20KNS%206400/KRK%20Systems%20KNS%206400.png)