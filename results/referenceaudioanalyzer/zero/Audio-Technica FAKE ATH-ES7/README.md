# Audio-Technica FAKE ATH-ES7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.9; 49 -2.9; 54 -4.0; 60 -5.0; 66 -5.8; 72 -6.3; 79 -6.8; 87 -7.1; 96 -7.4; 106 -7.7; 116 -7.9; 128 -8.1; 141 -8.1; 155 -8.1; 170 -8.1; 187 -8.1; 206 -8.1; 227 -7.9; 249 -7.8; 274 -7.7; 302 -7.6; 332 -7.4; 365 -7.4; 402 -7.4; 442 -7.4; 486 -7.3; 535 -7.1; 588 -7.1; 647 -7.1; 712 -7.1; 783 -7.1; 861 -6.8; 947 -6.2; 1042 -5.6; 1146 -5.4; 1261 -4.6; 1387 -2.9; 1526 -2.3; 1678 -2.9; 1846 -4.1; 2031 -5.3; 2234 -5.8; 2457 -5.8; 2703 -5.0; 2973 -3.5; 3270 -2.1; 3597 -1.7; 3957 -1.4; 4353 -1.0; 4788 -2.3; 5267 -3.9; 5793 -4.8; 6373 -6.6; 7010 -12.0; 7711 -15.4; 8482 -14.8; 9330 -11.2; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica FAKE ATH-ES7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica FAKE ATH-ES7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.69 | 8.2 dB   |
| Peaking | 92 Hz    | 0.31 | -2.7 dB  |
| Peaking | 1495 Hz  | 3.48 | 4.3 dB   |
| Peaking | 4257 Hz  | 1.43 | 6.2 dB   |
| Peaking | 7958 Hz  | 2.92 | -11.1 dB |
| Peaking | 734 Hz   | 3.94 | -0.6 dB  |
| Peaking | 1778 Hz  | 5.21 | 1.0 dB   |
| Peaking | 2426 Hz  | 2.12 | -1.2 dB  |
| Peaking | 3192 Hz  | 5.5  | 1.5 dB   |
| Peaking | 11243 Hz | 5.21 | 1.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.7 dB |
| Peaking | 16000 Hz | 1.41 | 1.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20FAKE%20ATH-ES7/Audio-Technica%20FAKE%20ATH-ES7.png)