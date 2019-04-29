# Audio Technica ATH-LS200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.0; 25 -4.1; 28 -4.3; 31 -4.4; 34 -4.6; 37 -4.7; 41 -4.9; 45 -5.0; 49 -5.2; 54 -5.5; 60 -5.8; 66 -6.1; 72 -6.5; 79 -6.8; 87 -7.1; 96 -7.6; 106 -8.0; 116 -8.3; 128 -8.6; 141 -8.9; 155 -9.0; 170 -9.2; 187 -9.2; 206 -9.3; 227 -9.1; 249 -9.0; 274 -8.9; 302 -8.7; 332 -8.4; 365 -8.2; 402 -7.9; 442 -7.6; 486 -7.3; 535 -6.9; 588 -6.5; 647 -6.1; 712 -5.6; 783 -5.1; 861 -4.7; 947 -4.5; 1042 -4.7; 1146 -5.4; 1261 -6.1; 1387 -6.6; 1526 -6.6; 1678 -6.3; 1846 -6.0; 2031 -6.2; 2234 -6.7; 2457 -7.2; 2703 -6.6; 2973 -4.8; 3270 -3.4; 3597 -2.6; 3957 -2.6; 4353 -3.7; 4788 -4.9; 5267 -3.4; 5793 -0.5; 6373 -0.5; 7010 -3.5; 7711 -7.0; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -7.5; 16529 -7.6; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-LS200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-LS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.17 | 2.3 dB  |
| Peaking | 171 Hz   | 0.46 | -3.9 dB |
| Peaking | 871 Hz   | 2.54 | 2.2 dB  |
| Peaking | 3721 Hz  | 4.07 | 3.7 dB  |
| Peaking | 6077 Hz  | 4.62 | 6.3 dB  |
| Peaking | 1450 Hz  | 5.48 | -0.7 dB |
| Peaking | 2565 Hz  | 3.78 | -1.9 dB |
| Peaking | 3087 Hz  | 4.41 | 1.3 dB  |
| Peaking | 15934 Hz | 3.78 | -3.1 dB |
| Peaking | 17558 Hz | 2.05 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audio%20Technica%20ATH-LS200/Audio%20Technica%20ATH-LS200.png)