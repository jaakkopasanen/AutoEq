# JBL Everest Elite 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.6; 25 -6.7; 28 -6.8; 31 -6.8; 34 -6.8; 37 -6.7; 41 -6.5; 45 -6.4; 49 -6.3; 54 -6.2; 60 -6.1; 66 -5.9; 72 -5.7; 79 -5.6; 87 -5.5; 96 -5.5; 106 -5.5; 116 -5.5; 128 -5.5; 141 -5.6; 155 -5.6; 170 -5.7; 187 -5.7; 206 -5.8; 227 -5.9; 249 -5.9; 274 -5.8; 302 -5.7; 332 -5.5; 365 -5.3; 402 -5.5; 442 -5.9; 486 -6.3; 535 -6.5; 588 -6.5; 647 -6.2; 712 -5.9; 783 -5.7; 861 -5.7; 947 -5.9; 1042 -5.9; 1146 -5.6; 1261 -7.0; 1387 -8.6; 1526 -8.3; 1678 -8.0; 1846 -8.7; 2031 -9.2; 2234 -9.5; 2457 -9.2; 2703 -8.6; 2973 -8.2; 3270 -7.5; 3597 -6.6; 3957 -5.9; 4353 -4.3; 4788 -1.1; 5267 -0.5; 5793 -4.8; 6373 -5.9; 7010 -5.7; 7711 -5.9; 8482 -7.9; 9330 -9.8; 10263 -13.1; 11289 -16.5; 12418 -14.6; 13660 -8.2; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 1848 Hz  | 1.28 | -2.3 dB  |
| Peaking | 2390 Hz  | 0.03 | 0.8 dB   |
| Peaking | 2556 Hz  | 1.55 | -2.3 dB  |
| Peaking | 5042 Hz  | 4.37 | 6.6 dB   |
| Peaking | 11440 Hz | 2.44 | -11.9 dB |
| Peaking | 553 Hz   | 3.85 | -1.0 dB  |
| Peaking | 1258 Hz  | 2.17 | 1.7 dB   |
| Peaking | 1377 Hz  | 5.21 | -2.7 dB  |
| Peaking | 12779 Hz | 6.29 | -1.9 dB  |
| Peaking | 14264 Hz | 3.57 | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Everest%20Elite%20700/JBL%20Everest%20Elite%20700.png)