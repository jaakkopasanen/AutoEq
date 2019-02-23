# Bang & Olufsen Beoplay E8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.1; 25 -2.3; 28 -2.7; 31 -3.1; 34 -3.3; 37 -3.4; 41 -3.3; 45 -3.2; 49 -3.0; 54 -2.7; 60 -2.6; 66 -2.5; 72 -2.3; 79 -2.1; 87 -2.1; 96 -2.3; 106 -2.6; 116 -3.1; 128 -3.7; 141 -4.4; 155 -5.1; 170 -5.9; 187 -6.6; 206 -7.4; 227 -7.9; 249 -8.3; 274 -8.5; 302 -8.6; 332 -8.5; 365 -8.3; 402 -8.0; 442 -7.5; 486 -7.0; 535 -6.4; 588 -5.6; 647 -4.8; 712 -3.9; 783 -3.3; 861 -3.4; 947 -4.1; 1042 -5.0; 1146 -5.8; 1261 -6.3; 1387 -6.5; 1526 -6.5; 1678 -6.4; 1846 -5.7; 2031 -3.7; 2234 -1.2; 2457 -0.5; 2703 -0.9; 2973 -1.7; 3270 -2.3; 3597 -2.1; 3957 -1.8; 4353 -2.5; 4788 -3.2; 5267 -4.4; 5793 -6.7; 6373 -11.4; 7010 -15.0; 7711 -12.5; 8482 -9.6; 9330 -11.2; 10263 -13.9; 11289 -11.4; 12418 -6.2; 13660 -5.8; 15026 -5.8; 16529 -7.7; 18182 -11.7; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay E8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay E8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.9  | 3.9 dB   |
| Peaking | 4498 Hz  | 0.79 | 9.5 dB   |
| Peaking | 7128 Hz  | 1.02 | -12.8 dB |
| Peaking | 18364 Hz | 2.14 | -6.4 dB  |
| Peaking | 20885 Hz | 1.82 | -3.3 dB  |
| Peaking | 21 Hz    | 2.54 | 3.0 dB   |
| Peaking | 324 Hz   | 0.67 | -8.9 dB  |
| Peaking | 475 Hz   | 0.27 | 5.9 dB   |
| Peaking | 1449 Hz  | 1.78 | -5.1 dB  |
| Peaking | 10503 Hz | 7.64 | -5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.9 dB  |
| Peaking | 125 Hz   | 1.41 | 2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.9 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20E8/Bang%20&%20Olufsen%20Beoplay%20E8.png)