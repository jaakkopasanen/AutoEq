# Audio Technica ATH-M10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.7; 37 -2.9; 41 -4.2; 45 -5.4; 49 -6.2; 54 -6.5; 60 -6.7; 66 -6.4; 72 -5.0; 79 -5.3; 87 -8.2; 96 -6.8; 106 -8.6; 116 -9.5; 128 -10.0; 141 -10.4; 155 -10.5; 170 -10.2; 187 -10.6; 206 -10.5; 227 -10.7; 249 -10.7; 274 -10.7; 302 -10.5; 332 -10.4; 365 -10.2; 402 -10.0; 442 -10.2; 486 -10.1; 535 -10.3; 588 -10.4; 647 -10.7; 712 -10.9; 783 -11.2; 861 -11.6; 947 -11.9; 1042 -10.5; 1146 -7.6; 1261 -10.0; 1387 -10.0; 1526 -8.5; 1678 -7.3; 1846 -8.0; 2031 -7.0; 2234 -4.9; 2457 -3.1; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -3.9; 7010 -4.5; 7711 -7.2; 8482 -8.8; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.06 | 6.7 dB  |
| Peaking | 208 Hz  | 0.62 | -4.2 dB |
| Peaking | 834 Hz  | 1.08 | -4.5 dB |
| Peaking | 1745 Hz | 1.74 | -2.6 dB |
| Peaking | 3577 Hz | 0.98 | 7.5 dB  |
| Peaking | 76 Hz   | 8.13 | 2.2 dB  |
| Peaking | 2753 Hz | 4.79 | 2.4 dB  |
| Peaking | 3288 Hz | 1.53 | -1.4 dB |
| Peaking | 5659 Hz | 3.55 | 3.4 dB  |
| Peaking | 8450 Hz | 2.82 | -3.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -4.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-M10/Audio%20Technica%20ATH-M10.png)