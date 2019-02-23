# JBL E50BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.6; 25 -8.2; 28 -8.9; 31 -9.4; 34 -9.6; 37 -9.8; 41 -9.8; 45 -9.7; 49 -9.7; 54 -9.8; 60 -9.7; 66 -9.7; 72 -9.7; 79 -9.6; 87 -9.7; 96 -9.7; 106 -9.7; 116 -9.8; 128 -9.8; 141 -9.6; 155 -9.4; 170 -8.9; 187 -8.4; 206 -7.5; 227 -6.3; 249 -4.8; 274 -3.0; 302 -0.7; 332 -0.5; 365 -0.5; 402 -0.5; 442 -0.8; 486 -1.8; 535 -2.6; 588 -3.5; 647 -4.4; 712 -5.2; 783 -6.0; 861 -6.7; 947 -7.0; 1042 -7.0; 1146 -7.3; 1261 -7.9; 1387 -8.8; 1526 -9.4; 1678 -10.7; 1846 -10.9; 2031 -10.6; 2234 -9.7; 2457 -8.2; 2703 -8.1; 2973 -8.0; 3270 -7.3; 3597 -5.6; 3957 -5.2; 4353 -7.3; 4788 -7.9; 5267 -6.7; 5793 -3.6; 6373 -2.7; 7010 -4.3; 7711 -7.8; 8482 -11.0; 9330 -12.4; 10263 -11.7; 11289 -10.1; 12418 -8.5; 13660 -6.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E50BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 136 Hz  | 0.25 | -4.6 dB |
| Peaking | 369 Hz  | 1.06 | 10.2 dB |
| Peaking | 1820 Hz | 1.81 | -4.6 dB |
| Peaking | 6462 Hz | 3.53 | 5.8 dB  |
| Peaking | 9482 Hz | 1.9  | -6.6 dB |
| Peaking | 34 Hz   | 3.26 | -0.7 dB |
| Peaking | 186 Hz  | 3.11 | -0.7 dB |
| Peaking | 297 Hz  | 9.75 | 1.4 dB  |
| Peaking | 3847 Hz | 6.6  | 2.5 dB  |
| Peaking | 4627 Hz | 6.47 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 5.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20E50BT/JBL%20E50BT.png)