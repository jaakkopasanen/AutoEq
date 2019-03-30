# Audio-Technica FAKE ATH-ES7 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.0; 87 -1.5; 96 -2.1; 106 -2.7; 116 -3.1; 128 -3.6; 141 -3.9; 155 -4.2; 170 -4.5; 187 -4.7; 206 -4.8; 227 -4.7; 249 -4.9; 274 -5.1; 302 -5.1; 332 -5.2; 365 -5.4; 402 -5.4; 442 -5.4; 486 -5.4; 535 -5.4; 588 -5.7; 647 -5.7; 712 -5.9; 783 -6.1; 861 -6.3; 947 -6.8; 1042 -7.8; 1146 -9.1; 1261 -9.4; 1387 -8.6; 1526 -7.6; 1678 -7.7; 1846 -8.7; 2031 -9.2; 2234 -9.1; 2457 -8.5; 2703 -7.8; 2973 -6.2; 3270 -4.5; 3597 -3.8; 3957 -3.5; 4353 -3.9; 4788 -5.8; 5267 -8.0; 5793 -8.4; 6373 -10.4; 7010 -13.1; 7711 -13.3; 8482 -10.7; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica FAKE ATH-ES7 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica FAKE ATH-ES7 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.28 | 6.3 dB  |
| Peaking | 1225 Hz | 4.46 | -3.0 dB |
| Peaking | 2206 Hz | 2.2  | -3.2 dB |
| Peaking | 3828 Hz | 2.37 | 4.1 dB  |
| Peaking | 7307 Hz | 2.86 | -7.8 dB |
| Peaking | 74 Hz   | 3.3  | 0.8 dB  |
| Peaking | 140 Hz  | 1.63 | -0.6 dB |
| Peaking | 499 Hz  | 1.14 | 0.7 dB  |
| Peaking | 8395 Hz | 6.34 | -1.4 dB |
| Peaking | 9842 Hz | 2.82 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 2.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20FAKE%20ATH-ES7%202/Audio-Technica%20FAKE%20ATH-ES7%202.png)