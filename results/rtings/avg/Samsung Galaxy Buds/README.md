# Samsung Galaxy Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.7; 31 -2.0; 34 -2.2; 37 -2.3; 41 -2.4; 45 -2.5; 49 -2.5; 54 -2.4; 60 -2.3; 66 -2.3; 72 -2.3; 79 -2.3; 87 -2.3; 96 -2.4; 106 -2.5; 116 -2.6; 128 -2.7; 141 -2.8; 155 -2.9; 170 -3.0; 187 -3.1; 206 -3.2; 227 -3.3; 249 -3.4; 274 -3.5; 302 -3.5; 332 -3.4; 365 -3.3; 402 -3.2; 442 -3.1; 486 -2.9; 535 -2.5; 588 -2.1; 647 -1.6; 712 -1.2; 783 -1.0; 861 -1.0; 947 -1.5; 1042 -2.2; 1146 -2.9; 1261 -3.7; 1387 -4.3; 1526 -4.5; 1678 -4.3; 1846 -2.7; 2031 -3.2; 2234 -3.6; 2457 -3.2; 2703 -3.2; 2973 -3.4; 3270 -3.8; 3597 -3.9; 3957 -3.8; 4353 -3.8; 4788 -4.3; 5267 -3.7; 5793 -2.7; 6373 -2.8; 7010 -3.1; 7711 -2.6; 8482 -2.9; 9330 -2.9; 10263 -6.9; 11289 -7.2; 12418 -3.4; 13660 -2.9; 15026 -3.2; 16529 -6.1; 18182 -7.9; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Samsung Galaxy Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Samsung Galaxy Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.65 | 3.5 dB  |
| Peaking | 807 Hz   | 2.44 | 2.3 dB  |
| Peaking | 1466 Hz  | 3.28 | -2.0 dB |
| Peaking | 4009 Hz  | 1.8  | -1.0 dB |
| Peaking | 19637 Hz | 0.5  | -5.8 dB |
| Peaking | 296 Hz   | 1.85 | -0.8 dB |
| Peaking | 9313 Hz  | 2.33 | 1.9 dB  |
| Peaking | 10805 Hz | 3    | -6.9 dB |
| Peaking | 13772 Hz | 1.01 | 2.7 dB  |
| Peaking | 17039 Hz | 1.66 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Samsung%20Galaxy%20Buds/Samsung%20Galaxy%20Buds.png)