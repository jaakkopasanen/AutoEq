# Grado GR 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.0; 25 -9.1; 28 -9.2; 31 -9.2; 34 -9.2; 37 -9.2; 41 -9.2; 45 -9.2; 49 -9.4; 54 -9.5; 60 -9.5; 66 -9.5; 72 -9.5; 79 -9.5; 87 -9.5; 96 -9.5; 106 -9.3; 116 -9.2; 128 -9.5; 141 -9.4; 155 -9.2; 170 -9.2; 187 -9.2; 206 -9.2; 227 -9.2; 249 -9.2; 274 -9.2; 302 -9.0; 332 -8.9; 365 -8.9; 402 -8.7; 442 -8.5; 486 -8.3; 535 -8.1; 588 -7.9; 647 -7.7; 712 -7.4; 783 -7.2; 861 -6.9; 947 -6.7; 1042 -6.5; 1146 -6.2; 1261 -6.0; 1387 -6.0; 1526 -5.8; 1678 -5.6; 1846 -5.8; 2031 -7.3; 2234 -9.1; 2457 -9.2; 2703 -6.7; 2973 -2.3; 3270 -0.5; 3597 -5.1; 3957 -9.2; 4353 -9.5; 4788 -6.4; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GR 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 81 Hz   | 0.18 | -3.1 dB |
| Peaking | 3254 Hz | 4.72 | 10.8 dB |
| Peaking | 4185 Hz | 1.36 | -9.0 dB |
| Peaking | 5725 Hz | 1.85 | 11.2 dB |
| Peaking | 7912 Hz | 2.53 | -2.1 dB |
| Peaking | 417 Hz  | 1.46 | -0.5 dB |
| Peaking | 1871 Hz | 1.33 | 2.8 dB  |
| Peaking | 2336 Hz | 2.69 | -4.6 dB |
| Peaking | 2902 Hz | 7.91 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20GR%208/Grado%20GR%208.png)