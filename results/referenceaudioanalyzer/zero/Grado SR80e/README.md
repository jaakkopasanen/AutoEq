# Grado SR80e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.8; 66 -2.9; 72 -3.7; 79 -4.4; 87 -5.0; 96 -5.4; 106 -5.6; 116 -5.7; 128 -5.5; 141 -5.4; 155 -5.2; 170 -4.9; 187 -4.5; 206 -4.2; 227 -3.9; 249 -3.7; 274 -3.5; 302 -3.3; 332 -3.2; 365 -3.1; 402 -2.9; 442 -3.0; 486 -3.2; 535 -3.2; 588 -3.2; 647 -3.2; 712 -2.9; 783 -2.9; 861 -2.9; 947 -2.9; 1042 -3.2; 1146 -3.5; 1261 -3.7; 1387 -4.3; 1526 -5.3; 1678 -7.4; 1846 -9.9; 2031 -11.4; 2234 -11.7; 2457 -11.1; 2703 -10.2; 2973 -9.2; 3270 -9.0; 3597 -10.1; 3957 -10.3; 4353 -8.7; 4788 -8.9; 5267 -11.8; 5793 -13.6; 6373 -15.0; 7010 -15.1; 7711 -12.4; 8482 -8.1; 9330 -6.5; 10263 -6.7; 11289 -7.5; 12418 -6.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR80e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR80e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 0.77 | 6.8 dB   |
| Peaking | 1618 Hz | 0.18 | 4.8 dB   |
| Peaking | 2089 Hz | 2.23 | -6.9 dB  |
| Peaking | 3334 Hz | 0.87 | -5.4 dB  |
| Peaking | 6595 Hz | 2.17 | -10.6 dB |
| Peaking | 36 Hz   | 3.11 | -1.1 dB  |
| Peaking | 55 Hz   | 2.76 | 1.7 dB   |
| Peaking | 100 Hz  | 2.09 | -1.2 dB  |
| Peaking | 9314 Hz | 3.66 | 3.3 dB   |
| Peaking | 9607 Hz | 1.4  | -1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | -2.9 dB |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20SR80e/Grado%20SR80e.png)