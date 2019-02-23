# Klipsch X10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.2; 25 -7.3; 28 -7.3; 31 -7.3; 34 -7.4; 37 -7.5; 41 -7.6; 45 -7.7; 49 -7.9; 54 -8.1; 60 -8.4; 66 -8.7; 72 -9.0; 79 -9.3; 87 -9.6; 96 -10.1; 106 -10.2; 116 -10.4; 128 -10.6; 141 -10.7; 155 -10.9; 170 -10.8; 187 -10.8; 206 -10.7; 227 -10.5; 249 -10.4; 274 -10.1; 302 -9.9; 332 -9.6; 365 -9.2; 402 -8.9; 442 -8.4; 486 -8.2; 535 -7.7; 588 -7.1; 647 -6.8; 712 -6.6; 783 -6.1; 861 -6.1; 947 -6.2; 1042 -6.4; 1146 -6.4; 1261 -6.5; 1387 -6.8; 1526 -7.0; 1678 -7.2; 1846 -6.8; 2031 -6.5; 2234 -6.3; 2457 -5.9; 2703 -6.3; 2973 -6.2; 3270 -3.7; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.8; 8482 -10.5; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.19 | -0.4 dB |
| Peaking | 138 Hz  | 0.66 | -3.6 dB |
| Peaking | 288 Hz  | 1.13 | -1.9 dB |
| Peaking | 5069 Hz | 1.31 | 7.1 dB  |
| Peaking | 8500 Hz | 4.51 | -6.3 dB |
| Peaking | 865 Hz  | 1.45 | 1.5 dB  |
| Peaking | 2176 Hz | 0.31 | -1.1 dB |
| Peaking | 2997 Hz | 5.15 | -1.7 dB |
| Peaking | 3622 Hz | 4.23 | 3.7 dB  |
| Peaking | 6415 Hz | 6.88 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X10/Klipsch%20X10.png)