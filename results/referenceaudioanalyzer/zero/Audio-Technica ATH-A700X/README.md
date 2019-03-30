# Audio-Technica ATH-A700X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.5; 25 -7.2; 28 -8.0; 31 -8.7; 34 -9.2; 37 -9.7; 41 -10.1; 45 -10.4; 49 -10.5; 54 -10.5; 60 -10.5; 66 -10.5; 72 -10.5; 79 -10.5; 87 -10.5; 96 -10.5; 106 -10.3; 116 -10.1; 128 -9.9; 141 -9.6; 155 -9.1; 170 -8.5; 187 -7.7; 206 -6.7; 227 -5.2; 249 -3.9; 274 -3.4; 302 -3.8; 332 -4.6; 365 -5.4; 402 -5.9; 442 -6.2; 486 -6.3; 535 -6.6; 588 -6.6; 647 -6.6; 712 -6.6; 783 -6.3; 861 -6.1; 947 -6.4; 1042 -6.6; 1146 -6.9; 1261 -7.0; 1387 -7.3; 1526 -7.3; 1678 -7.3; 1846 -7.3; 2031 -6.6; 2234 -4.6; 2457 -1.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.1; 3957 -6.6; 4353 -8.4; 4788 -8.7; 5267 -11.2; 5793 -14.0; 6373 -13.3; 7010 -8.2; 7711 -6.2; 8482 -6.5; 9330 -8.5; 10263 -8.7; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-A700X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-A700X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 106 Hz   | 0.31 | -4.6 dB |
| Peaking | 271 Hz   | 1.42 | 6.1 dB  |
| Peaking | 2991 Hz  | 2.71 | 7.6 dB  |
| Peaking | 5819 Hz  | 3.11 | -8.4 dB |
| Peaking | 22 Hz    | 2.49 | 2.2 dB  |
| Peaking | 1690 Hz  | 1.91 | -2.4 dB |
| Peaking | 3509 Hz  | 0.3  | 1.1 dB  |
| Peaking | 4276 Hz  | 5.23 | -2.7 dB |
| Peaking | 10020 Hz | 5.82 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | 3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-A700X/Audio-Technica%20ATH-A700X.png)