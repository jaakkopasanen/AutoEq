# JBL E45BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.1; 25 -8.1; 28 -8.2; 31 -8.2; 34 -8.2; 37 -8.2; 41 -8.2; 45 -8.2; 49 -8.2; 54 -8.2; 60 -8.5; 66 -8.9; 72 -9.3; 79 -9.5; 87 -9.6; 96 -9.7; 106 -9.5; 116 -9.4; 128 -9.3; 141 -9.2; 155 -9.1; 170 -9.0; 187 -8.7; 206 -8.4; 227 -7.7; 249 -6.3; 274 -4.6; 302 -3.3; 332 -2.2; 365 -1.0; 402 -0.5; 442 -0.5; 486 -0.9; 535 -1.4; 588 -1.8; 647 -2.6; 712 -4.1; 783 -5.1; 861 -5.9; 947 -6.5; 1042 -6.8; 1146 -6.7; 1261 -6.5; 1387 -6.5; 1526 -6.8; 1678 -6.3; 1846 -5.1; 2031 -5.7; 2234 -6.4; 2457 -6.8; 2703 -7.7; 2973 -9.5; 3270 -11.0; 3597 -11.6; 3957 -10.6; 4353 -8.1; 4788 -5.5; 5267 -6.8; 5793 -7.4; 6373 -8.9; 7010 -12.2; 7711 -10.8; 8482 -6.7; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.6; 15026 -7.7; 16529 -8.8; 18182 -9.7; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E45BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E45BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 212 Hz   | 0.27 | -4.9 dB |
| Peaking | 422 Hz   | 0.95 | 10.6 dB |
| Peaking | 3510 Hz  | 3.75 | -5.7 dB |
| Peaking | 7162 Hz  | 5.63 | -6.4 dB |
| Peaking | 18712 Hz | 0.93 | -3.8 dB |
| Peaking | 24 Hz    | 2.03 | -1.0 dB |
| Peaking | 640 Hz   | 3.95 | 1.6 dB  |
| Peaking | 884 Hz   | 1.07 | -0.9 dB |
| Peaking | 1905 Hz  | 4.88 | 1.8 dB  |
| Peaking | 10509 Hz | 1.59 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 7.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.3 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E45BT/JBL%20E45BT.png)