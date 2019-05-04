# JBL E55BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.6; 25 -9.8; 28 -9.9; 31 -10.0; 34 -10.0; 37 -10.0; 41 -9.9; 45 -9.7; 49 -9.6; 54 -9.6; 60 -9.7; 66 -9.9; 72 -9.9; 79 -10.0; 87 -10.3; 96 -10.8; 106 -11.3; 116 -11.6; 128 -11.7; 141 -11.5; 155 -10.9; 170 -10.0; 187 -8.8; 206 -7.3; 227 -5.3; 249 -3.4; 274 -1.6; 302 -0.5; 332 -0.5; 365 -1.3; 402 -2.5; 442 -3.4; 486 -4.6; 535 -5.8; 588 -6.9; 647 -7.5; 712 -7.7; 783 -7.6; 861 -7.4; 947 -7.3; 1042 -7.3; 1146 -7.2; 1261 -6.9; 1387 -6.3; 1526 -5.8; 1678 -5.6; 1846 -6.1; 2031 -6.8; 2234 -7.2; 2457 -7.2; 2703 -7.4; 2973 -7.9; 3270 -7.8; 3597 -6.5; 3957 -4.8; 4353 -3.4; 4788 -2.7; 5267 -4.3; 5793 -4.0; 6373 -2.6; 7010 -3.8; 7711 -7.4; 8482 -9.5; 9330 -7.5; 10263 -6.3; 11289 -7.0; 12418 -7.8; 13660 -6.4; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E55BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E55BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.25 | -2.9 dB |
| Peaking | 217 Hz   | 0.35 | -9.6 dB |
| Peaking | 311 Hz   | 1.06 | 15.3 dB |
| Peaking | 6411 Hz  | 1.62 | 4.6 dB  |
| Peaking | 8308 Hz  | 3.19 | -5.4 dB |
| Peaking | 135 Hz   | 5.56 | -0.7 dB |
| Peaking | 1613 Hz  | 3.2  | 1.7 dB  |
| Peaking | 3345 Hz  | 1.25 | -2.4 dB |
| Peaking | 4372 Hz  | 3.43 | 3.6 dB  |
| Peaking | 12167 Hz | 6.21 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.1 dB |
| Peaking | 250 Hz   | 1.41 | 4.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E55BT/JBL%20E55BT.png)