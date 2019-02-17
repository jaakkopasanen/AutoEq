# JBL E45BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.1; 25 -8.2; 28 -8.3; 31 -8.3; 34 -8.3; 37 -8.3; 41 -8.3; 45 -8.3; 49 -8.2; 54 -8.3; 60 -8.7; 66 -9.1; 72 -9.5; 79 -9.7; 87 -9.8; 96 -9.8; 106 -9.7; 116 -9.6; 128 -9.4; 141 -9.3; 155 -9.2; 170 -9.1; 187 -8.8; 206 -8.4; 227 -7.7; 249 -6.2; 274 -4.6; 302 -3.2; 332 -2.1; 365 -0.9; 402 -0.5; 442 -0.5; 486 -0.7; 535 -1.2; 588 -1.7; 647 -2.3; 712 -3.9; 783 -4.8; 861 -5.7; 947 -6.3; 1042 -6.5; 1146 -6.4; 1261 -6.2; 1387 -6.2; 1526 -6.4; 1678 -6.0; 1846 -4.6; 2031 -5.1; 2234 -5.4; 2457 -5.8; 2703 -7.0; 2973 -9.3; 3270 -11.1; 3597 -11.7; 3957 -10.9; 4353 -8.4; 4788 -4.8; 5267 -6.3; 5793 -7.3; 6373 -9.8; 7010 -12.1; 7711 -10.0; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.2; 15026 -8.0; 16529 -8.9; 18182 -9.8; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E45BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E45BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 177 Hz   | 0.3  | -4.6 dB |
| Peaking | 417 Hz   | 0.97 | 9.9 dB  |
| Peaking | 3556 Hz  | 3.76 | -5.8 dB |
| Peaking | 19950 Hz | 0.29 | -3.3 dB |
| Peaking | 22049 Hz | 2.07 | -3.0 dB |
| Peaking | 24 Hz    | 1.9  | -1.0 dB |
| Peaking | 1010 Hz  | 3.38 | -1.2 dB |
| Peaking | 1987 Hz  | 4.11 | 1.8 dB  |
| Peaking | 7053 Hz  | 3.24 | -9.0 dB |
| Peaking | 7241 Hz  | 1.09 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 7.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.4 dB |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E45BT/JBL%20E45BT.png)