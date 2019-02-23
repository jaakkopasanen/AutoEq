# AKG K812 sn001130
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.5; 25 -1.8; 28 -2.1; 31 -2.4; 34 -2.6; 37 -2.7; 41 -2.9; 45 -3.1; 49 -3.2; 54 -3.3; 60 -3.5; 66 -3.9; 72 -4.1; 79 -4.4; 87 -4.9; 96 -5.4; 106 -5.7; 116 -5.8; 128 -6.3; 141 -6.5; 155 -6.7; 170 -6.6; 187 -6.8; 206 -6.8; 227 -6.8; 249 -6.7; 274 -6.6; 302 -6.6; 332 -6.5; 365 -6.3; 402 -6.2; 442 -5.9; 486 -5.7; 535 -5.5; 588 -5.0; 647 -4.7; 712 -4.5; 783 -3.9; 861 -3.6; 947 -3.0; 1042 -2.8; 1146 -2.6; 1261 -2.3; 1387 -3.0; 1526 -3.2; 1678 -3.7; 1846 -2.7; 2031 -2.0; 2234 -2.7; 2457 -0.5; 2703 -2.0; 2973 -4.6; 3270 -5.9; 3597 -7.1; 3957 -6.0; 4353 -2.8; 4788 -2.0; 5267 -6.7; 5793 -10.8; 6373 -9.1; 7010 -4.2; 7711 -5.5; 8482 -7.1; 9330 -6.6; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -6.4; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K812 sn001130 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 sn001130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.99 | 3.7 dB  |
| Peaking | 1202 Hz | 1.78 | 2.8 dB  |
| Peaking | 2469 Hz | 3.15 | 4.9 dB  |
| Peaking | 4645 Hz | 4.82 | 11.5 dB |
| Peaking | 4986 Hz | 1.62 | -7.7 dB |
| Peaking | 63 Hz   | 1.75 | 1.2 dB  |
| Peaking | 201 Hz  | 0.71 | -2.0 dB |
| Peaking | 6136 Hz | 7.86 | -6.8 dB |
| Peaking | 6730 Hz | 3.19 | 4.7 dB  |
| Peaking | 8615 Hz | 5.93 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812%20sn001130/AKG%20K812%20sn001130.png)