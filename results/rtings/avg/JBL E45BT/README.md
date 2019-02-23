# JBL E45BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.2; 25 -8.3; 28 -8.4; 31 -8.4; 34 -8.4; 37 -8.4; 41 -8.4; 45 -8.3; 49 -8.3; 54 -8.4; 60 -8.8; 66 -9.2; 72 -9.5; 79 -9.7; 87 -9.9; 96 -9.8; 106 -9.8; 116 -9.6; 128 -9.5; 141 -9.4; 155 -9.3; 170 -9.2; 187 -8.8; 206 -8.5; 227 -7.8; 249 -6.3; 274 -4.6; 302 -3.3; 332 -2.2; 365 -1.0; 402 -0.5; 442 -0.5; 486 -0.8; 535 -1.3; 588 -1.8; 647 -2.4; 712 -3.9; 783 -4.9; 861 -5.8; 947 -6.4; 1042 -6.6; 1146 -6.5; 1261 -6.3; 1387 -6.3; 1526 -6.5; 1678 -6.1; 1846 -4.7; 2031 -5.2; 2234 -5.5; 2457 -5.9; 2703 -7.1; 2973 -9.4; 3270 -11.2; 3597 -11.8; 3957 -10.9; 4353 -8.5; 4788 -4.9; 5267 -6.4; 5793 -7.4; 6373 -9.9; 7010 -12.2; 7711 -10.1; 8482 -6.6; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -7.3; 15026 -8.1; 16529 -9.0; 18182 -9.9; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E45BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E45BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 180 Hz   | 0.28 | -4.8 dB |
| Peaking | 417 Hz   | 0.98 | 10.1 dB |
| Peaking | 3553 Hz  | 3.6  | -6.0 dB |
| Peaking | 20271 Hz | 0.23 | -3.5 dB |
| Peaking | 21229 Hz | 2.27 | -2.6 dB |
| Peaking | 24 Hz    | 2.03 | -1.2 dB |
| Peaking | 4307 Hz  | 1.48 | -4.0 dB |
| Peaking | 4833 Hz  | 7.21 | 3.7 dB  |
| Peaking | 5660 Hz  | 0.6  | 3.9 dB  |
| Peaking | 6973 Hz  | 3.2  | -8.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 7.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E45BT/JBL%20E45BT.png)