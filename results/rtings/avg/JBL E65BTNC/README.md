# JBL E65BTNC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.9; 23 -12.7; 25 -12.5; 28 -12.2; 31 -12.0; 34 -11.7; 37 -11.4; 41 -11.1; 45 -10.8; 49 -10.6; 54 -10.4; 60 -10.2; 66 -10.1; 72 -9.8; 79 -9.6; 87 -9.5; 96 -9.8; 106 -10.3; 116 -10.5; 128 -10.5; 141 -10.1; 155 -9.4; 170 -8.6; 187 -7.7; 206 -6.7; 227 -5.8; 249 -4.9; 274 -4.3; 302 -3.9; 332 -3.9; 365 -4.1; 402 -4.3; 442 -4.6; 486 -4.5; 535 -4.3; 588 -4.2; 647 -4.1; 712 -4.2; 783 -4.7; 861 -5.2; 947 -5.9; 1042 -6.7; 1146 -7.0; 1261 -6.3; 1387 -6.2; 1526 -6.6; 1678 -5.5; 1846 -4.8; 2031 -4.0; 2234 -2.8; 2457 -2.0; 2703 -1.9; 2973 -0.5; 3270 -4.5; 3597 -9.4; 3957 -8.0; 4353 -5.5; 4788 -2.1; 5267 -2.7; 5793 -6.3; 6373 -8.0; 7010 -9.7; 7711 -8.7; 8482 -6.1; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.8; 13660 -7.3; 15026 -5.8; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E65BTNC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E65BTNC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.69 | -6.9 dB |
| Peaking | 67 Hz   | 1.29 | -2.4 dB |
| Peaking | 127 Hz  | 2.32 | -4.2 dB |
| Peaking | 2650 Hz | 3.35 | 4.8 dB  |
| Peaking | 7136 Hz | 5.39 | -4.7 dB |
| Peaking | 307 Hz  | 3.21 | 1.8 dB  |
| Peaking | 1033 Hz | 0.62 | 4.3 dB  |
| Peaking | 1164 Hz | 1.2  | -5.5 dB |
| Peaking | 3690 Hz | 6.54 | -5.4 dB |
| Peaking | 4975 Hz | 8.38 | 5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | 1.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E65BTNC/JBL%20E65BTNC.png)