# Bang & Olufsen Beoplay H6 2nd Gen
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.6; 23 -8.8; 25 -8.9; 28 -9.1; 31 -9.2; 34 -9.3; 37 -9.2; 41 -9.1; 45 -8.8; 49 -8.5; 54 -8.1; 60 -7.8; 66 -7.8; 72 -7.8; 79 -7.9; 87 -8.1; 96 -8.1; 106 -8.1; 116 -8.0; 128 -7.7; 141 -7.1; 155 -6.2; 170 -4.9; 187 -3.4; 206 -1.9; 227 -1.0; 249 -0.6; 274 -1.1; 302 -2.2; 332 -3.3; 365 -4.4; 402 -5.1; 442 -5.5; 486 -5.9; 535 -6.1; 588 -6.2; 647 -6.4; 712 -6.5; 783 -6.5; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.3; 1387 -6.4; 1526 -6.6; 1678 -7.2; 1846 -8.0; 2031 -8.5; 2234 -8.0; 2457 -6.6; 2703 -5.2; 2973 -3.6; 3270 -2.9; 3597 -3.0; 3957 -1.2; 4353 -1.0; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.9; 7010 -5.4; 7711 -9.0; 8482 -11.3; 9330 -9.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.9; 18182 -10.2; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H6 2nd Gen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H6 2nd Gen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.07 | -2.4 dB |
| Peaking | 251 Hz   | 1.35 | 8.2 dB  |
| Peaking | 5212 Hz  | 1.29 | 7.2 dB  |
| Peaking | 8394 Hz  | 3.19 | -7.4 dB |
| Peaking | 18377 Hz | 1.61 | -4.1 dB |
| Peaking | 65 Hz    | 3.04 | 0.9 dB  |
| Peaking | 123 Hz   | 3.34 | -0.8 dB |
| Peaking | 2101 Hz  | 3.36 | -3.0 dB |
| Peaking | 3143 Hz  | 3.14 | 1.5 dB  |
| Peaking | 14925 Hz | 2.58 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 6.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen.png)