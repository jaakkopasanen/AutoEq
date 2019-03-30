# Audio-Technica ATH-M50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.6; 25 -5.1; 28 -5.7; 31 -6.3; 34 -6.7; 37 -7.1; 41 -7.4; 45 -7.4; 49 -6.9; 54 -6.1; 60 -5.6; 66 -5.9; 72 -6.3; 79 -6.6; 87 -7.1; 96 -7.8; 106 -8.5; 116 -9.0; 128 -9.4; 141 -9.6; 155 -9.7; 170 -9.6; 187 -9.3; 206 -8.8; 227 -7.9; 249 -6.8; 274 -5.5; 302 -4.2; 332 -2.9; 365 -1.5; 402 -0.7; 442 -0.5; 486 -0.8; 535 -1.4; 588 -2.2; 647 -3.0; 712 -3.6; 783 -4.0; 861 -4.2; 947 -4.2; 1042 -4.2; 1146 -4.2; 1261 -4.6; 1387 -5.0; 1526 -5.0; 1678 -4.7; 1846 -4.0; 2031 -3.1; 2234 -3.0; 2457 -3.7; 2703 -4.2; 2973 -4.1; 3270 -3.8; 3597 -5.4; 3957 -9.2; 4353 -11.0; 4788 -9.8; 5267 -6.1; 5793 -3.4; 6373 -3.6; 7010 -4.9; 7711 -4.9; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 40 Hz   | 3.15 | -2.3 dB  |
| Peaking | 164 Hz  | 0.89 | -5.5 dB  |
| Peaking | 422 Hz  | 1.36 | 5.9 dB   |
| Peaking | 4033 Hz | 0.87 | 3.7 dB   |
| Peaking | 4355 Hz | 3.13 | -10.3 dB |
| Peaking | 63 Hz   | 4.76 | 0.7 dB   |
| Peaking | 1522 Hz | 4.2  | -0.8 dB  |
| Peaking | 2080 Hz | 5.68 | 1.3 dB   |
| Peaking | 6030 Hz | 4.88 | 2.9 dB   |
| Peaking | 6453 Hz | 1.23 | -1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 5.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.3 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-M50/Audio-Technica%20ATH-M50.png)