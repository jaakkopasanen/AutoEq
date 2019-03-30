# Technics RP-F880
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.2; 49 -2.1; 54 -3.0; 60 -4.2; 66 -5.6; 72 -6.7; 79 -7.5; 87 -8.2; 96 -8.8; 106 -9.0; 116 -9.2; 128 -9.3; 141 -9.1; 155 -8.9; 170 -8.7; 187 -8.4; 206 -8.1; 227 -7.5; 249 -6.8; 274 -6.6; 302 -6.9; 332 -7.0; 365 -6.9; 402 -6.6; 442 -6.4; 486 -6.3; 535 -6.1; 588 -6.0; 647 -6.3; 712 -6.4; 783 -6.5; 861 -6.8; 947 -7.2; 1042 -7.7; 1146 -8.4; 1261 -9.2; 1387 -9.9; 1526 -10.5; 1678 -10.2; 1846 -9.2; 2031 -8.1; 2234 -7.2; 2457 -6.7; 2703 -6.4; 2973 -4.7; 3270 -0.7; 3597 -0.6; 3957 -5.8; 4353 -8.1; 4788 -7.8; 5267 -8.1; 5793 -10.2; 6373 -9.5; 7010 -4.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Technics RP-F880 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Technics RP-F880 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.46 | 7.3 dB  |
| Peaking | 100 Hz  |  0.82 | -5.7 dB |
| Peaking | 1545 Hz |  2.14 | -4.2 dB |
| Peaking | 3399 Hz |  5.58 | 7.4 dB  |
| Peaking | 5790 Hz |  4.82 | -4.2 dB |
| Peaking | 178 Hz  |  5    | -0.5 dB |
| Peaking | 565 Hz  |  1.92 | 0.8 dB  |
| Peaking | 3689 Hz | 14.38 | 2.2 dB  |
| Peaking | 4289 Hz |  5.74 | -2.2 dB |
| Peaking | 7089 Hz | 11.95 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Technics%20RP-F880/Technics%20RP-F880.png)