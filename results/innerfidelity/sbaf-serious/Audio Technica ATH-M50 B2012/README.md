# Audio Technica ATH-M50 B2012
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.2; 25 -6.4; 28 -6.8; 31 -7.0; 34 -7.2; 37 -7.3; 41 -7.4; 45 -7.4; 49 -7.3; 54 -7.3; 60 -7.2; 66 -7.0; 72 -6.4; 79 -6.2; 87 -4.6; 96 -3.1; 106 -5.9; 116 -7.4; 128 -8.1; 141 -8.2; 155 -7.4; 170 -7.0; 187 -7.1; 206 -6.3; 227 -5.4; 249 -4.6; 274 -4.0; 302 -3.7; 332 -4.9; 365 -5.5; 402 -5.9; 442 -6.3; 486 -6.9; 535 -7.1; 588 -6.9; 647 -6.9; 712 -7.0; 783 -6.8; 861 -6.8; 947 -6.6; 1042 -6.4; 1146 -6.4; 1261 -6.8; 1387 -7.2; 1526 -8.1; 1678 -9.5; 1846 -10.2; 2031 -9.9; 2234 -9.3; 2457 -8.0; 2703 -6.7; 2973 -4.9; 3270 -3.5; 3597 -3.0; 3957 -6.0; 4353 -8.9; 4788 -6.0; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.1; 7711 -9.3; 8482 -13.1; 9330 -11.2; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50 B2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 289 Hz  | 3.84 | 3.0 dB  |
| Peaking | 1940 Hz | 2.33 | -4.1 dB |
| Peaking | 3361 Hz | 5.86 | 4.1 dB  |
| Peaking | 6034 Hz | 3.34 | 7.6 dB  |
| Peaking | 8566 Hz | 4.14 | -8.3 dB |
| Peaking | 15 Hz   | 1.23 | 1.6 dB  |
| Peaking | 43 Hz   | 1.02 | -1.1 dB |
| Peaking | 95 Hz   | 5.41 | 4.3 dB  |
| Peaking | 131 Hz  | 2.79 | -2.1 dB |
| Peaking | 4357 Hz | 9.93 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M50%20B2012/Audio%20Technica%20ATH-M50%20B2012.png)