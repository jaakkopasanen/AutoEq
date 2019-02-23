# JBL Everest Elite 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -6.9; 25 -7.0; 28 -7.1; 31 -7.1; 34 -7.1; 37 -6.9; 41 -6.8; 45 -6.7; 49 -6.6; 54 -6.5; 60 -6.3; 66 -6.2; 72 -6.1; 79 -6.0; 87 -5.9; 96 -5.9; 106 -5.9; 116 -5.9; 128 -5.9; 141 -5.9; 155 -6.0; 170 -6.0; 187 -6.0; 206 -6.1; 227 -6.2; 249 -6.1; 274 -6.0; 302 -5.9; 332 -5.7; 365 -5.4; 402 -5.7; 442 -6.0; 486 -6.4; 535 -6.6; 588 -6.5; 647 -6.2; 712 -5.9; 783 -5.6; 861 -5.7; 947 -5.9; 1042 -5.9; 1146 -5.7; 1261 -7.0; 1387 -8.5; 1526 -8.2; 1678 -7.9; 1846 -8.5; 2031 -8.9; 2234 -8.8; 2457 -8.4; 2703 -8.1; 2973 -8.2; 3270 -7.9; 3597 -6.9; 3957 -6.3; 4353 -4.9; 4788 -1.1; 5267 -0.5; 5793 -5.1; 6373 -6.8; 7010 -5.7; 7711 -6.1; 8482 -8.2; 9330 -11.6; 10263 -13.7; 11289 -15.5; 12418 -14.5; 13660 -9.2; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest Elite 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest Elite 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 1004 Hz  | 1.34 | 3.2 dB   |
| Peaking | 1627 Hz  | 0.34 | -7.1 dB  |
| Peaking | 3011 Hz  | 0.1  | 4.1 dB   |
| Peaking | 5058 Hz  | 4.66 | 7.0 dB   |
| Peaking | 11378 Hz | 1.62 | -12.6 dB |
| Peaking | 30 Hz    | 1.96 | -0.8 dB  |
| Peaking | 6237 Hz  | 6.24 | -2.3 dB  |
| Peaking | 7646 Hz  | 2.19 | 1.9 dB   |
| Peaking | 9263 Hz  | 4.57 | -2.2 dB  |
| Peaking | 14500 Hz | 8.09 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Everest%20Elite%20700/JBL%20Everest%20Elite%20700.png)