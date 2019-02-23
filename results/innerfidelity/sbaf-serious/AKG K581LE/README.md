# AKG K581LE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.7; 31 -2.3; 34 -2.8; 37 -3.3; 41 -3.8; 45 -4.3; 49 -4.4; 54 -4.7; 60 -5.7; 66 -6.3; 72 -6.6; 79 -6.8; 87 -8.1; 96 -8.3; 106 -7.2; 116 -8.0; 128 -9.1; 141 -10.2; 155 -10.5; 170 -10.1; 187 -9.6; 206 -9.4; 227 -9.7; 249 -8.8; 274 -8.4; 302 -8.8; 332 -8.2; 365 -7.6; 402 -6.9; 442 -6.5; 486 -6.5; 535 -6.4; 588 -6.4; 647 -6.5; 712 -6.8; 783 -6.8; 861 -7.2; 947 -7.4; 1042 -7.6; 1146 -7.7; 1261 -7.5; 1387 -8.2; 1526 -8.6; 1678 -8.4; 1846 -8.0; 2031 -7.2; 2234 -6.4; 2457 -5.1; 2703 -4.0; 2973 -3.2; 3270 -2.7; 3597 -2.7; 3957 -2.9; 4353 -3.4; 4788 -2.7; 5267 -4.4; 5793 -1.4; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K581LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K581LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.71 | 5.9 dB  |
| Peaking | 165 Hz  | 0.95 | -4.0 dB |
| Peaking | 1664 Hz | 1.45 | -2.9 dB |
| Peaking | 3410 Hz | 1.26 | 4.3 dB  |
| Peaking | 6197 Hz | 5.24 | 5.3 dB  |
| Peaking | 94 Hz   | 5.41 | -1.3 dB |
| Peaking | 109 Hz  | 6.01 | 1.5 dB  |
| Peaking | 318 Hz  | 3.46 | -0.9 dB |
| Peaking | 466 Hz  | 2.26 | 0.8 dB  |
| Peaking | 8324 Hz | 3.99 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K581LE/AKG%20K581LE.png)