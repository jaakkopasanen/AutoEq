# Audio Technica ATH-IM02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.2; 25 -3.4; 28 -3.7; 31 -3.9; 34 -4.2; 37 -4.4; 41 -4.7; 45 -4.9; 49 -5.1; 54 -5.4; 60 -5.8; 66 -6.1; 72 -6.5; 79 -6.9; 87 -7.4; 96 -7.9; 106 -8.3; 116 -8.7; 128 -9.1; 141 -9.4; 155 -9.7; 170 -9.9; 187 -10.1; 206 -10.2; 227 -10.2; 249 -10.1; 274 -10.1; 302 -10.0; 332 -9.8; 365 -9.6; 402 -9.4; 442 -9.2; 486 -8.9; 535 -8.5; 588 -8.1; 647 -7.7; 712 -7.1; 783 -6.6; 861 -6.1; 947 -5.8; 1042 -5.9; 1146 -6.4; 1261 -7.1; 1387 -7.5; 1526 -7.5; 1678 -7.3; 1846 -7.3; 2031 -7.7; 2234 -8.1; 2457 -6.9; 2703 -3.7; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -1.1; 5267 -2.8; 5793 -7.8; 6373 -7.8; 7010 -6.1; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.9; 13660 -12.5; 15026 -12.9; 16529 -13.2; 18182 -13.0; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-IM02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-IM02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.31 | 3.7 dB  |
| Peaking | 216 Hz   | 0.55 | -4.0 dB |
| Peaking | 2248 Hz  | 2.07 | -5.0 dB |
| Peaking | 3408 Hz  | 1.26 | 8.2 dB  |
| Peaking | 17327 Hz | 0.59 | -7.6 dB |
| Peaking | 917 Hz   | 4.62 | 1.4 dB  |
| Peaking | 4972 Hz  | 5.36 | 2.7 dB  |
| Peaking | 5956 Hz  | 6.09 | -4.6 dB |
| Peaking | 11362 Hz | 2.09 | 3.3 dB  |
| Peaking | 13213 Hz | 2.52 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -9.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audio%20Technica%20ATH-IM02/Audio%20Technica%20ATH-IM02.png)