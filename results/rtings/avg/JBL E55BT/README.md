# JBL E55BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -9.8; 25 -10.0; 28 -10.1; 31 -10.2; 34 -10.2; 37 -10.1; 41 -10.0; 45 -9.9; 49 -9.8; 54 -9.8; 60 -9.9; 66 -10.0; 72 -10.1; 79 -10.1; 87 -10.5; 96 -11.0; 106 -11.5; 116 -11.8; 128 -11.9; 141 -11.7; 155 -11.1; 170 -10.1; 187 -8.9; 206 -7.4; 227 -5.4; 249 -3.5; 274 -1.6; 302 -0.5; 332 -0.5; 365 -1.3; 402 -2.5; 442 -3.4; 486 -4.5; 535 -5.7; 588 -6.8; 647 -7.4; 712 -7.6; 783 -7.4; 861 -7.2; 947 -7.1; 1042 -7.1; 1146 -7.0; 1261 -6.7; 1387 -6.1; 1526 -5.6; 1678 -5.5; 1846 -5.8; 2031 -6.3; 2234 -6.3; 2457 -6.3; 2703 -6.8; 2973 -7.8; 3270 -8.0; 3597 -6.7; 3957 -5.1; 4353 -3.8; 4788 -2.2; 5267 -3.9; 5793 -3.9; 6373 -3.5; 7010 -3.9; 7711 -6.6; 8482 -9.8; 9330 -9.2; 10263 -6.5; 11289 -6.3; 12418 -7.5; 13660 -6.7; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
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

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.19 | -3.0 dB |
| Peaking | 208 Hz  | 0.37 | -9.5 dB |
| Peaking | 308 Hz  | 1.09 | 14.9 dB |
| Peaking | 5774 Hz | 1.64 | 3.6 dB  |
| Peaking | 8729 Hz | 4.17 | -5.1 dB |
| Peaking | 470 Hz  | 3.3  | 1.3 dB  |
| Peaking | 636 Hz  | 1.73 | -1.0 dB |
| Peaking | 1607 Hz | 3.07 | 1.3 dB  |
| Peaking | 3189 Hz | 4.49 | -2.6 dB |
| Peaking | 4641 Hz | 7.2  | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.3 dB |
| Peaking | 250 Hz   | 1.41 | 4.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E55BT/JBL%20E55BT.png)