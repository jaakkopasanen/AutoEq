# JBL Everest Elite 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.2; 23 -7.3; 25 -7.4; 28 -7.5; 31 -7.6; 34 -7.5; 37 -7.4; 41 -7.2; 45 -7.1; 49 -7.0; 54 -6.9; 60 -6.8; 66 -6.7; 72 -6.5; 79 -6.4; 87 -6.4; 96 -6.3; 106 -6.3; 116 -6.4; 128 -6.4; 141 -6.4; 155 -6.4; 170 -6.4; 187 -6.5; 206 -6.6; 227 -6.6; 249 -6.6; 274 -6.5; 302 -6.4; 332 -6.2; 365 -5.9; 402 -6.1; 442 -6.5; 486 -6.8; 535 -7.0; 588 -7.0; 647 -6.6; 712 -6.3; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.3; 1146 -6.1; 1261 -7.5; 1387 -9.0; 1526 -8.7; 1678 -8.3; 1846 -8.9; 2031 -9.3; 2234 -9.3; 2457 -8.9; 2703 -8.6; 2973 -8.6; 3270 -8.3; 3597 -7.4; 3957 -6.8; 4353 -5.4; 4788 -1.5; 5267 -0.5; 5793 -5.5; 6373 -7.2; 7010 -6.2; 7711 -6.1; 8482 -8.7; 9330 -12.0; 10263 -14.1; 11289 -16.0; 12418 -15.0; 13660 -9.7; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.83 | -1.2 dB  |
| Peaking | 88 Hz    | 1.85 | 0.2 dB   |
| Peaking | 2245 Hz  | 1.11 | -3.0 dB  |
| Peaking | 5070 Hz  | 4.78 | 7.6 dB   |
| Peaking | 11353 Hz | 2.15 | -10.6 dB |
| Peaking | 1199 Hz  | 2.03 | 1.6 dB   |
| Peaking | 1390 Hz  | 4.76 | -2.5 dB  |
| Peaking | 7751 Hz  | 4.03 | 4.7 dB   |
| Peaking | 8136 Hz  | 1.67 | -2.6 dB  |
| Peaking | 14806 Hz | 3.68 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Everest%20Elite%20700/JBL%20Everest%20Elite%20700.png)