# Audio-Technica ATH-A500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.1; 28 -2.5; 31 -4.0; 34 -5.2; 37 -6.3; 41 -7.5; 45 -8.3; 49 -8.9; 54 -9.3; 60 -9.5; 66 -9.5; 72 -9.6; 79 -9.8; 87 -9.8; 96 -9.7; 106 -9.3; 116 -8.8; 128 -8.3; 141 -8.0; 155 -7.5; 170 -6.7; 187 -6.0; 206 -5.6; 227 -5.5; 249 -5.1; 274 -4.5; 302 -4.2; 332 -4.6; 365 -5.9; 402 -7.3; 442 -8.3; 486 -8.5; 535 -8.6; 588 -8.5; 647 -8.5; 712 -8.8; 783 -8.7; 861 -7.9; 947 -7.4; 1042 -7.5; 1146 -7.4; 1261 -6.8; 1387 -5.8; 1526 -4.4; 1678 -3.1; 1846 -3.1; 2031 -3.6; 2234 -3.6; 2457 -3.3; 2703 -3.0; 2973 -2.9; 3270 -1.8; 3597 -0.5; 3957 -3.7; 4353 -7.8; 4788 -7.9; 5267 -4.3; 5793 -0.6; 6373 -2.0; 7010 -8.3; 7711 -13.5; 8482 -16.4; 9330 -16.8; 10263 -15.1; 11289 -13.3; 12418 -12.9; 13660 -12.7; 15026 -10.7; 16529 -7.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-A500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-A500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 3.55 | 7.3 dB   |
| Peaking | 2017 Hz  | 1.94 | 5.1 dB   |
| Peaking | 3440 Hz  | 2.5  | 9.4 dB   |
| Peaking | 6096 Hz  | 2.62 | 19.1 dB  |
| Peaking | 7442 Hz  | 0.58 | -14.5 dB |
| Peaking | 29 Hz    | 1.72 | 3.1 dB   |
| Peaking | 71 Hz    | 0.58 | -3.9 dB  |
| Peaking | 313 Hz   | 1.01 | 5.3 dB   |
| Peaking | 474 Hz   | 0.98 | -4.7 dB  |
| Peaking | 17273 Hz | 2.34 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | 3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.2 dB |
| Peaking | 16000 Hz | 1.41 | -4.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-A500/Audio-Technica%20ATH-A500.png)