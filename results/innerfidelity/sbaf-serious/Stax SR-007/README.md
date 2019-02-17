# Stax SR-007
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.3; 54 -3.8; 60 -3.7; 66 -3.0; 72 -2.8; 79 -2.7; 87 -2.9; 96 -3.1; 106 -3.3; 116 -3.3; 128 -3.6; 141 -3.9; 155 -4.1; 170 -4.2; 187 -4.3; 206 -4.6; 227 -4.6; 249 -4.8; 274 -4.8; 302 -5.0; 332 -5.1; 365 -5.2; 402 -5.3; 442 -5.1; 486 -4.4; 535 -4.1; 588 -4.9; 647 -5.9; 712 -6.2; 783 -5.9; 861 -6.0; 947 -6.3; 1042 -6.0; 1146 -4.5; 1261 -2.6; 1387 -6.6; 1526 -7.4; 1678 -6.8; 1846 -4.6; 2031 -2.7; 2234 -1.6; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.3; 3957 -1.9; 4353 -3.2; 4788 -4.5; 5267 -3.1; 5793 -1.3; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -7.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-007 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.69 | 6.0 dB  |
| Peaking | 126 Hz  |  0.51 | 2.3 dB  |
| Peaking | 519 Hz  |  4.3  | 1.9 dB  |
| Peaking | 2929 Hz |  1.48 | 6.6 dB  |
| Peaking | 6079 Hz |  4.33 | 4.9 dB  |
| Peaking | 1250 Hz |  5.64 | 5.6 dB  |
| Peaking | 1474 Hz |  2.14 | -3.9 dB |
| Peaking | 2109 Hz |  3.6  | 2.1 dB  |
| Peaking | 6771 Hz | 10.4  | 1.3 dB  |
| Peaking | 8969 Hz |  4.62 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | 2.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-007/Stax%20SR-007.png)