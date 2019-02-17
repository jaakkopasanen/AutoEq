# Bang & Olufsen Beoplay H6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.6; 25 -4.8; 28 -5.1; 31 -5.2; 34 -5.3; 37 -5.3; 41 -5.3; 45 -5.2; 49 -5.0; 54 -4.6; 60 -4.1; 66 -3.7; 72 -3.5; 79 -3.3; 87 -2.9; 96 -2.3; 106 -2.1; 116 -3.1; 128 -4.6; 141 -3.6; 155 -1.8; 170 -0.5; 187 -2.7; 206 -3.0; 227 -2.2; 249 -1.6; 274 -1.0; 302 -0.7; 332 -0.7; 365 -0.8; 402 -1.0; 442 -1.3; 486 -2.0; 535 -2.5; 588 -2.8; 647 -3.5; 712 -4.3; 783 -4.8; 861 -5.7; 947 -6.2; 1042 -6.6; 1146 -6.7; 1261 -6.8; 1387 -7.0; 1526 -7.2; 1678 -7.3; 1846 -6.9; 2031 -6.3; 2234 -4.8; 2457 -2.3; 2703 -2.0; 2973 -1.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.0; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.89 | 2.1 dB  |
| Peaking | 85 Hz   | 1.4  | 2.9 dB  |
| Peaking | 188 Hz  | 1.03 | 2.9 dB  |
| Peaking | 385 Hz  | 1.22 | 5.1 dB  |
| Peaking | 4282 Hz | 1.19 | 7.0 dB  |
| Peaking | 1858 Hz | 1.42 | -2.9 dB |
| Peaking | 2578 Hz | 2.06 | 3.5 dB  |
| Peaking | 6283 Hz | 2.71 | 6.5 dB  |
| Peaking | 6575 Hz | 1.08 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | 2.5 dB  |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 4.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bang%20&%20Olufsen%20Beoplay%20H6/Bang%20&%20Olufsen%20Beoplay%20H6.png)