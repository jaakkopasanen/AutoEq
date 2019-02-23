# Nocs NS700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.8; 25 -6.3; 28 -6.7; 31 -7.1; 34 -7.5; 37 -7.7; 41 -8.0; 45 -8.1; 49 -8.2; 54 -8.3; 60 -8.4; 66 -8.5; 72 -8.8; 79 -8.8; 87 -8.8; 96 -8.3; 106 -7.5; 116 -6.8; 128 -7.6; 141 -7.7; 155 -7.2; 170 -5.8; 187 -5.2; 206 -4.0; 227 -2.8; 249 -1.8; 274 -1.5; 302 -2.1; 332 -4.5; 365 -5.4; 402 -5.1; 442 -4.9; 486 -4.9; 535 -4.6; 588 -4.2; 647 -4.1; 712 -3.9; 783 -3.6; 861 -3.5; 947 -3.3; 1042 -2.9; 1146 -2.4; 1261 -1.9; 1387 -2.1; 1526 -2.9; 1678 -2.3; 1846 -1.8; 2031 -1.6; 2234 -1.9; 2457 -2.2; 2703 -3.0; 2973 -4.1; 3270 -4.6; 3597 -4.4; 3957 -2.4; 4353 -0.5; 4788 -1.7; 5267 -2.8; 5793 -0.8; 6373 -0.8; 7010 -2.9; 7711 -2.9; 8482 -3.2; 9330 -3.2; 10263 -3.2; 11289 -3.2; 12418 -3.2; 13660 -3.2; 15026 -3.2; 16529 -3.2; 18182 -3.2; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.68 | -4.5 dB |
| Peaking | 103 Hz  | 1.15 | -3.3 dB |
| Peaking | 467 Hz  | 2.76 | -1.8 dB |
| Peaking | 1822 Hz | 1.79 | 1.4 dB  |
| Peaking | 6072 Hz | 4.93 | 3.0 dB  |
| Peaking | 153 Hz  | 4.58 | -1.9 dB |
| Peaking | 273 Hz  | 2.65 | 3.2 dB  |
| Peaking | 353 Hz  | 4.26 | -2.3 dB |
| Peaking | 3345 Hz | 4.26 | -2.1 dB |
| Peaking | 4391 Hz | 7.2  | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS700/Nocs%20NS700.png)