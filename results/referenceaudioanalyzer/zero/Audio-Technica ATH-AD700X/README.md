# Audio-Technica ATH-AD700X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -1.6; 72 -2.3; 79 -3.1; 87 -3.9; 96 -4.7; 106 -5.5; 116 -6.1; 128 -6.6; 141 -7.0; 155 -7.3; 170 -7.6; 187 -7.7; 206 -7.9; 227 -7.9; 249 -7.9; 274 -7.7; 302 -7.6; 332 -7.4; 365 -7.2; 402 -7.0; 442 -7.0; 486 -7.0; 535 -7.0; 588 -6.9; 647 -6.6; 712 -6.6; 783 -6.6; 861 -6.6; 947 -6.9; 1042 -7.0; 1146 -7.2; 1261 -7.0; 1387 -6.9; 1526 -6.6; 1678 -5.9; 1846 -4.6; 2031 -3.3; 2234 -2.2; 2457 -1.1; 2703 -0.5; 2973 -0.5; 3270 -2.2; 3597 -7.1; 3957 -10.7; 4353 -11.2; 4788 -9.2; 5267 -7.4; 5793 -8.6; 6373 -9.6; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -8.5; 10263 -8.9; 11289 -8.7; 12418 -9.4; 13660 -8.8; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD700X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD700X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.61 | 7.4 dB  |
| Peaking | 596 Hz   | 0.08 | -1.4 dB |
| Peaking | 2977 Hz  | 1.38 | 10.8 dB |
| Peaking | 4023 Hz  | 2.17 | -9.4 dB |
| Peaking | 12059 Hz | 1.79 | -2.8 dB |
| Peaking | 36 Hz    | 1.26 | -3.7 dB |
| Peaking | 62 Hz    | 0.14 | 3.3 dB  |
| Peaking | 161 Hz   | 0.6  | -3.9 dB |
| Peaking | 6432 Hz  | 6.86 | -3.1 dB |
| Peaking | 7335 Hz  | 4.82 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-AD700X/Audio-Technica%20ATH-AD700X.png)