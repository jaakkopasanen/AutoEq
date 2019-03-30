# Grado iGi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.8; 25 -2.3; 28 -2.8; 31 -3.2; 34 -3.5; 37 -3.8; 41 -4.1; 45 -4.4; 49 -4.6; 54 -4.8; 60 -5.0; 66 -5.2; 72 -5.3; 79 -5.6; 87 -5.6; 96 -5.8; 106 -6.0; 116 -6.0; 128 -6.2; 141 -6.3; 155 -6.3; 170 -6.3; 187 -6.4; 206 -6.8; 227 -7.2; 249 -7.5; 274 -7.8; 302 -8.1; 332 -8.4; 365 -8.5; 402 -8.7; 442 -8.9; 486 -9.0; 535 -9.2; 588 -9.2; 647 -9.4; 712 -9.5; 783 -9.6; 861 -9.8; 947 -10.0; 1042 -10.3; 1146 -10.5; 1261 -10.5; 1387 -9.7; 1526 -8.7; 1678 -8.3; 1846 -7.8; 2031 -6.8; 2234 -5.9; 2457 -4.4; 2703 -2.8; 2973 -1.6; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -2.8; 5267 -3.8; 5793 -5.2; 6373 -7.3; 7010 -7.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado iGi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado iGi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.69 | 5.4 dB  |
| Peaking | 50 Hz   | 0.33 | 0.8 dB  |
| Peaking | 1573 Hz | 0.29 | -5.2 dB |
| Peaking | 3480 Hz | 0.94 | 10.4 dB |
| Peaking | 6589 Hz | 4.16 | -2.8 dB |
| Peaking | 180 Hz  | 5.78 | 0.5 dB  |
| Peaking | 733 Hz  | 2.67 | 0.5 dB  |
| Peaking | 1209 Hz | 5.06 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20iGi/Grado%20iGi.png)