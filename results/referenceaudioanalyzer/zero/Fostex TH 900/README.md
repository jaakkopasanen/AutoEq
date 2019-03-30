# Fostex TH 900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.2; 37 -1.9; 41 -2.6; 45 -3.3; 49 -3.8; 54 -4.4; 60 -5.0; 66 -5.4; 72 -5.7; 79 -5.8; 87 -6.0; 96 -6.2; 106 -6.2; 116 -6.0; 128 -5.8; 141 -5.8; 155 -5.8; 170 -5.8; 187 -5.8; 206 -5.6; 227 -5.3; 249 -5.2; 274 -4.9; 302 -4.8; 332 -4.4; 365 -4.0; 402 -3.5; 442 -3.0; 486 -2.4; 535 -1.9; 588 -2.5; 647 -3.4; 712 -3.8; 783 -4.5; 861 -6.0; 947 -7.6; 1042 -8.4; 1146 -8.4; 1261 -8.0; 1387 -7.4; 1526 -6.9; 1678 -6.8; 1846 -6.8; 2031 -6.4; 2234 -5.4; 2457 -4.1; 2703 -3.5; 2973 -4.0; 3270 -5.9; 3597 -8.2; 3957 -9.9; 4353 -11.4; 4788 -13.6; 5267 -14.9; 5793 -13.5; 6373 -10.7; 7010 -9.9; 7711 -9.5; 8482 -8.2; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH 900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.99 | 6.5 dB  |
| Peaking | 559 Hz  | 0.97 | 4.7 dB  |
| Peaking | 1054 Hz | 1.79 | -3.7 dB |
| Peaking | 2782 Hz | 2.88 | 4.5 dB  |
| Peaking | 5194 Hz | 1.86 | -8.6 dB |
| Peaking | 73 Hz   | 0.65 | 0.9 dB  |
| Peaking | 81 Hz   | 1.22 | -1.3 dB |
| Peaking | 7929 Hz | 4.31 | -1.7 dB |
| Peaking | 9259 Hz | 1.59 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 5.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fostex%20TH%20900/Fostex%20TH%20900.png)