# Audio-Technica ATH-PRO700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -3.0; 25 -4.7; 28 -6.9; 31 -8.6; 34 -10.0; 37 -11.1; 41 -12.1; 45 -12.8; 49 -13.2; 54 -13.2; 60 -12.6; 66 -12.3; 72 -12.6; 79 -12.9; 87 -12.7; 96 -12.5; 106 -12.6; 116 -12.6; 128 -12.5; 141 -12.3; 155 -12.0; 170 -11.7; 187 -11.3; 206 -10.7; 227 -9.7; 249 -8.2; 274 -6.4; 302 -5.2; 332 -5.2; 365 -6.1; 402 -7.3; 442 -8.2; 486 -8.6; 535 -8.9; 588 -9.0; 647 -9.0; 712 -9.0; 783 -8.7; 861 -8.5; 947 -8.2; 1042 -7.8; 1146 -7.7; 1261 -7.7; 1387 -7.3; 1526 -6.6; 1678 -5.8; 1846 -4.8; 2031 -3.8; 2234 -2.9; 2457 -2.6; 2703 -2.3; 2973 -1.4; 3270 -0.5; 3597 -1.3; 3957 -4.1; 4353 -4.8; 4788 -2.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.4; 8482 -7.6; 9330 -6.7; 10263 -6.5; 11289 -7.2; 12418 -8.4; 13660 -7.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-PRO700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-PRO700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.33 | 10.9 dB |
| Peaking | 46 Hz    | 0.42 | -7.6 dB |
| Peaking | 150 Hz   | 1.63 | -2.9 dB |
| Peaking | 3035 Hz  | 2.04 | 5.7 dB  |
| Peaking | 5742 Hz  | 3.39 | 6.3 dB  |
| Peaking | 320 Hz   | 3.59 | 3.7 dB  |
| Peaking | 636 Hz   | 1.15 | -2.6 dB |
| Peaking | 1248 Hz  | 5.42 | -0.9 dB |
| Peaking | 8411 Hz  | 6.73 | -2.0 dB |
| Peaking | 12474 Hz | 3.83 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-PRO700/Audio-Technica%20ATH-PRO700.png)