# HiFiMAN HE560 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.4; 25 -1.3; 28 -1.3; 31 -1.2; 34 -1.2; 37 -1.2; 41 -1.2; 45 -1.1; 49 -1.2; 54 -1.3; 60 -1.4; 66 -1.6; 72 -1.9; 79 -2.2; 87 -2.5; 96 -2.8; 106 -3.2; 116 -3.4; 128 -3.7; 141 -4.0; 155 -4.2; 170 -4.3; 187 -4.5; 206 -4.7; 227 -4.8; 249 -4.9; 274 -4.6; 302 -4.5; 332 -4.8; 365 -5.2; 402 -5.5; 442 -5.3; 486 -4.5; 535 -2.4; 588 -1.8; 647 -2.8; 712 -3.3; 783 -3.9; 861 -3.9; 947 -3.4; 1042 -3.2; 1146 -3.9; 1261 -3.9; 1387 -3.9; 1526 -3.2; 1678 -2.0; 1846 -0.9; 2031 -0.5; 2234 -1.3; 2457 -1.6; 2703 -2.4; 2973 -3.7; 3270 -4.9; 3597 -5.8; 3957 -6.0; 4353 -7.9; 4788 -7.1; 5267 -2.6; 5793 -3.4; 6373 -5.9; 7010 -4.9; 7711 -4.8; 8482 -6.7; 9330 -6.2; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE560 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE560 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.71 | 3.3 dB  |
| Peaking | 1960 Hz | 3.07 | 3.5 dB  |
| Peaking | 2468 Hz | 4.43 | 1.4 dB  |
| Peaking | 4332 Hz | 4.68 | -4.2 dB |
| Peaking | 8777 Hz | 5.87 | -3.4 dB |
| Peaking | 441 Hz  | 1.24 | -2.3 dB |
| Peaking | 576 Hz  | 2.9  | 3.8 dB  |
| Peaking | 3398 Hz | 5.32 | -0.9 dB |
| Peaking | 5366 Hz | 8.14 | 2.6 dB  |
| Peaking | 6434 Hz | 9.06 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE560%202014/HiFiMAN%20HE560%202014.png)