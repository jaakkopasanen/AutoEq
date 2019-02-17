# Fostex TH900mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.6; 23 -6.9; 25 -7.1; 28 -7.4; 31 -7.7; 34 -7.8; 37 -7.9; 41 -8.0; 45 -8.0; 49 -8.1; 54 -8.1; 60 -8.0; 66 -7.9; 72 -7.8; 79 -8.1; 87 -8.4; 96 -8.5; 106 -8.5; 116 -8.4; 128 -8.4; 141 -8.3; 155 -8.0; 170 -7.5; 187 -7.3; 206 -7.0; 227 -6.5; 249 -6.1; 274 -5.5; 302 -4.9; 332 -4.2; 365 -3.5; 402 -2.7; 442 -1.9; 486 -1.7; 535 -1.8; 588 -1.9; 647 -2.6; 712 -3.6; 783 -2.7; 861 -3.3; 947 -3.8; 1042 -3.7; 1146 -3.2; 1261 -2.7; 1387 -2.5; 1526 -2.5; 1678 -2.5; 1846 -2.4; 2031 -2.3; 2234 -2.0; 2457 -0.7; 2703 -0.5; 2973 -2.0; 3270 -3.5; 3597 -2.1; 3957 -2.2; 4353 -3.9; 4788 -5.3; 5267 -6.9; 5793 -9.9; 6373 -6.9; 7010 -5.5; 7711 -7.5; 8482 -5.6; 9330 -3.9; 10263 -3.9; 11289 -3.9; 12418 -3.9; 13660 -3.9; 15026 -3.9; 16529 -4.1; 18182 -7.2; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH900mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 33 Hz   |  0.63 | -3.2 dB |
| Peaking | 129 Hz  |  0.56 | -4.1 dB |
| Peaking | 476 Hz  |  1.63 | 3.1 dB  |
| Peaking | 2780 Hz |  0.89 | 2.8 dB  |
| Peaking | 5842 Hz |  2.31 | -5.9 dB |
| Peaking | 981 Hz  |  8.21 | -0.7 dB |
| Peaking | 3188 Hz |  2.62 | 2.2 dB  |
| Peaking | 3261 Hz |  6.38 | -4.2 dB |
| Peaking | 6738 Hz | 10.65 | 2.1 dB  |
| Peaking | 7886 Hz |  8.11 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH900mk2/Fostex%20TH900mk2.png)