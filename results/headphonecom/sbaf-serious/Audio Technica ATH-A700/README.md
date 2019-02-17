# Audio Technica ATH-A700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.3; 54 -2.3; 60 -2.9; 66 -2.1; 72 -3.0; 79 -4.6; 87 -5.0; 96 -4.9; 106 -5.1; 116 -5.3; 128 -5.3; 141 -5.2; 155 -5.0; 170 -4.5; 187 -4.3; 206 -3.8; 227 -3.1; 249 -3.3; 274 -2.5; 302 -1.7; 332 -1.6; 365 -3.7; 402 -6.0; 442 -7.1; 486 -7.4; 535 -7.1; 588 -6.5; 647 -6.2; 712 -6.9; 783 -5.2; 861 -6.1; 947 -6.4; 1042 -6.4; 1146 -6.0; 1261 -5.9; 1387 -6.6; 1526 -6.5; 1678 -5.5; 1846 -6.7; 2031 -7.0; 2234 -4.6; 2457 -2.2; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -5.8; 4788 -3.3; 5267 -0.5; 5793 -0.9; 6373 -2.4; 7010 -4.0; 7711 -9.3; 8482 -12.5; 9330 -11.2; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -8.5
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

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.57 | 6.4 dB  |
| Peaking | 288 Hz  | 2.3  | 4.7 dB  |
| Peaking | 3098 Hz | 2.27 | 6.4 dB  |
| Peaking | 5967 Hz | 2.08 | 5.9 dB  |
| Peaking | 8524 Hz | 3.58 | -8.3 dB |
| Peaking | 348 Hz  | 5.76 | 2.8 dB  |
| Peaking | 384 Hz  | 0.62 | 1.2 dB  |
| Peaking | 418 Hz  | 1.45 | -3.2 dB |
| Peaking | 1987 Hz | 6.45 | -2.4 dB |
| Peaking | 2550 Hz | 8.3  | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | 4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A700/Audio%20Technica%20ATH-A700.png)