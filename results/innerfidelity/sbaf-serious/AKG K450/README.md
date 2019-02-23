# AKG K450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.3; 28 -2.1; 31 -2.8; 34 -3.4; 37 -3.9; 41 -4.4; 45 -4.9; 49 -5.2; 54 -5.6; 60 -5.9; 66 -6.2; 72 -6.5; 79 -6.8; 87 -7.1; 96 -7.6; 106 -7.8; 116 -8.2; 128 -8.4; 141 -8.9; 155 -9.1; 170 -9.2; 187 -9.4; 206 -9.6; 227 -9.7; 249 -9.8; 274 -9.7; 302 -9.8; 332 -9.9; 365 -9.8; 402 -9.3; 442 -9.4; 486 -9.8; 535 -9.9; 588 -9.5; 647 -9.2; 712 -9.0; 783 -9.0; 861 -9.0; 947 -8.5; 1042 -8.1; 1146 -8.0; 1261 -6.9; 1387 -6.1; 1526 -5.0; 1678 -4.1; 1846 -3.3; 2031 -2.8; 2234 -2.8; 2457 -2.5; 2703 -3.4; 2973 -5.4; 3270 -7.7; 3597 -8.8; 3957 -7.5; 4353 -6.2; 4788 -2.8; 5267 -1.7; 5793 -3.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 14 Hz   |  0.51 | 7.2 dB  |
| Peaking | 939 Hz  |  0.11 | -4.0 dB |
| Peaking | 2265 Hz |  0.92 | 8.2 dB  |
| Peaking | 3608 Hz |  2.34 | -5.8 dB |
| Peaking | 5569 Hz |  1.52 | 6.7 dB  |
| Peaking | 413 Hz  |  8.67 | 0.6 dB  |
| Peaking | 1122 Hz |  7.69 | -0.6 dB |
| Peaking | 6527 Hz | 11.16 | 2.3 dB  |
| Peaking | 7684 Hz |  4.73 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K450/AKG%20K450.png)