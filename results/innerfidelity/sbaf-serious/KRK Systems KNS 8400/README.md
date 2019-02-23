# KRK Systems KNS 8400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.5; 31 -1.6; 34 -1.5; 37 -1.3; 41 -1.1; 45 -0.9; 49 -1.0; 54 -1.1; 60 -1.0; 66 -1.0; 72 -1.8; 79 -3.4; 87 -5.3; 96 -7.2; 106 -8.9; 116 -9.8; 128 -10.6; 141 -10.4; 155 -9.7; 170 -10.3; 187 -10.9; 206 -10.2; 227 -9.3; 249 -8.3; 274 -7.5; 302 -6.3; 332 -5.1; 365 -3.7; 402 -2.4; 442 -1.4; 486 -1.7; 535 -2.9; 588 -3.9; 647 -4.0; 712 -2.9; 783 -3.5; 861 -4.0; 947 -3.7; 1042 -3.4; 1146 -3.6; 1261 -4.0; 1387 -5.0; 1526 -6.2; 1678 -7.9; 1846 -9.0; 2031 -9.6; 2234 -10.2; 2457 -10.5; 2703 -10.7; 2973 -8.7; 3270 -8.5; 3597 -8.4; 3957 -8.0; 4353 -7.0; 4788 -4.3; 5267 -3.4; 5793 -2.9; 6373 -3.9; 7010 -4.2; 7711 -6.1; 8482 -6.5; 9330 -8.8; 10263 -7.0; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK Systems KNS 8400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 8400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.45 | 10.7 dB  |
| Peaking | 64 Hz   | 1.3  | 7.6 dB   |
| Peaking | 205 Hz  | 0.18 | -27.1 dB |
| Peaking | 382 Hz  | 0.21 | 26.2 dB  |
| Peaking | 2388 Hz | 1.26 | -7.5 dB  |
| Peaking | 446 Hz  | 5.24 | 1.7 dB   |
| Peaking | 601 Hz  | 4.56 | -1.8 dB  |
| Peaking | 4102 Hz | 2.87 | -3.5 dB  |
| Peaking | 5225 Hz | 1.72 | 3.7 dB   |
| Peaking | 9367 Hz | 3.77 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KRK%20Systems%20KNS%208400/KRK%20Systems%20KNS%208400.png)