# AKG K375
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.7; 25 -8.1; 28 -8.6; 31 -9.1; 34 -9.4; 37 -9.7; 41 -10.0; 45 -10.2; 49 -10.4; 54 -10.5; 60 -10.6; 66 -10.8; 72 -10.9; 79 -10.9; 87 -10.9; 96 -10.9; 106 -10.9; 116 -10.7; 128 -10.6; 141 -10.5; 155 -10.3; 170 -10.1; 187 -9.8; 206 -9.5; 227 -9.1; 249 -8.7; 274 -8.5; 302 -8.2; 332 -8.0; 365 -7.7; 402 -7.3; 442 -6.8; 486 -6.2; 535 -5.7; 588 -5.1; 647 -4.6; 712 -4.0; 783 -3.5; 861 -3.1; 947 -2.5; 1042 -1.5; 1146 -0.7; 1261 -0.5; 1387 -0.5; 1526 -0.6; 1678 -0.9; 1846 -1.4; 2031 -2.4; 2234 -3.8; 2457 -6.2; 2703 -8.3; 2973 -9.0; 3270 -7.9; 3597 -6.1; 3957 -5.0; 4353 -5.1; 4788 -5.9; 5267 -8.4; 5793 -11.0; 6373 -10.4; 7010 -5.3; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K375 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K375 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 68 Hz   |  0.39 | -2.4 dB |
| Peaking | 181 Hz  |  0.17 | -3.5 dB |
| Peaking | 1713 Hz |  0.43 | 7.7 dB  |
| Peaking | 2846 Hz |  1.89 | -9.2 dB |
| Peaking | 5901 Hz |  3.78 | -7.8 dB |
| Peaking | 4121 Hz |  3.87 | 0.5 dB  |
| Peaking | 7234 Hz | 10.1  | 2.3 dB  |
| Peaking | 7336 Hz |  0.69 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20K375/AKG%20K375.png)