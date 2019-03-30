# Audio-Technica FAKE ATH-ES3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -2.4; 87 -4.6; 96 -6.5; 106 -8.0; 116 -9.1; 128 -9.9; 141 -10.3; 155 -10.3; 170 -10.1; 187 -9.6; 206 -9.1; 227 -8.6; 249 -8.1; 274 -7.8; 302 -7.4; 332 -7.2; 365 -6.9; 402 -6.7; 442 -6.7; 486 -6.8; 535 -6.7; 588 -6.5; 647 -6.4; 712 -6.4; 783 -6.3; 861 -6.1; 947 -5.9; 1042 -5.8; 1146 -5.5; 1261 -5.9; 1387 -7.1; 1526 -8.7; 1678 -9.9; 1846 -10.3; 2031 -9.9; 2234 -8.9; 2457 -7.3; 2703 -4.9; 2973 -1.7; 3270 -0.5; 3597 -2.2; 3957 -6.1; 4353 -6.2; 4788 -2.9; 5267 -0.5; 5793 -0.6; 6373 -3.8; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.7; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica FAKE ATH-ES3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica FAKE ATH-ES3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 68 Hz   | 0.33 | 10.3 dB  |
| Peaking | 134 Hz  | 0.77 | -12.0 dB |
| Peaking | 1913 Hz | 2.82 | -4.6 dB  |
| Peaking | 3193 Hz | 4.59 | 7.0 dB   |
| Peaking | 5515 Hz | 4.08 | 6.7 dB   |
| Peaking | 19 Hz   | 1.31 | 2.2 dB   |
| Peaking | 43 Hz   | 0.63 | -1.1 dB  |
| Peaking | 71 Hz   | 4.14 | 2.2 dB   |
| Peaking | 1109 Hz | 3.01 | 1.6 dB   |
| Peaking | 2314 Hz | 0.11 | -0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 6.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20FAKE%20ATH-ES3/Audio-Technica%20FAKE%20ATH-ES3.png)