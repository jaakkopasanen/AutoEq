# AKG K612
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.2; 31 -2.8; 34 -3.2; 37 -3.6; 41 -4.1; 45 -4.4; 49 -4.7; 54 -5.1; 60 -5.5; 66 -5.9; 72 -5.7; 79 -5.2; 87 -6.5; 96 -6.1; 106 -6.9; 116 -7.4; 128 -7.9; 141 -8.2; 155 -8.4; 170 -8.4; 187 -8.5; 206 -8.6; 227 -8.5; 249 -8.5; 274 -8.4; 302 -8.3; 332 -7.9; 365 -7.7; 402 -7.6; 442 -7.3; 486 -7.3; 535 -7.1; 588 -6.2; 647 -5.7; 712 -5.8; 783 -5.5; 861 -5.9; 947 -6.0; 1042 -6.0; 1146 -5.7; 1261 -5.5; 1387 -5.9; 1526 -6.8; 1678 -7.3; 1846 -8.3; 2031 -9.6; 2234 -10.1; 2457 -10.3; 2703 -9.9; 2973 -8.5; 3270 -6.8; 3597 -5.2; 3957 -6.1; 4353 -8.1; 4788 -7.6; 5267 -5.0; 5793 -5.5; 6373 -7.0; 7010 -7.9; 7711 -8.5; 8482 -9.5; 9330 -8.0; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -6.4; 18182 -9.2; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K612 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K612 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.61 | 6.6 dB  |
| Peaking | 208 Hz   | 0.79 | -2.9 dB |
| Peaking | 2367 Hz  | 2.52 | -4.8 dB |
| Peaking | 8315 Hz  | 3.7  | -3.7 dB |
| Peaking | 18262 Hz | 2.28 | -3.7 dB |
| Peaking | 999 Hz   | 0.74 | 2.4 dB  |
| Peaking | 1047 Hz  | 0.44 | -1.7 dB |
| Peaking | 3718 Hz  | 5.23 | 3.1 dB  |
| Peaking | 4510 Hz  | 2.89 | -2.7 dB |
| Peaking | 5352 Hz  | 6.16 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K612/AKG%20K612.png)