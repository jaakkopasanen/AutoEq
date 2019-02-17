# Audio Technica ATH-M10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.9; 96 -1.6; 106 -3.0; 116 -3.7; 128 -4.4; 141 -4.9; 155 -5.2; 170 -5.1; 187 -5.8; 206 -6.0; 227 -6.3; 249 -6.5; 274 -6.7; 302 -7.0; 332 -7.1; 365 -7.0; 402 -7.1; 442 -6.8; 486 -7.1; 535 -7.2; 588 -6.9; 647 -7.0; 712 -7.5; 783 -7.8; 861 -8.5; 947 -8.7; 1042 -5.8; 1146 -5.1; 1261 -7.3; 1387 -7.2; 1526 -6.4; 1678 -4.7; 1846 -3.6; 2031 -3.1; 2234 -1.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -3.6; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.27 | 7.3 dB  |
| Peaking | 196 Hz  | 0.49 | -3.6 dB |
| Peaking | 873 Hz  | 4.3  | -2.8 dB |
| Peaking | 1415 Hz | 4.5  | -2.8 dB |
| Peaking | 3426 Hz | 0.75 | 6.8 dB  |
| Peaking | 81 Hz   | 6.08 | 1.0 dB  |
| Peaking | 3526 Hz | 5.22 | -0.9 dB |
| Peaking | 5725 Hz | 3.14 | 3.3 dB  |
| Peaking | 7915 Hz | 1.34 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M10/Audio%20Technica%20ATH-M10.png)