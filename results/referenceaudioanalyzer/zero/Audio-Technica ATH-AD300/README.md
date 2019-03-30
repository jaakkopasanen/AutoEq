# Audio-Technica ATH-AD300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.7; 60 -1.6; 66 -2.7; 72 -3.5; 79 -4.3; 87 -5.0; 96 -5.5; 106 -6.0; 116 -6.4; 128 -6.6; 141 -6.8; 155 -7.0; 170 -7.2; 187 -7.1; 206 -6.9; 227 -6.9; 249 -6.9; 274 -6.9; 302 -6.7; 332 -6.6; 365 -6.4; 402 -6.2; 442 -6.2; 486 -5.9; 535 -5.9; 588 -5.9; 647 -5.8; 712 -5.6; 783 -5.6; 861 -5.6; 947 -5.7; 1042 -5.9; 1146 -6.2; 1261 -6.6; 1387 -7.1; 1526 -7.7; 1678 -8.3; 1846 -8.3; 2031 -7.9; 2234 -7.5; 2457 -7.3; 2703 -7.7; 2973 -8.6; 3270 -9.5; 3597 -9.3; 3957 -7.9; 4353 -5.7; 4788 -5.2; 5267 -6.9; 5793 -7.2; 6373 -4.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -8.4; 11289 -9.6; 12418 -10.1; 13660 -9.9; 15026 -9.4; 16529 -7.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 34 Hz    |  0.81 | 7.0 dB  |
| Peaking | 1785 Hz  |  3.7  | -2.0 dB |
| Peaking | 3327 Hz  |  4.06 | -3.3 dB |
| Peaking | 6740 Hz  |  6.03 | 4.3 dB  |
| Peaking | 13111 Hz |  1.37 | -4.0 dB |
| Peaking | 35 Hz    |  3.01 | -1.4 dB |
| Peaking | 56 Hz    |  1.89 | 1.9 dB  |
| Peaking | 145 Hz   |  0.87 | -1.2 dB |
| Peaking | 744 Hz   |  1.45 | 1.1 dB  |
| Peaking | 4599 Hz  | 10.14 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-AD300/Audio-Technica%20ATH-AD300.png)