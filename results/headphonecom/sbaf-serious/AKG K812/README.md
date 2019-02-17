# AKG K812
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.5; 25 -6.8; 28 -7.1; 31 -7.3; 34 -7.5; 37 -7.6; 41 -7.8; 45 -8.0; 49 -8.2; 54 -8.3; 60 -8.5; 66 -8.9; 72 -8.9; 79 -9.0; 87 -9.2; 96 -9.4; 106 -9.8; 116 -10.0; 128 -10.3; 141 -10.5; 155 -10.7; 170 -10.6; 187 -10.6; 206 -10.7; 227 -10.7; 249 -10.4; 274 -10.3; 302 -10.0; 332 -9.8; 365 -9.4; 402 -9.2; 442 -9.0; 486 -8.6; 535 -8.2; 588 -7.9; 647 -7.4; 712 -6.9; 783 -6.3; 861 -5.9; 947 -5.7; 1042 -5.3; 1146 -4.4; 1261 -4.1; 1387 -4.6; 1526 -6.4; 1678 -6.0; 1846 -4.8; 2031 -5.1; 2234 -5.7; 2457 -3.6; 2703 -0.5; 2973 -5.7; 3270 -5.9; 3597 -7.0; 3957 -8.5; 4353 -3.1; 4788 -5.1; 5267 -9.0; 5793 -12.2; 6373 -11.9; 7010 -5.4; 7711 -5.2; 8482 -8.0; 9330 -11.3; 10263 -10.9; 11289 -5.7; 12418 -5.4; 13660 -5.4; 15026 -6.7; 16529 -6.5; 18182 -5.4; 20000 -12.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K812 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 93 Hz    | 0.31 | -2.7 dB |
| Peaking | 253 Hz   | 0.51 | -3.5 dB |
| Peaking | 3624 Hz  | 0.55 | 4.4 dB  |
| Peaking | 5800 Hz  | 0.63 | -6.6 dB |
| Peaking | 20049 Hz | 3.15 | -7.2 dB |
| Peaking | 3884 Hz  | 5.92 | -5.3 dB |
| Peaking | 4415 Hz  | 4.55 | 5.6 dB  |
| Peaking | 6119 Hz  | 3.97 | -9.5 dB |
| Peaking | 7041 Hz  | 2.28 | 7.4 dB  |
| Peaking | 9568 Hz  | 5.06 | -5.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K812/AKG%20K812.png)