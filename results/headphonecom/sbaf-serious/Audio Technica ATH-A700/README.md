# Audio Technica ATH-A700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.3; 45 -2.4; 49 -3.4; 54 -4.4; 60 -5.0; 66 -4.2; 72 -5.1; 79 -6.7; 87 -7.1; 96 -7.0; 106 -7.2; 116 -7.4; 128 -7.4; 141 -7.3; 155 -7.2; 170 -6.6; 187 -6.4; 206 -5.9; 227 -5.3; 249 -5.4; 274 -4.6; 302 -3.8; 332 -3.8; 365 -5.8; 402 -8.1; 442 -9.2; 486 -9.5; 535 -9.2; 588 -8.6; 647 -8.3; 712 -9.0; 783 -7.3; 861 -8.2; 947 -8.5; 1042 -8.6; 1146 -8.1; 1261 -8.0; 1387 -8.7; 1526 -8.6; 1678 -7.6; 1846 -8.8; 2031 -9.1; 2234 -6.8; 2457 -4.3; 2703 -2.0; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -1.7; 4353 -7.9; 4788 -5.4; 5267 -1.6; 5793 -2.8; 6373 -4.3; 7010 -4.4; 7711 -11.4; 8482 -14.6; 9330 -13.3; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 28 Hz   |  1.11 | 6.9 dB   |
| Peaking | 2091 Hz |  0.37 | -3.4 dB  |
| Peaking | 3131 Hz |  2.05 | 9.6 dB   |
| Peaking | 6325 Hz |  1.84 | 6.2 dB   |
| Peaking | 8484 Hz |  3.23 | -10.7 dB |
| Peaking | 120 Hz  |  1.56 | -1.5 dB  |
| Peaking | 338 Hz  |  1.65 | 5.5 dB   |
| Peaking | 431 Hz  |  2.07 | -5.3 dB  |
| Peaking | 2594 Hz |  9.21 | 0.9 dB   |
| Peaking | 5336 Hz | 13.97 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A700/Audio%20Technica%20ATH-A700.png)