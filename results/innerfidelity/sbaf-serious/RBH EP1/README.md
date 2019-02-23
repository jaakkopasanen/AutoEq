# RBH EP1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -13.5; 25 -13.2; 28 -12.8; 31 -12.5; 34 -12.3; 37 -12.0; 41 -11.5; 45 -11.2; 49 -11.0; 54 -10.8; 60 -10.5; 66 -10.4; 72 -10.3; 79 -10.2; 87 -10.1; 96 -10.0; 106 -9.9; 116 -9.3; 128 -9.5; 141 -9.3; 155 -8.6; 170 -8.7; 187 -8.2; 206 -7.9; 227 -7.4; 249 -7.0; 274 -6.7; 302 -6.1; 332 -5.8; 365 -5.4; 402 -5.0; 442 -4.4; 486 -4.2; 535 -3.7; 588 -3.3; 647 -2.4; 712 -2.6; 783 -2.5; 861 -2.9; 947 -3.3; 1042 -3.8; 1146 -4.3; 1261 -4.7; 1387 -5.6; 1526 -6.7; 1678 -7.6; 1846 -8.0; 2031 -8.0; 2234 -8.0; 2457 -7.2; 2703 -6.5; 2973 -4.6; 3270 -3.1; 3597 -2.7; 3957 -4.5; 4353 -8.4; 4788 -10.3; 5267 -7.3; 5793 -3.6; 6373 -0.5; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RBH EP1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RBH EP1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.31 | -8.4 dB |
| Peaking | 123 Hz  | 0.7  | -2.9 dB |
| Peaking | 687 Hz  | 1.66 | 3.5 dB  |
| Peaking | 4805 Hz | 6.55 | -5.9 dB |
| Peaking | 6405 Hz | 5.39 | 5.6 dB  |
| Peaking | 702 Hz  | 2.86 | -1.1 dB |
| Peaking | 1188 Hz | 0.83 | 3.2 dB  |
| Peaking | 1929 Hz | 0.87 | -5.2 dB |
| Peaking | 3481 Hz | 2.41 | 5.1 dB  |
| Peaking | 4310 Hz | 8    | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RBH%20EP1/RBH%20EP1.png)