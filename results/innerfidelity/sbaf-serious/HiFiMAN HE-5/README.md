# HiFiMAN HE-5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.2; 31 -2.7; 34 -3.0; 37 -3.3; 41 -3.5; 45 -3.7; 49 -3.8; 54 -3.6; 60 -3.8; 66 -4.5; 72 -4.7; 79 -4.9; 87 -5.2; 96 -5.5; 106 -5.7; 116 -5.9; 128 -6.2; 141 -6.5; 155 -6.8; 170 -6.9; 187 -7.0; 206 -7.3; 227 -7.4; 249 -7.6; 274 -7.5; 302 -7.5; 332 -7.4; 365 -7.6; 402 -7.9; 442 -7.5; 486 -7.3; 535 -7.7; 588 -7.5; 647 -7.5; 712 -7.1; 783 -6.5; 861 -6.9; 947 -7.0; 1042 -6.4; 1146 -5.3; 1261 -5.1; 1387 -4.9; 1526 -5.3; 1678 -4.4; 1846 -2.6; 2031 -2.9; 2234 -3.8; 2457 -3.3; 2703 -4.4; 2973 -6.1; 3270 -7.0; 3597 -7.3; 3957 -7.8; 4353 -10.3; 4788 -9.0; 5267 -6.2; 5793 -7.8; 6373 -10.7; 7010 -11.1; 7711 -11.0; 8482 -14.1; 9330 -16.0; 10263 -12.2; 11289 -9.1; 12418 -11.2; 13660 -13.5; 15026 -11.6; 16529 -7.4; 18182 -6.7; 20000 -11.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 14 Hz    |  0.36 | 6.3 dB  |
| Peaking | 2044 Hz  |  1.95 | 4.1 dB  |
| Peaking | 4381 Hz  |  5.62 | -3.5 dB |
| Peaking | 8951 Hz  |  2.24 | -8.7 dB |
| Peaking | 14154 Hz |  2.5  | -6.6 dB |
| Peaking | 390 Hz   |  0.66 | -1.2 dB |
| Peaking | 1239 Hz  |  5.01 | 1.2 dB  |
| Peaking | 5472 Hz  |  8.7  | 3.1 dB  |
| Peaking | 6298 Hz  |  5.58 | -2.6 dB |
| Peaking | 11114 Hz | 10.23 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -6.9 dB |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-5/HiFiMAN%20HE-5.png)