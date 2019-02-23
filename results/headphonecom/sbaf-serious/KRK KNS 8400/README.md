# KRK KNS 8400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -10.7; 25 -10.6; 28 -10.3; 31 -9.9; 34 -9.5; 37 -9.0; 41 -8.3; 45 -7.5; 49 -6.7; 54 -5.5; 60 -4.4; 66 -4.3; 72 -5.3; 79 -7.4; 87 -9.8; 96 -11.7; 106 -13.6; 116 -14.3; 128 -12.5; 141 -13.1; 155 -12.7; 170 -12.6; 187 -12.6; 206 -11.1; 227 -9.4; 249 -7.8; 274 -6.3; 302 -5.2; 332 -3.6; 365 -2.2; 402 -1.0; 442 -0.5; 486 -0.6; 535 -1.5; 588 -2.8; 647 -3.0; 712 -2.7; 783 -2.0; 861 -3.8; 947 -3.5; 1042 -3.4; 1146 -3.8; 1261 -4.2; 1387 -5.3; 1526 -6.2; 1678 -6.9; 1846 -7.8; 2031 -7.8; 2234 -8.6; 2457 -8.6; 2703 -8.5; 2973 -7.0; 3270 -7.0; 3597 -6.8; 3957 -7.6; 4353 -7.3; 4788 -4.6; 5267 -4.0; 5793 -4.5; 6373 -6.9; 7010 -5.1; 7711 -6.2; 8482 -8.2; 9330 -9.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.7; 20000 -15.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK KNS 8400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK KNS 8400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 2.02 | -4.9 dB |
| Peaking | 111 Hz  | 3.45 | -6.5 dB |
| Peaking | 176 Hz  | 1.71 | -6.6 dB |
| Peaking | 435 Hz  | 1.53 | 6.5 dB  |
| Peaking | 878 Hz  | 1.9  | 2.8 dB  |
| Peaking | 64 Hz   | 4.52 | 3.8 dB  |
| Peaking | 1881 Hz | 6.02 | -1.1 dB |
| Peaking | 2456 Hz | 2.71 | -2.5 dB |
| Peaking | 5258 Hz | 5.31 | 3.1 dB  |
| Peaking | 9010 Hz | 8.74 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -9.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 6.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KRK%20KNS%208400/KRK%20KNS%208400.png)