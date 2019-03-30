# Creative EP-600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.7; 23 -16.1; 25 -16.5; 28 -16.9; 31 -17.2; 34 -17.4; 37 -17.5; 41 -17.6; 45 -17.6; 49 -17.5; 54 -17.3; 60 -17.0; 66 -16.7; 72 -16.4; 79 -16.0; 87 -15.5; 96 -15.1; 106 -14.5; 116 -14.0; 128 -13.3; 141 -12.7; 155 -12.0; 170 -11.3; 187 -10.5; 206 -9.8; 227 -8.9; 249 -7.9; 274 -7.2; 302 -7.0; 332 -7.0; 365 -6.5; 402 -5.6; 442 -4.8; 486 -4.0; 535 -3.3; 588 -2.7; 647 -2.1; 712 -1.6; 783 -1.1; 861 -0.7; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -1.0; 1678 -1.7; 1846 -2.6; 2031 -3.7; 2234 -5.2; 2457 -7.1; 2703 -9.2; 2973 -10.5; 3270 -10.8; 3597 -9.9; 3957 -8.7; 4353 -8.2; 4788 -8.8; 5267 -10.3; 5793 -10.9; 6373 -9.6; 7010 -6.4; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Creative EP-600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative EP-600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 46 Hz   |  0.29 | -11.0 dB |
| Peaking | 1264 Hz |  0.41 | 7.2 dB   |
| Peaking | 3034 Hz |  1.53 | -8.3 dB  |
| Peaking | 5698 Hz |  3.67 | -5.0 dB  |
| Peaking | 23 Hz   |  1.17 | -0.6 dB  |
| Peaking | 269 Hz  |  3.86 | 0.9 dB   |
| Peaking | 354 Hz  |  4.36 | -0.8 dB  |
| Peaking | 7314 Hz | 10.01 | 1.6 dB   |
| Peaking | 9497 Hz |  8.91 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.9 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | -5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Creative%20EP-600/Creative%20EP-600.png)