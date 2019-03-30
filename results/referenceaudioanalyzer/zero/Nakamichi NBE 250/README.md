# Nakamichi NBE 250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.8; 25 -10.5; 28 -11.3; 31 -11.9; 34 -12.4; 37 -12.8; 41 -13.2; 45 -13.5; 49 -13.7; 54 -13.9; 60 -13.9; 66 -13.9; 72 -13.9; 79 -13.9; 87 -13.9; 96 -13.8; 106 -13.6; 116 -13.4; 128 -13.1; 141 -12.8; 155 -12.4; 170 -12.0; 187 -11.5; 206 -11.1; 227 -10.5; 249 -9.9; 274 -9.4; 302 -8.8; 332 -8.1; 365 -7.4; 402 -6.9; 442 -6.7; 486 -6.5; 535 -6.3; 588 -6.0; 647 -5.8; 712 -6.0; 783 -6.1; 861 -6.4; 947 -6.9; 1042 -7.7; 1146 -8.3; 1261 -8.7; 1387 -8.6; 1526 -7.9; 1678 -7.1; 1846 -6.7; 2031 -6.2; 2234 -5.8; 2457 -5.5; 2703 -5.5; 2973 -5.5; 3270 -6.7; 3597 -8.1; 3957 -8.5; 4353 -7.5; 4788 -5.1; 5267 -1.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nakamichi NBE 250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nakamichi NBE 250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 72 Hz   | 0.4  | -8.0 dB |
| Peaking | 1293 Hz | 4.28 | -2.5 dB |
| Peaking | 4040 Hz | 4.56 | -3.3 dB |
| Peaking | 5815 Hz | 3.08 | 6.9 dB  |
| Peaking | 208 Hz  | 1.49 | -1.0 dB |
| Peaking | 585 Hz  | 0.8  | 2.1 dB  |
| Peaking | 1476 Hz | 0.37 | -1.2 dB |
| Peaking | 2514 Hz | 1.8  | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Nakamichi%20NBE%20250/Nakamichi%20NBE%20250.png)