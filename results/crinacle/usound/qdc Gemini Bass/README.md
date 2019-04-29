# qdc Gemini Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.0; 25 -9.1; 28 -9.2; 31 -9.3; 34 -9.3; 37 -9.4; 41 -9.5; 45 -9.5; 49 -9.6; 54 -9.6; 60 -9.7; 66 -9.8; 72 -10.0; 79 -10.1; 87 -10.2; 96 -10.4; 106 -10.5; 116 -10.5; 128 -10.5; 141 -10.4; 155 -10.3; 170 -10.1; 187 -9.8; 206 -9.5; 227 -9.1; 249 -8.7; 274 -8.3; 302 -7.8; 332 -7.4; 365 -7.0; 402 -6.7; 442 -6.4; 486 -6.1; 535 -5.9; 588 -5.8; 647 -5.8; 712 -5.7; 783 -5.7; 861 -5.9; 947 -6.1; 1042 -6.6; 1146 -7.4; 1261 -8.0; 1387 -8.2; 1526 -7.8; 1678 -7.2; 1846 -6.4; 2031 -5.9; 2234 -5.5; 2457 -5.0; 2703 -4.2; 2973 -3.2; 3270 -3.4; 3597 -3.9; 3957 -4.1; 4353 -5.3; 4788 -3.5; 5267 -0.5; 5793 -0.7; 6373 -3.8; 7010 -4.9; 7711 -7.7; 8482 -7.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.3; 15026 -8.4; 16529 -7.7; 18182 -9.7; 20000 -14.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Gemini Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Gemini Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.45 | -2.7 dB |
| Peaking | 116 Hz   | 1.1  | -2.7 dB |
| Peaking | 198 Hz   | 1.8  | -1.8 dB |
| Peaking | 3110 Hz  | 2.91 | 3.4 dB  |
| Peaking | 5495 Hz  | 4.11 | 6.5 dB  |
| Peaking | 733 Hz   | 1.28 | 1.2 dB  |
| Peaking | 1375 Hz  | 2.19 | -2.3 dB |
| Peaking | 2140 Hz  | 2.11 | 0.6 dB  |
| Peaking | 20200 Hz | 0.73 | -7.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Gemini%20Bass/qdc%20Gemini%20Bass.png)