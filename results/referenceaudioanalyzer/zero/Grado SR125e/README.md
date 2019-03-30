# Grado SR125e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -1.6; 49 -2.5; 54 -3.4; 60 -4.2; 66 -4.8; 72 -5.3; 79 -5.6; 87 -5.6; 96 -5.6; 106 -5.6; 116 -5.4; 128 -5.2; 141 -4.9; 155 -4.7; 170 -4.4; 187 -4.1; 206 -3.8; 227 -3.5; 249 -3.6; 274 -4.3; 302 -4.6; 332 -4.5; 365 -4.1; 402 -3.8; 442 -3.6; 486 -3.6; 535 -3.4; 588 -3.3; 647 -3.3; 712 -3.3; 783 -3.3; 861 -3.3; 947 -3.4; 1042 -3.6; 1146 -3.8; 1261 -4.1; 1387 -4.6; 1526 -5.3; 1678 -6.8; 1846 -10.0; 2031 -12.1; 2234 -12.4; 2457 -11.6; 2703 -10.6; 2973 -9.0; 3270 -6.8; 3597 -5.2; 3957 -8.5; 4353 -11.9; 4788 -12.6; 5267 -12.4; 5793 -13.2; 6373 -14.3; 7010 -14.0; 7711 -10.6; 8482 -6.8; 9330 -6.5; 10263 -6.6; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.88 | 6.7 dB   |
| Peaking | 211 Hz  | 1.95 | 1.9 dB   |
| Peaking | 2192 Hz | 1.9  | -10.3 dB |
| Peaking | 2393 Hz | 0.19 | 5.1 dB   |
| Peaking | 5930 Hz | 1.26 | -11.8 dB |
| Peaking | 3629 Hz | 5.7  | 4.8 dB   |
| Peaking | 4352 Hz | 2.59 | -2.8 dB  |
| Peaking | 5703 Hz | 2.72 | 5.7 dB   |
| Peaking | 7058 Hz | 1.21 | -5.8 dB  |
| Peaking | 8549 Hz | 2.54 | 5.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20SR125e/Grado%20SR125e.png)