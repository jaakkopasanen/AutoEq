# Bang & Olufsen Beoplay H6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.5; 25 -8.7; 28 -9.0; 31 -9.1; 34 -9.2; 37 -9.2; 41 -9.2; 45 -9.1; 49 -8.9; 54 -8.5; 60 -8.0; 66 -7.6; 72 -7.4; 79 -7.2; 87 -6.8; 96 -6.2; 106 -6.0; 116 -7.0; 128 -8.5; 141 -7.5; 155 -5.7; 170 -3.9; 187 -6.6; 206 -6.9; 227 -6.1; 249 -5.5; 274 -4.9; 302 -4.6; 332 -4.6; 365 -4.7; 402 -4.9; 442 -5.2; 486 -5.9; 535 -6.4; 588 -6.7; 647 -7.4; 712 -8.2; 783 -8.7; 861 -9.6; 947 -10.1; 1042 -10.5; 1146 -10.6; 1261 -10.7; 1387 -10.9; 1526 -11.1; 1678 -11.2; 1846 -10.8; 2031 -10.2; 2234 -8.7; 2457 -6.2; 2703 -5.9; 2973 -5.6; 3270 -4.0; 3597 -2.6; 3957 -1.0; 4353 -2.7; 4788 -1.7; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -4.0; 7711 -7.1; 8482 -10.8; 9330 -11.2; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 1.13 | -3.1 dB |
| Peaking | 1479 Hz | 1.11 | -5.4 dB |
| Peaking | 3734 Hz | 2.1  | 4.0 dB  |
| Peaking | 5858 Hz | 1.85 | 6.4 dB  |
| Peaking | 8800 Hz | 3.34 | -6.9 dB |
| Peaking | 102 Hz  | 3.12 | 2.5 dB  |
| Peaking | 155 Hz  | 1.15 | -4.2 dB |
| Peaking | 165 Hz  | 5.06 | 5.7 dB  |
| Peaking | 311 Hz  | 1.03 | 3.2 dB  |
| Peaking | 864 Hz  | 2.83 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.1 dB |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bang%20&%20Olufsen%20Beoplay%20H6/Bang%20&%20Olufsen%20Beoplay%20H6.png)