# HiFiMAN HE1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.2; 25 -1.4; 28 -1.5; 31 -1.7; 34 -1.9; 37 -2.1; 41 -2.4; 45 -2.6; 49 -2.6; 54 -2.8; 60 -3.1; 66 -3.3; 72 -3.4; 79 -3.7; 87 -4.0; 96 -4.3; 106 -4.6; 116 -4.8; 128 -5.1; 141 -5.1; 155 -5.5; 170 -5.7; 187 -6.1; 206 -4.9; 227 -4.7; 249 -5.5; 274 -5.9; 302 -6.4; 332 -7.1; 365 -6.1; 402 -2.9; 442 -4.0; 486 -4.6; 535 -5.6; 588 -4.0; 647 -3.8; 712 -5.3; 783 -4.2; 861 -4.8; 947 -4.4; 1042 -4.9; 1146 -4.7; 1261 -2.2; 1387 -2.6; 1526 -2.2; 1678 -2.1; 1846 -1.7; 2031 -0.6; 2234 -1.1; 2457 -0.5; 2703 -0.7; 2973 -2.1; 3270 -3.6; 3597 -2.7; 3957 -2.8; 4353 -3.6; 4788 -8.4; 5267 -7.9; 5793 -4.0; 6373 -7.7; 7010 -9.4; 7711 -8.5; 8482 -8.3; 9330 -6.5; 10263 -4.6; 11289 -4.6; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.7; 20000 -8.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.23 | 3.7 dB  |
| Peaking | 201 Hz  | 0.62 | -1.3 dB |
| Peaking | 2334 Hz | 1.01 | 4.0 dB  |
| Peaking | 4916 Hz | 8.21 | -5.1 dB |
| Peaking | 7424 Hz | 2.6  | -5.2 dB |
| Peaking | 343 Hz  | 5.27 | -2.3 dB |
| Peaking | 407 Hz  | 6.72 | 2.9 dB  |
| Peaking | 1074 Hz | 8.28 | -1.5 dB |
| Peaking | 3286 Hz | 5.38 | -2.9 dB |
| Peaking | 3546 Hz | 2.39 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE1000/HiFiMAN%20HE1000.png)