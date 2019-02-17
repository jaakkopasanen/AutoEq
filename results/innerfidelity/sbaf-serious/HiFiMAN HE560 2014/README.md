# HiFiMAN HE560 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.4; 25 -1.3; 28 -1.3; 31 -1.2; 34 -1.2; 37 -1.2; 41 -1.2; 45 -1.1; 49 -1.2; 54 -1.3; 60 -1.4; 66 -1.6; 72 -1.9; 79 -2.2; 87 -2.5; 96 -2.8; 106 -3.2; 116 -3.4; 128 -3.7; 141 -4.0; 155 -4.2; 170 -4.3; 187 -4.5; 206 -4.7; 227 -4.8; 249 -4.9; 274 -4.6; 302 -4.5; 332 -4.8; 365 -5.2; 402 -5.5; 442 -5.3; 486 -4.5; 535 -2.4; 588 -1.8; 647 -2.8; 712 -3.3; 783 -3.9; 861 -3.9; 947 -3.4; 1042 -3.2; 1146 -3.9; 1261 -3.9; 1387 -3.9; 1526 -3.2; 1678 -2.0; 1846 -0.9; 2031 -0.5; 2234 -1.3; 2457 -1.6; 2703 -2.4; 2973 -3.7; 3270 -4.9; 3597 -5.8; 3957 -6.0; 4353 -7.9; 4788 -7.1; 5267 -2.6; 5793 -3.4; 6373 -5.9; 7010 -4.9; 7711 -4.8; 8482 -6.7; 9330 -6.2; 10263 -3.4; 11289 -3.4; 12418 -3.4; 13660 -3.4; 15026 -3.4; 16529 -3.4; 18182 -3.4; 20000 -3.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE560 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE560 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.53 | 2.5 dB  |
| Peaking | 242 Hz  | 0.78 | -1.8 dB |
| Peaking | 2064 Hz | 3.03 | 3.3 dB  |
| Peaking | 4293 Hz | 3.47 | -4.6 dB |
| Peaking | 8604 Hz | 4.63 | -3.8 dB |
| Peaking | 432 Hz  | 3.98 | -1.6 dB |
| Peaking | 570 Hz  | 5.34 | 2.7 dB  |
| Peaking | 1323 Hz | 5.8  | -1.0 dB |
| Peaking | 5351 Hz | 9.36 | 2.5 dB  |
| Peaking | 6453 Hz | 8.81 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE560%202014/HiFiMAN%20HE560%202014.png)