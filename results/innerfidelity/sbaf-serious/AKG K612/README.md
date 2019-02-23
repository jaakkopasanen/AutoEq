# AKG K612
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.3; 31 -1.8; 34 -2.3; 37 -2.7; 41 -3.1; 45 -3.5; 49 -3.8; 54 -4.1; 60 -4.6; 66 -5.0; 72 -4.7; 79 -4.3; 87 -5.5; 96 -5.2; 106 -5.9; 116 -6.5; 128 -6.9; 141 -7.2; 155 -7.5; 170 -7.5; 187 -7.6; 206 -7.7; 227 -7.6; 249 -7.5; 274 -7.4; 302 -7.3; 332 -7.0; 365 -6.8; 402 -6.7; 442 -6.4; 486 -6.4; 535 -6.1; 588 -5.3; 647 -4.8; 712 -4.8; 783 -4.6; 861 -4.9; 947 -5.0; 1042 -5.0; 1146 -4.8; 1261 -4.6; 1387 -5.0; 1526 -5.8; 1678 -6.4; 1846 -7.3; 2031 -8.7; 2234 -9.2; 2457 -9.3; 2703 -9.0; 2973 -7.5; 3270 -5.9; 3597 -4.3; 3957 -5.1; 4353 -7.1; 4788 -6.7; 5267 -4.1; 5793 -4.5; 6373 -6.0; 7010 -7.0; 7711 -7.6; 8482 -8.6; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -8.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K612 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K612 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.08 | 6.0 dB  |
| Peaking | 54 Hz    | 1.6  | 1.4 dB  |
| Peaking | 1103 Hz  | 1.07 | 2.2 dB  |
| Peaking | 2370 Hz  | 2.03 | -3.8 dB |
| Peaking | 3609 Hz  | 4.98 | 3.2 dB  |
| Peaking | 217 Hz   | 1.17 | -1.4 dB |
| Peaking | 657 Hz   | 4.28 | 1.0 dB  |
| Peaking | 5537 Hz  | 7.51 | 3.1 dB  |
| Peaking | 8474 Hz  | 4.86 | -2.3 dB |
| Peaking | 18310 Hz | 2.86 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K612/AKG%20K612.png)