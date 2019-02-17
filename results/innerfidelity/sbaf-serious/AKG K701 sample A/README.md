# AKG K701 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.0; 34 -1.5; 37 -2.0; 41 -2.5; 45 -2.9; 49 -3.3; 54 -3.8; 60 -4.3; 66 -4.4; 72 -4.2; 79 -4.3; 87 -4.7; 96 -5.8; 106 -6.6; 116 -7.1; 128 -7.7; 141 -8.1; 155 -8.2; 170 -8.3; 187 -8.7; 206 -8.9; 227 -8.8; 249 -8.9; 274 -8.9; 302 -8.9; 332 -8.7; 365 -8.7; 402 -8.5; 442 -8.1; 486 -7.7; 535 -7.6; 588 -6.9; 647 -6.3; 712 -5.7; 783 -5.4; 861 -5.8; 947 -6.0; 1042 -6.5; 1146 -6.2; 1261 -5.9; 1387 -6.0; 1526 -6.4; 1678 -7.2; 1846 -8.0; 2031 -8.9; 2234 -8.7; 2457 -8.3; 2703 -7.2; 2973 -5.2; 3270 -3.6; 3597 -4.3; 3957 -5.6; 4353 -7.1; 4788 -7.4; 5267 -7.7; 5793 -10.0; 6373 -10.4; 7010 -8.3; 7711 -8.3; 8482 -8.4; 9330 -8.3; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.3  | 6.5 dB  |
| Peaking | 216 Hz  | 0.79 | -3.0 dB |
| Peaking | 2241 Hz | 3.25 | -2.9 dB |
| Peaking | 3379 Hz | 3.34 | 3.7 dB  |
| Peaking | 6261 Hz | 2.03 | -3.6 dB |
| Peaking | 81 Hz   | 6.31 | 1.0 dB  |
| Peaking | 415 Hz  | 2.41 | -0.7 dB |
| Peaking | 764 Hz  | 3.17 | 1.6 dB  |
| Peaking | 1309 Hz | 5.06 | 0.9 dB  |
| Peaking | 9008 Hz | 7.69 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701%20sample%20A/AKG%20K701%20sample%20A.png)