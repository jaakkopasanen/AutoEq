# Panasonic HJE 120
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -4.0; 25 -4.9; 28 -6.0; 31 -6.8; 34 -7.4; 37 -8.0; 41 -8.5; 45 -9.0; 49 -9.3; 54 -9.7; 60 -10.0; 66 -10.2; 72 -10.4; 79 -10.5; 87 -10.6; 96 -10.6; 106 -10.6; 116 -10.6; 128 -10.6; 141 -10.5; 155 -10.3; 170 -10.2; 187 -10.0; 206 -9.8; 227 -9.5; 249 -9.2; 274 -8.9; 302 -8.5; 332 -8.0; 365 -7.4; 402 -6.9; 442 -6.5; 486 -6.0; 535 -5.5; 588 -4.9; 647 -4.2; 712 -3.4; 783 -2.7; 861 -2.1; 947 -1.5; 1042 -1.1; 1146 -0.7; 1261 -0.5; 1387 -0.5; 1526 -0.6; 1678 -1.1; 1846 -1.9; 2031 -3.1; 2234 -4.8; 2457 -7.1; 2703 -9.1; 2973 -9.9; 3270 -9.2; 3597 -7.6; 3957 -6.2; 4353 -5.7; 4788 -6.7; 5267 -8.1; 5793 -7.9; 6373 -5.0; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic HJE 120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic HJE 120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.41 | 4.5 dB  |
| Peaking | 61 Hz   | 0.52 | -3.5 dB |
| Peaking | 194 Hz  | 0.48 | -3.6 dB |
| Peaking | 1409 Hz | 0.67 | 6.5 dB  |
| Peaking | 2888 Hz | 1.78 | -7.2 dB |
| Peaking | 22 Hz   | 0.84 | 0.4 dB  |
| Peaking | 4279 Hz | 3.5  | 1.7 dB  |
| Peaking | 5541 Hz | 2.71 | -3.4 dB |
| Peaking | 6758 Hz | 6.41 | 4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Panasonic%20HJE%20120/Panasonic%20HJE%20120.png)