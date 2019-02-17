# Audio Technica ATH-AD900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.0; 79 -1.2; 87 -1.3; 96 -2.2; 106 -2.8; 116 -3.3; 128 -4.1; 141 -4.7; 155 -5.2; 170 -5.3; 187 -5.2; 206 -5.0; 227 -5.1; 249 -5.4; 274 -5.4; 302 -5.5; 332 -5.5; 365 -5.6; 402 -5.6; 442 -5.5; 486 -5.7; 535 -5.7; 588 -5.6; 647 -5.7; 712 -5.8; 783 -5.6; 861 -6.0; 947 -6.3; 1042 -6.6; 1146 -6.9; 1261 -7.5; 1387 -8.4; 1526 -9.3; 1678 -9.3; 1846 -7.6; 2031 -6.2; 2234 -5.2; 2457 -4.3; 2703 -4.8; 2973 -5.3; 3270 -4.6; 3597 -6.9; 3957 -10.2; 4353 -11.8; 4788 -10.4; 5267 -7.2; 5793 -5.8; 6373 -4.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.39 | 6.5 dB  |
| Peaking | 1599 Hz | 1.51 | -7.8 dB |
| Peaking | 2060 Hz | 0.63 | 5.5 dB  |
| Peaking | 4340 Hz | 3.17 | -7.7 dB |
| Peaking | 6655 Hz | 6.05 | 3.0 dB  |
| Peaking | 33 Hz   | 0.19 | 1.8 dB  |
| Peaking | 39 Hz   | 0.9  | -2.4 dB |
| Peaking | 148 Hz  | 1.75 | -1.8 dB |
| Peaking | 8638 Hz | 3.24 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD900/Audio%20Technica%20ATH-AD900.png)