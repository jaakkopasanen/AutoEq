# JBL E55BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.2; 25 -9.3; 28 -9.5; 31 -9.6; 34 -9.6; 37 -9.5; 41 -9.4; 45 -9.3; 49 -9.1; 54 -9.1; 60 -9.3; 66 -9.4; 72 -9.4; 79 -9.5; 87 -9.8; 96 -10.3; 106 -10.9; 116 -11.2; 128 -11.3; 141 -11.0; 155 -10.4; 170 -9.5; 187 -8.3; 206 -6.8; 227 -4.8; 249 -2.8; 274 -0.9; 302 -0.5; 332 -0.5; 365 -0.7; 402 -1.9; 442 -2.8; 486 -3.9; 535 -5.1; 588 -6.2; 647 -6.8; 712 -6.9; 783 -6.8; 861 -6.6; 947 -6.5; 1042 -6.4; 1146 -6.4; 1261 -6.0; 1387 -5.4; 1526 -5.0; 1678 -4.9; 1846 -5.2; 2031 -5.6; 2234 -5.7; 2457 -5.7; 2703 -6.2; 2973 -7.2; 3270 -7.4; 3597 -6.1; 3957 -4.5; 4353 -3.2; 4788 -1.6; 5267 -3.2; 5793 -3.3; 6373 -2.9; 7010 -4.0; 7711 -6.3; 8482 -9.2; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.9; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E55BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E55BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.57 | -2.8 dB |
| Peaking | 137 Hz  | 0.98 | -5.4 dB |
| Peaking | 308 Hz  | 1.53 | 8.0 dB  |
| Peaking | 5501 Hz | 1.55 | 4.3 dB  |
| Peaking | 8737 Hz | 4.52 | -4.3 dB |
| Peaking | 460 Hz  | 2.37 | 1.9 dB  |
| Peaking | 613 Hz  | 1.24 | -1.8 dB |
| Peaking | 1645 Hz | 2.24 | 1.6 dB  |
| Peaking | 3207 Hz | 5.12 | -2.3 dB |
| Peaking | 4638 Hz | 7.79 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | 5.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E55BT/JBL%20E55BT.png)