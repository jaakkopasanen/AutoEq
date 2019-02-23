# JBL T450BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.0; 25 -4.5; 28 -5.2; 31 -5.8; 34 -6.2; 37 -6.6; 41 -7.0; 45 -7.3; 49 -7.6; 54 -7.8; 60 -8.2; 66 -8.8; 72 -9.3; 79 -9.8; 87 -10.1; 96 -10.4; 106 -10.7; 116 -10.9; 128 -11.0; 141 -10.9; 155 -10.9; 170 -10.7; 187 -10.4; 206 -9.9; 227 -9.2; 249 -8.4; 274 -7.6; 302 -6.6; 332 -6.8; 365 -6.1; 402 -5.3; 442 -5.3; 486 -5.6; 535 -5.8; 588 -6.0; 647 -6.1; 712 -6.1; 783 -6.2; 861 -6.2; 947 -6.1; 1042 -5.8; 1146 -5.5; 1261 -5.4; 1387 -5.6; 1526 -5.5; 1678 -5.3; 1846 -4.9; 2031 -4.7; 2234 -3.6; 2457 -3.7; 2703 -4.3; 2973 -5.5; 3270 -6.2; 3597 -5.4; 3957 -4.0; 4353 -3.0; 4788 -1.3; 5267 -0.5; 5793 -0.6; 6373 -2.5; 7010 -5.3; 7711 -9.2; 8482 -11.6; 9330 -12.6; 10263 -11.0; 11289 -8.7; 12418 -7.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL T450BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL T450BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.67 | 3.2 dB  |
| Peaking | 132 Hz  | 0.72 | -5.5 dB |
| Peaking | 1793 Hz | 0.07 | 1.3 dB  |
| Peaking | 5659 Hz | 2.06 | 6.9 dB  |
| Peaking | 9018 Hz | 1.74 | -8.4 dB |
| Peaking | 207 Hz  | 4.36 | -0.8 dB |
| Peaking | 416 Hz  | 2.18 | 1.3 dB  |
| Peaking | 782 Hz  | 1.17 | -0.8 dB |
| Peaking | 2364 Hz | 3.89 | 1.8 dB  |
| Peaking | 3279 Hz | 5.53 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20T450BT/JBL%20T450BT.png)