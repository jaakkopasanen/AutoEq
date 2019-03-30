# Westone UM1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.3; 25 -4.8; 28 -5.4; 31 -5.9; 34 -6.2; 37 -6.5; 41 -6.8; 45 -7.1; 49 -7.2; 54 -7.5; 60 -7.7; 66 -7.9; 72 -8.0; 79 -8.2; 87 -8.3; 96 -8.3; 106 -8.3; 116 -8.5; 128 -8.6; 141 -8.8; 155 -9.0; 170 -9.0; 187 -9.0; 206 -9.1; 227 -9.3; 249 -9.3; 274 -9.3; 302 -9.3; 332 -9.3; 365 -9.3; 402 -9.3; 442 -9.6; 486 -9.6; 535 -9.6; 588 -9.6; 647 -9.6; 712 -9.4; 783 -9.3; 861 -9.3; 947 -9.3; 1042 -9.3; 1146 -9.3; 1261 -9.3; 1387 -9.3; 1526 -9.3; 1678 -9.3; 1846 -9.0; 2031 -8.8; 2234 -8.2; 2457 -7.5; 2703 -6.6; 2973 -6.5; 3270 -7.5; 3597 -8.3; 3957 -8.2; 4353 -6.5; 4788 -3.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.01 | 3.6 dB  |
| Peaking | 79 Hz    | 0.38 | -1.2 dB |
| Peaking | 427 Hz   | 0.31 | -2.3 dB |
| Peaking | 2507 Hz  | 0.24 | -1.5 dB |
| Peaking | 5717 Hz  | 2.57 | 8.3 dB  |
| Peaking | 1770 Hz  | 2.51 | -0.6 dB |
| Peaking | 2848 Hz  | 3.02 | 2.4 dB  |
| Peaking | 3869 Hz  | 2.24 | -2.2 dB |
| Peaking | 4949 Hz  | 8.04 | 2.4 dB  |
| Peaking | 12817 Hz | 1.8  | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Westone%20UM1/Westone%20UM1.png)