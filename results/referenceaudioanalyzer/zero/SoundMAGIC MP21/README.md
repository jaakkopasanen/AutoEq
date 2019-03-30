# SoundMAGIC MP21
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.3; 28 -3.3; 31 -4.2; 34 -4.9; 37 -5.4; 41 -6.0; 45 -6.5; 49 -7.0; 54 -7.4; 60 -7.7; 66 -7.9; 72 -8.1; 79 -8.2; 87 -8.1; 96 -8.3; 106 -8.3; 116 -8.1; 128 -8.2; 141 -8.1; 155 -7.8; 170 -7.7; 187 -7.5; 206 -7.2; 227 -7.0; 249 -6.8; 274 -6.6; 302 -6.3; 332 -6.1; 365 -5.9; 402 -5.6; 442 -5.5; 486 -5.2; 535 -5.2; 588 -5.0; 647 -4.9; 712 -4.9; 783 -4.9; 861 -5.2; 947 -5.2; 1042 -5.3; 1146 -5.3; 1261 -4.9; 1387 -4.8; 1526 -5.0; 1678 -5.3; 1846 -5.3; 2031 -4.8; 2234 -3.7; 2457 -3.3; 2703 -3.6; 2973 -3.1; 3270 -1.9; 3597 -1.3; 3957 -1.3; 4353 -1.4; 4788 -2.3; 5267 -3.8; 5793 -4.1; 6373 -2.3; 7010 -1.6; 7711 -3.8; 8482 -4.1; 9330 -4.1; 10263 -4.1; 11289 -4.1; 12418 -4.1; 13660 -4.1; 15026 -4.1; 16529 -4.1; 18182 -4.1; 20000 -4.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundMAGIC MP21 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC MP21 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.38 | 5.6 dB  |
| Peaking | 92 Hz    | 0.49 | -3.5 dB |
| Peaking | 107 Hz   | 0    | -0.9 dB |
| Peaking | 3827 Hz  | 1.87 | 3.4 dB  |
| Peaking | 627 Hz   | 3.88 | 0.5 dB  |
| Peaking | 1945 Hz  | 2.71 | -1.7 dB |
| Peaking | 2221 Hz  | 2.64 | 1.7 dB  |
| Peaking | 6790 Hz  | 8.38 | 3.3 dB  |
| Peaking | 14388 Hz | 0.23 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/SoundMAGIC%20MP21/SoundMAGIC%20MP21.png)