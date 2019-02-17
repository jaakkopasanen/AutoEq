# Audio Technica ATH-M10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.4; 54 -1.6; 60 -1.8; 66 -1.5; 72 -0.5; 79 -0.7; 87 -3.3; 96 -1.9; 106 -3.7; 116 -4.6; 128 -5.1; 141 -5.5; 155 -5.6; 170 -5.4; 187 -5.7; 206 -5.6; 227 -5.8; 249 -5.8; 274 -5.8; 302 -5.7; 332 -5.5; 365 -5.3; 402 -5.2; 442 -5.3; 486 -5.3; 535 -5.5; 588 -5.5; 647 -5.8; 712 -6.1; 783 -6.3; 861 -6.7; 947 -7.0; 1042 -5.6; 1146 -2.7; 1261 -5.1; 1387 -5.1; 1526 -3.7; 1678 -2.4; 1846 -3.1; 2031 -2.2; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 28 Hz   |  0.5  | 6.2 dB  |
| Peaking | 76 Hz   |  2.35 | 3.0 dB  |
| Peaking | 411 Hz  |  2.16 | 1.1 dB  |
| Peaking | 2790 Hz |  0.94 | 6.1 dB  |
| Peaking | 5431 Hz |  2.3  | 4.6 dB  |
| Peaking | 972 Hz  |  3.52 | -1.9 dB |
| Peaking | 1112 Hz | 10.56 | 3.9 dB  |
| Peaking | 4247 Hz |  3.64 | 1.3 dB  |
| Peaking | 6401 Hz |  4.3  | 4.2 dB  |
| Peaking | 6929 Hz |  1.43 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-M10/Audio%20Technica%20ATH-M10.png)