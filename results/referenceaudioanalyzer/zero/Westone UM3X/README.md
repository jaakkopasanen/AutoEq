# Westone UM3X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -10.1; 25 -10.5; 28 -10.9; 31 -11.2; 34 -11.5; 37 -11.7; 41 -11.9; 45 -12.0; 49 -12.1; 54 -12.3; 60 -12.4; 66 -12.4; 72 -12.4; 79 -12.4; 87 -12.4; 96 -12.4; 106 -12.4; 116 -12.4; 128 -12.4; 141 -12.4; 155 -12.5; 170 -12.4; 187 -12.4; 206 -12.3; 227 -12.1; 249 -12.1; 274 -11.8; 302 -11.6; 332 -11.4; 365 -11.2; 402 -10.9; 442 -10.6; 486 -10.3; 535 -9.9; 588 -9.6; 647 -9.2; 712 -8.8; 783 -8.5; 861 -8.2; 947 -7.9; 1042 -7.8; 1146 -7.8; 1261 -7.9; 1387 -8.2; 1526 -8.2; 1678 -8.0; 1846 -7.5; 2031 -6.8; 2234 -5.8; 2457 -4.7; 2703 -3.9; 2973 -4.2; 3270 -4.9; 3597 -3.7; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone UM3X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.44 | -4.6 dB |
| Peaking | 233 Hz  | 0.39 | -4.9 dB |
| Peaking | 1615 Hz | 2.26 | -1.5 dB |
| Peaking | 2615 Hz | 4.26 | 1.8 dB  |
| Peaking | 4940 Hz | 1.61 | 7.0 dB  |
| Peaking | 3539 Hz | 6.41 | -1.8 dB |
| Peaking | 3995 Hz | 3.91 | 2.2 dB  |
| Peaking | 4823 Hz | 4.1  | -1.4 dB |
| Peaking | 6344 Hz | 3.69 | 3.8 dB  |
| Peaking | 7508 Hz | 1.79 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Westone%20UM3X/Westone%20UM3X.png)