# JBL E25BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.6; 23 -9.9; 25 -10.2; 28 -10.5; 31 -10.8; 34 -11.0; 37 -11.2; 41 -11.4; 45 -11.5; 49 -11.6; 54 -11.7; 60 -11.9; 66 -12.0; 72 -12.1; 79 -12.2; 87 -12.4; 96 -12.5; 106 -12.5; 116 -12.5; 128 -12.4; 141 -12.2; 155 -11.9; 170 -11.6; 187 -11.2; 206 -10.7; 227 -10.2; 249 -9.7; 274 -9.1; 302 -8.4; 332 -7.9; 365 -7.4; 402 -6.8; 442 -6.1; 486 -5.4; 535 -4.5; 588 -3.6; 647 -2.7; 712 -1.7; 783 -0.8; 861 -0.5; 947 -1.1; 1042 -2.3; 1146 -3.2; 1261 -3.7; 1387 -3.8; 1526 -3.5; 1678 -3.3; 1846 -3.5; 2031 -3.7; 2234 -3.6; 2457 -3.2; 2703 -3.5; 2973 -4.5; 3270 -5.6; 3597 -6.1; 3957 -6.1; 4353 -6.3; 4788 -7.1; 5267 -8.0; 5793 -9.7; 6373 -11.1; 7010 -9.6; 7711 -6.6; 8482 -6.5; 9330 -7.5; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.8; 16529 -13.0; 18182 -12.4; 20000 -11.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E25BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E25BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 174 Hz   | 0.13 | -6.6 dB |
| Peaking | 929 Hz   | 0.69 | 17.4 dB |
| Peaking | 1078 Hz  | 1.14 | -8.5 dB |
| Peaking | 6207 Hz  | 3.03 | -5.1 dB |
| Peaking | 18134 Hz | 0.95 | -7.1 dB |
| Peaking | 2672 Hz  | 3.59 | 1.5 dB  |
| Peaking | 3345 Hz  | 2.16 | -1.3 dB |
| Peaking | 8119 Hz  | 5.72 | 1.3 dB  |
| Peaking | 9947 Hz  | 8.3  | -2.0 dB |
| Peaking | 13395 Hz | 3.15 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E25BT/JBL%20E25BT.png)