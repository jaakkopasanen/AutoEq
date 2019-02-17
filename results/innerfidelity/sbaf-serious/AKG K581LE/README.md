# AKG K581LE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.3; 34 -1.8; 37 -2.3; 41 -2.8; 45 -3.2; 49 -3.4; 54 -3.7; 60 -4.6; 66 -5.3; 72 -5.5; 79 -5.8; 87 -7.0; 96 -7.3; 106 -6.2; 116 -6.9; 128 -8.0; 141 -9.2; 155 -9.5; 170 -9.1; 187 -8.6; 206 -8.3; 227 -8.6; 249 -7.8; 274 -7.4; 302 -7.7; 332 -7.2; 365 -6.6; 402 -5.8; 442 -5.5; 486 -5.4; 535 -5.4; 588 -5.3; 647 -5.5; 712 -5.7; 783 -5.8; 861 -6.1; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.4; 1387 -7.1; 1526 -7.5; 1678 -7.4; 1846 -7.0; 2031 -6.1; 2234 -5.3; 2457 -4.1; 2703 -3.0; 2973 -2.2; 3270 -1.7; 3597 -1.7; 3957 -1.8; 4353 -2.3; 4788 -1.7; 5267 -3.4; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K581LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K581LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  0.87 | 6.2 dB  |
| Peaking | 50 Hz   |  2.6  | 1.1 dB  |
| Peaking | 163 Hz  |  1.58 | -3.1 dB |
| Peaking | 3590 Hz |  1.67 | 5.2 dB  |
| Peaking | 6084 Hz |  4.15 | 5.2 dB  |
| Peaking | 558 Hz  |  1.99 | 1.4 dB  |
| Peaking | 1656 Hz |  2.31 | -1.7 dB |
| Peaking | 2650 Hz |  5.16 | 1.3 dB  |
| Peaking | 4796 Hz | 11.64 | 1.6 dB  |
| Peaking | 8293 Hz |  3.29 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K581LE/AKG%20K581LE.png)