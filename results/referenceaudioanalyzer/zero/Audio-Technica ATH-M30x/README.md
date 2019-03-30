# Audio-Technica ATH-M30x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.1; 28 -2.2; 31 -3.6; 34 -4.7; 37 -5.7; 41 -6.8; 45 -7.6; 49 -8.1; 54 -8.4; 60 -8.5; 66 -8.4; 72 -8.2; 79 -7.9; 87 -7.6; 96 -7.4; 106 -7.2; 116 -7.0; 128 -6.7; 141 -6.2; 155 -5.7; 170 -5.1; 187 -4.3; 206 -3.3; 227 -2.1; 249 -1.3; 274 -1.4; 302 -2.5; 332 -3.8; 365 -4.8; 402 -5.4; 442 -5.8; 486 -6.0; 535 -6.2; 588 -6.2; 647 -6.2; 712 -6.2; 783 -6.1; 861 -5.9; 947 -5.8; 1042 -6.0; 1146 -6.6; 1261 -7.2; 1387 -7.7; 1526 -8.1; 1678 -8.4; 1846 -8.7; 2031 -9.0; 2234 -9.4; 2457 -9.4; 2703 -9.1; 2973 -8.7; 3270 -7.9; 3597 -8.0; 3957 -8.5; 4353 -7.5; 4788 -4.2; 5267 -5.0; 5793 -10.8; 6373 -13.9; 7010 -13.9; 7711 -10.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M30x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M30x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.94 | 7.4 dB  |
| Peaking | 49 Hz    | 0.75 | -3.8 dB |
| Peaking | 255 Hz   | 1.82 | 5.6 dB  |
| Peaking | 2266 Hz  | 1.61 | -3.1 dB |
| Peaking | 6715 Hz  | 4.7  | -8.9 dB |
| Peaking | 943 Hz   | 4.56 | 1.0 dB  |
| Peaking | 4191 Hz  | 3.63 | -2.3 dB |
| Peaking | 5014 Hz  | 4.23 | 5.6 dB  |
| Peaking | 5884 Hz  | 6.52 | -3.4 dB |
| Peaking | 20812 Hz | 1.59 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | 5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-M30x/Audio-Technica%20ATH-M30x.png)