# Blue Lola
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.9; 25 -7.1; 28 -7.2; 31 -7.4; 34 -7.4; 37 -7.6; 41 -7.7; 45 -7.8; 49 -7.9; 54 -8.0; 60 -8.2; 66 -8.3; 72 -8.4; 79 -8.6; 87 -8.9; 96 -9.3; 106 -9.1; 116 -8.9; 128 -9.1; 141 -9.5; 155 -9.9; 170 -8.8; 187 -9.1; 206 -8.8; 227 -8.1; 249 -7.3; 274 -6.4; 302 -5.8; 332 -5.6; 365 -5.6; 402 -5.9; 442 -5.5; 486 -4.8; 535 -3.6; 588 -4.4; 647 -4.9; 712 -5.4; 783 -5.4; 861 -5.7; 947 -6.3; 1042 -6.5; 1146 -6.7; 1261 -6.9; 1387 -7.0; 1526 -7.4; 1678 -7.6; 1846 -7.0; 2031 -6.2; 2234 -5.7; 2457 -4.6; 2703 -4.1; 2973 -3.5; 3270 -3.0; 3597 -0.6; 3957 -0.5; 4353 -4.2; 4788 -4.6; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue Lola GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue Lola ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 82 Hz   | 0.71 | -2.1 dB |
| Peaking | 162 Hz  | 1.77 | -2.2 dB |
| Peaking | 536 Hz  | 2.02 | 2.6 dB  |
| Peaking | 3630 Hz | 3.08 | 5.6 dB  |
| Peaking | 5906 Hz | 3.69 | 6.3 dB  |
| Peaking | 309 Hz  | 5.57 | 1.2 dB  |
| Peaking | 1649 Hz | 2.24 | -1.6 dB |
| Peaking | 2640 Hz | 2.59 | 1.5 dB  |
| Peaking | 3293 Hz | 7.26 | -1.1 dB |
| Peaking | 8292 Hz | 4.65 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20Lola/Blue%20Lola.png)