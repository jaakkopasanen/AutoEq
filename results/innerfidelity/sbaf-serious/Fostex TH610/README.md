# Fostex TH610
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.2; 25 -7.3; 28 -7.5; 31 -7.6; 34 -7.6; 37 -7.7; 41 -7.8; 45 -7.9; 49 -8.0; 54 -8.1; 60 -8.2; 66 -8.3; 72 -8.3; 79 -8.4; 87 -8.8; 96 -9.2; 106 -9.6; 116 -9.7; 128 -10.0; 141 -10.2; 155 -10.2; 170 -9.8; 187 -10.0; 206 -9.8; 227 -9.6; 249 -9.3; 274 -9.0; 302 -8.5; 332 -8.0; 365 -7.4; 402 -6.7; 442 -6.0; 486 -5.8; 535 -5.4; 588 -4.8; 647 -4.8; 712 -4.8; 783 -4.6; 861 -4.5; 947 -4.9; 1042 -5.1; 1146 -5.0; 1261 -5.0; 1387 -5.4; 1526 -5.8; 1678 -5.8; 1846 -5.3; 2031 -4.1; 2234 -1.8; 2457 -0.5; 2703 -2.8; 2973 -4.2; 3270 -4.3; 3597 -4.6; 3957 -4.8; 4353 -5.4; 4788 -4.1; 5267 -1.9; 5793 -2.7; 6373 -4.2; 7010 -4.1; 7711 -5.6; 8482 -5.9; 9330 -7.5; 10263 -7.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -10.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH610 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH610 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 60 Hz   |  0.44 | -2.0 dB |
| Peaking | 174 Hz  |  1.01 | -3.7 dB |
| Peaking | 2426 Hz |  3.54 | 5.3 dB  |
| Peaking | 5513 Hz |  3.23 | 3.8 dB  |
| Peaking | 9801 Hz |  5.68 | -2.8 dB |
| Peaking | 181 Hz  |  2.76 | 1.2 dB  |
| Peaking | 314 Hz  |  0.73 | -2.3 dB |
| Peaking | 560 Hz  |  0.59 | 2.5 dB  |
| Peaking | 1690 Hz |  2.67 | -1.1 dB |
| Peaking | 4423 Hz | 11.05 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH610/Fostex%20TH610.png)