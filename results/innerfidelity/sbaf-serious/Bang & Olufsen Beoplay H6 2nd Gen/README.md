# Bang & Olufsen Beoplay H6 2nd Gen
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.3; 25 -3.0; 28 -3.9; 31 -4.7; 34 -5.3; 37 -5.8; 41 -6.3; 45 -6.6; 49 -6.9; 54 -7.1; 60 -7.1; 66 -7.1; 72 -6.9; 79 -6.8; 87 -6.6; 96 -6.0; 106 -5.1; 116 -5.0; 128 -6.0; 141 -6.1; 155 -3.7; 170 -1.1; 187 -1.6; 206 -0.8; 227 -0.5; 249 -0.5; 274 -0.8; 302 -1.8; 332 -2.7; 365 -3.3; 402 -3.7; 442 -4.1; 486 -4.7; 535 -5.0; 588 -4.9; 647 -5.2; 712 -5.7; 783 -5.9; 861 -6.3; 947 -6.4; 1042 -6.5; 1146 -6.4; 1261 -6.3; 1387 -6.6; 1526 -6.8; 1678 -7.0; 1846 -6.7; 2031 -6.1; 2234 -5.2; 2457 -3.5; 2703 -1.8; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.3; 9330 -8.8; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H6 2nd Gen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H6 2nd Gen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 2.43 | 5.4 dB  |
| Peaking | 176 Hz  | 4.66 | 2.7 dB  |
| Peaking | 259 Hz  | 1.43 | 5.9 dB  |
| Peaking | 4557 Hz | 0.94 | 7.1 dB  |
| Peaking | 8981 Hz | 2.77 | -4.1 dB |
| Peaking | 56 Hz   | 2.8  | -0.9 dB |
| Peaking | 71 Hz   | 3.16 | -0.7 dB |
| Peaking | 1852 Hz | 1.61 | -2.0 dB |
| Peaking | 2865 Hz | 3.92 | 2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 6.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen.png)