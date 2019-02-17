# Yamaha Pro300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.8; 206 -1.2; 227 -1.5; 249 -1.2; 274 -1.1; 302 -1.8; 332 -2.1; 365 -3.0; 402 -3.4; 442 -4.1; 486 -4.9; 535 -5.1; 588 -3.5; 647 -3.8; 712 -4.6; 783 -4.8; 861 -5.4; 947 -6.0; 1042 -6.8; 1146 -7.5; 1261 -8.5; 1387 -10.0; 1526 -10.8; 1678 -11.9; 1846 -11.9; 2031 -10.3; 2234 -7.7; 2457 -5.0; 2703 -2.9; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.7; 6373 -2.8; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha Pro300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.14 | 6.0 dB  |
| Peaking | 235 Hz  | 0.72 | 2.7 dB  |
| Peaking | 685 Hz  | 2.75 | 1.6 dB  |
| Peaking | 1780 Hz | 1.68 | -8.7 dB |
| Peaking | 3592 Hz | 0.93 | 7.9 dB  |
| Peaking | 902 Hz  | 4.78 | 0.3 dB  |
| Peaking | 2960 Hz | 2.82 | 2.1 dB  |
| Peaking | 3791 Hz | 1.29 | -3.0 dB |
| Peaking | 5279 Hz | 1.24 | 3.2 dB  |
| Peaking | 8106 Hz | 1.46 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 4.8 dB  |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 9.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro300/Yamaha%20Pro300.png)