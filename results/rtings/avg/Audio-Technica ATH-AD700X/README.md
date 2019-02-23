# Audio-Technica ATH-AD700X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.9; 49 -1.4; 54 -1.9; 60 -2.5; 66 -3.2; 72 -3.7; 79 -4.2; 87 -4.8; 96 -5.4; 106 -6.1; 116 -6.5; 128 -6.9; 141 -7.3; 155 -7.5; 170 -7.7; 187 -7.8; 206 -7.8; 227 -7.7; 249 -7.6; 274 -7.5; 302 -7.5; 332 -7.7; 365 -7.8; 402 -7.9; 442 -8.1; 486 -8.1; 535 -8.2; 588 -7.9; 647 -7.8; 712 -7.8; 783 -7.8; 861 -7.8; 947 -8.0; 1042 -8.1; 1146 -8.3; 1261 -8.7; 1387 -9.0; 1526 -9.0; 1678 -8.8; 1846 -8.2; 2031 -7.3; 2234 -4.8; 2457 -2.1; 2703 -1.4; 2973 -1.6; 3270 -1.7; 3597 -4.0; 3957 -8.6; 4353 -7.4; 4788 -0.9; 5267 -1.5; 5793 -6.3; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -12.5; 10263 -12.7; 11289 -9.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.0; 18182 -11.7; 20000 -14.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD700X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD700X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.88 | 7.0 dB  |
| Peaking | 2867 Hz | 3.95 | 6.1 dB  |
| Peaking | 4992 Hz | 9.19 | 6.7 dB  |
| Peaking | 6666 Hz | 6.36 | 5.1 dB  |
| Peaking | 9933 Hz | 3.26 | -7.4 dB |
| Peaking | 66 Hz   | 1.32 | 2.1 dB  |
| Peaking | 242 Hz  | 0.18 | -1.6 dB |
| Peaking | 1686 Hz | 1.36 | -5.0 dB |
| Peaking | 2235 Hz | 0.92 | 3.6 dB  |
| Peaking | 4105 Hz | 9.43 | -5.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-AD700X/Audio-Technica%20ATH-AD700X.png)