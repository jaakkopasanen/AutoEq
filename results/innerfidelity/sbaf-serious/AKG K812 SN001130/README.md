# AKG K812 sn001130
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.5; 25 -1.8; 28 -2.1; 31 -2.4; 34 -2.6; 37 -2.7; 41 -2.9; 45 -3.1; 49 -3.2; 54 -3.3; 60 -3.5; 66 -3.9; 72 -4.1; 79 -4.4; 87 -4.9; 96 -5.4; 106 -5.7; 116 -5.8; 128 -6.3; 141 -6.5; 155 -6.7; 170 -6.6; 187 -6.8; 206 -6.8; 227 -6.8; 249 -6.7; 274 -6.6; 302 -6.6; 332 -6.5; 365 -6.3; 402 -6.2; 442 -5.9; 486 -5.7; 535 -5.5; 588 -5.0; 647 -4.7; 712 -4.5; 783 -3.9; 861 -3.6; 947 -3.0; 1042 -2.8; 1146 -2.6; 1261 -2.3; 1387 -3.0; 1526 -3.2; 1678 -3.7; 1846 -2.7; 2031 -2.0; 2234 -2.7; 2457 -0.5; 2703 -2.0; 2973 -4.6; 3270 -5.9; 3597 -7.1; 3957 -6.0; 4353 -2.8; 4788 -2.0; 5267 -6.7; 5793 -10.8; 6373 -9.1; 7010 -4.2; 7711 -5.5; 8482 -7.1; 9330 -6.6; 10263 -3.5; 11289 -2.8; 12418 -2.8; 13660 -2.8; 15026 -2.8; 16529 -4.3; 18182 -6.4; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K812 sn001130 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 sn001130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.53 | 2.4 dB  |
| Peaking | 215 Hz   | 0.48 | -4.3 dB |
| Peaking | 3583 Hz  | 5.95 | -4.4 dB |
| Peaking | 5977 Hz  | 5.1  | -9.2 dB |
| Peaking | 19830 Hz | 0.81 | -6.4 dB |
| Peaking | 2530 Hz  | 9.04 | 3.7 dB  |
| Peaking | 4642 Hz  | 8.65 | 4.3 dB  |
| Peaking | 7007 Hz  | 3.03 | 5.2 dB  |
| Peaking | 8598 Hz  | 1.19 | -9.1 dB |
| Peaking | 10544 Hz | 1.08 | 5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812%20sn001130/AKG%20K812%20sn001130.png)