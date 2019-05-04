# Audio-Technica ATH-AD700X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.8; 49 -1.2; 54 -1.7; 60 -2.4; 66 -3.0; 72 -3.5; 79 -4.0; 87 -4.6; 96 -5.2; 106 -5.8; 116 -6.3; 128 -6.8; 141 -7.1; 155 -7.4; 170 -7.5; 187 -7.6; 206 -7.6; 227 -7.5; 249 -7.4; 274 -7.4; 302 -7.5; 332 -7.7; 365 -7.7; 402 -7.9; 442 -8.1; 486 -8.2; 535 -8.2; 588 -8.0; 647 -7.9; 712 -7.9; 783 -8.0; 861 -7.9; 947 -8.1; 1042 -8.3; 1146 -8.5; 1261 -8.8; 1387 -9.3; 1526 -9.5; 1678 -9.1; 1846 -8.6; 2031 -7.7; 2234 -5.6; 2457 -3.0; 2703 -2.0; 2973 -1.7; 3270 -1.4; 3597 -3.9; 3957 -8.3; 4353 -6.9; 4788 -0.8; 5267 -1.9; 5793 -6.0; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -7.5; 9330 -10.8; 10263 -12.2; 11289 -10.6; 12418 -6.6; 13660 -6.5; 15026 -6.5; 16529 -8.9; 18182 -11.5; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD700X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD700X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 33 Hz    |  0.83 | 7.0 dB  |
| Peaking | 2980 Hz  |  4.26 | 5.9 dB  |
| Peaking | 4976 Hz  |  8.9  | 6.4 dB  |
| Peaking | 6584 Hz  |  6.52 | 5.3 dB  |
| Peaking | 10216 Hz |  3.02 | -6.4 dB |
| Peaking | 374 Hz   |  0.44 | -1.4 dB |
| Peaking | 1800 Hz  |  1.22 | -6.3 dB |
| Peaking | 2253 Hz  |  1.18 | 5.1 dB  |
| Peaking | 3957 Hz  | 11.38 | -2.9 dB |
| Peaking | 4212 Hz  | 14.92 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-AD700X/Audio-Technica%20ATH-AD700X.png)