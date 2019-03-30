# Westone UM Pro 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.6; 25 -8.8; 28 -9.1; 31 -9.4; 34 -9.7; 37 -9.9; 41 -10.1; 45 -10.3; 49 -10.4; 54 -10.4; 60 -10.6; 66 -10.7; 72 -10.7; 79 -10.7; 87 -10.7; 96 -10.7; 106 -10.7; 116 -10.7; 128 -10.7; 141 -10.4; 155 -10.4; 170 -10.4; 187 -10.4; 206 -10.4; 227 -10.2; 249 -10.0; 274 -10.1; 302 -10.1; 332 -9.9; 365 -9.7; 402 -9.7; 442 -9.6; 486 -9.4; 535 -9.3; 588 -9.1; 647 -8.9; 712 -8.6; 783 -8.4; 861 -8.2; 947 -8.1; 1042 -7.8; 1146 -7.8; 1261 -7.7; 1387 -7.4; 1526 -7.7; 1678 -7.8; 1846 -7.8; 2031 -7.8; 2234 -7.5; 2457 -7.5; 2703 -8.2; 2973 -9.0; 3270 -9.0; 3597 -8.3; 3957 -7.7; 4353 -6.4; 4788 -3.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM Pro 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM Pro 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.29 | -4.1 dB |
| Peaking | 461 Hz  | 0.65 | -1.9 dB |
| Peaking | 4421 Hz | 0.8  | -4.9 dB |
| Peaking | 5558 Hz | 1.99 | 11.1 dB |
| Peaking | 3165 Hz | 5.84 | -1.0 dB |
| Peaking | 4217 Hz | 0.48 | 0.3 dB  |
| Peaking | 7887 Hz | 5.87 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Westone%20UM%20Pro%2010/Westone%20UM%20Pro%2010.png)