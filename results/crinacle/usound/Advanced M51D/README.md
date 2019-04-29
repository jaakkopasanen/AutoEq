# Advanced M51D
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.0; 45 -1.4; 49 -1.7; 54 -2.1; 60 -2.6; 66 -3.0; 72 -3.4; 79 -4.0; 87 -4.5; 96 -5.0; 106 -5.6; 116 -6.1; 128 -6.5; 141 -7.0; 155 -7.4; 170 -7.7; 187 -8.0; 206 -8.3; 227 -8.6; 249 -8.8; 274 -9.1; 302 -9.3; 332 -9.5; 365 -9.7; 402 -9.8; 442 -9.9; 486 -9.8; 535 -9.6; 588 -9.2; 647 -8.6; 712 -8.0; 783 -7.2; 861 -6.4; 947 -6.0; 1042 -6.2; 1146 -6.8; 1261 -7.6; 1387 -8.3; 1526 -8.6; 1678 -8.6; 1846 -8.5; 2031 -8.2; 2234 -7.4; 2457 -6.2; 2703 -4.7; 2973 -3.8; 3270 -3.5; 3597 -4.3; 3957 -6.0; 4353 -6.2; 4788 -2.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.9; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -11.1; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced M51D GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced M51D ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.51 | 6.4 dB  |
| Peaking | 339 Hz   | 0.72 | -3.5 dB |
| Peaking | 1787 Hz  | 2.46 | -2.4 dB |
| Peaking | 3064 Hz  | 3.72 | 3.2 dB  |
| Peaking | 5707 Hz  | 3.16 | 6.9 dB  |
| Peaking | 563 Hz   | 2.8  | -1.0 dB |
| Peaking | 969 Hz   | 2.3  | 1.9 dB  |
| Peaking | 1440 Hz  | 2.15 | -1.3 dB |
| Peaking | 1699 Hz  | 3.93 | 0.8 dB  |
| Peaking | 19513 Hz | 1.24 | -7.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20M51D/Advanced%20M51D.png)