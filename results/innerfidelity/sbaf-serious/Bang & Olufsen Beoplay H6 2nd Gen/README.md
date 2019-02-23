# Bang & Olufsen Beoplay H6 2nd Gen
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.5; 25 -6.2; 28 -7.1; 31 -7.9; 34 -8.5; 37 -9.0; 41 -9.5; 45 -9.8; 49 -10.1; 54 -10.3; 60 -10.4; 66 -10.3; 72 -10.2; 79 -10.0; 87 -9.8; 96 -9.2; 106 -8.3; 116 -8.2; 128 -9.2; 141 -9.3; 155 -6.9; 170 -4.3; 187 -4.8; 206 -4.1; 227 -2.8; 249 -3.1; 274 -4.1; 302 -5.1; 332 -5.9; 365 -6.5; 402 -7.0; 442 -7.3; 486 -7.9; 535 -8.2; 588 -8.2; 647 -8.5; 712 -8.9; 783 -9.1; 861 -9.5; 947 -9.6; 1042 -9.8; 1146 -9.6; 1261 -9.5; 1387 -9.8; 1526 -10.0; 1678 -10.2; 1846 -10.0; 2031 -9.4; 2234 -8.4; 2457 -6.7; 2703 -5.0; 2973 -2.5; 3270 -1.1; 3597 -1.4; 3957 -0.9; 4353 -2.8; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -2.2; 7010 -5.2; 7711 -7.8; 8482 -10.5; 9330 -12.0; 10263 -9.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bang & Olufsen Beoplay H6 2nd Gen GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang & Olufsen Beoplay H6 2nd Gen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 70 Hz    | 0.66 | -4.0 dB |
| Peaking | 230 Hz   | 1.85 | 4.9 dB  |
| Peaking | 3255 Hz  | 0.31 | -7.6 dB |
| Peaking | 3421 Hz  | 1.34 | 12.4 dB |
| Peaking | 5695 Hz  | 2.52 | 9.4 dB  |
| Peaking | 20 Hz    | 2.99 | 2.8 dB  |
| Peaking | 140 Hz   | 5.2  | -4.7 dB |
| Peaking | 143 Hz   | 2.49 | 2.6 dB  |
| Peaking | 9296 Hz  | 3.13 | -6.8 dB |
| Peaking | 10613 Hz | 1.13 | 3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen/Bang%20&%20Olufsen%20Beoplay%20H6%202nd%20Gen.png)