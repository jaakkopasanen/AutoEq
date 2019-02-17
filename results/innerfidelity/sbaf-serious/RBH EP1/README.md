# RBH EP1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.7; 25 -13.4; 28 -13.0; 31 -12.7; 34 -12.5; 37 -12.2; 41 -11.7; 45 -11.4; 49 -11.2; 54 -11.0; 60 -10.7; 66 -10.5; 72 -10.4; 79 -10.3; 87 -10.3; 96 -10.2; 106 -10.1; 116 -9.5; 128 -9.7; 141 -9.5; 155 -8.8; 170 -8.9; 187 -8.3; 206 -8.1; 227 -7.6; 249 -7.2; 274 -6.9; 302 -6.3; 332 -6.0; 365 -5.6; 402 -5.1; 442 -4.6; 486 -4.4; 535 -3.9; 588 -3.5; 647 -2.6; 712 -2.8; 783 -2.7; 861 -3.1; 947 -3.5; 1042 -4.0; 1146 -4.4; 1261 -4.9; 1387 -5.8; 1526 -6.9; 1678 -7.8; 1846 -8.2; 2031 -8.2; 2234 -8.2; 2457 -7.4; 2703 -6.7; 2973 -4.8; 3270 -3.2; 3597 -2.9; 3957 -4.7; 4353 -8.5; 4788 -10.5; 5267 -7.5; 5793 -3.8; 6373 -0.5; 7010 -1.3; 7711 -3.5; 8482 -3.8; 9330 -3.9; 10263 -3.8; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RBH EP1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RBH EP1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.18 | -9.9 dB |
| Peaking | 153 Hz  | 0.8  | -3.4 dB |
| Peaking | 1979 Hz | 2.18 | -5.0 dB |
| Peaking | 4802 Hz | 5.18 | -7.4 dB |
| Peaking | 6553 Hz | 5.25 | 4.7 dB  |
| Peaking | 736 Hz  | 2.15 | 1.9 dB  |
| Peaking | 1507 Hz | 5.72 | -0.9 dB |
| Peaking | 3398 Hz | 1.68 | -2.4 dB |
| Peaking | 3465 Hz | 3.87 | 4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RBH%20EP1/RBH%20EP1.png)