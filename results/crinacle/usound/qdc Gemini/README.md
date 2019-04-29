# qdc Gemini
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.1; 25 -6.2; 28 -6.3; 31 -6.4; 34 -6.5; 37 -6.5; 41 -6.6; 45 -6.7; 49 -6.8; 54 -6.9; 60 -7.0; 66 -7.2; 72 -7.4; 79 -7.6; 87 -7.7; 96 -8.0; 106 -8.2; 116 -8.2; 128 -8.3; 141 -8.3; 155 -8.3; 170 -8.2; 187 -8.0; 206 -7.8; 227 -7.5; 249 -7.3; 274 -7.0; 302 -6.7; 332 -6.5; 365 -6.2; 402 -6.0; 442 -5.9; 486 -5.9; 535 -5.8; 588 -5.9; 647 -6.0; 712 -6.0; 783 -6.2; 861 -6.3; 947 -6.7; 1042 -7.2; 1146 -8.0; 1261 -8.7; 1387 -8.9; 1526 -8.6; 1678 -7.9; 1846 -7.2; 2031 -6.7; 2234 -6.4; 2457 -5.9; 2703 -5.1; 2973 -4.2; 3270 -4.2; 3597 -4.5; 3957 -4.9; 4353 -6.1; 4788 -4.3; 5267 -0.5; 5793 -0.9; 6373 -4.6; 7010 -5.5; 7711 -8.5; 8482 -8.6; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -8.0; 15026 -9.3; 16529 -8.5; 18182 -10.5; 20000 -15.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Gemini GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Gemini ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 130 Hz   | 1.04 | -2.1 dB |
| Peaking | 1404 Hz  | 2.73 | -2.8 dB |
| Peaking | 3140 Hz  | 3.1  | 2.5 dB  |
| Peaking | 5501 Hz  | 5.13 | 6.8 dB  |
| Peaking | 20401 Hz | 0.52 | -9.0 dB |
| Peaking | 18 Hz    | 1.64 | 0.4 dB  |
| Peaking | 529 Hz   | 1.68 | 0.9 dB  |
| Peaking | 8104 Hz  | 4.46 | -4.5 dB |
| Peaking | 8291 Hz  | 1.59 | 1.5 dB  |
| Peaking | 19305 Hz | 3.26 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -3.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/qdc%20Gemini/qdc%20Gemini.png)