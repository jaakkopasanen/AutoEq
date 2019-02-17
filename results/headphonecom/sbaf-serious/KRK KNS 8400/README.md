# KRK KNS 8400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -10.9; 25 -10.8; 28 -10.5; 31 -10.1; 34 -9.7; 37 -9.2; 41 -8.5; 45 -7.7; 49 -6.9; 54 -5.7; 60 -4.7; 66 -4.5; 72 -5.5; 79 -7.6; 87 -10.0; 96 -11.9; 106 -13.8; 116 -14.5; 128 -12.7; 141 -13.3; 155 -12.9; 170 -12.8; 187 -12.9; 206 -11.3; 227 -9.6; 249 -8.0; 274 -6.5; 302 -5.4; 332 -3.8; 365 -2.4; 402 -1.2; 442 -0.5; 486 -0.7; 535 -1.7; 588 -3.0; 647 -3.2; 712 -2.9; 783 -2.2; 861 -4.0; 947 -3.7; 1042 -3.6; 1146 -4.0; 1261 -4.5; 1387 -5.5; 1526 -6.4; 1678 -7.2; 1846 -8.0; 2031 -8.0; 2234 -8.8; 2457 -8.8; 2703 -8.8; 2973 -7.2; 3270 -7.2; 3597 -7.0; 3957 -7.8; 4353 -7.5; 4788 -4.8; 5267 -4.2; 5793 -4.7; 6373 -7.1; 7010 -5.0; 7711 -4.1; 8482 -8.4; 9330 -9.5; 10263 -3.7; 11289 -3.4; 12418 -3.4; 13660 -4.5; 15026 -5.0; 16529 -5.7; 18182 -8.9; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`KRK KNS 8400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `KRK KNS 8400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 1.14 | -7.9 dB  |
| Peaking | 113 Hz   | 2.15 | -9.7 dB  |
| Peaking | 183 Hz   | 2.33 | -8.1 dB  |
| Peaking | 2590 Hz  | 1.04 | -5.5 dB  |
| Peaking | 9004 Hz  | 5.73 | -6.9 dB  |
| Peaking | 15 Hz    | 2.17 | -0.6 dB  |
| Peaking | 453 Hz   | 2.75 | 4.0 dB   |
| Peaking | 3063 Hz  | 6.72 | 1.4 dB   |
| Peaking | 4151 Hz  | 8.52 | -2.2 dB  |
| Peaking | 19810 Hz | 1.02 | -11.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB   |
| Peaking | 125 Hz   | 1.41 | -11.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/KRK%20KNS%208400/KRK%20KNS%208400.png)