# KRK Systems KNS 6400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.2; 31 -1.5; 34 -1.6; 37 -1.7; 41 -1.5; 45 -1.2; 49 -0.8; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -2.3; 87 -4.1; 96 -5.0; 106 -5.4; 116 -6.5; 128 -7.2; 141 -7.5; 155 -7.6; 170 -8.1; 187 -8.8; 206 -8.6; 227 -8.7; 249 -8.2; 274 -8.0; 302 -8.6; 332 -8.6; 365 -8.6; 402 -8.3; 442 -7.8; 486 -8.2; 535 -8.6; 588 -8.8; 647 -7.6; 712 -6.5; 783 -6.7; 861 -6.8; 947 -6.5; 1042 -6.6; 1146 -7.0; 1261 -7.1; 1387 -7.2; 1526 -8.2; 1678 -8.9; 1846 -10.1; 2031 -10.3; 2234 -10.2; 2457 -10.7; 2703 -10.5; 2973 -8.6; 3270 -9.1; 3597 -7.2; 3957 -6.4; 4353 -5.0; 4788 -3.1; 5267 -1.9; 5793 -3.3; 6373 -4.8; 7010 -4.9; 7711 -6.2; 8482 -6.9; 9330 -8.8; 10263 -8.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.6; 20000 -11.4
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
| Peaking | 18 Hz   | 0.44 | 5.8 dB  |
| Peaking | 64 Hz   | 1.44 | 5.3 dB  |
| Peaking | 209 Hz  | 0.51 | -2.6 dB |
| Peaking | 2384 Hz | 1.53 | -4.5 dB |
| Peaking | 5206 Hz | 3.09 | 5.3 dB  |
| Peaking | 570 Hz  | 4.04 | -1.9 dB |
| Peaking | 806 Hz  | 1.15 | 1.0 dB  |
| Peaking | 1799 Hz | 7.28 | -1.1 dB |
| Peaking | 7074 Hz | 4.84 | 0.8 dB  |
| Peaking | 9578 Hz | 4.76 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KRK%20Systems%20KNS%206400/KRK%20Systems%20KNS%206400.png)