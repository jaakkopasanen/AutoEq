# Audio-Technica ATH-M20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -2.2; 72 -3.3; 79 -4.4; 87 -5.5; 96 -6.4; 106 -7.0; 116 -7.5; 128 -7.9; 141 -8.1; 155 -8.1; 170 -7.9; 187 -7.6; 206 -7.2; 227 -6.8; 249 -6.3; 274 -5.7; 302 -5.4; 332 -5.2; 365 -5.1; 402 -4.7; 442 -4.2; 486 -3.7; 535 -3.3; 588 -3.3; 647 -4.0; 712 -5.6; 783 -7.8; 861 -9.9; 947 -11.5; 1042 -12.6; 1146 -13.3; 1261 -13.3; 1387 -13.3; 1526 -13.3; 1678 -12.6; 1846 -11.0; 2031 -8.9; 2234 -7.0; 2457 -6.1; 2703 -4.6; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -2.5; 4353 -3.8; 4788 -2.6; 5267 -0.5; 5793 -0.5; 6373 -1.6; 7010 -5.2; 7711 -7.9; 8482 -10.2; 9330 -12.1; 10263 -12.5; 11289 -11.3; 12418 -8.8; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.9  | 7.2 dB  |
| Peaking | 1380 Hz | 1.68 | -8.3 dB |
| Peaking | 3288 Hz | 2.71 | 6.8 dB  |
| Peaking | 5776 Hz | 2.41 | 7.3 dB  |
| Peaking | 9781 Hz | 1.78 | -7.2 dB |
| Peaking | 59 Hz   | 3.2  | 2.5 dB  |
| Peaking | 138 Hz  | 1.24 | -2.6 dB |
| Peaking | 586 Hz  | 1.14 | 4.5 dB  |
| Peaking | 888 Hz  | 2.76 | -3.5 dB |
| Peaking | 1047 Hz | 5.97 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 5.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -6.8 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-M20/Audio-Technica%20ATH-M20.png)