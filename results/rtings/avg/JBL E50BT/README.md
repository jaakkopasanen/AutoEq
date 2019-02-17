# JBL E50BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -7.2; 25 -7.7; 28 -8.4; 31 -8.9; 34 -9.2; 37 -9.3; 41 -9.3; 45 -9.2; 49 -9.2; 54 -9.3; 60 -9.3; 66 -9.3; 72 -9.2; 79 -9.2; 87 -9.2; 96 -9.2; 106 -9.2; 116 -9.3; 128 -9.3; 141 -9.1; 155 -8.9; 170 -8.5; 187 -7.9; 206 -7.0; 227 -5.8; 249 -4.3; 274 -2.5; 302 -0.5; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.5; 486 -1.3; 535 -2.1; 588 -3.0; 647 -3.9; 712 -4.7; 783 -5.5; 861 -6.2; 947 -6.5; 1042 -6.5; 1146 -6.8; 1261 -7.5; 1387 -8.3; 1526 -8.9; 1678 -10.2; 1846 -10.4; 2031 -10.1; 2234 -9.2; 2457 -7.7; 2703 -7.6; 2973 -7.5; 3270 -6.8; 3597 -5.2; 3957 -4.7; 4353 -6.9; 4788 -7.4; 5267 -6.2; 5793 -3.2; 6373 -2.2; 7010 -4.1; 7711 -7.3; 8482 -10.5; 9330 -12.0; 10263 -11.2; 11289 -9.6; 12418 -8.0; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E50BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 144 Hz  | 0.27 | -4.3 dB |
| Peaking | 369 Hz  | 0.98 | 9.9 dB  |
| Peaking | 1811 Hz | 2.05 | -4.3 dB |
| Peaking | 6409 Hz | 3.41 | 5.9 dB  |
| Peaking | 9458 Hz | 2.06 | -6.2 dB |
| Peaking | 34 Hz   | 3.19 | -0.7 dB |
| Peaking | 186 Hz  | 3.13 | -0.7 dB |
| Peaking | 291 Hz  | 9.28 | 1.4 dB  |
| Peaking | 3860 Hz | 6.05 | 2.7 dB  |
| Peaking | 4642 Hz | 6.05 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | 2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 5.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E50BT/JBL%20E50BT.png)