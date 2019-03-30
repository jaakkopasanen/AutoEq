# QKZ X36M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.0; 23 -16.1; 25 -16.1; 28 -16.2; 31 -16.3; 34 -16.3; 37 -16.3; 41 -16.1; 45 -16.1; 49 -16.0; 54 -15.9; 60 -15.7; 66 -15.5; 72 -15.3; 79 -15.0; 87 -14.7; 96 -14.4; 106 -14.1; 116 -13.7; 128 -13.3; 141 -12.8; 155 -12.3; 170 -11.7; 187 -11.1; 206 -10.4; 227 -9.7; 249 -9.1; 274 -8.6; 302 -8.0; 332 -7.3; 365 -6.5; 402 -5.7; 442 -4.9; 486 -4.1; 535 -3.3; 588 -2.7; 647 -2.2; 712 -1.8; 783 -1.8; 861 -1.9; 947 -1.8; 1042 -1.7; 1146 -1.4; 1261 -1.1; 1387 -1.2; 1526 -1.2; 1678 -0.8; 1846 -0.5; 2031 -1.3; 2234 -2.8; 2457 -4.5; 2703 -6.0; 2973 -6.9; 3270 -6.8; 3597 -6.1; 3957 -5.7; 4353 -5.6; 4788 -6.3; 5267 -9.4; 5793 -12.1; 6373 -11.1; 7010 -5.0; 7711 -5.0; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -5.3; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`QKZ X36M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `QKZ X36M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 36 Hz   | 0.1  | -11.0 dB |
| Peaking | 925 Hz  | 0.19 | 4.0 dB   |
| Peaking | 1351 Hz | 0.27 | 1.9 dB   |
| Peaking | 3043 Hz | 1.96 | -5.9 dB  |
| Peaking | 5858 Hz | 3.54 | -9.2 dB  |
| Peaking | 637 Hz  | 1.74 | 1.5 dB   |
| Peaking | 850 Hz  | 0.61 | -0.9 dB  |
| Peaking | 1883 Hz | 4.77 | 1.5 dB   |
| Peaking | 6663 Hz | 7.05 | -2.0 dB  |
| Peaking | 7114 Hz | 8.55 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.4 dB |
| Peaking | 62 Hz    | 1.41 | -7.6 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/QKZ%20X36M/QKZ%20X36M.png)