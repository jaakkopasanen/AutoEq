# Audeze LCD-3 sn2312454
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.3; 25 -3.2; 28 -3.2; 31 -3.4; 34 -3.6; 37 -3.7; 41 -3.7; 45 -3.5; 49 -3.8; 54 -5.1; 60 -5.4; 66 -5.4; 72 -5.5; 79 -5.7; 87 -6.0; 96 -6.3; 106 -6.6; 116 -6.8; 128 -7.1; 141 -7.3; 155 -7.4; 170 -7.6; 187 -7.8; 206 -7.9; 227 -7.9; 249 -8.0; 274 -8.1; 302 -8.2; 332 -8.3; 365 -8.2; 402 -8.2; 442 -7.9; 486 -7.8; 535 -7.8; 588 -7.8; 647 -8.0; 712 -8.2; 783 -7.7; 861 -7.4; 947 -6.5; 1042 -6.1; 1146 -6.0; 1261 -5.7; 1387 -6.0; 1526 -6.3; 1678 -6.1; 1846 -5.4; 2031 -5.1; 2234 -5.5; 2457 -5.2; 2703 -5.5; 2973 -5.3; 3270 -4.9; 3597 -3.8; 3957 -3.8; 4353 -3.0; 4788 -0.9; 5267 -1.3; 5793 -1.7; 6373 -0.5; 7010 -3.2; 7711 -5.5; 8482 -5.7; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -6.4; 16529 -9.4; 18182 -13.0; 20000 -9.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312454 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312454 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 29 Hz    |  0.69 | 2.7 dB  |
| Peaking | 268 Hz   |  0.5  | -2.5 dB |
| Peaking | 705 Hz   |  2.95 | -1.4 dB |
| Peaking | 5411 Hz  |  1.71 | 5.1 dB  |
| Peaking | 18599 Hz |  1.18 | -8.0 dB |
| Peaking | 1988 Hz  |  7.29 | 0.5 dB  |
| Peaking | 5584 Hz  | 10    | -2.5 dB |
| Peaking | 6495 Hz  |  3.19 | 3.2 dB  |
| Peaking | 7571 Hz  |  2.72 | -2.5 dB |
| Peaking | 14268 Hz |  2.97 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -3.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312454/Audeze%20LCD-3%20sn2312454.png)