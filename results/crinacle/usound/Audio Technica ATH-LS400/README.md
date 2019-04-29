# Audio Technica ATH-LS400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.8; 25 -7.0; 28 -7.2; 31 -7.4; 34 -7.5; 37 -7.6; 41 -7.8; 45 -7.9; 49 -8.1; 54 -8.3; 60 -8.5; 66 -8.8; 72 -9.1; 79 -9.5; 87 -9.8; 96 -10.2; 106 -10.5; 116 -10.9; 128 -11.1; 141 -11.4; 155 -11.6; 170 -11.6; 187 -11.6; 206 -11.6; 227 -11.5; 249 -11.4; 274 -11.1; 302 -10.9; 332 -10.6; 365 -10.3; 402 -9.9; 442 -9.5; 486 -9.0; 535 -8.5; 588 -7.9; 647 -7.4; 712 -6.7; 783 -6.0; 861 -5.4; 947 -5.1; 1042 -5.0; 1146 -5.4; 1261 -5.7; 1387 -5.5; 1526 -4.9; 1678 -4.2; 1846 -4.0; 2031 -4.8; 2234 -6.1; 2457 -6.1; 2703 -4.8; 2973 -3.2; 3270 -2.4; 3597 -4.7; 3957 -5.2; 4353 -3.4; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -5.3; 7711 -10.9; 8482 -6.9; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.4; 16529 -12.2; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-LS400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-LS400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 232 Hz   | 0.36 | -5.9 dB |
| Peaking | 1031 Hz  | 0.38 | 2.9 dB  |
| Peaking | 5184 Hz  | 2.57 | 5.1 dB  |
| Peaking | 6486 Hz  | 3.75 | 4.5 dB  |
| Peaking | 7630 Hz  | 5.17 | -6.9 dB |
| Peaking | 2423 Hz  | 4.72 | -2.5 dB |
| Peaking | 3318 Hz  | 2.44 | 3.7 dB  |
| Peaking | 3779 Hz  | 4.38 | -3.6 dB |
| Peaking | 14116 Hz | 3.18 | 1.7 dB  |
| Peaking | 15963 Hz | 2.66 | -7.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audio%20Technica%20ATH-LS400/Audio%20Technica%20ATH-LS400.png)