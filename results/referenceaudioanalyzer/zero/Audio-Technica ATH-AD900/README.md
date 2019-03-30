# Audio-Technica ATH-AD900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -1.2; 72 -1.8; 79 -2.4; 87 -2.9; 96 -3.3; 106 -3.6; 116 -3.9; 128 -4.2; 141 -4.5; 155 -4.7; 170 -4.8; 187 -4.6; 206 -4.5; 227 -4.6; 249 -4.6; 274 -4.6; 302 -4.6; 332 -4.6; 365 -4.6; 402 -4.6; 442 -4.6; 486 -4.7; 535 -4.9; 588 -4.9; 647 -4.9; 712 -4.9; 783 -4.9; 861 -4.9; 947 -5.1; 1042 -5.3; 1146 -5.6; 1261 -6.0; 1387 -6.4; 1526 -6.9; 1678 -7.2; 1846 -6.9; 2031 -6.5; 2234 -6.1; 2457 -5.6; 2703 -5.6; 2973 -5.0; 3270 -4.6; 3597 -7.5; 3957 -11.3; 4353 -13.6; 4788 -14.3; 5267 -13.8; 5793 -12.6; 6373 -10.5; 7010 -9.0; 7711 -9.4; 8482 -10.4; 9330 -10.9; 10263 -10.9; 11289 -10.0; 12418 -8.7; 13660 -8.1; 15026 -7.2; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.42 | 6.4 dB  |
| Peaking | 481 Hz   | 0.57 | 1.8 dB  |
| Peaking | 3249 Hz  | 2.67 | 5.4 dB  |
| Peaking | 4644 Hz  | 1.63 | -8.9 dB |
| Peaking | 10246 Hz | 1.71 | -3.9 dB |
| Peaking | 57 Hz    | 0.9  | -0.9 dB |
| Peaking | 59 Hz    | 2.04 | 1.5 dB  |
| Peaking | 1692 Hz  | 2.09 | -2.2 dB |
| Peaking | 2186 Hz  | 0.83 | 2.0 dB  |
| Peaking | 3226 Hz  | 1.25 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 1.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-AD900/Audio-Technica%20ATH-AD900.png)