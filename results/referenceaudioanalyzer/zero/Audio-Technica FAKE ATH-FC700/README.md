# Audio-Technica FAKE ATH-FC700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.3; 60 -2.2; 66 -2.8; 72 -3.3; 79 -3.7; 87 -4.2; 96 -4.7; 106 -5.2; 116 -5.6; 128 -6.0; 141 -6.2; 155 -6.4; 170 -6.7; 187 -6.7; 206 -7.0; 227 -7.3; 249 -7.4; 274 -7.6; 302 -7.7; 332 -7.7; 365 -7.7; 402 -8.0; 442 -8.0; 486 -8.2; 535 -8.3; 588 -8.3; 647 -8.6; 712 -8.8; 783 -9.0; 861 -9.3; 947 -9.8; 1042 -9.8; 1146 -9.1; 1261 -7.9; 1387 -6.3; 1526 -4.6; 1678 -3.8; 1846 -4.0; 2031 -4.8; 2234 -5.3; 2457 -4.5; 2703 -2.1; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -1.0; 4353 -1.2; 4788 -2.9; 5267 -4.6; 5793 -6.4; 6373 -9.1; 7010 -12.9; 7711 -14.2; 8482 -11.5; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica FAKE ATH-FC700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica FAKE ATH-FC700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.63 | 6.7 dB  |
| Peaking | 1452 Hz | 0.39 | -4.7 dB |
| Peaking | 1627 Hz | 2.96 | 4.9 dB  |
| Peaking | 3469 Hz | 0.94 | 9.3 dB  |
| Peaking | 7441 Hz | 2.97 | -9.9 dB |
| Peaking | 878 Hz  | 0.56 | 2.7 dB  |
| Peaking | 1000 Hz | 2.69 | -1.5 dB |
| Peaking | 1233 Hz | 0.19 | -1.8 dB |
| Peaking | 3708 Hz | 0.87 | 1.1 dB  |
| Peaking | 9775 Hz | 5.61 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20FAKE%20ATH-FC700/Audio-Technica%20FAKE%20ATH-FC700.png)