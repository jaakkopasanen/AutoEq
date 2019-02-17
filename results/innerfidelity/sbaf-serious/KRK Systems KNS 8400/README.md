# KRK Systems KNS 8400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.2; 28 -1.5; 31 -1.6; 34 -1.5; 37 -1.3; 41 -1.1; 45 -0.8; 49 -0.9; 54 -1.1; 60 -0.9; 66 -1.0; 72 -1.8; 79 -3.4; 87 -5.3; 96 -7.2; 106 -8.9; 116 -9.8; 128 -10.6; 141 -10.4; 155 -9.7; 170 -10.3; 187 -10.9; 206 -10.2; 227 -9.2; 249 -8.3; 274 -7.5; 302 -6.3; 332 -5.1; 365 -3.7; 402 -2.4; 442 -1.4; 486 -1.7; 535 -2.9; 588 -3.9; 647 -3.9; 712 -2.9; 783 -3.5; 861 -3.9; 947 -3.7; 1042 -3.4; 1146 -3.5; 1261 -3.9; 1387 -5.0; 1526 -6.2; 1678 -7.9; 1846 -9.0; 2031 -9.6; 2234 -10.1; 2457 -10.4; 2703 -10.6; 2973 -8.7; 3270 -8.5; 3597 -8.4; 3957 -8.0; 4353 -7.0; 4788 -4.3; 5267 -3.3; 5793 -2.9; 6373 -3.9; 7010 -3.5; 7711 -3.2; 8482 -5.8; 9330 -8.8; 10263 -6.7; 11289 -3.5; 12418 -3.4; 13660 -3.4; 15026 -3.4; 16529 -3.4; 18182 -4.8; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK Systems KNS 8400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK Systems KNS 8400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.56 | 2.7 dB  |
| Peaking | 64 Hz   | 2.16 | 3.7 dB  |
| Peaking | 147 Hz  | 1    | -8.3 dB |
| Peaking | 2512 Hz | 1.38 | -7.6 dB |
| Peaking | 9483 Hz | 5.84 | -5.9 dB |
| Peaking | 157 Hz  | 4.43 | 3.3 dB  |
| Peaking | 201 Hz  | 1.12 | -2.3 dB |
| Peaking | 440 Hz  | 2.3  | 3.7 dB  |
| Peaking | 4134 Hz | 3.14 | -4.3 dB |
| Peaking | 4827 Hz | 1.68 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -7.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/KRK%20Systems%20KNS%208400/KRK%20Systems%20KNS%208400.png)