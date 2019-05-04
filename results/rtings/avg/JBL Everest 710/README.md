# JBL Everest 710
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.1; 25 -3.1; 28 -3.1; 31 -2.9; 34 -2.7; 37 -2.5; 41 -2.3; 45 -2.1; 49 -1.9; 54 -1.8; 60 -1.9; 66 -2.1; 72 -2.5; 79 -3.0; 87 -3.6; 96 -3.9; 106 -4.0; 116 -4.1; 128 -4.0; 141 -3.6; 155 -2.8; 170 -2.1; 187 -2.1; 206 -1.7; 227 -1.3; 249 -1.3; 274 -1.4; 302 -1.8; 332 -2.0; 365 -1.9; 402 -2.4; 442 -4.2; 486 -5.2; 535 -5.2; 588 -5.3; 647 -5.5; 712 -5.9; 783 -6.4; 861 -6.6; 947 -6.7; 1042 -6.5; 1146 -6.7; 1261 -7.2; 1387 -7.7; 1526 -8.1; 1678 -8.0; 1846 -7.5; 2031 -6.1; 2234 -5.4; 2457 -4.7; 2703 -3.5; 2973 -3.4; 3270 -3.3; 3597 -2.7; 3957 -2.4; 4353 -0.5; 4788 -0.5; 5267 -2.0; 5793 -5.1; 6373 -5.2; 7010 -6.1; 7711 -7.5; 8482 -7.1; 9330 -6.1; 10263 -8.0; 11289 -10.8; 12418 -10.0; 13660 -7.1; 15026 -6.1; 16529 -5.0; 18182 -4.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Everest 710 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Everest 710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 260 Hz   | 0.9  | 3.5 dB  |
| Peaking | 1355 Hz  | 0.58 | -3.7 dB |
| Peaking | 4863 Hz  | 1.04 | 7.8 dB  |
| Peaking | 6497 Hz  | 1.22 | -6.1 dB |
| Peaking | 11799 Hz | 2.24 | -6.5 dB |
| Peaking | 14 Hz    | 0.56 | 1.2 dB  |
| Peaking | 54 Hz    | 1.07 | 2.4 dB  |
| Peaking | 111 Hz   | 1.77 | -1.3 dB |
| Peaking | 1077 Hz  | 6.07 | 0.8 dB  |
| Peaking | 9456 Hz  | 7.57 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Everest%20710/JBL%20Everest%20710.png)