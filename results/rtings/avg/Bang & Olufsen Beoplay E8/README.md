# Bang & Olufsen Beoplay E8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.1; 25 -6.3; 28 -6.7; 31 -7.0; 34 -7.2; 37 -7.4; 41 -7.3; 45 -7.2; 49 -7.0; 54 -6.6; 60 -6.2; 66 -5.8; 72 -5.4; 79 -5.0; 87 -4.7; 96 -4.5; 106 -4.4; 116 -4.4; 128 -4.6; 141 -4.8; 155 -5.2; 170 -5.6; 187 -6.0; 206 -6.6; 227 -7.0; 249 -7.3; 274 -7.6; 302 -7.7; 332 -7.6; 365 -7.4; 402 -7.1; 442 -6.6; 486 -6.2; 535 -5.5; 588 -4.8; 647 -4.0; 712 -3.2; 783 -2.6; 861 -2.6; 947 -3.3; 1042 -4.2; 1146 -5.1; 1261 -5.6; 1387 -5.8; 1526 -5.8; 1678 -5.7; 1846 -5.1; 2031 -3.2; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.9; 3270 -1.2; 3597 -0.9; 3957 -0.6; 4353 -1.2; 4788 -2.7; 5267 -3.9; 5793 -5.7; 6373 -9.6; 7010 -14.1; 7711 -12.2; 8482 -8.1; 9330 -8.8; 10263 -12.6; 11289 -11.3; 12418 -5.6; 13660 -5.1; 15026 -5.1; 16529 -6.9; 18182 -10.6; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay E8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay E8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 2508 Hz  | 3.63 | 3.8 dB   |
| Peaking | 3990 Hz  | 1.54 | 4.8 dB   |
| Peaking | 7110 Hz  | 3.71 | -10.1 dB |
| Peaking | 10603 Hz | 4.31 | -8.1 dB  |
| Peaking | 18316 Hz | 2.11 | -6.2 dB  |
| Peaking | 38 Hz    | 1.81 | -2.6 dB  |
| Peaking | 320 Hz   | 1.43 | -2.9 dB  |
| Peaking | 807 Hz   | 2.38 | 3.1 dB   |
| Peaking | 1477 Hz  | 2.52 | -1.7 dB  |
| Peaking | 13735 Hz | 2.91 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20E8/Bang%20&%20Olufsen%20Beoplay%20E8.png)