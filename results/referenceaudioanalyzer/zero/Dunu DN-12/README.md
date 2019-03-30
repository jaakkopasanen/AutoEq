# Dunu DN-12
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.8; 23 -14.8; 25 -14.8; 28 -14.7; 31 -14.6; 34 -14.5; 37 -14.4; 41 -14.2; 45 -14.2; 49 -14.1; 54 -13.9; 60 -13.6; 66 -13.3; 72 -13.0; 79 -12.8; 87 -12.8; 96 -12.6; 106 -12.3; 116 -11.8; 128 -11.3; 141 -11.1; 155 -11.2; 170 -11.1; 187 -10.5; 206 -10.0; 227 -9.3; 249 -8.8; 274 -8.0; 302 -7.3; 332 -6.7; 365 -6.1; 402 -5.4; 442 -4.8; 486 -4.2; 535 -3.6; 588 -3.1; 647 -2.5; 712 -2.1; 783 -1.6; 861 -1.3; 947 -1.0; 1042 -0.8; 1146 -0.6; 1261 -0.5; 1387 -0.7; 1526 -0.9; 1678 -0.8; 1846 -1.1; 2031 -2.1; 2234 -3.5; 2457 -5.1; 2703 -6.5; 2973 -7.5; 3270 -7.9; 3597 -7.5; 3957 -7.0; 4353 -7.3; 4788 -7.2; 5267 -6.3; 5793 -4.6; 6373 -2.5; 7010 -2.2; 7711 -4.4; 8482 -4.7; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN-12 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN-12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.89 | -9.6 dB |
| Peaking | 42 Hz   | 0.34 | -8.3 dB |
| Peaking | 191 Hz  | 0.66 | -3.4 dB |
| Peaking | 2054 Hz | 0.35 | 7.3 dB  |
| Peaking | 3290 Hz | 0.96 | -9.8 dB |
| Peaking | 2754 Hz | 3.51 | -0.3 dB |
| Peaking | 3776 Hz | 3.44 | 1.2 dB  |
| Peaking | 4850 Hz | 3.16 | -1.5 dB |
| Peaking | 6688 Hz | 4.8  | 4.1 dB  |
| Peaking | 7743 Hz | 1.17 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Dunu%20DN-12/Dunu%20DN-12.png)