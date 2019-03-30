# Audio-Technica ATH-ES55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.9; 206 -1.1; 227 -1.4; 249 -1.5; 274 -1.8; 302 -1.9; 332 -1.7; 365 -1.5; 402 -1.5; 442 -1.3; 486 -1.2; 535 -1.2; 588 -1.7; 647 -3.2; 712 -5.5; 783 -7.7; 861 -9.7; 947 -11.0; 1042 -11.6; 1146 -12.0; 1261 -12.3; 1387 -12.7; 1526 -13.2; 1678 -13.6; 1846 -13.9; 2031 -14.1; 2234 -13.7; 2457 -12.9; 2703 -11.8; 2973 -10.6; 3270 -9.6; 3597 -8.8; 3957 -7.7; 4353 -7.0; 4788 -7.8; 5267 -9.2; 5793 -9.4; 6373 -7.8; 7010 -6.5; 7711 -8.6; 8482 -11.7; 9330 -13.0; 10263 -11.9; 11289 -9.0; 12418 -6.6; 13660 -6.7; 15026 -7.7; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ES55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ES55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 58 Hz    | 0.09 | 6.1 dB  |
| Peaking | 587 Hz   | 1.34 | 7.0 dB  |
| Peaking | 935 Hz   | 0.76 | -8.0 dB |
| Peaking | 2091 Hz  | 1.37 | -5.7 dB |
| Peaking | 9465 Hz  | 2.79 | -6.9 dB |
| Peaking | 4353 Hz  | 4.62 | 1.8 dB  |
| Peaking | 5736 Hz  | 2.87 | -3.0 dB |
| Peaking | 6919 Hz  | 3.18 | 2.9 dB  |
| Peaking | 8283 Hz  | 6.62 | -1.4 dB |
| Peaking | 15439 Hz | 6.34 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 4.9 dB  |
| Peaking | 250 Hz   | 1.41 | 3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 6.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.8 dB |
| Peaking | 2000 Hz  | 1.41 | -7.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-ES55/Audio-Technica%20ATH-ES55.png)