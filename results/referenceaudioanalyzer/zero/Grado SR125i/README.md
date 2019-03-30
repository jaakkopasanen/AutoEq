# Grado SR125i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.0; 54 -2.0; 60 -2.9; 66 -3.7; 72 -4.3; 79 -4.7; 87 -4.8; 96 -5.1; 106 -4.9; 116 -4.8; 128 -4.6; 141 -4.4; 155 -4.2; 170 -4.0; 187 -3.8; 206 -3.5; 227 -3.4; 249 -3.2; 274 -3.2; 302 -2.9; 332 -2.9; 365 -2.9; 402 -2.7; 442 -2.5; 486 -2.5; 535 -2.3; 588 -2.5; 647 -2.8; 712 -2.9; 783 -2.9; 861 -2.9; 947 -3.0; 1042 -3.2; 1146 -3.4; 1261 -3.9; 1387 -4.4; 1526 -5.1; 1678 -7.0; 1846 -10.4; 2031 -12.4; 2234 -12.5; 2457 -12.0; 2703 -11.8; 2973 -10.7; 3270 -8.3; 3597 -6.6; 3957 -8.7; 4353 -12.2; 4788 -13.9; 5267 -13.9; 5793 -14.2; 6373 -15.8; 7010 -15.6; 7711 -11.7; 8482 -7.6; 9330 -6.8; 10263 -7.7; 11289 -7.7; 12418 -6.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.76 | 6.6 dB  |
| Peaking | 514 Hz  | 0.38 | 4.0 dB  |
| Peaking | 1488 Hz | 1.39 | 2.9 dB  |
| Peaking | 2129 Hz | 1.79 | -8.7 dB |
| Peaking | 6102 Hz | 1.8  | -9.5 dB |
| Peaking | 2859 Hz | 3.3  | -3.5 dB |
| Peaking | 4008 Hz | 1.41 | 5.7 dB  |
| Peaking | 4506 Hz | 3.6  | -7.4 dB |
| Peaking | 7110 Hz | 6.45 | -3.4 dB |
| Peaking | 8800 Hz | 5.13 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Grado%20SR125i/Grado%20SR125i.png)